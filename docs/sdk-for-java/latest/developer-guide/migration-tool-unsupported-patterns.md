---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-tool-unsupported-patterns.html
---

# Unsupported code patterns of the migration tool
<a name="migration-tool-unsupported-patterns"></a>

The migration tool automatically converts most v1 code to v2. However, some code patterns require manual migration. This topic provides detailed examples of the most common unsupported patterns and shows you how to manually convert them.

The following list of patterns is not exhaustive. If your code doesn't compile after running the migration tool, follow the [step-by-step migration instructions](migration-steps.md) to manually migrate the remaining v1 code.

## Request object constructors with parameters
<a name="request-pojo-constructors"></a>

For request POJOs (excluding Amazon S3), the migration tool transforms only setter methods. The tool does not support constructors with parameters.

**Supported pattern: Request object using setters (no constructor parameters)**

Before (original v1 code):

```
import com.amazonaws.services.sqs.model.SendMessageRequest;

SendMessageRequest request = new SendMessageRequest().withMessageBody("Hello World");
request.setQueueUrl("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue");
```

After (migration tool result):

```
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;

SendMessageRequest request = SendMessageRequest.builder()
    .messageBody("Hello World").build();
request = request.toBuilder()
    .queueUrl("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue").build();
```

**Unsupported pattern: Request object constructor with parameters**

The migration tool cannot convert constructors with parameters:

Before manual migration, but after migration tool:

```
import software.amazon.awssdk.services.sqs.model.SendMessageRequest; // Import updated to v2.

// This pattern requires manual migration.
SendMessageRequest request = new SendMessageRequest(
    "https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue",
    "Hello World");
```

The migration tool transforms the import to v2, but the constructor code remains unchanged and requires manual updates to use the builder pattern.

After manual migration:

```
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;

SendMessageRequest request = SendMessageRequest.builder()
    .messageBody("Hello World")
    .queueUrl("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue")
    .build();
```

## Service client methods with individual parameters
<a name="service-client-method-overloads"></a>

The migration tool cannot convert service client methods that take individual parameters instead of request objects (excluding Amazon S3).

Before (v1 code):

```
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClient;

AmazonSQS sqs = new AmazonSQSClient();
// The following v1 method takes individual parameters.
sqs.sendMessage("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue", "Hello World");
```

After (migration tool result–does not compile):

```
import software.amazon.awssdk.services.sqs.SqsClient;  // Import updated to v2.
// No import statement for the v2 request POJO.

SqsClient sqs = SqsClient.builder().build();

// Does not compile–v2 methods only accept request POJOs.
sqs.sendMessage("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue", "Hello World");
```

You must manually update the method arguments to use a request object:

```
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SendMessageRequest; // Add manually.

SqsClient sqs = SqsClient.builder().build();

// Corrected v2 code.
SendMessageRequest request = SendMessageRequest.builder()
    .queueUrl("https://sqs.us-west-2.amazonaws.com/0123456789012/demo-queue")
    .messageBody("Hello World")
    .build();
sqs.sendMessage(request);
```

## Request timeout methods
<a name="request-pojo-timeout-configuration"></a>

The migration tool does not convert methods that set timeouts on request objects.

Before (v1 code):

```
import com.amazonaws.services.sqs.model.SendMessageRequest;

SendMessageRequest request = new SendMessageRequest();
request.setSdkRequestTimeout(7);
```

After (migration tool result–does not compile):

```
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;  // Import updated to v2.

SendMessageRequest request = SendMessageRequest.builder().build();

// Does not compile.
request.setSdkRequestTimeout(7);
```

You must manually migrate to use v2's `overrideConfiguration` method:

```
import software.amazon.awssdk.services.sqs.model.SendMessageRequest;
import java.time.Duration;

SendMessageRequest request = SendMessageRequest.builder().build();

// Corrected v2 code.
request = request.toBuilder()
    .overrideConfiguration(o -> o.apiCallTimeout(Duration.ofSeconds(7)))
    .build();
```

## Service client constructors with parameters
<a name="service-client-constructors-with-args"></a>

The migration tool converts empty service client constructors but cannot convert constructors that accept parameters like credentials or configuration.

Before (v1 code):

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.AmazonSQSClient;

AWSCredentials awsCredentials = new BasicAWSCredentials("akid", "skid");
AmazonSQS sqs = new AmazonSQSClient(awsCredentials);
```

After (migration tool result–does not compile):

```
import software.amazon.awssdk.auth.credentials.AwsCredentials;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.services.sqs.SqsClient;  // Import updated to v2.

AwsCredentials awsCredentials = AwsBasicCredentials.create("akid", "skid");

// Does not compile.
SqsClient sqs = new SqsClient(awsCredentials);
```

You must manually update the service client constructor to use the builder pattern:

```
import software.amazon.awssdk.auth.credentials.AwsCredentials;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;  // Add manually.
import software.amazon.awssdk.services.sqs.SqsClient;

AwsCredentials awsCredentials = AwsBasicCredentials.create("akid", "skid");

// Corrected v2 code.
SqsClient sqs = SqsClient.builder()
    .credentialsProvider(StaticCredentialsProvider.create(awsCredentials))
    .build();
```
