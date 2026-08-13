---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/interceptors.html
---

# Use execution interceptors in the AWS SDK for Java 2.x
<a name="interceptors"></a>

Execution interceptors in the AWS SDK for Java 2.x hook into the request and response lifecycle to perform custom logic at various stages of API call execution. Use interceptors to implement cross-cutting concerns such as logging, metrics collection, request modification, debugging, and error handling.

Interceptors implement the [`ExecutionInterceptor`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/interceptor/ExecutionInterceptor.html) interface, which provides hooks for different phases of request execution.

## Interceptor lifecycle
<a name="interceptor-lifecycle"></a>

The `ExecutionInterceptor` interface provides methods that are called at specific points during request execution:
+ `beforeExecution` - Called before the request executes
+ `modifyRequest` - Modifies the SDK request object
+ `beforeMarshalling` - Called before the request marshals to HTTP
+ `afterMarshalling` - Called after the request marshals to HTTP
+ `modifyHttpRequest` - Modifies the HTTP request
+ `beforeTransmission` - Called before the HTTP request sends
+ `afterTransmission` - Called after the HTTP response is received
+ `modifyHttpResponse` - Modifies the HTTP response
+ `beforeUnmarshalling` - Called before the HTTP response unmarshals
+ `afterUnmarshalling` - Called after the HTTP response unmarshals
+ `modifyResponse` - Modifies the SDK response object
+ `afterExecution` - Called after successful request execution
+ `onExecutionFailure` - Called when request execution fails

## Register interceptors
<a name="registering-interceptors"></a>

Register interceptors when you build a service client using the `overrideConfiguration` method. You can register multiple interceptors, and they execute in the order you register them.

```
// Register a single interceptor.
SqsClient client = SqsClient.builder()
    .overrideConfiguration(c -> c.addExecutionInterceptor(new LoggingInterceptor()))
    .build();

// Register multiple interceptors.
S3Client s3Client = S3Client.builder()
    .overrideConfiguration(config -> config
        .addExecutionInterceptor(new TimingInterceptor())
        .addExecutionInterceptor(new LoggingInterceptor())
        .addExecutionInterceptor(new RequestModificationInterceptor()))
    .build();
```

## Interceptor example
<a name="interceptor-examples"></a>

The following class demonstrates how to use execution interceptors to add cross-cutting concerns like logging, performance monitoring, and request modification to your S3 operations without changing your core business logic.

This example shows you how to register multiple interceptors on an S3 client and see them in action during real AWS API calls.

### Imports
<a name="interceptor-example-imports"></a>

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.core.ApiName;
import software.amazon.awssdk.core.SdkRequest;
import software.amazon.awssdk.core.interceptor.Context;
import software.amazon.awssdk.core.interceptor.ExecutionAttributes;
import software.amazon.awssdk.core.interceptor.ExecutionInterceptor;
import software.amazon.awssdk.http.SdkHttpRequest;
import software.amazon.awssdk.http.SdkHttpResponse;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.HeadBucketRequest;
import software.amazon.awssdk.services.s3.model.ListBucketsResponse;

import java.time.Duration;
import java.time.Instant;
```

```
public class S3InterceptorsDemo {
    private static final Logger logger = LoggerFactory.getLogger(S3InterceptorsDemo.class);

    public static void main(String[] args) {
        logger.info("=== AWS SDK for Java v2 - S3 Interceptors Demo ===");

        // Create an S3 client with multiple interceptors.
        S3Client s3Client = S3Client.builder()
            .overrideConfiguration(config -> config
                .addExecutionInterceptor(new TimingInterceptor())
                .addExecutionInterceptor(new LoggingInterceptor())
                .addExecutionInterceptor(new RequestModificationInterceptor()))
            .build();

        try {
            logger.info("Starting S3 operations with interceptors...");

            // Operation 1: List buckets.
            logger.info("Operation 1: Listing S3 buckets");
            logger.info("----------------------------------------");
            ListBucketsResponse listBucketsResponse = s3Client.listBuckets();
            logger.info("Found {} buckets", listBucketsResponse.buckets().size());

            // Operation 2: Try to access a bucket that likely doesn't exist.
            logger.info("Operation 2: Checking non-existent bucket (demonstrating error interceptor)");
            logger.info("----------------------------------------");
            try {
                s3Client.headBucket(HeadBucketRequest.builder()
                    .bucket("amzn-s3-demo-bucket-that-does-not-exist-1234")
                    .build());
            } catch (Exception e) {
                logger.info("Expected error occurred (interceptor should have logged it)");
            }

        } catch (Exception e) {
            logger.error(" Error during S3 operations: {}", e.getMessage(), e);
        } finally {
            s3Client.close();
            logger.info("Demo completed - S3 client closed");
        }
    }

    // Logging interceptor.
    private static class LoggingInterceptor implements ExecutionInterceptor {
        private static final Logger logger = LoggerFactory.getLogger(LoggingInterceptor.class);

        @Override
        public void beforeExecution(Context.BeforeExecution context, ExecutionAttributes executionAttributes) {
            logger.info("[LOGGING] Starting request: {}", context.request().getClass().getSimpleName());
        }

        @Override
        public void afterExecution(Context.AfterExecution context, ExecutionAttributes executionAttributes) {
            logger.info("[LOGGING] Completed request: {}", context.request().getClass().getSimpleName());
        }

