---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/client-configuration.html
---

# Client configuration
<a name="client-configuration"></a>

In 1.x, SDK client configuration was modified by setting a `ClientConfiguration` instance on the client or client builder. In version 2.x, the client configuration is split into separate configuration classes. With the separate configuration classes, you can configure different HTTP clients for async versus synchronous clients but still use the same `ClientOverrideConfiguration` class.

**Example of client configuration in version 1.x**

```
AmazonDynamoDBClientBuilder.standard()
.withClientConfiguration(clientConfiguration)
.build()
```

**Example of synchronous client configuration in version 2.x**

```
ProxyConfiguration.Builder proxyConfig = ProxyConfiguration.builder();

ApacheHttpClient.Builder httpClientBuilder =
        ApacheHttpClient.builder()
                        .proxyConfiguration(proxyConfig.build());

ClientOverrideConfiguration.Builder overrideConfig =
        ClientOverrideConfiguration.builder();

DynamoDbClient client =
        DynamoDbClient.builder()
                      .httpClientBuilder(httpClientBuilder)
                      .overrideConfiguration(overrideConfig.build())
                      .build();
```

**Example of asynchronous client configuration in version 2.x**

```
NettyNioAsyncHttpClient.Builder httpClientBuilder =
        NettyNioAsyncHttpClient.builder();

ClientOverrideConfiguration.Builder overrideConfig =
        ClientOverrideConfiguration.builder();

ClientAsyncConfiguration.Builder asyncConfig =
        ClientAsyncConfiguration.builder();

DynamoDbAsyncClient client =
        DynamoDbAsyncClient.builder()
                           .httpClientBuilder(httpClientBuilder)
                           .overrideConfiguration(overrideConfig.build())
                           .asyncConfiguration(asyncConfig.build())
                           .build();
```

## HTTP clients
<a name="client-configuration-http"></a>

### Notable changes
<a name="client-configuration-http-notables"></a>
+ In version 2.x, you can change which HTTP client to use at runtime by specifying an implementation using `clientBuilder.httpClientBuilder`.
+ When you pass an HTTP client by using `clientBuilder.httpClient` to a service client builder, the HTTP client is not closed by default if the service client closes. This allows you to share HTTP clients between service clients.
+ Asynchronous HTTP clients now use non-blocking IO.
+ Some operations now use HTTP/2 for improved performance.

### Settings changes
<a name="client-configuration-http-setting-diffs"></a>

