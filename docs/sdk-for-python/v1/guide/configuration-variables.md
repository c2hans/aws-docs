---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/configuration-variables.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Configuration variables
<a name="configuration-variables"></a>

This page lists all configuration variables supported by the AWS SDK for Python, including their default values and usage examples where applicable.

## aws\_credentials\_identity\_resolver
<a name="config-aws-credentials-identity-resolver"></a>

An `IdentityResolver` that resolves AWS credentials for request authentication. Set this field only to use a specific resolver instead of the default credential resolver chain. For more information, see [Credential providers](credential-providers.md).

|  |  |
| --- |--- |
| Default | None (the client uses the default credential resolver chain) |
| Valid values | IdentityResolver[AWSCredentialsIdentity, AWSIdentityProperties] |

To provide static credentials directly, see [Configure static credentials](credential-providers.md#credproviders-static).

## endpoint\_uri
<a name="config-endpoint-uri"></a>

A custom endpoint URL to use instead of the standard AWS regional endpoint.

|  |  |
| --- |--- |
| Env var | AWS\_ENDPOINT\_URL (global), AWS\_ENDPOINT\_URL\_<SERVICE\_ID> (service-specific) |
| Profile key | endpoint\_url |
| Default | None (uses standard regional endpoint) |

Service-specific configs resolve this with extended precedence. See [Service-specific endpoint resolution](config-resolution.md#service-specific-endpoint-resolution).

```
# Environment variable — global (applies to all services)
export AWS_ENDPOINT_URL=http://localhost:4566

# Environment variable — service-specific
export AWS_ENDPOINT_URL_BEDROCK_RUNTIME=http://localhost:5000
```

```
# Config file
[default]
endpoint_url = http://localhost:4566
```

## interceptors
<a name="config-interceptors"></a>

A list of interceptor hooks that are called at various points during request execution. Interceptors can inspect or modify requests and responses.

|  |  |
| --- |--- |
| Default | [] (empty list) |

## max\_attempts
<a name="config-max-attempts"></a>

An integer representing the maximum number of attempts made for a single request, including the initial attempt. For example, setting this value to 5 results in a request being retried up to 4 times. If not provided, the number of retries defaults to whatever is modeled, which is typically 3 in the `standard` retry mode.

|  |  |
| --- |--- |
| Env var | AWS\_MAX\_ATTEMPTS |
| Profile key | max\_attempts |
| Default | None (the retry strategy uses its own default, typically 3 for standard mode) |
| Valid values | Positive integer (>= 1) |

```
# Environment variable
export AWS_MAX_ATTEMPTS=5
```

```
# Config file
[default]
max_attempts = 5
```

## region
<a name="config-region"></a>

The AWS Region to send requests to.

|  |  |
| --- |--- |
| Env vars | AWS\_REGION, AWS\_DEFAULT\_REGION |
| Profile key | region |
| Default | None |
| Valid values | AWS Region identifiers like us-east-1, eu-west-1, ap-southeast-1 |

```
# Environment variable
export AWS_REGION=us-west-2
```

```
# Config file
[default]
region = us-west-2
```

```
# Explicit override
config = await AsyncBedrockRuntimeConfig.resolve(region="us-west-2")
```

## retry\_mode
<a name="config-retry-mode"></a>

A string that represents the type of retries the SDK performs.

|  |  |
| --- |--- |
| Env var | AWS\_RETRY\_MODE |
| Profile key | retry\_mode |
| Default | "standard" |
| Valid values | "standard". Values "legacy" and "adaptive" from environment variables or config files are accepted but mapped to "standard" with a warning. |
+ **`standard`**: a standardized set of retry rules across the AWS SDKs. This includes a standard set of errors that are retried and support for retry quotas, which limit the number of unsuccessful retries the SDK can make. This mode will default the maximum number of attempts to 3 unless a `max_attempts` is explicitly provided.
+ **`legacy`**: not supported in this SDK. If set, it maps to `"standard"` with a warning.
+ **`adaptive`**: not supported at the moment. If set, it maps to `"standard"` with a warning.

```
# Environment variable
export AWS_RETRY_MODE=standard
```

```
# Config file
[default]
retry_mode = standard
```

## retry\_strategy
<a name="config-retry-strategy"></a>

An explicit retry strategy instance that bypasses `retry_mode` and `max_attempts` entirely. Use this when you need full control over retry behavior.

|  |  |
| --- |--- |
| Default | None (uses retry\_mode/max\_attempts to construct a strategy) |

## sdk\_ua\_app\_id
<a name="config-sdk-ua-app-id"></a>

An optional application-specific identifier that can be set. When set, it is appended to the SDK's User-Agent header, allowing you to identify your application in AWS service logs.

|  |  |
| --- |--- |
| Env var | AWS\_SDK\_UA\_APP\_ID |
| Profile key | sdk\_ua\_app\_id |
| Default | None |
| Valid values | Any string |

```
# Environment variable
export AWS_SDK_UA_APP_ID=my-web-app
```

```
# Config file
[default]
sdk_ua_app_id = my-web-app
```

## transport
<a name="config-transport"></a>

The HTTP client that the SDK uses to send requests. For details, including the optional `AWSCRTHTTPClient` and custom HTTP clients, see the [HTTP configuration](http-configuration.md) page.

|  |  |
| --- |--- |
| Default | AIOHTTPClient |

## user\_agent\_extra
<a name="config-user-agent-extra"></a>

An additional string appended to the User-Agent header.

|  |  |
| --- |--- |
| Default | None |
