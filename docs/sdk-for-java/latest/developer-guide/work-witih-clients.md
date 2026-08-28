---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/work-witih-clients.html
---

# Making AWS service requests using the AWS SDK for Java 2.x
<a name="work-witih-clients"></a>

## Using service clients to make requests
<a name="using-service-client"></a>

After completing the steps in [Setting up the SDK](setup.md) and understanding how to [configure service clients](configuring-service-clients.md), you are ready to make requests to AWS services such as Amazon S3, Amazon DynamoDB, AWS Identity and Access Management, Amazon EC2, and more.

### Create a service client
<a name="work-with-clients-create"></a>

To make a request to an AWS service, you must first instantiate a service client for that service by using the static factory method, `builder()`. The `builder()` method returns a `builder` object that allows you to customize the service client. The fluent setter methods return the `builder` object, so that you can chain the method calls for convenience and for more readable code. After you configure the properties you want, call the `build()` method to create the client.

As an example, the following code snippet instantiates an `Ec2Client` object as a service client for Amazon EC2.

```
Region region = Region.US_WEST_2;
Ec2Client ec2Client = Ec2Client.builder()
        .region(region)
        .build();
```

**Note**
Service clients in the SDK are thread-safe. For best performance, treat them as long-lived objects. Each client has its own connection pool resource that is released when the client is garbage collected.
A service client object is immutable, so you must create a new client for each service to which you make requests, or if you want to use a different configuration for making requests to the same service.
Specifying the `Region` in the service client builder is not required for all AWS services; however, it is a best practice to set the Region for the API calls you make in your applications. See [AWS region selection](region-selection.md) for more information.

### Default client configuration
<a name="using-default-client"></a>

The client builders have another factory method named `create()`. This method creates a service client with the default configuration. It uses the [default provider chain](credentials-chain.md) to load credentials and the [default AWS Region provider chain](region-selection.md#automatically-determine-the-aws-region-from-the-environment). If credentials or the Region can’t be determined from the environment that the application is running in, the call to `create` fails. See [Using credentials](credentials.md) and [Region selection](region-selection.md) for more information about how the SDK determines the credentials and Region to use.

For example, the following code snippet instantiates a `DynamoDbClient` object as a service client for Amazon DynamoDB:

```
DynamoDbClient dynamoDbClient = DynamoDbClient.create();
```

### Configure service clients
<a name="using-configure-service-clients"></a>

For details about how to configure service clients, see [Client configuration externally](configuring-service-clients-ext.md) and [Client configuration in code](configuring-service-clients-code.md).

### Close the service client
<a name="using-closing-client"></a>

As a best practice, you should use a service clients for multiple API service calls during the life of an application. However, if you need a service client for a one-time use or no longer need the service client, close it.

Call the `close()` method when the service client is no longer needed to free up resources.

```
ec2Client.close();
```

If you need a service client for one-time use, you can instantiate the service client as a resource in a `try`-with-resources statement. Service clients implement the `[Autoclosable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/AutoCloseable.html)` interface, so the JDK automatically calls the `close()` method at the end of the statement.

The following example demonstrates how to use a service client for a one-off call. The `StsClient` that calls the AWS Security Token Service is closed after it returns the account ID.

```
import software.amazon.awssdk.services.sts.StsClient;

String getAccountID() {
    try (StsClient stsClient = StsClient.create()) {
       return stsClient.getCallerIdentity().account();
    }
}
```

## Make requests
<a name="using-making-requests"></a>

Use the service client to make requests to the corresponding AWS service.

For example, this code snippet shows how to create a `RunInstancesRequest` object to create a new Amazon EC2 instance:

```
// Create the request by using the fluid setter methods of the request builder.
RunInstancesRequest runInstancesRequest = RunInstancesRequest.builder()
        .imageId(amiId)
        .instanceType(InstanceType.T1_MICRO)
        .maxCount(1)
        .minCount(1)
        .build();

// Use the configured request with the service client.
RunInstancesResponse response = ec2Client.runInstances(runInstancesRequest);
```

Rather than create a request and pass in the instance, the SDK provides a fluent API that you can use to create a request. With the fluent API you can use a Java lambda expressions to create the request 'in-line'.

The following example rewrites the previous example by using the version of the `runInstances` [method that uses a builder](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#runInstances(java.util.function.Consumer)) to create the request.

```
// Create the request by using a lambda expression.
RunInstancesResponse response = ec2.runInstances(r -> r
                .imageId(amiId)
                .instanceType(InstanceType.T1_MICRO)
                .maxCount(1)
                .minCount(1));
```

### Use requests to override client configuration
<a name="using-override-client-config-request"></a>

Although a service client is immutable, you can override many of its settings at the request level. When you build a request, you can provide an [AwsRequestOverrideConfiguration](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/awscore/AwsRequestOverrideConfiguration.html) instance to provide the overridden settings. Some of the methods you can use to override client settings are:
+ `apiCallAttemptTimeout`
+ `apiCallTimeout`
+ `credentialProvider`
+ `compressionConfiguration`
+ `putHeader`

For an example of overriding a client setting with a request, assume that you have the following S3 client that uses default settings.

```
S3Client s3Client = S3Client.create();
```

You want to download a large file and want to be sure the request doesn't timeout before the download finishes. To accomplish this, increase the timeout values for only a single `GetObject` request as shown in the following code.

------
#### [ Standard API ]

```
AwsRequestOverrideConfiguration overrideConfiguration = AwsRequestOverrideConfiguration.builder()
    .apiCallTimeout(Duration.ofSeconds(100L))
    .apiCallAttemptTimeout(Duration.ofSeconds(25L))
    .build();

GetObjectRequest request = GetObjectRequest.builder()
    .bucket("amzn-s3-demo-bucket")
    .key("demo-key")
    .overrideConfiguration(overrideConfiguration)
    .build();

s3Client.getObject(request, myPath);
```

------
#### [ Fluent API ]

```
s3Client.getObject(b -> b
        .bucket("amzn-s3-demo-bucket")
        .key("demo-key")
        .overrideConfiguration(c -> c
            .apiCallTimeout(Duration.ofSeconds(100L))
            .apiCallAttemptTimeout(Duration.ofSeconds(25L))),
    myPath);
```

------

## Handle responses
<a name="using-handling-responses"></a>

The SDK returns a response object for most service operations. Your code can process the information in the response object according to your needs.

For example, the following code snippet prints out the first instance id returned with the [`RunInstancesResponse`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/RunInstancesResponse.html) object from the previous request.

```
RunInstancesResponse runInstancesResponse = ec2Client.runInstances(runInstancesRequest);
System.out.println(runInstancesResponse.instances().get(0).instanceId());
```

Not all operations return a response object with service-specific data, however. In these situations, you can query the HTTP response status to learn if the operation was successful.

For example, the code in the following snippet checks the HTTP response to see if the [`DeleteContactList`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/sesv2/SesV2Client.html#deleteContactList(software.amazon.awssdk.services.sesv2.model.DeleteContactListRequest)) operation of Amazon Simple Email Service was successful.

```
SesV2Client sesv2Client = SesV2Client.create();

DeleteContactListRequest request = DeleteContactListRequest.builder()
    .contactListName("ExampleContactListName")
    .build();

DeleteContactListResponse response = sesv2Client.deleteContactList(request);
if (response.sdkHttpResponse().isSuccessful()) {
    System.out.println("Contact list deleted successfully");
} else {
    System.out.println("Failed to delete contact list. Status code: " + response.sdkHttpResponse().statusCode());
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