| Setting | 1.x | 2.x Sync, Apache | 2.x Async, Netty |
| --- | --- | --- | --- |
|  |  <pre>ClientConfiguration clientConfig = <br />    new ClientConfiguration()</pre>  |  <pre>ApacheHttpClient.Builder httpClientBuilder = <br />    ApacheHttpClient.builder()</pre>  |  <pre>NettyNioAsyncHttpClient.Builder httpClientBuilder = <br />    NettyNioAsyncHttpClient.builder()</pre>  |
| Max connections |  <pre>clientConfig.setMaxConnections(...)<br />clientConfig.withMaxConnections(...)</pre>  |  <pre>httpClientBuilder.maxConnections(...)</pre>  |  <pre>httpClientBuilder.maxConcurrency(...)</pre>  |
| Connection timeout |  <pre>clientConfig.setConnectionTimeout(...)<br />clientConfig.withConnectionTimeout(...)</pre>  |  <pre>httpClientBuilder.connectionTimeout(...)<br />httpClientBuilder.connectionAcquisitionTimeout(...)</pre>  |  <pre>httpClientBuilder.connectionTimeout(...)</pre>  |
| Socket timeout |  <pre>clientConfig.setSocketTimeout(...)<br />clientConfig.withSocketTimeout(...)</pre>  |  <pre>httpClientBuilder.socketTimeout(...)</pre>  |  <pre>httpClientBuilder.writeTimeout(...)<br />httpClientBuilder.readTimeout(...)</pre>  |
| Connection TTL |  <pre>clientConfig.setConnectionTTL(...)<br />clientConfig.withConnectionTTL(...)</pre>  |  <pre>httpClientBuilder.connectionTimeToLive(...)</pre>  |  <pre>httpClientBuilder.connectionTimeToLive(...)</pre>  |
| Connection max idle |  <pre>clientConfig.setConnectionMaxIdleMillis(...)<br />clientConfig.withConnectionMaxIdleMillis(...)</pre>  |  <pre>httpClientBuilder.connectionMaxIdleTime(...)</pre>  |  <pre>httpClientBuilder.connectionMaxIdleTime(...)</pre>  |
| Validate after inactivity |  <pre>clientConfig.setValidateAfterInactivityMillis(...)<br />clientConfig.withValidateAfterInactivityMillis(...)</pre>  | Not supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Local address |  <pre>clientConfig.setLocalAddress(...)<br />clientConfig.withLocalAddress(...)</pre>  |  <pre>httpClientBuilder.localAddress(...)</pre>  | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/857) |
| Expect-continue enabled |  <pre>clientConfig.setUseExpectContinue(...)<br />clientConfig.withUseExpectContinue(...)</pre>  |  <pre>httpClientBuilder.expectContinueEnabled(...)</pre>  | Not supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Connection reaper |  <pre>clientConfig.setUseReaper(...)<br />clientConfig.withReaper(...)</pre>  |  <pre>httpClientBuilder.useIdleConnectionReaper(...)</pre>  |  <pre>httpClientBuilder.useIdleConnectionReaper(...)</pre>  |
|  |  <pre>AmazonDynamoDBClientBuilder.standard()<br />    .withClientConfiguration(clientConfiguration)<br />    .build()</pre>  |  <pre>DynamoDbClient.builder()<br />    .httpClientBuilder(httpClientBuilder)<br />    .build()</pre>  |  <pre>DynamoDbAsyncClient.builder()<br />.httpClientBuilder(httpClientBuilder)<br />.build()</pre>  |

## HTTP client proxies
<a name="client-configuration-http-proxy"></a>

