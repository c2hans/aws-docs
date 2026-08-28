---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/http-client-config.html
---

# HTTP client configuration
<a name="http-client-config"></a>

By default, the AWS SDK for Kotlin uses an HTTP client based on [OkHttp](https://square.github.io/okhttp). You can override the HTTP client and its configuration by supplying an explicitly configured client.

**Warning**
Regardless of which HTTP engine you use, other dependencies in your project might have transitive dependencies that conflict with the specific engine version required by the SDK. In particular, frameworks such as Spring Boot are known to manage dependencies like OkHttp and to rely on older versions than the SDK. Please see [How do I resolve dependency conflicts?](ts-faq-dep-conflict-resolution.md) for more information.

**Note**
By default, each service client uses its own copy of an HTTP client. If you use multiple services in your application, you might want to construct a single HTTP client and share it across all service clients.

## Basic configuration
<a name="basic-http-confg"></a>

When you configure a service client, you can configure the default engine type. The SDK manages the resulting HTTP client engine and automatically closes it when it is no longer needed.

The following example shows configuration of an HTTP client during the initialization of a DynamoDB client.

### Imports
<a name="basic-config-ex-imports"></a>

```
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient
import kotlin.time.Duration.Companion.seconds
```

### Code
<a name="basic-config-ex-code"></a>

```
DynamoDbClient {
    region = "us-east-2"
    httpClient {
        maxConcurrency = 64u
        connectTimeout = 10.seconds
    }
}.use { ddb ->

    // Perform some actions with Amazon DynamoDB.
}
```

## Advanced configuration
<a name="advanced-http-config"></a>

The default HTTP configuration is suitable for most use cases. For some advanced use cases, such as high-throughput environments, the following advanced configuration options provide additional features and capabilities:

### Specify an HTTP engine type
<a name="http-config-engine"></a>

To specify a non-default HTTP engine type, or to customize configuration that is specific to a particular HTTP engine type, you may pass an additional parameter to `httpClient` that specifies the engine type.

The following example specifies the [OkHttpEngine](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine/index.html) that you can use to configure the [maxConcurrencyPerHost](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine-config/index.html) property.

#### Imports
<a name="http-config-specify-engine-imports"></a>

```
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient
import aws.smithy.kotlin.runtime.http.engine.okhttp.OkHttpEngine
```

#### Code
<a name="http-config-specify-engine-code"></a>

```
DynamoDbClient {
    region = "us-east-2"
    httpClient(OkHttpEngine) {  // The first parameter specifies the HTTP engine type.
        // The following parameter is generic HTTP configuration available in any engine type.
        maxConcurrency = 64u

            // The following parameter is OkHttp-specific configuration.
        maxConcurrencyPerHost = 32u
    }
}.use { ddb ->

    // Perform some actions with Amazon DynamoDB.
}
```

The possible values for the engine type are [`OkHttpEngine`](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine/index.html), [OkHttp4Engine](/smithy-kotlin/api/latest/http-client-engine-okhttp4/aws.smithy.kotlin.runtime.http.engine.okhttp4/-ok-http4-engine/index.html), and [CrtHttpEngine](/smithy-kotlin/api/latest/http-client-engine-crt/aws.smithy.kotlin.runtime.http.engine.crt/-crt-http-engine/index.html).

To use configuration parameters specific to an HTTP engine, you must add the engine as a compile-time dependency. For the [`OkHttpEngine`](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine/index.html), you add the following dependency using Gradle.

Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://github.com/smithy-lang/smithy-kotlin/releases/latest).

```
implementation(platform("aws.smithy.kotlin:bom:{{X.Y.Z}}"))
implementation("aws.smithy.kotlin:http-client-engine-okhttp")
```

For the [`CrtHttpEngine`](/smithy-kotlin/api/latest/http-client-engine-crt/aws.smithy.kotlin.runtime.http.engine.crt/-crt-http-engine/index.html), add the following dependency.

```
implementation(platform("aws.smithy.kotlin:bom:{{X.Y.Z}}"))
implementation("aws.smithy.kotlin:http-client-engine-crt")
```

#### Use the `OkHttp4Engine`
<a name="http-config-okhttp4engine"></a>

Use the [`OkHttp4Engine`](/smithy-kotlin/api/latest/http-client-engine-okhttp4/aws.smithy.kotlin.runtime.http.engine.okhttp4/-ok-http4-engine/index.html) if you can’t use the default [`OkHttpEngine`](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine/index.html). The [smithy-kotlin GitHub repository](https://github.com/smithy-lang/smithy-kotlin/tree/main/runtime/protocol/http-client-engines/http-client-engine-okhttp4) has information about how you configure and use the [`OkHttp4Engine`](/smithy-kotlin/api/latest/http-client-engine-okhttp4/aws.smithy.kotlin.runtime.http.engine.okhttp4/-ok-http4-engine/index.html).

#### Use an explicit HTTP client
<a name="http-client-explicit-usage"></a>

When you use an explicit HTTP client, you’re responsible for its lifetime, including closing when you no longer need it. An HTTP client must live at least as long as any service client that uses it.

The following code example shows code that keeps the HTTP client stays alive while the [`DynamoDbClient`](/sdk-for-kotlin/api/latest/dynamodb/aws.sdk.kotlin.services.dynamodb/-dynamo-db-client/index.html) is active. The [use](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.io/use.html) function makes sure the HTTP client closes properly.

##### Imports
<a name="http-client-explicit-usage-ex-imports"></a>

```
import aws.sdk.kotlin.services.dynamodb.DynamoDbClient
import aws.smithy.kotlin.runtime.http.engine.okhttp.OkHttpEngine
import kotlin.time.Duration.Companion.seconds
```

##### Code
<a name="http-client-explicit-usage-ex-code"></a>

```
OkHttpEngine {
    maxConcurrency = 64u
    connectTimeout = 10.seconds
}.use { okHttpClient ->

     DynamoDbClient {
        region = "us-east-2"
        httpClient = okHttpClient
    }.use { ddb ->
        {
            // Perform some actions with Amazon DynamoDB.
        }
    }
}
```

### Idle connection monitoring
<a name="http-idle-connection-monitoring"></a>

**Important**
The OkHttp engine’s connection idle polling feature ( [connectionIdlePollingInterval](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine-config/connection-idle-polling-interval.html)) has been superseded by automatic connection failure retries ( [retryOnConnectionFailure](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine-config/retry-on-connection-failure.html)). Connection idle polling will be **deprecated** in SDK version **v1.8** and will be **removed** in SDK version **v1.9**. See [the related GitHub Discussion post](https://github.com/aws/aws-sdk-kotlin/discussions/1797) for more details.

 [OkHttpEngine](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine/) provides the [connectionIdlePollingInterval](/smithy-kotlin/api/latest/http-client-engine-okhttp/aws.smithy.kotlin.runtime.http.engine.okhttp/-ok-http-engine-config/connection-idle-polling-interval.html) configuration option to monitor idle connections for remote closure. This feature detects when services have closed connections that are still in the connection pool, preventing errors on subsequent requests.

When `connectionIdlePollingInterval` is set to a non-null value, the engine polls connections that are released back to the connection pool. The polling process performs blocking reads with the socket timeout set to the specified interval. Polling is automatically cancelled when the engine acquires the connection from the pool or when the connection is evicted and closed.

When this value is `null` (the default), polling is disabled. Idle connections in the pool that are closed remotely may encounter errors when they are acquired for subsequent calls.

**Note**
Because the polling loop uses blocking reads, engine calls to acquire or close a connection may be delayed by as much as the `connectionIdlePollingInterval` interval. Choosing a low value for the interval means the SDK will acquire connections faster, at the expense of higher idle resource usage.

#### Imports
<a name="http-idle-connection-ex-imports"></a>

```
import aws.sdk.kotlin.services.s3.S3Client
import aws.smithy.kotlin.runtime.http.engine.okhttp.OkHttpEngine
import kotlin.time.Duration.Companion.milliseconds
```

#### Code
<a name="http-idle-connection-ex-code"></a>

```
S3Client.fromEnvironment {
    httpEngine(OkHttpEngine) {
        connectionIdlePollingInterval = 50.milliseconds
    }
}.use { s3 ->
  // Use the Amazon S3 client
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
