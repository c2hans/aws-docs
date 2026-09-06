---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-url.html
---

# Configure the URLConnection-based HTTP client
<a name="http-configuration-url"></a>

The AWS SDK for Java 2.x offers a lighter-weight `[UrlConnectionHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.html)` HTTP client in comparison to the default `ApacheHttpClient`. The `UrlConnectionHttpClient` is based on Java's `[URLConnection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URLConnection.html)`.

The `UrlConnectionHttpClient` loads more quickly than the Apache-based HTTP client, but has fewer features. Because it loads more quickly, it is a [good solution](lambda-optimize-starttime.md) for Java AWS Lambda functions.

The `UrlConnectionHttpClient` has several [configurable options](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.Builder.html) that you can access.

**Note**
The `UrlConnectionHttpClient` does not support the HTTP PATCH method.
A handful of AWS API operations require PATCH requests. Those operation names usually start with `Update*`. The following are several examples.
[Several `Update*` operations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html) in the AWS Security Hub CSPM API and also the [BatchUpdateFindings](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) operation
All Amazon API Gateway API [`Update*` operations](https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateAccount.html)
If you might use the `UrlConnectionHttpClient`, first refer to the API Reference for the AWS service that you're using. Check to see if the operations you need use the PATCH operation.

**Note**
The `UrlConnectionHttpClient` does not support a configurable idle connection timeout.
Connection pooling is managed internally by the JVM. To configure the idle timeout, set the JVM system property `http.keepAlive.time.server` to the desired value in seconds:

```
$ java -Dhttp.keepAlive.time.server=60 -cp ... App
```
This is a JVM-global setting that affects all `HttpURLConnection` usage in the process, not just SDK clients. If you need per-client control over idle connection timeout, use the `ApacheHttpClient` with the `connectionMaxIdleTime` setting.

## Access the `UrlConnectionHttpClient`
<a name="http-url-dependency"></a>

To configure and use the `UrlConnectionHttpClient`, you declare a dependency on the `url-connection-client` Maven artifact in your `pom.xml` file.

Unlike the `ApacheHttpClient`, the `UrlConnectionHttpClient` is not automatically added to your project, so use must specifically declare it.

The following example of a `pom.xml` file shows the dependencies required to use and configure the HTTP client.

```
<dependencyManagement>
   <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>2.27.21</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<!-- other dependencies such as s3 or dynamodb -->

<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>url-connection-client</artifactId>
    </dependency>
</dependencies>
```

## Use and configure the `UrlConnectionHttpClient`
<a name="http-url-config"></a>

You can configure an instance of `UrlConnectionHttpClient` along with building a service client, or you can configure a single instance to share across multiple service clients.

With either approach, you use the [UrlConnectionHttpClient.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/UrlConnectionHttpClient.Builder.html) to configure the properties for the URLConnection-based HTTP client.

### Best practice: dedicate an `UrlConnectionHttpClient` instance to a service client
<a name="http-config-url-one-client"></a>

If you need to configure an instance of the `UrlConnectionHttpClient`, we recommend that you build the dedicated `UrlConnectionHttpClient` instance. You can do so by using the `httpClientBuilder` method of the service client's builder. This way, the lifecycle of the HTTP client is managed by the SDK, which helps avoid potential memory leaks if the `UrlConnectionHttpClient` instance is not closed down when it's no longer needed.

The following example creates an `S3Client` and configures the embedded instance of `UrlConnectionHttpClient` with `socketTimeout` and `proxyConfiguration` values. The `proxyConfiguration` method takes a Java lambda expression of type ` Consumer<[ProxyConfiguration.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/ProxyConfiguration.Builder.html)>`.

 **Imports**

```
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import java.net.URI;
import java.time.Duration;
```

 **Code**

```
// Singleton: Use the s3Client for all requests.
S3Client s3Client =
    S3Client.builder()
            .httpClientBuilder(UrlConnectionHttpClient.builder()
                    .socketTimeout(Duration.ofMinutes(5))
                    .proxyConfiguration(proxy -> proxy.endpoint(URI.create("http://proxy.mydomain.net:8888"))))
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .build();

// Perform work with the s3Client.

s3Client.close();   // Requests completed: Close the s3client.
```

### Alternative approach: share an `UrlConnectionHttpClient` instance
<a name="http-config-url-multi-clients"></a>

To help keep resource and memory usage lower for your application, you can configure an `UrlConnectionHttpClient` and share it across multiple service clients. The HTTP connection pool will be shared, which lowers resource usage.

**Note**
When an `UrlConnectionHttpClient` instance is shared, you must close it when it is ready to be disposed. The SDK will not close the instance when the service client is closed.