        @Override
        public void onExecutionFailure(Context.FailedExecution context, ExecutionAttributes executionAttributes) {
            logger.error("[LOGGING] Request failed: {}", context.request().getClass().getSimpleName());
            if (context.exception() instanceof AwsServiceException) {
                AwsServiceException ase = (AwsServiceException) context.exception();
                if (ase.awsErrorDetails().errorCode() != null) {
                    SdkHttpResponse httpResponse = ase.awsErrorDetails().sdkHttpResponse();
                    logger.error("   HTTP Status: {}", httpResponse.statusCode());
                    logger.error("   Error Code: {}", ase.awsErrorDetails().errorCode());
                    logger.error("   Error Message: {}", ase.awsErrorDetails().errorMessage());
                }
            }
        }
    }

    // Performance timing interceptor.
    private static class TimingInterceptor implements ExecutionInterceptor {
        private static final Logger logger = LoggerFactory.getLogger(TimingInterceptor.class);
        private Instant startTime;

        @Override
        public void beforeExecution(Context.BeforeExecution context, ExecutionAttributes executionAttributes) {
            startTime = Instant.now();
            logger.info("⏱️  [TIMING] Request started at: {}", startTime);
        }

        @Override
        public void afterExecution(Context.AfterExecution context, ExecutionAttributes executionAttributes) {
            if (startTime != null) {
                Duration duration = Duration.between(startTime, Instant.now());
                logger.info("⏱️  [TIMING] Request completed in: {}ms", duration.toMillis());
            }
        }

        @Override
        public void onExecutionFailure(Context.FailedExecution context, ExecutionAttributes executionAttributes) {
            if (startTime != null) {
                Duration duration = Duration.between(startTime, Instant.now());
                logger.warn("⏱️  [TIMING] Request failed after: {}ms", duration.toMillis());
            }
        }
    }

    // Request modification interceptor
    private static class RequestModificationInterceptor implements ExecutionInterceptor {
        private static final Logger logger = LoggerFactory.getLogger(RequestModificationInterceptor.class);

        @Override
        public SdkRequest modifyRequest(Context.ModifyRequest context, ExecutionAttributes executionAttributes) {
            SdkRequest originalRequest = context.request();
            logger.info("[MODIFY] Modifying request: {}", originalRequest.getClass().getSimpleName());

            // For ListBucketsRequest, we can't modify much since it has no settable properties
            // For HeadBucketRequest, we can demonstrate modifying the request
            if (originalRequest instanceof HeadBucketRequest) {
                HeadBucketRequest headRequest = (HeadBucketRequest) originalRequest;

                // Create a new request with an API name added.
                return HeadBucketRequest.builder()
                        .bucket(headRequest.bucket())
                        .overrideConfiguration(b -> b.addApiName(ApiName.builder()
                                .name("My-API")
                                .version("1.0")
                                .build()))
                        .build();
            }
            logger.info("Not a HeadBucketRequest, returning original request");
            return originalRequest;
        }

        @Override
        public SdkHttpRequest modifyHttpRequest(Context.ModifyHttpRequest context, ExecutionAttributes executionAttributes) {
            logger.info("[MODIFY] Adding custom HTTP headers");
            return context.httpRequest().toBuilder()
                .putHeader("X-Custom-Header", "S3InterceptorDemo")
                .putHeader("X-Request-ID", java.util.UUID.randomUUID().toString())
                .build();
        }
    }
}
```

### Maven pom file
<a name="interceptor-example-pom"></a>

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>interceptors-examples</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>interceptors-examples</name>
    <description>Demonstration of execution interceptors in AWS SDK for Java v2</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <aws.java.sdk.version>2.31.62</aws.java.sdk.version>
        <exec.mainClass>org.example.S3InterceptorsDemo</exec.mainClass>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>software.amazon.awssdk</groupId>
                <artifactId>bom</artifactId>
                <version>${aws.java.sdk.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.apache.logging.log4j</groupId>
                <artifactId>log4j-bom</artifactId>
                <version>2.23.1</version>
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
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.13</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j2-impl</artifactId>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-1.2-api</artifactId>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>

            <!-- Surefire Plugin for running tests -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.2</version>
            </plugin>

            <!-- Exec Plugin for running the main class -->
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <mainClass>${exec.mainClass}</mainClass>
                </configuration>
            </plugin>

            <!-- Shade Plugin to create executable JAR -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.4.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>${exec.mainClass}</mainClass>
                                </transformer>
                            </transformers>
                            <createDependencyReducedPom>false</createDependencyReducedPom>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

## Best practices
<a name="interceptor-best-practices"></a>
+ **Keep interceptors lightweight** - Interceptors execute for every request, so avoid heavy computations or blocking operations that could impact performance.
+ **Handle exceptions gracefully** - If your interceptor throws an exception, it causes the entire request to fail. Always use try-catch blocks for potentially failing operations.
+ **Order matters** - Interceptors execute in the order you register them. Consider the dependencies between your interceptors when you register them.
+ **Use ExecutionAttributes for state** - If you need to pass data between different interceptor methods, use `ExecutionAttributes` rather than instance variables to ensure thread safety.
+ **Be mindful of sensitive data** - When you log requests and responses, be careful not to log sensitive information such as credentials or personal data.

## Context objects
<a name="interceptor-context-objects"></a>

Each interceptor method receives a context object that provides access to request and response information at different stages of execution:
+ `Context.BeforeExecution` - Provides access to the original SDK request
+ `Context.ModifyRequest` - Modifies the SDK request
+ `Context.ModifyHttpRequest` - Modifies the HTTP request
+ `Context.AfterExecution` - Provides access to both request and response
+ `Context.FailedExecution` - Provides access to the request and the exception that occurred
