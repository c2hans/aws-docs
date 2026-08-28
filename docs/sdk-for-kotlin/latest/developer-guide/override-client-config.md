---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/override-client-config.html
---

# Override service client configuration
<a name="override-client-config"></a>

After a [service client is created](creating-clients.md), the service client uses a fixed configuration for all operations. However, sometimes you might need to override the configuration for one or more specific operations.

Each service client has a `withConfig` extension so that you can modify a copy of the existing configuration. The `withConfig` extension returns a new service client with a modified configuration. The original client exists independently and uses its original configuration.

The following example shows the creation of an [`S3Client`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/index.html) instance that calls two operations.

```
val s3 = S3Client.fromEnvironment {
    logMode = LogMode.LogRequest
    region = "us-west-2"
    // ...other configuration settings...
}

s3.listBuckets { ... }
s3.listObjectsV2 { ... }
```

The following snippet shows how to override the configuration for a single [`listObjectV2`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/list-objects-v2.html) operation.

```
s3.withConfig {
    region = "eu-central-1"
}.use { overriddenS3 ->
    overriddenS3.listObjectsV2 { ... }
}
```

The operation calls on the `s3` client use the original configuration that was specified when the client was created. Its configuration includes [request logging](logging.md#sdk-log-mode) and `us-west-2 region` for the Region.

The [`listObjectsV2`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/list-objects-v2.html) invocation on the `overriddenS3` client uses same settings as the original `s3` client except for the Region, which is now `eu-central-1`.

## Lifecycle of an overridden client
<a name="override-client-lifecycle"></a>

In the previous example, the `s3` client and the `overriddenS3` client are independent of each other. Operations can be invoked on either client for as long as they remain open. Each uses a separate configuration, but they can share underlying resources (such as an HTTP engine) unless those are also overridden.

You close a client with an overridden configuration and the original client separately. You can close a client with overridden configuration before or after you close its original client. Unless you need to use a client with overridden configuration for a long time, we recommend that you wrap its lifecycle with the `use` method. The `use` method ensures that the client is closed if exceptions occur.

## Resources shared between clients
<a name="override-client-shared-res"></a>

When you create a service client by using `withConfig`, it might share resources with the original client. In contrast, when you create a client by using [fromEnvironment](creating-clients.md#loading-from-the-environment) or you [explicitly configure it](creating-clients.md#programmatic-config), the client uses independent resources. Resources such as HTTP engines and credentials providers are shared unless they are overridden in the `withConfig` block.

Because the lifecycle of each client is independent, shared resources remain open and usable until the last client is closed. Therefore, it is important for you to close overridden service clients when you no longer need them. This prevents shared resources from remaining open and consuming system resources such as memory, connection, and CPU cycles.

The following example shows both shared and independent resources.

The `s3` and `overriddenS3` clients share the same credentials provider instance, including its caching configuration. Calls made by `overriddenS3` reuse credentials if the cached value is still current from calls made by the `s3` client.

The HTTP engine is not shared between the two clients. Each client has an independent HTTP engine because it was overridden in the `withConfig` call.

```
val s3 = S3Client.fromEnvironment {
    region = "us-west-2"
    credentialsProvider = CachedCredentialsProvider(CredentialsProviderChain(...))
    httpClientEngine = OkHttpEngine { ... }
}

s3.listBuckets { ... }

s3.withConfig {
    httpClientEngine = CrtHttpEngine { ... }
}.use { overriddenS3 ->
    overriddenS3.listObjectsV2 { ... }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
