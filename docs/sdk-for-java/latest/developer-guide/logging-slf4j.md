---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/logging-slf4j.html
---

# Logging with the SDK for Java 2.x
<a name="logging-slf4j"></a>

The AWS SDK for Java 2.x uses [SLF4J](https://www.slf4j.org/manual.html), which is an abstraction layer that enables the use of any one of several logging systems at runtime.

Supported logging systems include the Java Logging Framework and Apache[ Log4j 2](https://logging.apache.org/log4j/2.x/), among others. This topic shows you how to use Log4j 2 as the logging system for working with the SDK.

## Log4j 2 configuration file
<a name="log4j-configuration-file"></a>

You typically use a configuration file, named`log4j2.xml` with Log4j 2. Example configuration files are shown below. To learn more about the values used in the configuration file, see the [manual for Log4j configuration](https://logging.apache.org/log4j/2.x/manual/configuration.html).

The `log4j2.xml` file needs to be on the classpath when your application starts up. For a Maven project, put the file in the `<project-dir>/src/main/resources` directory.

The `log4j2.xml` configuration file specifies properties such as [logging level](https://logging.apache.org/log4j/2.x/manual/configuration.html#Loggers), where logging output is sent (for example, [to a file or to the console](https://logging.apache.org/log4j/2.x/manual/appenders.html)), and the [format of the output](https://logging.apache.org/log4j/2.x/manual/layouts.html). The logging level specifies the level of detail that Log4j 2 outputs. Log4j 2 supports the concept of multiple logging [*hierarchies*](https://logging.apache.org/log4j/2.x/manual/architecture.html#). The logging level is set independently for each hierarchy. The main logging hierarchy that you use with the AWS SDK for Java 2.x is `software.amazon.awssdk`.

## Add logging dependency
<a name="sdk-java-logging-classpath"></a>

To configure the Log4j 2 binding for SLF4J in your build file, use the following.

------
#### [ Maven ]

Add the following elements to your `pom.xml` file.

```
...
<dependency>
   <groupId>org.apache.logging.log4j</groupId>
   <artifactId>log4j-slf4j2-impl</artifactId>
   <version>{{VERSION}}</version>
</dependency>
...
```

------
#### [ Gradle–Kotlin DSL ]

Add the following to your `build.gradle.kts` file.

```
...
dependencies {
    ...
    implementation("org.apache.logging.log4j:log4j-slf4j2-impl:{{VERSION}}")
    ...
}
...
```

------

Use `2.20.0` for the minimum version of the `log4j-slf4j2-impl` artifact. For the latest version, use the version published to [Maven central](https://central.sonatype.com/artifact/org.apache.logging.log4j/log4j-slf4j2-impl). Replace {{VERSION}} with version you'll use.

## SDK-specific errors and warnings
<a name="sdk-java-logging-service"></a>

We recommend that you always leave the "software.amazon.awssdk" logger hierarchy set to "WARN" to catch any important messages from the SDK's client libraries. For example, if the Amazon S3 client detects that your application hasn’t properly closed an `InputStream` and could be leaking resources, the S3 client reports it through a warning message to the logs. This also ensures that messages are logged if the client has any problems handling requests or responses.

The following `log4j2.xml` file sets the `rootLogger` to "WARN", which causes warning and error-level messages from all loggers in the application to be output, *including* those in the "software.amazon.awssdk" hierarchy. Alternatively, you can explicitly set the "software.amazon.awssdk" logger hierarchy to "WARN" if `<Root level="ERROR">` is used.

**Example Log4j2.xml configuration file**

This configuration will log messages at the "ERROR" and "WARN" levels to the console for all logger hierarchies.

```
<Configuration status="WARN">
 <Appenders>
  <Console name="ConsoleAppender" target="SYSTEM_OUT">
   <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
  </Console>
 </Appenders>

 <Loggers>
  <Root level="WARN">
   <AppenderRef ref="ConsoleAppender"/>
  </Root>
 </Loggers>
</Configuration>
```

## Request/response summary logging
<a name="sdk-java-logging-request-response"></a>

Every request to an AWS service generates a unique AWS request ID that is useful if you run into an issue with how an AWS service is handling a request. AWS request IDs are accessible programmatically through [`SdkServiceException`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/exception/SdkServiceException.html#requestId()) objects in the SDK for any failed service call, and can also be reported through the "DEBUG" log level of the "software.amazon.awssdk.request" logger.

The following `log4j2.xml` file enables a summary of requests and responses.

```
<Configuration status="WARN">
 <Appenders>
  <Console name="ConsoleAppender" target="SYSTEM_OUT">
   <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
  </Console>
 </Appenders>

 <Loggers>
  <Root level="ERROR">
   <AppenderRef ref="ConsoleAppender"/>
  </Root>
  <Logger name="software.amazon.awssdk" level="WARN" />
  <Logger name="software.amazon.awssdk.request" level="DEBUG" />
 </Loggers>
</Configuration>
```

Here is an example of the log output:

```
2022-09-23 16:02:08 [main] DEBUG software.amazon.awssdk.request:85 - Sending Request: DefaultSdkHttpFullRequest(httpMethod=POST, protocol=https, host=dynamodb.us-east-1.amazonaws.com, encodedPath=/, headers=[amz-sdk-invocation-id, Content-Length, Content-Type, User-Agent, X-Amz-Target], queryParameters=[])
2022-09-23 16:02:08 [main] DEBUG software.amazon.awssdk.request:85 - Received successful response: 200, Request ID: QS9DUMME2NHEDH8TGT9N5V53OJVV4KQNSO5AEMVJF66Q9ASUAAJG, Extended Request ID: not available
```

If you are interested in only the request ID use `<Logger name="software.amazon.awssdk.requestId" level="DEBUG" />`.

## Debug-level SDK logging
<a name="sdk-debug-level-logging"></a>

If you need more detail about what the SDK is doing, you can set the logging level of the `software.amazon.awssdk` logger to `DEBUG`. At this level, the SDK outputs a large amount of detail, so we recommend that you set this level to resolve errors using integration tests.

At this logging level, the SDK logs information about configuration, credentials resolution, execution interceptors, high-level TLS activity, request signing, and much more.

The following is a sampling of statements that are output by the SDK at `DEBUG` level for a `S3Client#listBuckets()` call.

```
DEBUG s.a.a.r.p.AwsRegionProviderChain:57 - Unable to load region from software.amazon.awssdk.regions.providers.SystemSettingsRegionProvider@324dcd31:Unable to load region from system settings. Region must be specified either via environment variable (AWS_REGION) or  system property (aws.region).
DEBUG s.a.a.c.i.h.l.ClasspathSdkHttpServiceProvider:85 - The HTTP implementation loaded is software.amazon.awssdk.http.apache.ApacheSdkHttpService@a23a01d
DEBUG s.a.a.c.i.ExecutionInterceptorChain:85 - Creating an interceptor chain that will apply interceptors in the following order: [software.amazon.awssdk.core.internal.interceptor.HttpChecksumValidationInterceptor@69b2f8e5, software.amazon.awssdk.awscore.interceptor.HelpfulUnknownHostExceptionInterceptor@6331250e, software.amazon.awssdk.awscore.eventstream.EventStreamInitialRequestInterceptor@a10c1b5, software.amazon.awssdk.awscore.interceptor.TraceIdExecutionInterceptor@644abb8f, software.amazon.awssdk.services.s3.auth.scheme.internal.S3AuthSchemeInterceptor@1a411233, software.amazon.awssdk.services.s3.endpoints.internal.S3ResolveEndpointInterceptor@70325d20, software.amazon.awssdk.services.s3.endpoints.internal.S3RequestSetEndpointInterceptor@7c2327fa, software.amazon.awssdk.services.s3.internal.handlers.StreamingRequestInterceptor@4d847d32, software.amazon.awssdk.services.s3.internal.handlers.CreateBucketInterceptor@5f462e3b, software.amazon.awssdk.services.s3.internal.handlers.CreateMultipartUploadRequestInterceptor@3d7fa3ae, software.amazon.awssdk.services.s3.internal.handlers.DecodeUrlEncodedResponseInterceptor@58065f0c, software.amazon.awssdk.services.s3.internal.handlers.GetBucketPolicyInterceptor@3605c4d3, software.amazon.awssdk.services.s3.internal.handlers.S3ExpressChecksumInterceptor@585c13de, software.amazon.awssdk.services.s3.internal.handlers.AsyncChecksumValidationInterceptor@187eb9a8, software.amazon.awssdk.services.s3.internal.handlers.SyncChecksumValidationInterceptor@726a6b94, software.amazon.awssdk.services.s3.internal.handlers.EnableTrailingChecksumInterceptor@6ad11a56, software.amazon.awssdk.services.s3.internal.handlers.ExceptionTranslationInterceptor@522b2631, software.amazon.awssdk.services.s3.internal.handlers.GetObjectInterceptor@3ff57625, software.amazon.awssdk.services.s3.internal.handlers.CopySourceInterceptor@1ee29c84, software.amazon.awssdk.services.s3.internal.handlers.ObjectMetadataInterceptor@7c8326a4]
DEBUG s.a.a.u.c.CachedSupplier:85 - (SsoOidcTokenProvider()) Cached value is stale and will be refreshed.
...
DEBUG s.a.a.c.i.ExecutionInterceptorChain:85 - Creating an interceptor chain that will apply interceptors in the following order: [software.amazon.awssdk.core.internal.interceptor.HttpChecksumValidationInterceptor@51351f28, software.amazon.awssdk.awscore.interceptor.HelpfulUnknownHostExceptionInterceptor@21618fa7, software.amazon.awssdk.awscore.eventstream.EventStreamInitialRequestInterceptor@15f2eda3, software.amazon.awssdk.awscore.interceptor.TraceIdExecutionInterceptor@34cf294c, software.amazon.awssdk.services.sso.auth.scheme.internal.SsoAuthSchemeInterceptor@4d7aaca2, software.amazon.awssdk.services.sso.endpoints.internal.SsoResolveEndpointInterceptor@604b1e1d, software.amazon.awssdk.services.sso.endpoints.internal.SsoRequestSetEndpointInterceptor@62566842]
...
DEBUG s.a.a.request:85 - Sending Request: DefaultSdkHttpFullRequest(httpMethod=GET, protocol=https, host=portal.sso.us-east-1.amazonaws.com, encodedPath=/federation/credentials, headers=[amz-sdk-invocation-id, User-Agent, x-amz-sso_bearer_token], queryParameters=[role_name, account_id])
DEBUG s.a.a.c.i.h.p.s.SigningStage:85 - Using SelectedAuthScheme: smithy.api#noAuth
DEBUG s.a.a.h.a.i.c.SdkTlsSocketFactory:366 - Connecting socket to portal.sso.us-east-1.amazonaws.com/18.235.195.183:443 with timeout 2000
...
DEBUG s.a.a.requestId:85 - Received successful response: 200, Request ID: bb4f40f4-e920-4b5c-8648-58f26e7e08cd, Extended Request ID: not available
DEBUG s.a.a.request:85 - Received successful response: 200, Request ID: bb4f40f4-e920-4b5c-8648-58f26e7e08cd, Extended Request ID: not available
DEBUG s.a.a.u.c.CachedSupplier:85 - (software.amazon.awssdk.services.sso.auth.SsoCredentialsProvider@b965857) Successfully refreshed cached value. Next Prefetch Time: 2024-04-25T22:03:10.097Z. Next Stale Time: 2024-04-25T22:05:30Z
DEBUG s.a.a.c.i.ExecutionInterceptorChain:85 - Interceptor 'software.amazon.awssdk.services.s3.endpoints.internal.S3RequestSetEndpointInterceptor@7c2327fa' modified the message with its modifyHttpRequest method.
...
DEBUG s.a.a.c.i.h.p.s.SigningStage:85 - Using SelectedAuthScheme: aws.auth#sigv4
...
DEBUG s.a.a.a.s.Aws4Signer:85 - AWS4 Canonical Request: GET
...
DEBUG s.a.a.h.a.a.i.s.DefaultV4RequestSigner:85 - AWS4 String to sign: AWS4-HMAC-SHA256
20240425T210631Z
20240425/us-east-1/s3/aws4_request
aafb7784627fa7a49584256cb746279751c48c2076f813259ef767ecce304d64
DEBUG s.a.a.h.a.i.c.SdkTlsSocketFactory:366 - Connecting socket to s3.us-east-1.amazonaws.com/52.217.41.86:443 with timeout 2000
...
```

The following `log4j2.xml` file configures the previous output.

```
<Configuration status="WARN">
    <Appenders>
        <Console name="ConsoleAppender" target="SYSTEM_OUT">
            <PatternLayout pattern="%-5p %c{1.}:%L - %m%n" />
        </Console>
    </Appenders>

    <Loggers>
        <Root level="WARN">
            <AppenderRef ref="ConsoleAppender"/>
        </Root>
        <Logger name="software.amazon.awssdk" level="DEBUG" />
    </Loggers>
</Configuration>
```

## Enable wire logging
<a name="sdk-java-logging-verbose"></a>

It can be useful to see the exact requests and responses that the SDK for Java 2.x sends and receives. If you need access to this information, you can temporarily enable it by adding the necessary configuration depending on the HTTP client the service client uses.

By default, synchronous service clients, such as the [S3Client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3Client.html), use an underlying Apache HttpClient, and asynchronous service clients, such as the [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html), use a Netty non-blocking HTTP client.

Here is a breakdown of HTTP clients you can use for the two categories of service clients:

| Synchronous HTTP Clients | Asynchronous HTTP Clients |
| --- | --- |
| [ApacheHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html) (default) | [NettyNioAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html) (default) |
| [UrlConnectionHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.html) | [AwsCrtAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtAsyncHttpClient.html) |
| [AwsCrtHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtHttpClient.html) |  |
| [Apache5HttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache5/Apache5HttpClient.html)  |

Consult the appropriate tab below for configuration settings you need to add depending on the underlying HTTP client.

**Warning**
We recommend you only use wire logging for debugging purposes. Disable it in your production environments because it can log sensitive data. It logs the full request or response without encryption, even for an HTTPS call. For large requests (e.g., to upload a file to Amazon S3) or responses, verbose wire logging can also significantly impact your application’s performance.

------
#### [ ApacheHttpClient ]

Add the "org.apache.http.wire" logger to the `log4j2.xml` configuration file and set the level to "DEBUG".

The following `log4j2.xml` file turns on full wire logging for the Apache HttpClient.

```
<Configuration status="WARN">
 <Appenders>
  <Console name="ConsoleAppender" target="SYSTEM_OUT">
   <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
  </Console>
 </Appenders>

 <Loggers>
  <Root level="WARN">
   <AppenderRef ref="ConsoleAppender"/>
  </Root>
  <Logger name="software.amazon.awssdk" level="WARN" />
  <Logger name="software.amazon.awssdk.request" level="DEBUG" />
  <Logger name="org.apache.http.wire" level="DEBUG" />
 </Loggers>
</Configuration>
```

An additional Maven dependency on the `log4j-1.2-api` artifact is required for wire logging with Apache since it uses 1.2 under the hood.

The full set of Maven dependencies for log4j 2, including wire logging for the Apache HTTP client are shown in the following build file snippets.

**Maven**

```
...
<dependencyManagement>
    ...
    <dependencies>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-bom</artifactId>
            <version>{{VERSION}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
     </dependencies>
</dependencyManagement>
...
<!-- The following is needed for Log4j2 with SLF4J -->
<dependency>
   <groupId>org.apache.logging.log4j</groupId>
   <artifactId>log4j-slf4j2-impl</artifactId>
</dependency>

<!-- The following is needed for Apache HttpClient wire logging -->
<dependency>
   <groupId>org.apache.logging.log4j</groupId>
   <artifactId>log4j-1.2-api</artifactId>
</dependency>
...
```

**Gradle–Kotlin DSL**

```
...
dependencies {
    ...
    implementation(platform("org.apache.logging.log4j:log4j-bom:{{VERSION}}"))
    implementation("org.apache.logging.log4j:log4j-slf4j2-impl")
    implementation("org.apache.logging.log4j:log4j-1.2-api")
}
...
```

Use `2.20.0` for the minimum version of the `log4j-bom` artifact. For the latest version, use the version published to [Maven central](https://central.sonatype.com/artifact/org.apache.logging.log4j/log4j-bom). Replace {{VERSION}} with version you'll use.

------
#### [ Apache5HttpClient ]

Add the "org.apache.hc.client5.http.wire" logger to the `log4j2.xml` configuration file and set the level to "DEBUG".

The following `log4j2.xml` file turns on full wire logging for the Apache5 HttpClient.

```
<Configuration status="WARN">
 <Appenders>
  <Console name="ConsoleAppender" target="SYSTEM_OUT">
   <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
  </Console>
 </Appenders>

 <Loggers>
  <Root level="WARN">
   <AppenderRef ref="ConsoleAppender"/>
  </Root>
  <Logger name="software.amazon.awssdk" level="WARN" />
  <Logger name="software.amazon.awssdk.request" level="DEBUG" />
  <Logger name="org.apache.hc.client5.http.wire" level="DEBUG" />
 </Loggers>
</Configuration>
```

------
#### [ UrlConnectionHttpClient ]

To log details for service clients that use the `UrlConnectionHttpClient`, first create a `logging.properties` file with the following contents:

```
handlers=java.util.logging.ConsoleHandler
java.util.logging.ConsoleHandler.level=FINEST
sun.net.www.protocol.http.HttpURLConnection.level=ALL
```

Set the following JVM system property with the full path of the `logging.properties`:

```
-Djava.util.logging.config.file=/full/path/to/logging.properties
```

This configuration will log the only the headers of the request and response, for example:

```
<Request>  FINE: sun.net.www.MessageHeader@35a9782c11 pairs: {GET /fileuploadtest HTTP/1.1: null}{amz-sdk-invocation-id: 5f7e707e-4ac5-bef5-ba62-00d71034ffdc}{amz-sdk-request: attempt=1; max=4}{Authorization: AWS4-HMAC-SHA256 Credential=<deleted>/20220927/us-east-1/s3/aws4_request, SignedHeaders=amz-sdk-invocation-id;amz-sdk-request;host;x-amz-content-sha256;x-amz-date;x-amz-te, Signature=e367fa0bc217a6a65675bb743e1280cf12fbe8d566196a816d948fdf0b42ca1a}{User-Agent: aws-sdk-java/2.17.230 Mac_OS_X/12.5 OpenJDK_64-Bit_Server_VM/25.332-b08 Java/1.8.0_332 vendor/Amazon.com_Inc. io/sync http/UrlConnection cfg/retry-mode/legacy}{x-amz-content-sha256: UNSIGNED-PAYLOAD}{X-Amz-Date: 20220927T133955Z}{x-amz-te: append-md5}{Host: tkhill-test1.s3.amazonaws.com}{Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2}{Connection: keep-alive}
<Response> FINE: sun.net.www.MessageHeader@70a36a6611 pairs: {null: HTTP/1.1 200 OK}{x-amz-id-2: sAFeZDOKdUMsBbkdjyDZw7P0oocb4C9KbiuzfJ6TWKQsGXHM/dFuOvr2tUb7Y1wEHGdJ3DSIxq0=}{x-amz-request-id: P9QW9SMZ97FKZ9X7}{Date: Tue, 27 Sep 2022 13:39:57 GMT}{Last-Modified: Tue, 13 Sep 2022 14:38:12 GMT}{ETag: "2cbe5ad4a064cedec33b452bebf48032"}{x-amz-transfer-encoding: append-md5}{Accept-Ranges: bytes}{Content-Type: text/plain}{Server: AmazonS3}{Content-Length: 67}
```

To see the request/response bodies, add `-Djavax.net.debug=all` to the JVM properties. This additional property logs a great deal of information, including all SSL information.

Within the log console or log file, search for `"GET"` or `"POST"` to quickly go to the section of the log containing actual requests and responses. Search for `"Plaintext before ENCRYPTION"` for requests and `"Plaintext after DECRYPTION"` for responses to see the full text of the headers and bodies.

------
#### [ NettyNioAsyncHttpClient ]

If your asynchronous service client uses the default `NettyNioAsyncHttpClient`, add two additional loggers to your `log4j2.xml` file to log HTTP headers and request/response bodies.

```
<Logger name="io.netty.handler.logging" level="DEBUG" />
<Logger name="io.netty.handler.codec.http2.Http2FrameLogger" level="DEBUG" />
```

Here is a complete `log4j2.xml` example:

```
<Configuration status="WARN">
    <Appenders>
        <Console name="ConsoleAppender" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c:%L - %m%n" />
        </Console>
    </Appenders>

    <Loggers>
        <Root level="WARN">
            <AppenderRef ref="ConsoleAppender"/>
        </Root>
        <Logger name="software.amazon.awssdk" level="WARN" />
        <Logger name="software.amazon.awssdk.request" level="DEBUG" />
        <Logger name="io.netty.handler.logging" level="DEBUG" />
        <Logger name="io.netty.handler.codec.http2.Http2FrameLogger" level="DEBUG" />
    </Loggers>
</Configuration>
```

These settings log all header details and request/response bodies.

------
#### [ AwsCrtAsyncHttpClient/AwsCrtHttpClient ]

If you have configured your service client to use an instance of an AWS CRT-based HTTP client, you can log details by setting JVM system properties or programmatically.

<table>
<tbody>
  <tr><td colspan="2"> <b>Log to a file at "Debug" level</b> </td></tr>
  <tr><td>Using system properties:<pre>-Daws.crt.log.level=Trace <br />-Daws.crt.log.destination=File <br />-Daws.crt.log.filename=<path to file></pre></td><td>Programmatically:<pre>import software.amazon.awssdk.crt.Log;<br /><br />// Execute this statement before constructing the SDK service client.<br />Log.initLoggingToFile(Log.LogLevel.Trace, "<path to file>");</pre></td></tr>
  <tr><td colspan="2"> <b>Log to the console at "Debug" level</b> </td></tr>
  <tr><td>Using system properties:<pre>-Daws.crt.log.level=Trace <br />-Daws.crt.log.destination=Stdout</pre></td><td>Programmatically:<pre>import software.amazon.awssdk.crt.Log;<br /><br />// Execute this statement before constructing the SDK service client.<br />Log.initLoggingToStdout(Log.LogLevel.Trace);</pre></td></tr>
</tbody>
</table>

For security reasons, at the "Trace" level the AWS CRT-based HTTP clients log only response headers. Request headers, request bodies, and response bodies are not logged.

------
