---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/troubleshooting.html
---

# Troubleshooting FAQs
<a name="troubleshooting"></a>

As you use the AWS SDK for Java 2.x in your applications, you might encounter the runtime errors listed in this topic. Use the suggestions here to help you uncover the root cause and resolve the error.

## How do I fix "`java.net.SocketException`: Connection reset" or "server failed to complete the response" error?
<a name="faq-socketexception"></a>

A connection reset error indicates that your host, the AWS service, or any intermediary party (for example, a NAT gateway, a proxy, a load balancer) closed the connection before the request was complete. Because there are many causes, finding a solution requires that you know why the connection is being closed. The following items commonly cause a connection to be closed.
+ **The connection is inactive. **This is common for streaming operations, where data is not being written to or from the wire for a period of time, so an intermediary party detects the connection as dead and closes it. To prevent this, be sure your application actively downloads or uploads data.
+ **You've closed the HTTP or SDK client.** Be sure not to close resources while they are in use.
+ **A misconfigured proxy.** Try to bypass any proxies that you've configured to see if it fixes the problem. If this fixes the issue, the proxy is closing your connection for some reason. Research your specific proxy to determine why it's closing the connection.

If you cannot identify the problem, try running a TCP dump for an affected connection at the client edge of your network (for example, after any proxies that you control).

