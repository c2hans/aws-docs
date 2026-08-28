---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-apache5.html
---

# Configure the Apache 5.x based HTTP client
<a name="http-configuration-apache5"></a>

## Access the Apache5HttpClient
<a name="http-apache-5-dependency"></a>

In order to use the `Apache5HttpClient` you must add a dependency on **apache5-client** and explicitly configure `Apache5HttpClient` on your service clients.

```
<dependencyManagement>
   <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>{{2.41.0*}}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>s3</artifactId>
    </dependency>

    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>apache5-client</artifactId>
    </dependency>
</dependencies>
```

\*Replace the version shown in red with the version of the Java SDK that you want to use. Find the latest on [Maven Central](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

### Use and configure the `Apache5HttpClient`
<a name="http-config-apache-5-config"></a>

You can configure an instance of `Apache5HttpClient` along with building a service client, or you can configure a single instance to share across multiple service clients.

With either approach, you use the [Apache5HttpClient.Builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache5/Apache5HttpClient.Builder.html) to configure the properties for the Apache 5 based HTTP client.

#### Best practice: dedicate an Apache5HttpClient instance to a service client
<a name="http-apache5-dedicated-instance"></a>

If you need to configure an instance of the `Apache5HttpClient`, we recommend that you build the dedicated `Apache5HttpClient` instance. You can do so by using the httpClientBuilder method of the service client's builder. This way, the lifecycle of the HTTP client is managed by the SDK, which helps avoid potential memory leaks if the `Apache5HttpClient` instance is not closed down when it's no longer needed.

The following example creates an S3Client and configures the embedded instance of `Apache5HttpClient` with maxConnections and connectionTimeout values. The HTTP instance is created using the `httpClientBuilder` method of `S3Client.Builder`.

**Imports**

```
import software.amazon.awssdk.http.apache5.Apache5HttpClient;
import software.amazon.awssdk.services.s3.S3Client;
import java.time.Duration;
```

**Code**

```
S3Client s3Client = S3Client   // Singleton: Use the s3Client for all requests.
    .builder()
    .httpClientBuilder(Apache5HttpClient.builder()
        .maxConnections(100)
        .connectionTimeout(Duration.ofSeconds(5))
    )
    .build();

// Perform work with the s3Client.

s3Client.close();   // Requests completed: Close all service clients.
```

#### Alternative approach: share an `Apache5HttpClient` instance
<a name="http-apache5-shared-instance"></a>

To help keep resource and memory usage lower for your application, you can configure an `Apache5HttpClient` and share it across multiple service clients. The HTTP connection pool will be shared, which lowers resource usage.

**Note**
When an `Apache5HttpClient` instance is shared, you must close it when it is ready to be disposed. The SDK will not close the instance when the service client is closed.

The following example configures an Apache-based HTTP client that is used by two service clients. The configured `ApacheHttpClient` instance is passed to the httpClient method of each builder. When the service clients and the HTTP client are no longer needed, the code explicitly closes them. The code closes the HTTP client last.

**Imports**

```
import software.amazon.awssdk.http.SdkHttpClient;
import software.amazon.awssdk.http.apache5.Apache5HttpClient;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.s3.S3Client;
```

**Code**

```
SdkHttpClient apache5HttpClient = Apache5HttpClient.builder()
        .maxConnections(100).build();

// Singletons: Use the s3Client and dynamoDbClient for all requests.
S3Client s3Client =
    S3Client.builder()
            .httpClient(apache5HttpClient).build();

DynamoDbClient dynamoDbClient =
    DynamoDbClient.builder()
                  .httpClient(apache5HttpClient).build();

// Perform work with the s3Client and dynamoDbClient.

// Requests completed: Close all service clients.
s3Client.close();
dynamoDbClient.close();
apache5HttpClient.close();  // Explicitly close apache5HttpClient.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