| Settings | 1.x | 2.x Sync, Apache | 2.x Async, Netty |
| --- | --- | --- | --- |
|  |  <pre>ClientConfiguration clientConfig =<br />    new ClientConfiguration()</pre>  |  <pre>ProxyConfiguration.Builder proxyConfig =<br />    ProxyConfiguration.builder()</pre>  |  <pre>ProxyConfiguration.Builder proxyConfig =<br />    ProxyConfiguration.builder()</pre>  |
| Proxy host |  <pre>clientConfig.setProxyHost(...)<br />clientConfig.withProxyHost(...)</pre>  |  <pre>proxyConfig.endpoint(...)</pre>  |  <pre>proxyConfig.host(...)</pre>  |
| Proxy port |  <pre>clientConfig.setProxyPort(...)<br />clientConfig.withProxyPort(...)</pre>  | <pre>proxyConfig.endpoint(...)</pre>[Proxy port](http-configuration-apache.md#http-configuration-apache-proxy-conf-ex) is embedded in `endpoint` |  <pre>proxyConfig.port(...)</pre>  |
| Proxy username |  <pre>clientConfig.setProxyUsername(...)<br />clientConfig.withProxyUsername(...)</pre>  |  <pre>proxyConfig.username(...)</pre>  |  <pre>proxyConfig.username(...)</pre>  |
| Proxy password |  <pre>clientConfig.setProxyPassword(...)<br />clientConfig.withProxyPassword(...)</pre>  |  <pre>proxyConfig.password(...)</pre>  |  <pre>proxyConfig.password(...)</pre>  |
| Proxy domain |  <pre>clientConfig.setProxyDomain(...)<br />clientConfig.withProxyDomain(...)</pre>  |  <pre>proxyConfig.ntlmDomain(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Proxy workstation |  <pre>clientConfig.setProxyWorkspace(...)<br />clientConfig.withProxyWorkstation(...)</pre>  |  <pre>proxyConfig.ntlmWorkstation(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Proxy authentication methods |  <pre>clientConfig.setProxyAuthenticationMethods(...)<br />clientConfig.withProxyAuthenticationMethods(...)</pre>  | [Not Supported](https://github.com/aws/aws-sdk-java-v2/issues/858) | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Preemptive basic proxy authentication |  <pre>clientConfig.setPreemptiveBasicProxyAuth(...)<br />clientConfig.withPreemptiveBasicProxyAuth(...)</pre>  |  <pre>proxyConfig.preemptiveBasicAuthenticationEnabled(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Non-proxy hosts |  <pre>clientConfig.setNonProxyHosts(...)<br />clientConfig.withNonProxyHosts(...)</pre>  |  <pre>proxyConfig.nonProxyHosts(...)</pre>  |  <pre>proxyConfig.nonProxyHosts(...)</pre>  |
| Disable socket proxy |  <pre>clientConfig.setDisableSocketProxy(...)<br />clientConfig.withDisableSocketProxy(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|  |  <pre>AmazonDynamoDBClientBuilder.standard()<br />    .withClientConfiguration(clientConfiguration)<br />    .build()</pre>  |  <pre>httpClientBuilder.proxyConfiguration(<br />    proxyConfig.build())</pre>  |  <pre>httpClientBuilder.proxyConfiguration(<br />    proxyConfig.build())</pre>  |

## Client overrides
<a name="client-override-config-diffs"></a>

| Setting | 1.x | 2.x |
| --- | --- | --- |
|  |  <pre>ClientConfiguration clientConfig =<br />    new ClientConfiguration()</pre>  |  <pre>ClientOverrideConfiguration.Builder overrideConfig =<br />    ClientOverrideConfiguration.builder()</pre>  |
| User agent prefix |  <pre>clientConfig.setUserAgentPrefix(...)<br />clientConfig.withUserAgentPrefix(...)</pre>  |  <pre>overrideConfig.advancedOption(<br />    SdkAdvancedClientOption.USER_AGENT_PREFIX, ...)</pre>  |
| User agent suffix |  <pre>clientConfig.setUserAgentSuffix(...)<br />clientConfig.withUserAgentSuffix(...)</pre>  |  <pre>overrideConfig.advancedOption(<br />    SdkAdvancedClientOption.USER_AGENT_SUFFIX, ...)</pre>  |
| Signer |  <pre>clientConfig.setSignerOverride(...)<br />clientConfig.withSignerOverride(...)</pre>  |  <pre>overrideConfig.advancedOption(<br />    SdkAdvancedClientOption.SIGNER, ...)</pre>  |
| Additional headers |  <pre>clientConfig.addHeader(...)<br />clientConfig.withHeader(...)</pre>  |  <pre>overrideConfig.putHeader(...)</pre>  |
| Request timeout |  <pre>clientConfig.setRequestTimeout(...)<br />clientConfig.withRequestTimeout(...)</pre>  |  <pre>overrideConfig.apiCallAttemptTimeout(...)</pre>  |
| Client execution timeout |  <pre>clientConfig.setClientExecutionTimeout(...)<br />clientConfig.withClientExecutionTimeout(...)</pre>  |  <pre>overrideConfig.apiCallTimeout(...)</pre>  |
| Use Gzip |  <pre>clientConfig.setUseGzip(...)<br />clientConfig.withGzip(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Socket buffer size hint |  <pre>clientConfig.setSocketBufferSizeHints(...)<br />clientConfig.withSocketBufferSizeHints(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Cache response metadata |  <pre>clientConfig.setCacheResponseMetadata(...)<br />clientConfig.withCacheResponseMetadata(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| Response metadata cache size |  <pre>clientConfig.setResponseMetadataCacheSize(...)<br />clientConfig.withResponseMetadataCacheSize(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| DNS resolver |  <pre>clientConfig.setDnsResolver(...)<br />clientConfig.withDnsResolver(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
| TCP keepalive |  <pre>clientConfig.setUseTcpKeepAlive(...)<br />clientConfig.withTcpKeepAlive(...)</pre>  | This option is now in the HTTP Client configuration<pre>- ApacheHttpClient.builder().tcpKeepAlive(true)<br />- NettyNioAsyncHttpClient.builder().tcpKeepAlive(true)</pre> |
| Secure random |  <pre>clientConfig.setSecureRandom(...)<br />clientConfig.withSecureRandom(...)</pre>  | Not Supported ([Request Feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|  |  <pre>AmazonDynamoDBClientBuilder.standard()<br />    .withClientConfiguration(clientConfiguration)<br />    .build()</pre>  |  <pre>DynamoDbClient.builder()<br />    .overrideConfiguration(overrideConfig.build())<br />    .build()</pre>  |

## Client override retries
<a name="client-override-retry-config-diffs"></a>

| Setting | 1.x | 2.x |
| --- | --- | --- |
|  |  <pre>ClientConfiguration clientConfig =<br />    new ClientConfiguration()</pre>  |  <pre>ClientOverrideConfiguration.Builder overrideConfigBuilder = <br />    ClientOverrideConfiguration.builder();</pre>  |
| Max error retry |  <pre>clientConfig.setMaxErrorRetry(...)<br />clientConfig.withMaxErrorRetry(...)</pre>  |  <pre>// Configure the default retry strategy.<br />overrideConfigBuilder.retryStrategy(b -> b.maxAttempts(...));</pre>  |
| Use throttled retries |  <pre>clientConfig.setUseThrottleRetries(...)<br />clientConfig.withUseThrottleRetries(...)</pre>  | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/645) |
| Max consecutive retries before throttling |  <pre>clientConfig.setMaxConsecutiveRetriesBeforeThrottling(...)<br />clientConfig.withMaxConsecutiveRetriesBeforeThrottling(...)</pre>  | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/645) |
|  |  <pre>AmazonDynamoDBClientBuilder.standard()<br />    .withClientConfiguration(clientConfiguration)<br />    .build()</pre>  |  <pre>DynamoDbClient.builder()<br />        .overrideConfiguration(overrideConfigBuilder.build())<br />        .build();<br /><br />// You also have the option to use a lambda expression to configure and<br />// build the 'ClientOverrideConfiguration.Builder'.<br />DynamoDbClient client = DynamoDbClient.builder()<br />        .overrideConfiguration(o -> o.retryStrategy(b -> b.maxAttempts(5)))<br />        .build();</pre>  |

## Asynchronous clients
<a name="client-async-config-diffs"></a>

| Setting | 1.x | 2.x |
| --- | --- | --- |
|  |  |  <pre>ClientAsyncConfiguration.Builder asyncConfig =<br />    ClientAsyncConfiguration.builder()</pre>  |
| Executor |  <pre>AmazonDynamoDBAsyncClientBuilder.standard()<br />    .withExecutorFactory(...)<br />    .build()</pre>  |  <pre>asyncConfig.advancedOption(<br />    SdkAdvancedAsyncClientOption.FUTURE_COMPLETION_EXECUTOR, ...)</pre>  |
|  |  |  <pre>DynamoDbAsyncClient.builder()<br />    .asyncConfiguration(asyncConfig)<br />    .build()</pre>  |

## Other client changes
<a name="client-config-other-diffs"></a>

The following `ClientConfiguration` option from 1.x has changed in 2.x of the SDK and doesn't have a direct equivalent.

| Setting | 1.x | 2.x equivalent |
| --- | --- | --- |
| Protocol |  <pre>clientConfig.setProtocol(Protocol.HTTP)<br />clientConfig.withProtocol(Protocol.HTTP)</pre>  | The protocol setting is HTTPS by default. To modify the setting, specify the protocol setting an HTTP endpoint on the client builder:<pre>clientBuilder.endpointOverride(<br />    URI.create("http://..."))</pre> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
