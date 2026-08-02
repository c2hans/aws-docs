---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/logging.html
---

# Logging
<a name="logging"></a>

The AWS SDK for Kotlin configures an [SLF4J](https://www.slf4j.org/manual.html) compatible logger as the default `LoggerProvider` of the telemetry provider. With SLF4J, which is an abstraction layer, you can use of any one of several logging systems at runtime. Supported logging systems include the [Java Logging APIs](https://docs.oracle.com/javase/8/docs/technotes/guides/logging/), [Log4j 2](https://logging.apache.org/log4j/2.x/), and [Logback](https://logback.qos.ch/).

**Warning**
We recommend that you only use wire logging for debugging purposes. (Wire logging is discussed below.) Turn it off in your production environments because it can log sensitive data such as email addresses, security tokens, API keys, passwords, and AWS Secrets Manager secrets. Wire logging logs the full request or response without encryption, even for an HTTPS call.
For large requests (such as uploading a file to Amazon S3) or responses, verbose wire logging can also significantly impact your application’s performance.

## Example Log4j 2 logging configuration
<a name="_example_log4j_2_logging_configuration"></a>

While any `SLF4J`-compatible log library may be used, this example enables log output from the SDK in JVM programs using Log4j 2:

 **Gradle dependencies**

Replace {{X.Y.Z}} with the version you’re using in your app or with the [latest version available](https://search.maven.org/#search|gav|1|g:org.apache.logging.log4j%20AND%20a:log4j-slf4j2-impl).

```
implementation("org.apache.logging.log4j:log4j-slf4j2-impl:{{X.Y.Z}}")
```

 **Log4j 2 configuration file**

Create a file named `log4j2.xml` in your `resources` directory (for example, `<project-dir>/src/main/resources`). Add the following XML configuration to the file:

```
<Configuration status="ERROR">
    <Appenders>
        <Console name="Out">
            <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} %-5p %c:%L %X - %encode{%m}{CRLF}%n"/>
        </Console>
    </Appenders>
    <Loggers>
        <Root level="info">
            <AppenderRef ref="Out"/>
        </Root>
    </Loggers>
</Configuration>
```

This configuration includes the `%X` specifier in the `pattern` attribute that enables MDC (mapped diagnostic context) logging.

The SDK adds the following MDC elements for each operation.

 **rpc**
The name of the invoked RPC, for example `S3.GetObject`.

 **sdkInvocationId**
A unique ID assigned by the service client for the operation. The ID correlates all logging events related to the invocation of a single operation.

## Specify log mode for wire-level messages
<a name="sdk-log-mode"></a>

By default, the AWS SDK for Kotlin doesn’t log wire-level messages because they might contain sensitive data from API requests and responses. However, sometimes you need this level of detail for debugging purposes.

With the Kotlin SDK, you can set a log mode in code or using environment settings to enable debug messaging for the following:
+ HTTP requests
+ HTTP responses

The log mode is backed by a bit-field where each bit is a flag (mode) and values are additive. You can combine one request mode and one response mode.

### Set log mode in code
<a name="set-log-mode-programmatically"></a>

To opt into additional logging, set the `logMode` property when you construct a service client.

The following example shows how to enable logging of requests (with the body) and the response (without the body).

```
import aws.smithy.kotlin.runtime.client.LogMode

// ...

val client = DynamoDbClient {
    // ...
    logMode = LogMode.LogRequestWithBody + LogMode.LogResponse
}
```

A log mode value set during service client construction, overrides any log mode value set from the environment.

### Set log mode from the environment
<a name="set-log-mode-from-enviironment"></a>

To set a log mode globally for all service clients not explicitly configured in code, use one of the following:
+ JVM system property: `sdk.logMode`
+ Environment variable: `SDK_LOG_MODE`

The following case-insensitive values are available:
+  `LogRequest`
+  `LogRequestWithBody`
+  `LogResponse`
+  `LogResponseWithBody`

To create a combined log mode using settings from the environment, you separate the values with a pipe (`|`) symbol.

For example, the following examples set the same log mode as the previous example.

```
# Environment variable.
export SDK_LOG_MODE=LogRequestWithBody|LogResponse
```

```
# JVM system property.
java -Dsdk.logMode=LogRequestWithBody|LogResponse ...
```

**Note**
You must also configure a compatible SLF4J logger and set the logging level to DEBUG to enable wire-level logging.