The following example configures an URLConnection-based HTTP client that is used by two service clients. The configured `UrlConnectionHttpClient` instance is passed to the `httpClient` method of each builder. When the service clients and the HTTP client are no longer needed, the code explicitly closes them. The code closes the HTTP client last.

**Imports**

```
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.awscore.defaultsmode.DefaultsMode;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.urlconnection.ProxyConfiguration;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.s3.S3Client;
import java.net.URI;
import java.time.Duration;
```

 **Code**

```
SdkHttpClient urlHttpClient = UrlConnectionHttpClient.create();

// Singletons: Use the s3Client and dynamoDbClient for all requests.
S3Client s3Client =
    S3Client.builder()
            .httpClient(urlHttpClient)
            .defaultsMode(DefaultsMode.IN_REGION)
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .build();

DynamoDbClient dynamoDbClient =
    DynamoDbClient.builder()
                  .httpClient(urlHttpClient)
                  .defaultsMode(DefaultsMode.IN_REGION)
                  .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
                  .build();

// Perform work with the s3Client and dynamoDbClient.

// Requests completed: Close all service clients.
s3Client.close();
dynamoDbClient.close();
urlHttpClient.close();
```

#### Use `URLConnectionHttpClient` and `ApacheHttpClient` together
<a name="http-config-url-caveat"></a>

When you use the `UrlConnectionHttpClient` in your application, you must supply each service client with either a `URLConnectionHttpClient` instance or a `ApacheHttpClient` instance using the service client builder's `httpClientBuilder` method.

An exception occurs if your program uses multiple service clients and both of the following are true:
+ One service client is configured to use a `UrlConnectionHttpClient` instance
+ Another service client uses the default `ApacheHttpClient` without explicitly building it with the `httpClient()` or `httpClientBuilder()` methods

The exception will state that multiple HTTP implementations were found on the classpath.

The following example code snippet leads to an exception.

```
// The dynamoDbClient uses the UrlConnectionHttpClient
DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
        .httpClient(UrlConnectionHttpClient.create())
        .build();

// The s3Client below uses the ApacheHttpClient at runtime, without specifying it.
// An SdkClientException is thrown with the message that multiple HTTP implementations were found on the classpath.
S3Client s3Client = S3Client.create();

// Perform work with the s3Client and dynamoDbClient.

dynamoDbClient.close();
s3Client.close();
```

Avoid the exception by explicitly configuring the `S3Client` with an `ApacheHttpClient`.

```
DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
        .httpClient(UrlConnectionHttpClient.create())
        .build();

S3Client s3Client = S3Client.builder()
        .httpClient(ApacheHttpClient.create())    // Explicitly build the ApacheHttpClient.
        .build();

// Perform work with the s3Client and dynamoDbClient.

dynamoDbClient.close();
s3Client.close();
```

**Note**
To explicitly create the `ApacheHttpClient`, you must [add a dependency](http-configuration-apache.md#http-apache-dependency) on the `apache-client` artifact in your Maven project file.

## Proxy configuration example
<a name="http-configuration-url-proxy-conf-ex"></a>

The following code snippet uses the [proxy configuration builder for the URL connection HTTP client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/urlconnection/ProxyConfiguration.Builder.html).

```
SdkHttpClient urlHttpClient = UrlConnectionHttpClient.builder()
                .proxyConfiguration(ProxyConfiguration.builder()
                        .endpoint(URI.create("http://example.com:1234"))
                        .username("username")
                        .password("password")
                        .addNonProxyHost("localhost")
                        .addNonProxyHost("host.example.com")
                        .build())
                .build();
```

The equivalent Java system properties for the proxy configuration are shown in the following command line snippet.

```
$ java -Dhttp.proxyHost=example.com -Dhttp.proxyPort=1234 -Dhttp.proxyUser=username \
-Dhttp.proxyPassword=password -Dhttp.nonProxyHosts=localhost|host.example.com -cp ... App
```

The equivalent setup that uses environment variables is:

```
// Set the following environment variables.
// $ export HTTP_PROXY="http://username:password@example.com:1234"
// $ export NO_PROXY="localhost|host.example.com"

// Set the 'useSystemPropertyValues' to false on the proxy configuration.
SdkHttpClient apacheHttpClient = UrlConnectionHttpClient.builder()
                .proxyConfiguration(ProxyConfiguration.builder()
                        .useSystemPropertyValues(Boolean.FALSE)
                        .build())
                .build();

// Run the application.
// $ java -cp ... App
```

**Note**
The URLConnection-based HTTP client does not currently support HTTPS proxy system properties or the HTTPS\_PROXY environment variable.
