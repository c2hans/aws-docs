---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-config-proxy-support.html
---

# Configure HTTP proxies
<a name="http-config-proxy-support"></a>

You can configure HTTP proxies by using code, by setting Java system properties, or by setting environment variables.

## Configure in code
<a name="http-config-proxy-support-in-code"></a>

You configure proxies in code with a client-specific `ProxyConfiguration` builder when you build the service client. The following code shows an example proxy configuration for an Apache-based HTTP client that is used by an Amazon S3 service client.

```
SdkHttpClient httpClient1 = ApacheHttpClient.builder()
    .proxyConfiguration(ProxyConfiguration.builder()
        .endpoint(URI.create("http://proxy.example.com"))
        .username("username")
        .password("password")
        .addNonProxyHost("localhost")
        .build())
    .build();

S3Client s3Client = S3Client.builder()
    .httpClient(httpClient)
    .build();
```

The section for each HTTP client in this topic shows a proxy configuration example.
+ [Apache HTTP client](http-configuration-apache.md#http-configuration-apache-proxy-conf-ex)
+ [URLConnection-based HTTP client](http-configuration-url.md#http-configuration-url-proxy-conf-ex)
+ [Netty-based HTTP client](http-configuration-netty.md#http-config-netty-proxy-ex)
+ [AWS CRT-based HTTP client](http-configuration-crt.md#http-config-crt-proxy-ex)

## Configure HTTP proxies with external settings
<a name="http-config-proxy-support-external"></a>

Even if you don't explicitly use a `ProxyConfiguration` builder in code, the SDK looks for external settings to configure a default proxy configuration.

By default, the SDK first searches for JVM system properties. If even one property is found, the SDK uses the value and any other system property values. If no system properties are available, the SDK looks for proxy environment variables.

The SDK can use the following Java system properties and environment variables.

**Java system properties**

| System property | Description | HTTP client support |
| --- | --- | --- |
| http.proxyHost | Host name of the HTTP proxy server | All |
| http.proxyPort | Port number of the HTTP proxy server | All |
| http.proxyUser | Username for HTTP proxy authentication | All |
| http.proxyPassword | Password for HTTP proxy authentication | All |
| http.nonProxyHosts | List of hosts that should be reached directly, bypassing the proxy. [This list is also valid when HTTPS is used](https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html). | All |
| https.proxyHost | Host name of the HTTPS proxy server | Netty, CRT |
| https.proxyPort | Port number of the HTTPS proxy server | Netty, CRT |
| https.proxyUser | Username for HTTPS proxy authentication | Netty, CRT |
| https.proxyPassword | Password for HTTPS proxy authentication | Netty, CRT |

**Environment variables**

| Environment variable | Description | HTTP client support |
| --- | --- | --- |
| HTTP\_PROXY1 | A valid URL with a scheme of HTTP | All |
| HTTPS\_PROXY1 | A valid URL with a scheme of HTTPS | Netty, CRT |
| NO\_PROXY2 | List of hosts that should be reached directly, bypassing the proxy. The list is valid for both HTTP and HTTPS. | All |

### View key and footnotes
<a name="http-config-proxy-support-ext-key-footnote"></a>

**All** - All HTTP clients offered by the SDK–`UrlConnectionHttpClient`, `ApacheHttpClient`, `NettyNioAsyncHttpClient`, `AwsCrtAsyncHttpClient`.

**Netty** - The Netty-based HTTP client (`NettyNioAsyncHttpClient`).

**CRT** - The AWS CRT-based HTTP clients, (`AwsCrtHttpClient` and `AwsCrtAsyncHttpClient`).

1The environment variable queried, whether `HTTP_PROXY` or `HTTPS_PROXY`, depends on the scheme setting in the client's `ProxyConfiguration`. The default scheme is HTTP. The following snippet shows how to change the scheme to HTTPS used for environment variable resolution.

```
SdkHttpClient httpClient = ApacheHttpClient.builder()
    .proxyConfiguration(ProxyConfiguration.builder()
        .scheme("https")
        .build())
    .build();
```

2The `NO_PROXY` environment variable supports a mix of "\|" and "," separators between host names. For supported wildcard formats, see [nonProxyHosts wildcard behavior](#http-config-proxy-nonproxyhosts-behavior).

## Use a combination of settings
<a name="http-config-proxy-support-combo"></a>

You can use a combination of HTTP proxy settings in code, system properties, and environment variables.

**Example – configuration provided by a system property and by code**

```
// Command line with the proxy password set as a system property.
$ java -Dhttp.proxyPassword=SYS_PROP_password -cp ... App

// Since the 'useSystemPropertyValues' setting is 'true' (the default), the SDK will supplement
// the proxy configuration in code with the 'http.proxyPassword' value from the system property.
SdkHttpClient apacheHttpClient = ApacheHttpClient.builder()
            .proxyConfiguration(ProxyConfiguration.builder()
                    .endpoint(URI.create("http://localhost:1234"))
                    .username("username")
                    .build())
            .build();

// Use the apache HTTP client with proxy configuration.
DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
                    .httpClient(apacheHttpClient)
                    .build();
```
The SDK resolves the following proxy settings.

```
Host = localhost
Port = 1234
Password = SYS_PROP_password
UserName = username
Non ProxyHost = null
```

**Example – both system properties and environment variables are available**
Each HTTP client's `ProxyConfiguration` builder offers settings named `useSystemPropertyValues` and `useEnvironmentVariablesValues`. By default, both setting are `true`. When `true`, the SDK automatically uses values from system properties or environment variables for options that are not provided by the `ProxyConfiguration` builder.
System properties take precedence over environment variables. If an HTTP proxy system property is found, the SDK retrieves ***all*** values from system properties and none from environment variables. If you want to prioritize environment variables over system properties, set `useSystemPropertyValues` to `false`.
For this example, the following settings are available a runtime:

```
// System properties
http.proxyHost=SYS_PROP_HOST.com
http.proxyPort=2222
http.password=SYS_PROP_PASSWORD
http.user=SYS_PROP_USER

// Environment variables
HTTP_PROXY="http://EnvironmentUser:EnvironmentPassword@ENV_VAR_HOST:3333"
NO_PROXY="environmentnonproxy.host,environmentnonproxy2.host:1234"
```
The service client is created with one of the following statements. None of the statements explicitly set a proxy setting.

```
DynamoDbClient client = DynamoDbClient.create();
DynamoDbClient client = DynamoDbClient.builder().build();
DynamoDbClient client = DynamoDbClient.builder()
    .httpClient(ApacheHttpClient.builder()
        .proxyConfiguration(ProxyConfiguration.builder()
            .build())
        .build())
    .build();
```
The following proxy settings are resolved by the SDK:

```
Host = SYS_PROP_HOST.com
Port = 2222
Password = SYS_PROP_PASSWORD
UserName = SYS_PROP_USER
Non ProxyHost = null
```
Because the service client has default proxy settings, the SDK searches for system properties and then environment variables. Since system properties settings take precedence over environment variables, the SDK uses only system properties.
If the use of system properties is changed to `false` as shown in the following code, the SDK resolves only the environment variables.

```
DynamoDbClient client = DynamoDbClient.builder()
    .httpClient(ApacheHttpClient.builder()
        .proxyConfiguration(ProxyConfiguration.builder()
            .useSystemPropertyValues(Boolean.FALSE)
            .build())
        .build())
    .build();
```
The resolved proxy settings using HTTP are:

```
Host = ENV_VAR_HOST
Port = 3333
Password = EnvironmentPassword
UserName = EnvironmentUser
Non ProxyHost = environmentnonproxy.host, environmentnonproxy2.host:1234
```

## nonProxyHosts wildcard behavior
<a name="http-config-proxy-nonproxyhosts-behavior"></a>

With `nonProxyHosts`, you can specify the hosts that bypass the proxy. Set this value through the `ProxyConfiguration` builder, the `http.nonProxyHosts` system property, or the `NO_PROXY` environment variable. Each source supports the following entry formats.
+ **Exact host**: `example.com` (matches only the specified host)
+ **Leading wildcard**: `*.example.com` (matches the domain and all subdomains)
+ **Bare wildcard**: `*` (bypasses all hosts)
+ **CIDR range**: `10.0.0.0/8` (matches all IP addresses in the range)

### Behavior differences across HTTP clients
<a name="http-config-proxy-nonproxyhosts-behavior-diffs"></a>

The HTTP client type and entry source affect two important matching behaviors.

#### Builder entries compared with external settings
<a name="http-config-proxy-nonproxyhosts-builder-vs-external"></a>

When you supply wildcard entries (`*.example.com` or `*`) through the `nonProxyHosts(Set)` or `addNonProxyHost(String)` methods on the `ProxyConfiguration` builder, wildcards work only with the AWS CRT-based HTTP clients (`AwsCrtHttpClient` and `AwsCrtAsyncHttpClient`).

The Apache, Netty, and URLConnection-based clients throw a `PatternSyntaxException` for wildcard entries that you supply through the builder.

When entries come from the `http.nonProxyHosts` system property or the `NO_PROXY` environment variable, wildcards work with all clients.

**Important**
If you need wildcards to work across all HTTP clients, use the `http.nonProxyHosts` system property or the `NO_PROXY` environment variable instead of the builder.

#### Root-domain matching for leading wildcard entries
<a name="http-config-proxy-nonproxyhosts-root-domain"></a>

The AWS CRT-based clients and the other HTTP clients handle the `*.example.com` pattern differently:
+ **CRT-based clients**: `*.example.com` matches both the root domain (`example.com`) and subdomains (for example, `api.example.com`).
+ **Apache, Netty, and URLConnection-based clients**: `*.example.com` matches only subdomains. The root domain `example.com` doesn't match, and the SDK routes it through the proxy.

### Summary of wildcard behavior by entry source
<a name="http-config-proxy-nonproxyhosts-summary-table"></a>

The following table summarizes the matching behavior when you supply entries through the `http.nonProxyHosts` system property or the `NO_PROXY` environment variable. All clients support wildcards from these sources.

| Entry format | Non-CRT clients (Apache, Netty, and URLConnection) | CRT-based clients |
| --- | --- | --- |
| Exact host (`example.com`) | Honored | Honored |
| Leading wildcard (`*.example.com`) | Honored (subdomains only) | Honored (root domain and subdomains) |
| Bare wildcard (`*`) | Honored | Honored |
| CIDR range (`10.0.0.0/8`) | Honored | Honored |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
