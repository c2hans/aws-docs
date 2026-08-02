---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/config-endpoint.html
---

# Configure client endpoints
<a name="config-endpoint"></a>

When the AWS SDK for Kotlin calls an AWS service, one of its first steps is to determine where to route the request. This process is known as endpoint resolution.

You can configure endpoint resolution for the SDK when you build a service client. The default configuration for endpoint resolution is usually fine, but there are several reasons that might lead you to modify the default configuration. Two example reasons are as follows:
+ Make requests to a prerelease version of a service or to a local deployment of a service.
+ Access to specific service features not yet modeled in the SDK.

**Warning**
Endpoint resolution is an advanced SDK topic. If you change the default settings, you risk breaking your code. The default settings should apply to most users in production environments.

## Custom configuration
<a name="config-endpoint-custom-config"></a>

You can customize endpoint resolution of a service client with two properties that are available when you build the client:

1.  `endpointUrl: Url`

1.  `endpointProvider: EndpointProvider`

### Set `endpointUrl`
<a name="config-endpoint-custom-config-endpointurl"></a>

You can set a value for `endpointUrl` to indicate a "base" hostname for the service. This value, however, is not final since it is passed as a parameter to the client’s `EndpointProvider` instance. The `EndpointProvider` implementation then can inspect and potentially modify that value to determine the final endpoint.

As an example, if you specify an `endpointUrl` value for an Amazon Simple Storage Service (Amazon S3) client and perform a `GetObject` operation, the default endpoint provider implementation injects the bucket name into the hostname value.

In practice, users set an `endpointUrl` value to point at a development or preview instance of a service.

### Set `endpointProvider`
<a name="config-endpoint-custom-config-endpointprovider"></a>

A service client’s `EndpointProvider` implementation determines final endpoint resolution. The `EndpointProvider` interface shown in the following code block exposes the `resolveEndpoint` method.

```
public fun interface EndpointProvider<T> {
    public suspend fun resolveEndpoint(params: T): Endpoint
}
```

A service client calls the `resolveEndpoint` method for every request. The service client uses the `Endpoint` value returned by the provider with no further changes.

#### `EndpointProvider` properties
<a name="config-endpoint-custom-config-endpointprovider-params"></a>

The `resolveEndpoint` method accepts a service-specific `EndpointParameters` object that contains properties used in endpoint resolution.

Every service includes the following base properties.

| Name | Type | Description |
| --- | --- | --- |
|  `region`  | String | The client’s AWS Region |
|  `endpoint`  | String | A string representation of the value set of `endpointUrl`  |
|  `useFips`  | Boolean | Whether FIPS endpoints are enabled in the client’s configuration |
|  `useDualStack`  | Boolean | Whether dual-stack endpoints are enabled in the client’s configuration |

Services can specify additional properties required for resolution. For example, Amazon S3 [S3EndpointParameters](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.endpoints/-s3-endpoint-parameters/index.html) includes the bucket name and also several Amazon S3-specific feature settings. For example, the `forcePathStyle` property determines whether virtual host addressing can be used.

If you implement your own provider, you shouldn’t need to construct your own instance of `EndpointParameters`. The SDK provides the properties for each request and passes them to your implementation of `resolveEndpoint`.

### `endpointUrl` or `endpointProvider`
<a name="config-endpoint-custom-config-which"></a>

It is important to understand that the following two statements do NOT produce clients with equivalent endpoint resolution behavior:

```
// Use endpointUrl.
S3Client.fromEnvironment {
    endpointUrl = Url.parse("https://endpoint.example")
}

// Use endpointProvider.
S3Client.fromEnvironment {
    endpointProvider = object : S3EndpointProvider {
        override suspend fun resolveEndpoint(params: S3EndpointParameters): Endpoint = Endpoint("https://endpoint.example")
    }
}
```

The statement that sets the `endpointUrl` property specifies a *base* URL that is passed to the (default) provider, which can be modified as part of endpoint resolution.

The statement that sets the `endpointProvider` specifies the *final* URL the `S3Client` uses.

Although you can set both properties, in most cases that need customization, you provide one of them. As a general SDK user, you most often provide an `endpointUrl` value.

### A note about Amazon S3
<a name="config-endpoint-custom-config-s3"></a>

Amazon S3 is a complex service with many of its features modeled through customized endpoints customizations, such as bucket virtual hosting. Virtual hosting is a feature of Amazon S3 where the bucket name is inserted into the hostname.

Because of this, we recommend that you don’t replace the `EndpointProvider` implementation in an Amazon S3 service client. If you need to extend its resolution behavior, perhaps by sending requests to a local development stack with additional endpoint considerations, we recommend wrapping the default implementation. The following `endpointProvider` example shows a sample implementation of this approach.

## Examples
<a name="config-endpoint-examples"></a>

### `endpointUrl` example
<a name="config-endpoint-examples-endpointurl"></a>

The following code snippet shows how the general service endpoint can be overridden for an Amazon S3 client.

```
val client = S3Client.fromEnvironment {
    endpointUrl = Url.parse("https://custom-s3-endpoint.local")
    // EndpointProvider is left as the default.
}
```

### `endpointProvider` example
<a name="config-endpoint-examples-endpointprovider"></a>

The following code snippet shows how to provide a custom endpoint provider that wraps the default implementation for Amazon S3.

```
import aws.sdk.kotlin.services.s3.endpoints.DefaultS3EndpointProvider
import aws.sdk.kotlin.services.s3.endpoints.S3EndpointParameters
import aws.sdk.kotlin.services.s3.endpoints.S3EndpointProvider
import aws.smithy.kotlin.runtime.client.endpoints.Endpoint

public class CustomS3EndpointProvider : S3EndpointProvider {
    override suspend fun resolveEndpoint(params: S3EndpointParameters) =
        if (/* Input params indicate we must route another endpoint for whatever reason. */) {
            Endpoint(/* ... */)
        } else {
            // Fall back to the default resolution.
            DefaultS3EndpointProvider().resolveEndpoint(params)
        }
}
```

### `endpointUrl` and `endpointProvider`
<a name="config-endpoint-examples-both"></a>

The following example program demonstrates the interaction between the `endpointUrl` and `endpointProvider` settings. This is an advanced use case.

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.sdk.kotlin.services.s3.endpoints.DefaultS3EndpointProvider
import aws.sdk.kotlin.services.s3.endpoints.S3EndpointParameters
import aws.sdk.kotlin.services.s3.endpoints.S3EndpointProvider
import aws.smithy.kotlin.runtime.client.endpoints.Endpoint

fun main() = runBlocking {
    S3Client.fromEnvironment {
        endpointUrl = Url.parse("https://example.endpoint")
        endpointProvider = CustomS3EndpointProvider()
    }.use { s3 ->
        // ...
    }
}

class CustomS3EndpointProvider : S3EndpointProvider {
    override suspend fun resolveEndpoint(params: S3EndpointParameters) {
        // The resolved string value of the endpointUrl set in the client above is available here.
        println(params.endpoint)
        // ...
    }
}
```