If you see that the AWS endpoint is sending a `TCP RST` (reset), [contact the affected service](https://aws.amazon.com/contact-us/) to see if they can determine why the reset is occurring. Be prepared to provide request IDs and timestamps of when the issue occurred. The AWS support team might also benefit from [wire logs](logging-slf4j.md#sdk-java-logging-verbose) that show exactly what bytes your application is sending and receiving and when.

## How do I fix "connection timeout"?
<a name="faq-connection-timeout"></a>

A connection timeout error indicates that your host, the AWS service, or any intermediary party (for example, a NAT gateway, a proxy, a load balancer) failed to establish a new connection with the server within the configured connection timeout. The following items describe common causes of this issue.
+ **The configured connection timeout is too low.** By default, the connection timeout is 2 seconds in the AWS SDK for Java 2.x. If you set the connection timeout too low, you may get this error. The recommended connection timeout is 1 second if you make only in-region calls and 3 seconds if you make cross-region requests.
+ **A misconfigured proxy.** Try to bypass any proxies that you configured to see if it fixes the problem. If this fixes the issue, the proxy is the reason for the connection timeout. Research your specific proxy to determine why that is happening

If you cannot identify the problem, try running a TCP dump for an affected connection at the client edge of your network (for example, after any proxies that you control) to investigate any network issue.

## How do I fix "`java.net.SocketTimeoutException`: Read timed out"?
<a name="faq-socket-timeout"></a>

A read timed out error indicates that the JVM attempted to read data from the underlying operating system, but data was not returned within the time configured via the SDK. This error can occur if the operating system, the AWS service, or any intermediary party (for example, a NAT gateway, a proxy, a load balancers) fails to send data within the time expected by the JVM. Because there are many causes, finding a solution requires that you know why the data is not being returned.

Try running a TCP dump for an affected connection at the client edge of your network (for example, after any proxies that you control).

If you see that the AWS endpoint is sending a `TCP RST` (reset), [contact the affected service](https://aws.amazon.com/contact-us/). Be prepared to provide request IDs and timestamps of when the issue occurred. The AWS support team might also benefit from [wire logs](logging-slf4j.md#sdk-java-logging-verbose) that show exactly what bytes your application is sending and receiving and when.

## How do I fix "Unable to execute HTTP request: Timeout waiting for connection from pool" error?
<a name="faq-pool-timeout"></a>

This error indicates that a request cannot get a connection from the pool within the specified maximum time. To troubleshoot the issue, we recommend that you [enable SDK client-side metrics](metrics.md) to publish metrics to Amazon CloudWatch. The HTTP metrics can help narrow down the root cause. The following items describe common causes of this error.
+ **Connection leak.** You can investigate this by checking `LeasedConcurrency` , `AvailableConcurrency`, and `MaxConcurrency` metrics. If `LeasedConcurrency` increases until it reaches `MaxConcurrency` but never decreases, there may be a connection leak. A common cause of a leak is because a streaming operation—such as a S3 `getObject` method—is not closed. We recommend that your application read all data from the input stream as soon as possible and [close the input stream afterwards](best-practices.md#bestpractice2). The following chart shows what SDK metrics might look like for connection leak.
![A screenshot of CloudWatch metrics that show a likely connection leak.](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/images/JavaDevGuide-connection-leak-metrics-chart.png)
+ **Connection pool starvation. **This can happen if your request rate is too high and the connection pool size that has been configured cannot meet the request demand. The default connection pool size is 50, and when the connections in the pool reach the maximum, the HTTP client queues incoming requests until connections become available. The following chart shows what SDK metrics might look like for connection pool starvation.
![A screenshot of CloudWatch metrics that shows how connection pool starvation might look like.](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/images/JavaDevGuide-connection-pool-starvation-chart.png)

  To mitigate this issue, consider taking any of the following actions.
  + Increase the connection pool size,
  + Increase acquire timeout.
  + Slow the request rate.

  By increasing the maximum number of connections, client throughput can increase (unless the network interface is already fully utilized). However, you can eventually hit operation system limitations on the number of file descriptors used by the process. If you already fully use your network interface or cannot further increase your connection count, try increasing the acquire timeout. With the increase, you gain extra time for requests to acquire a connection before timing out. If the connections don't free up, the subsequent requests will still timeout.

  If you are unable to fix the issue by using the first two mechanisms, slow the request rate by trying the following options.
  + Smooth out your requests so that large traffic bursts don't overload the client.
  + Be more efficient with calls to AWS services.
  + Increase the number of hosts sending requests.
+ **I/O Threads are too busy.** This only applies if you are using an asynchronous SDK client with [`NettyNioAsyncHttpClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html). If the `AvailableConcurrency` metric is not low—indicating that connections are available in the pool—but `ConcurrencyAcquireDuration` is high, it might be because I/O threads are not able to handle the requests. Be sure you are not passing `Runnable:run` as a [future completion executor](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/client/config/SdkAdvancedAsyncClientOption.html#FUTURE_COMPLETION_EXECUTOR) and performing time-consuming task in the response future completion chain since this can block an I/O thread. If that is not the case, consider increasing the number of I/O threads by using the `[eventLoopGroupBuilder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.Builder.html#eventLoopGroupBuilder(software.amazon.awssdk.http.nio.netty.SdkEventLoopGroup.Builder))` method. For reference, the default number of I/O threads for a `NettyNioAsyncHttpClient` instance is twice the number of CPU cores of the host.
+ **High TLS handshake latency.** If your `AvailableConcurrency` metric is near 0 and `LeasedConcurrency` is lower than `MaxConcurrency`, it might be because the TLS handshake latency is high. The following chart shows what SDK metrics might look like for high TLS handshake latency.
![A screenshot of CloudWatch metrics that might indicate high TLS handshake latency.](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/images/JavaDevGuide-high-tls-latency-chart.png)

  For HTTP clients offered by the Java SDK that are not based on CRT, try enabling [TLS logs](security-java-tls.md) to troubleshoot TLS issues. For the AWS CRT-based HTTP client, try enabling [AWS CRT logs](logging-slf4j.md#sdk-java-logging-verbose). If you see that the AWS endpoint seems to take a long time to perform a TLS handshake, you should [contact the affected service](https://aws.amazon.com/contact-us/).

## How do I fix a `NoClassDefFoundError`, `NoSuchMethodError` or `NoSuchFieldError`?
<a name="faq-classpath-errors"></a>

A `NoClassDefFoundError` indicates that a class could not be loaded at runtime. The two most common causes for this error are:
+ the class does not exist in the classpath because the JAR is missing or the wrong version of the JAR is on the classpath.
+ the class failed to load because its static initializer threw an exception.

Similarly, `NoSuchMethodError`s and `NoSuchFieldError`s typically result from a mismatched JAR version. We recommend that you perform the following steps.

1. **Check your dependencies** to make sure that you're using the *same version of all SDK jars*. The most common reason that a class, method, or field cannot be found is when you upgrade to a new client version but you continue to use an old 'shared' SDK dependency version. The new client version might attempt to use classes that exist only in newer 'shared' SDK dependencies. Try running `mvn dependency:tree` or `gradle dependencies` (for Gradle) to verify that the SDK library versions all match. To avoid this issue completely in the future, we recommend using [BOM (Bill of Materials)](setup-project-maven.md#sdk-as-dependency) to manage SDK module versions.

   The following example shows you an example of mixed SDK versions.

   ```
   [INFO] +- software.amazon.awssdk:dynamodb:jar:2.20.00:compile
   [INFO] |  +- software.amazon.awssdk:aws-core:jar:2.13.19:compile
   [INFO] +- software.amazon.awssdk:netty-nio-client:jar:2.20.00:compile
   ```

   The version of `dynamodb` is 2.20.00 and the version of `aws-core` is 2.13.19. The `aws-core` artifact version should also be 2.20.00.

1. **Check statements early in your logs** to see if a class is failing to load because of a static initialization failure. The first time the class fails to load, it may throw a different, more useful exception that specifies *why* the class cannot be loaded. This potentially useful exception occurs only once, so later log statements will only report that the class is not found.

1. **Check your deployment process** to make sure that it actually deploys required JAR files along with your application. It's possible that you're building with the correct version, but the process that creates the classpath for your application is excluding a required dependency.

## How do I fix a "`SignatureDoesNotMatch`" error or "The request signature we calculated does not match the signature you provided" error?
<a name="faq-signature-does-not-match-error"></a>

A `SignatureDoesNotMatch` error indicates that the signature generated by the AWS SDK for Java and the signature generated by the AWS service do not match. The following items describe potential causes.
+ A proxy or intermediary party modifies the request. For example, a proxy or load balancer might modify a header, path or query string that was signed by the SDK.
+ The service and SDK differ in the way they encode the request when each generates the string to sign.

To debug this issue, we recommend that you [enable debug logging](logging-slf4j.md#sdk-debug-level-logging) for the SDK. Try to reproduce the error and find the canonical request that the SDK generated. In the log, the canonical request is labeled with `AWS4 Canonical Request: ...` and the string to sign is labeled `AWS4 String to sign: ...` .

If you cannot enable debugging—for example, because it's only reproducible in production—add logic to your application that logs information about the request when the error occurs. You can then use that information to try to replicate the error outside of production in an integration test with debug logging enabled.

After you have collected the canonical request and string to sign, compare them against the [AWS Signature Version 4 specification](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) to determine if there are any issues in the way the SDK generated the string to sign. If something seems wrong, you can create a [GitHub bug report](https://github.com/aws/aws-sdk-java-v2/issues/new/choose) to the AWS SDK for Java.

If nothing appears wrong, you can compare the SDK's string to sign with the string to sign that some AWS services return as part of the failure response (Amazon S3, for example) . If this isn't available, you should [contact the affected service](https://aws.amazon.com/contact-us/) to see what canonical request and string to sign they generated for comparison. These comparisons can help to identify intermediary parties that might have modified the request or encoding differences between the service and client.

For more background information about signing requests, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) in the AWS Identity and Access Management User Guide.

**Example of a canonical request**

```
PUT
/Example-Bucket/Example-Object
partNumber=19&uploadId=string
amz-sdk-invocation-id:f8c2799d-367c-f024-e8fa-6ad6d0a1afb9
amz-sdk-request:attempt=1; max=4
content-encoding:aws-chunked
content-length:51
content-type:application/octet-stream
host:xxxxx
x-amz-content-sha256:STREAMING-UNSIGNED-PAYLOAD-TRAILER
x-amz-date:20240308T034733Z
x-amz-decoded-content-length:10
x-amz-sdk-checksum-algorithm:CRC32
x-amz-trailer:x-amz-checksum-crc32
```

**Example of a string to sign**

```
AWS4-HMAC-SHA256
20240308T034435Z
20240308/us-east-1/s3/aws4_request
5f20a7604b1ef65dd89c333fd66736fdef9578d11a4f5d22d289597c387dc713
```

## How do I fix "`java.lang.IllegalStateException`: Connection pool shut down" error?
<a name="faq-connection-pool-shutdown-exception"></a>

This error indicates the underlying Apache HTTP connection pool was closed. The following items describe potential causes.
+ **The SDK client was closed prematurely. **The SDK only closes the connection pool when the associated client is closed. Be sure not to close resources while they are in use.
+ **A `java.lang.Error` was thrown.** Errors such as `OutOfMemoryError` cause an Apache HTTP connection pool to [shut down](https://github.com/apache/httpcomponents-client/blob/6a741b4f8f23e6c5c7cc42c36c2acabfac19c3d6/httpclient/src/main/java/org/apache/http/impl/execchain/MainClientExec.java#L368). Examine your logs for error stack traces. Also review your code for places where it catches `Throwable`s or `Error`s but swallows the output that prevents the error from surfacing. If your code does not report errors, rewrite the code so information is logged. The logged information helps determine the root cause of the error.
+ **You attempted to use the credentials provider returned from `DefaultCredentialsProvider#create()` after it was closed**. [`DefaultCredentialsProvider#create`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/DefaultCredentialsProvider.html#create()) returns a singleton instance, so if it's closed and your code calls the `resolveCredentials` method, the exception is thrown after cached credentials (or token) expire.

  Check your code for places where the `DefaultCredentialsProvider` is closed, as shown in the following examples.
  + The singleton instance is closed by calling `DefaultCredentialsProvider#close().`

    ```
    DefaultCredentialsProvider defaultCredentialsProvider = DefaultCredentialsProvider.create(); // Singleton instance returned.
    AwsCredentials credentials = defaultCredentialsProvider.resolveCredentials();

    // Make calls to AWS services.

    defaultCredentialsProvider.close();  // Explicit close.

    // Make calls to AWS services.

    // After the credentials expire, either of the following calls eventually results in a "Connection pool shut down" exception.
    credentials = defaultCredentialsProvider.resolveCredentials();
    // Or
    credentials = DefaultCredentialsProvider.create().resolveCredentials();
    ```
  + Invoke `DefaultCredentialsProvider#create()` in a try-with-resources block.

    ```
    try (DefaultCredentialsProvider defaultCredentialsProvider = DefaultCredentialsProvider.create()) {
        AwsCredentials credentials = defaultCredentialsProvider.resolveCredentials();

        // Make calls to AWS services.

    } // After the try-with-resources block exits, the singleton DefaultCredentialsProvider is closed.

    // Make calls to AWS services.

    DefaultCredentialsProvider defaultCredentialsProvider = DefaultCredentialsProvider.create(); // The closed singleton instance is returned.
    // If the credentials (or token) has expired, the following call results in the error.
    AwsCredentials credentials = defaultCredentialsProvider.resolveCredentials();
    ```

  Create a new, non-singleton instance by calling `DefaultCredentialsProvider.builder().build()` if your code has closed the singleton instance and you need to resolve credentials by using a `DefaultCredentialsProvider`.

## How do I fix "Unable to load credentials from any of the providers in the chain AwsCredentialsProviderChain"?
<a name="faq-credentials-provider-chain"></a>

This error indicates that the AWS SDK for Java 2.x could not find valid AWS credentials through any of the credential providers in the default credential provider chain. The SDK automatically searches for credentials in a specific order, and this error occurs when all providers in the chain fail to provide valid credentials.

The full error message typically looks like this (line endings and indents added to improve readability):

```
Unable to load credentials from any of the providers in the chain AwsCredentialsProviderChain(
    credentialsProviders=[
        SystemPropertyCredentialsProvider(),
        EnvironmentVariableCredentialsProvider(),
        WebIdentityTokenCredentialsProvider(),
        ProfileCredentialsProvider(profileName=default, profileFile=ProfileFile(sections=[])),
        ContainerCredentialsProvider(),
        InstanceProfileCredentialsProvider()
    ]) : [
        SystemPropertyCredentialsProvider(): Unable to load credentials from system settings.
        Access key must be specified either via environment variable (AWS_ACCESS_KEY_ID)
        or system property (aws.accessKeyId).,

        EnvironmentVariableCredentialsProvider(): Unable to load credentials from system settings.
        Access key must be specified either via environment variable (AWS_ACCESS_KEY_ID)
        or system property (aws.accessKeyId).,

        WebIdentityTokenCredentialsProvider(): To use web identity tokens, the 'sts' service module
        must be on the class path.,

        ProfileCredentialsProvider(profileName=default, profileFile=ProfileFile(sections=[])):
        Profile file contained no credentials for profile 'default': ProfileFile(sections=[]),

        ContainerCredentialsProvider(): Cannot fetch credentials from container - neither
        AWS_CONTAINER_CREDENTIALS_FULL_URI or AWS_CONTAINER_CREDENTIALS_RELATIVE_URI environment
        variables are set.,

        InstanceProfileCredentialsProvider(): Failed to load credentials from IMDS.]
```

### Common causes and solutions
<a name="faq-cred-provider-chain-common-causes-and-solutions"></a>

#### Review your credential configuration
<a name="faq-cred-provider-chain-check-config"></a>

When you use the default credentials provider (by calling `ServiceClient.create()` without explicitly configuring credentials), the SDK searches for credentials in a specific order. Review [how the default credential provider chain works](credentials-chain.md) to understand which credential sources the SDK checks and in what order.

Ensure that the credential configuration method you intend to use is properly set up in your environment:

##### For Amazon EC2 instances
<a name="faq-cred-check-ec2"></a>
+ **Check IAM role:** Verify that an IAM role is attached to your instance.
+ **Intermittent IMDS failures:** If you're experiencing intermittent failures (typically lasting a few hundred milliseconds), this usually indicates transient network issues reaching the Instance Metadata Service (IMDS).

  Solutions:
  + Enable [debug logging](logging-slf4j.md#sdk-debug-level-logging) to analyze the timing and frequency of failures
  + Consider implementing retry logic in your application for credential-related failures
  + Check for network connectivity issues between your instance and the IMDS endpoint

##### For container environments
<a name="faq-cred-check-container-env"></a>

Confirm that task roles (Amazon ECS) or service accounts (Amazon EKS) are configured and that required environment variables are set.

##### For local development
<a name="faq-cred-check-local-dev"></a>

Check that environment variables, credentials files, or IAM Identity Center configuration is in place.

##### For web identity federation
<a name="faq-cred-check-web-id-federation"></a>
+ **Verify configuration: **Verify that the web identity token file exists and that the required environment variables are configured.
+ **Missing STS module dependency:** If you see the error `To use web identity tokens, the 'sts' service module must be on the class path`, you need to add the STS module as a dependency. This is common when using Amazon EKS Pod Identity or other web identity token authentication.

  Solution: Add the STS module to your project dependencies:
  +

    ```
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>sts</artifactId>
    </dependency>
    ```

    For some services, you might also need the `aws-query-protocol` dependency:

    ```
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>aws-query-protocol</artifactId>
    </dependency>
    ```

#### Network or proxy connectivity issues
<a name="faq-credentials-provider-chain-network-issues"></a>

If you see `Connection refused` errors in the credential provider chain, this typically indicates network connectivity problems when the SDK tries to reach AWS endpoints.

**Solutions:**
+ Verify proxy configuration if you're using a proxy server
+ Check that your network allows outbound HTTPS connections to AWS endpoints
+ Enable [debug logging](logging-slf4j.md#sdk-debug-level-logging) to see detailed connection attempts
+ Test connectivity using tools like `curl` to verify network access to AWS endpoints
