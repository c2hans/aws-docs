---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html
---

# Configure AWS CRT-based HTTP clients
<a name="http-configuration-crt"></a>

The AWS CRT-based HTTP clients include the synchronous [AwsCrtHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtHttpClient.html) and asynchronous [AwsCrtAsyncHttpClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtAsyncHttpClient.html). The AWS CRT-based HTTP clients provide the following HTTP client benefits:
+ Faster SDK startup time
+ Smaller memory footprint
+ Reduced latency time
+ Connection health management
+ DNS load balancing

**AWS CRT-based components in the SDK**

The AWS CRT-based* HTTP* clients, described in this topic, and the AWS CRT-based *S3* client are different components in the SDK.

The synchronous and asynchronous **AWS CRT-based HTTP clients** are implementations SDK HTTP client interfaces and are used for general HTTP communication. They are alternatives to the other synchronous or asynchronous HTTP clients in the SDK with additional benefits.

The **[AWS CRT-based S3 client](crt-based-s3-client.md)** is an implementation of the [S3AsyncClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html) interface and is used for working with the Amazon S3 service. It is an alternative to the Java-based implementation of the `S3AsyncClient` interface and offers several advantages.

Although both components use libraries from the [AWS Common Runtime](https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html), the AWS CRT-based HTTP clients do not use the [aws-c-s3 library](https://github.com/awslabs/aws-c-s3) and do not support the [S3 multipart upload API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) features. The AWS CRT-based S3 client, by contrast, was purpose-built to support the S3 multipart upload API features.

## Access the AWS CRT-based HTTP clients
<a name="http-config-crt-access"></a>

Before you can use the AWS CRT-based HTTP clients, add the `aws-crt-client` artifact with a minimum version of 2.22.0 to your project's dependencies.

Use one of the following options to set up your Maven `pom.xml` file.

**Note**
 You might choose to use the *Platform-specific jar option* if you need to keep the size of the runtime dependencies smaller, for example if your application runs in an AWS Lambda function.

------
#### [ Uber-jar option ]

By default, the `aws-crt-client` uses an uber-jar of AWS CRT artifacts that contains binaries for several platforms, including Linux, Windows, and macOS.

```
<project>
   <properties>
     <aws.sdk.java.version>{{2.29.10*}}</aws.sdk.java.version>
  </properties>
  <dependencyManagement>
   <dependencies>
      <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>bom</artifactId>
        <version>${aws.sdk.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
   </dependencies>
  </dependencyManagement>
  <dependencies>
   <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>aws-crt-client</artifactId>
   </dependency>
  </dependencies>
</project>
```

\*Replace the version shown in red with the version of the Java SDK that you want to use. Find the latest on [Maven Central](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

------
#### [ Platform-specific jar option ]

To restrict the Java runtime to platform-specific version of the AWS CRT library, make the following changes to the *Uber-jar option*.
+ Add an `exclusions` element to the SDK's `aws-crt-client` artifact. This exclusion prevents the SDK from transitively using the AWS CRT uber-jar.
+ Add a dependency element for the specific AWS CRT platform version you need. See the **Steps to determine the AWS CRT artifact version** below for how you can determine the correct version.

```
<project>
   <properties>
     <aws.sdk.java.version>{{2.29.101}}</aws.sdk.java.version>
  </properties>
   <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>software.amazon.awssdk</groupId>
                <artifactId>bom</artifactId>
                <version>${aws.sdk.java.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>aws-crt-client</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>software.amazon.awssdk.crt</groupId>
                    <artifactId>aws-crt</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>software.amazon.awssdk.crt</groupId>
            <artifactId>aws-crt</artifactId>
            <version>{{0.31.32}}</version>
            <classifier>{{linux-x86_643}}</classifier>
        </dependency>
    </dependencies>
```

1Replace the version shown in red with the version of the Java SDK that you want to use. Find the latest on [Maven Central](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

2Replace the version of `software.amazon.awssdk.crt:aws-crt` that would be provided by the *Uber-jar option*. See the following **Steps to determine the AWS CRT artifact version**.

3Replace the `classifier` value with one for your platform. Refer to the AWS CRT for Java GitHub page for a [listing of available values](https://github.com/awslabs/aws-crt-java?tab=readme-ov-file#platform-specific-jars).

**Steps to determine the AWS CRT artifact version**

Use the following steps to determine the AWS CRT artifact version that is compatible with the version of the SDK for Java that you are using.

1. Set up your `pom.xml` file as shown in the *Uber-jar option*. This setup allows you to see what version of `software.amazon.awssdk.crt:aws-crt` the SDK brings in by default.

1. At the root of the project (in the same directory as the `pom.xml` file), run the following Maven command:

   ```
   mvn dependency:tree -Dincludes=software.amazon.awssdk.crt:aws-crt
   ```

   Maven might perform other actions, but at the end you should see console output of the `software.amazon.awssdk.crt:aws-crt` dependency that the SDK transitively uses. The following snippet shows sample output based on an SDK version of `2.29.10`:

   ```
   [INFO] org.example:yourProject:jar:1.0-SNAPSHOT
   [INFO] \- software.amazon.awssdk:aws-crt-client:jar:2.29.10:compile
   [INFO]    \- software.amazon.awssdk.crt:aws-crt:jar:0.31.3:compile
   ```

1. Use the version that the console shows for the `software.amazon.awssdk.crt:aws-crt` artifact. In this case, add `0.31.3` to your `pom.xml` file.

------

## Use and configure an AWS CRT-based HTTP client
<a name="http-crt-config"></a>

You can configure an AWS CRT-based HTTP client along with building a service client, or you can configure a single instance to share across multiple service clients.

With either approach, you use a builder to [configure the properties](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtHttpClient.Builder.html) for the AWS CRT-based HTTP client instance.

### Best practice: dedicate an instance to a service client
<a name="http-config-crt-one-client"></a>

If you need to configure an instance of an AWS CRT-based HTTP client, we recommend that you dedicate the instance by building it along with the service client . You can do so by using the `httpClientBuilder` method of the service client's builder. This way, the lifecycle of the HTTP client is managed by the SDK, which helps avoid potential memory leaks if the AWS CRT-based HTTP client instance is not closed down when it's no longer needed.

The following example creates an S3 service client and configures an AWS CRT-based HTTP client with `connectionTimeout` and `maxConcurrency` values.

------
#### [ Synchronous client ]

**Imports**

```
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import java.time.Duration;
```

**Code**

```
// Singleton: Use s3Client for all requests.
S3Client s3Client = S3Client.builder()
    .httpClientBuilder(AwsCrtHttpClient
        .builder()
        .connectionTimeout(Duration.ofSeconds(3))
        .maxConcurrency(100))
    .build();

// Perform work with the s3Client.

// Requests completed: Close the s3Client.
s3Client.close();
```

------
#### [ Asynchronous client ]

**Imports**

```
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import java.time.Duration;
```

**Code**

```
// Singleton: Use s3AsyncClient for all requests.
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
    .httpClientBuilder(AwsCrtAsyncHttpClient
        .builder()
        .connectionTimeout(Duration.ofSeconds(3))
        .maxConcurrency(100))
    .build();

// Perform work with the s3AsyncClient.

// Requests completed: Close the s3AsyncClient.
s3AsyncClient.close();
```

------

### Alternative approach: share an instance
<a name="http-config-crt-multi-clients"></a>

To help keep resource and memory usage lower for your application, you can configure an AWS CRT-based HTTP client and share it across multiple service clients. The HTTP connection pool will be shared, which lowers resource usage.

**Note**
When an AWS CRT-based HTTP client instance is shared, you must close it when it is ready to be disposed. The SDK will not close the instance when the service client is closed.

The following example configures an AWS CRT-based HTTP client instance with `connectionTimeout` and `maxConcurrency` values. The configured instance is passed to the `httpClient` method of each service client's builder. When the service clients and the HTTP client are no longer needed, they are explicitly closed. The HTTP client is closed last.

------
#### [ Synchronous client ]

**Imports**

```
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.awscore.defaultsmode.DefaultsMode;
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.s3.S3Client;
import java.time.Duration;
```

**Code**

```
// Create an AwsCrtHttpClient shared instance.
SdkHttpClient crtHttpClient = AwsCrtHttpClient.builder()
    .connectionTimeout(Duration.ofSeconds(3))
    .maxConcurrency(100)
    .build();

// Singletons: Use the s3Client and dynamoDbClient for all requests.
S3Client s3Client = S3Client.builder()
    .httpClient(crtHttpClient)
    .credentialsProvider(EnvironmentVariableCredentialsProvider.crea
    .defaultsMode(DefaultsMode.IN_REGION)
    .region(Region.US_EAST_1)
    .build();

DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
    .httpClient(crtHttpClient)
    .credentialsProvider(EnvironmentVariableCredentialsProvider.crea
    .defaultsMode(DefaultsMode.IN_REGION)
    .region(Region.US_EAST_1)
    .build();

// Requests completed: Close all service clients.
s3Client.close();
dynamoDbClient.close();
crtHttpClient.close();  // Explicitly close crtHttpClient.
```

------
#### [ Asynchronous client ]

**Imports**

```
import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.awscore.defaultsmode.DefaultsMode;
import software.amazon.awssdk.http.async.SdkAsyncHttpClient;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import java.time.Duration;
```

**Code**

```
// Create an AwsCrtAsyncHttpClient shared instance.
SdkAsyncHttpClient crtAsyncHttpClient = AwsCrtAsyncHttpClient.builder()
    .connectionTimeout(Duration.ofSeconds(3))
    .maxConcurrency(100)
    .build();

// Singletons: Use the s3AsyncClient and dynamoDbAsyncClient for all requests.
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
    .httpClient(crtAsyncHttpClient)
    .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
    .defaultsMode(DefaultsMode.IN_REGION)
    .region(Region.US_EAST_1)
    .build();

DynamoDbAsyncClient dynamoDbAsyncClient = DynamoDbAsyncClient.builder()
    .httpClient(crtAsyncHttpClient)
    .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
    .defaultsMode(DefaultsMode.IN_REGION)
    .region(Region.US_EAST_1)
    .build();

// Requests completed: Close all service clients.
s3AsyncClient.close();
dynamoDbAsyncClient.close();
crtAsyncHttpClient.close();  // Explicitly close crtAsyncHttpClient.
```

------

## Set an AWS CRT-based HTTP client as the default
<a name="setting-the-crt-based-http-client-as-the-default"></a>

You can setup your Maven build file to have the SDK use an AWS CRT-based HTTP client as the default HTTP client for service clients.

You do this by adding an `exclusions` element with the default HTTP client dependencies to each service client artifact.

In the following `pom.xml` example, the SDK uses an AWS CRT-based HTTP client for S3 services. If the service client in your code is an `S3AsyncClient`, the SDK uses `AwsCrtAsyncHttpClient`. If the service client is an S3Client, the SDK uses `AwsCrtHttpClient`. With this setup the default Netty-based asynchronous HTTP client and the default Apache-based synchronous HTTP are not available.

```
<project>
   <properties>
     <aws.sdk.version>{{VERSION}}</aws.sdk.version>
  </properties>
  <dependencies>
   <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>s3</artifactId>
      <version>${aws.sdk.version}</version>
      <exclusions>
         <exclusion>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>netty-nio-client</artifactId>
         </exclusion>
         <exclusion>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>apache-client</artifactId>
         </exclusion>
      </exclusions>
   </dependency>
   <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>aws-crt-client</artifactId>
   </dependency>
  </dependencies>
</project>
```

Visit the Maven central repository for the latest [{{VERSION}}](https://central.sonatype.com/artifact/software.amazon.awssdk/bom) value.

**Note**
If multiple service clients are declared in a `pom.xml` file, all require the `exclusions` XML element.

### Use a Java system property
<a name="setting-via-java-system-property"></a>

To use the AWS CRT-based HTTP clients as the default HTTP for your application, you can set the Java system property `software.amazon.awssdk.http.async.service.impl` to a value of `software.amazon.awssdk.http.crt.AwsCrtSdkHttpService`.

To set during application startup, run a command similar to the following.

```
java app.jar -Dsoftware.amazon.awssdk.http.async.service.impl=\
software.amazon.awssdk.http.crt.AwsCrtSdkHttpService
```

Use the following code snippet to set the system property in your application code.

```
System.setProperty("software.amazon.awssdk.http.async.service.impl",
"software.amazon.awssdk.http.crt.AwsCrtSdkHttpService");
```

**Note**
You need to add a dependency on the `aws-crt-client` artifact in your `poml.xml` file when you use a system property to configure the use of the AWS CRT-based HTTP clients.

## Advanced configuration of AWS CRT-based HTTP clients
<a name="configuring-the-crt-based-http-client"></a>

You can use various configuration settings of the AWS CRT-based HTTP clients, including connection health configuration and maximum idle time. You can review the configuration [options available](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/AwsCrtAsyncHttpClient.Builder.html) for the `AwsCrtAsyncHttpClient`. You can configure the same options for the `AwsCrtHttpClient`.

### Connection health configuration
<a name="connection-health-checks"></a>

You can configure connection health configuration for the AWS CRT-based HTTP clients by using the `connectionHealthConfiguration` method on the HTTP client builder.

The following example creates an S3 service client that uses a AWS CRT-based HTTP client instance configured with connection health configuration and a maximum idle time for connections.

------
#### [ Synchronous client ]

**Imports**

```
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import java.time.Duration;
```

**Code**

```
// Singleton: Use the s3Client for all requests.
S3Client s3Client = S3Client.builder()
    .httpClientBuilder(AwsCrtHttpClient
        .builder()
        .connectionHealthConfiguration(builder -> builder
            .minimumThroughputInBps(32000L)
            .minimumThroughputTimeout(Duration.ofSeconds(3)))
        .connectionMaxIdleTime(Duration.ofSeconds(5)))
    .build();

// Perform work with s3Client.

// Requests complete: Close the service client.
s3Client.close();
```

------
#### [ Asynchronous client ]

**Imports**

```
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import java.time.Duration;
```

**Code**

```
// Singleton: Use the s3AsyncClient for all requests.
S3AsyncClient s3AsyncClient = S3AsyncClient.builder()
    .httpClientBuilder(AwsCrtAsyncHttpClient
        .builder()
        .connectionHealthConfiguration(builder -> builder
            .minimumThroughputInBps(32000L)
            .minimumThroughputTimeout(Duration.ofSeconds(3)))
        .connectionMaxIdleTime(Duration.ofSeconds(5)))
    .build();

// Perform work with s3AsyncClient.

// Requests complete: Close the service client.
s3AsyncClient.close();
```

------

## Proxy configuration example
<a name="http-config-crt-proxy-ex"></a>

The following code snippet shows the use of the [`ProxyConfiguration.Builder`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/crt/ProxyConfiguration.Builder.html) that you use to configure proxy setting in code.

------
#### [ Synchronous client ]

**Imports**

```
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.crt.AwsCrtHttpClient;
import software.amazon.awssdk.http.crt.ProxyConfiguration;
```

**Code**

```
SdkHttpClient crtHttpClient = AwsCrtHttpClient.builder()
    .proxyConfiguration(ProxyConfiguration.builder()
        .scheme("https")
        .host("myproxy")
        .port(1234)
        .username("username")
        .password("password")
        .nonProxyHosts(Set.of("localhost", "host.example.com"))
        .build())
    .build();
```

------
#### [ Asynchronous client ]

**Imports**

```
import software.amazon.awssdk.http.async.SdkAsyncHttpClient;
import software.amazon.awssdk.http.crt.AwsCrtAsyncHttpClient;
import software.amazon.awssdk.http.crt.ProxyConfiguration;
```

**Code**

```
SdkAsyncHttpClient crtAsyncHttpClient = AwsCrtAsyncHttpClient.builder()
    .proxyConfiguration(ProxyConfiguration.builder()
        .scheme("https")
        .host("myproxy")
        .port(1234)
        .username("username")
        .password("password")
        .nonProxyHosts(Set.of("localhost", "host.example.com"))
        .build())
    .build();
```

------

The equivalent Java system properties for the proxy configuration are shown in the following command line snippet.

```
$ java -Dhttps.proxyHost=myproxy -Dhttps.proxyPort=1234 -Dhttps.proxyUser=username \
-Dhttps.proxyPassword=password -Dhttp.nonProxyHosts=localhost|host.example.com -cp ... App
```

**Important**
To use any of the HTTPS proxy system properties, the `scheme` property must be set in code to `https`. If the scheme property is not set in code, the scheme defaults to HTTP and the SDK looks only for `http.*` system properties.

The equivalent setup that uses environment variables is:

```
// Set the following environment variables.
// $ export HTTPS_PROXY="https://username:password@myproxy:1234"
// $ export NO_PROXY="localhost|host.example.com"

// Set the 'useSystemPropertyValues' to false on the proxy configuration.
SdkAsyncHttpClient crtAsyncHttpClient = AwsCrtAsyncHttpClient.builder()
    .proxyConfiguration(ProxyConfiguration.builder()
        .scheme("https")
        .useSystemPropertyValues(Boolean.FALSE)
        .build())
    .build();

// Run the application.
// $ java -cp ... App
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
