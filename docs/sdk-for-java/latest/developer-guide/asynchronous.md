---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/asynchronous.html
---

# Programming asynchronously using the AWS SDK for Java 2.x
<a name="asynchronous"></a>

The AWS SDK for Java 2.x features asynchronous clients with non-blocking I/O support that implement high concurrency across a few threads. However, total non-blocking I/O is not guaranteed. Asynchronous client may perform blocking calls in some cases such as credential retrieval, request signing using [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html), or endpoint discovery.

Synchronous methods block your thread’s execution until the client receives a response from the service. Asynchronous methods return immediately, giving control back to the calling thread without waiting for a response.

Because an asynchronous method returns before a response is available, you need a way to get the response when it’s ready. The methods for asynchronous client in 2.x of the AWS SDK for Java return *CompletableFuture objects* that allow you to access the response when it’s ready.

## Use asynchronous client APIs
<a name="basics-async-non-streaming"></a>

The signatures of asynchronous client methods are the same their synchronous counterpart, but the asynchronous methods return a [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/concurrent/CompletableFuture.html) object that contains the results of the asynchronous operation *in the future*. If an error is thrown while the SDK's asynchronous method executes, the error is thrown as `CompletionException`.

One approach you can use to get the result is to chain a `whenComplete()` method onto the `CompletableFuture` returned by the SDK method call. The `whenComplete()` method receives the result or a Throwable object of type `CompletionException` depending on how the asynchronous call completed. You provide an action to `whenComplete()` to process or check the results before it is returned to the calling code.

If you want to return something other than the object returned by the SDK method, use the `handle()` method instead. The `handle()` method takes the same parameters as `whenComplete()`, but you can process the result and return an object.

To wait for the asynchronous chain to complete and retrieve the completion results, you can call the `join()` method. If the `Throwable` object was not handled in the chain, the `join()` method throws an unchecked `CompletionException` that wraps the original exception. You access the original exception with `CompletionException#getCause()`. You can also call the `CompletableFuture#get()` method to get the completion results. The `get()` method, however, can throw checked exceptions.

The following example shows two variations of how you can work with the `listTables()` method of the DynamoDB asynchronous client. The action passed to `whenComplete()` simply logs a successful response, whereas the `handle()` version extracts the list of table names and returns the list. In both cases if an error is generated in the asynchronous chain, the error is rethrown so the client code has a chance to handle it.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.dynamodb.model.ListTablesRequest;
import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;

import java.util.List;
import java.util.concurrent.CompletableFuture;
```

 **Code**

------
#### [ whenComplete() variation ]

```
public class DynamoDbAsyncListTables {

    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        DynamoDbAsyncClient dynamoDbAsyncClient = DynamoDbAsyncClient.builder().region(region).build();
        try {
            ListTablesResponse listTablesResponse = listTablesWhenComplete(dynamoDbAsyncClient).join();  // The join() method may throw a CompletionException.
            if (listTablesResponse.hasTableNames()){
                System.out.println("Table exist in this region: " + region.id());
            }
        } catch (RuntimeException e) {
            // Handle as needed. Here we simply print out the class names.
            System.out.println(e.getClass()); // Prints 'class java.util.concurrent.CompletionException'.
            System.out.println(e.getCause().getClass()); // Prints 'class software.amazon.awssdk.services.dynamodb.model.DynamoDbException'.
        }
    }

    public static CompletableFuture<ListTablesResponse> listTablesWhenComplete(DynamoDbAsyncClient client) {
        return client.listTables(ListTablesRequest.builder().build())
            .whenComplete((listTablesResponse, throwable) -> {
                if (listTablesResponse != null) {  // Consume the response.
                    System.out.println("The SDK's listTables method completed successfully.");
                } else {
                    RuntimeException cause = (RuntimeException) throwable.getCause(); // If an error was thrown during the SDK's listTables method it is wrapped in a CompletionException.
                                                                                      // The SDK throws only RuntimeExceptions, so this is a safe cast.
                    System.out.println(cause.getMessage());  // Log error here, but rethrow so the calling code can handle as needed.
                    throw cause;
                }
            });
    }
```

------
#### [ handle() variation ]

```
public class DynamoDbAsyncListTables {

    public static void main(String[] args) {
        Region region = Region.US_EAST_1;
        DynamoDbAsyncClient dynamoDbAsyncClient = DynamoDbAsyncClient.builder().region(region).build();
        try {
            List<String> tableNames = listTablesHandle(dynamoDbAsyncClient).join(); // The join() method may throw a CompletionException.
            tableNames.forEach(System.out::println);
        } catch (RuntimeException e) {
            // Handle as needed. Here we simply print out the class names.
            System.out.println(e.getClass()); // Prints 'class java.util.concurrent.CompletionException'.
            System.out.println(e.getCause().getClass()); // Prints 'class software.amazon.awssdk.services.dynamodb.model.DynamoDbException'.
        }
    }

    public static CompletableFuture<List<String>> listTablesHandle(DynamoDbAsyncClient client) {
        return client.listTables(ListTablesRequest.builder().build())
            .handle((listTablesResponse, throwable) -> {
                if (listTablesResponse != null) {
                    return listTablesResponse.tableNames(); // Return the list of table names.
                } else {
                    RuntimeException cause = (RuntimeException) throwable.getCause(); // If an error was thrown during the SDK's listTables method it is wrapped in a CompletionException.
                                                                                      // The SDK throws only RuntimeExceptions, so this is a safe cast.
                    System.out.println(cause.getMessage());  // Log error here, but rethrow so the calling code can handle as needed.
                    throw cause;
                }
            });
    }
}
```

------

## Handle streaming in asynchronous methods
<a name="basics-async-streaming"></a>

For asynchronous methods with streaming content, you must provide an [AsyncRequestBody](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncRequestBody.html) to provide the content incrementally, or an [AsyncResponseTransformer](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/AsyncResponseTransformer.html) to receive and process the response.

The following example uploads a file to Amazon S3 asynchronously by using the asynchronous form of the `PutObject` operation.

 **Imports**

```
import software.amazon.awssdk.core.async.AsyncRequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.PutObjectResponse;
import java.nio.file.Paths;
import java.util.concurrent.CompletableFuture;
```

 **Code**

```
/**
 * To run this AWS code example, ensure that you have setup your development environment, including your AWS credentials.
 *
 * For information, see this documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class S3AsyncOps {

     public static void main(String[] args) {

         final String USAGE = "\n" +
                 "Usage:\n" +
                 "    S3AsyncOps <bucketName> <key> <path>\n\n" +
                 "Where:\n" +
                 "    bucketName - the name of the Amazon S3 bucket (for example, bucket1). \n\n" +
                 "    key - the name of the object (for example, book.pdf). \n" +
                 "    path - the local path to the file (for example, C:/AWS/book.pdf). \n" ;

        if (args.length != 3) {
            System.out.println(USAGE);
             System.exit(1);
        }

        String bucketName = args[0];
        String key = args[1];
        String path = args[2];

        Region region = Region.US_WEST_2;
        S3AsyncClient client = S3AsyncClient.builder()
                .region(region)
                .build();

        PutObjectRequest objectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        // Put the object into the bucket
        CompletableFuture<PutObjectResponse> future = client.putObject(objectRequest,
                AsyncRequestBody.fromFile(Paths.get(path))
        );
        future.whenComplete((resp, err) -> {
            try {
                if (resp != null) {
                    System.out.println("Object uploaded. Details: " + resp);
                } else {
                    // Handle error
                    err.printStackTrace();
                }
            } finally {
                // Only close the client when you are completely done with it
                client.close();
            }
        });

        future.join();
    }
}
```

The following example gets a file from Amazon S3 by using the asynchronous form of the `GetObject` operation.

 **Imports**

```
import software.amazon.awssdk.core.async.AsyncResponseTransformer;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import java.nio.file.Paths;
import java.util.concurrent.CompletableFuture;
```

 **Code**

```
/**
 * To run this AWS code example, ensure that you have setup your development environment, including your AWS credentials.
 *
 * For information, see this documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */

public class S3AsyncStreamOps {

    public static void main(String[] args) {

        final String USAGE = "\n" +
                "Usage:\n" +
                "    S3AsyncStreamOps <bucketName> <objectKey> <path>\n\n" +
                "Where:\n" +
                "    bucketName - the name of the Amazon S3 bucket (for example, bucket1). \n\n" +
                "    objectKey - the name of the object (for example, book.pdf). \n" +
                "    path - the local path to the file (for example, C:/AWS/book.pdf). \n" ;

        if (args.length != 3) {
            System.out.println(USAGE);
            System.exit(1);
         }

        String bucketName = args[0];
        String objectKey = args[1];
        String path = args[2];

        Region region = Region.US_WEST_2;
        S3AsyncClient client = S3AsyncClient.builder()
                .region(region)
                .build();

        GetObjectRequest objectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(objectKey)
                .build();

        CompletableFuture<GetObjectResponse> futureGet = client.getObject(objectRequest,
                AsyncResponseTransformer.toFile(Paths.get(path)));

        futureGet.whenComplete((resp, err) -> {
            try {
                if (resp != null) {
                    System.out.println("Object downloaded. Details: "+resp);
                } else {
                    err.printStackTrace();
                }
            } finally {
               // Only close the client when you are completely done with it
                client.close();
            }
        });
        futureGet.join();
    }
}
```

## Configure advanced asynchronous options
<a name="advanced-operations"></a>

The AWS SDK for Java 2.x uses [Netty](https://netty.io), an asynchronous event-driven network application framework, to handle I/O threads. The AWS SDK for Java 2.x creates an `ExecutorService` behind Netty, to complete the futures returned from the HTTP client request through to the Netty client. This abstraction reduces the risk of an application breaking the async process if developers choose to stop or sleep threads. By default, each asynchronous client creates a threadpool based on the number of processors and manages the tasks in a queue within the `ExecutorService`.

You can specify a specific JDK implementation of `ExecutorService` when you build your asynchronous client. The following snippet create an `ExecutorService` with a fixed number of threads.

 **Code**

```
S3AsyncClient clientThread = S3AsyncClient.builder()
  .asyncConfiguration(
    b -> b.advancedOption(SdkAdvancedAsyncClientOption
      .FUTURE_COMPLETION_EXECUTOR,
      Executors.newFixedThreadPool(10)
    )
  )
  .build();
```

To optimize performance, you can manage your own thread pool executor, and include it when you configure your client.

```
ThreadPoolExecutor executor = new ThreadPoolExecutor(50, 50,
    10, TimeUnit.SECONDS,
    new LinkedBlockingQueue<>({{<custom_value>}}),
    new ThreadFactoryBuilder()
      .threadNamePrefix("sdk-async-response").build());

// Allow idle core threads to time out
executor.allowCoreThreadTimeOut(true);

S3AsyncClient clientThread = S3AsyncClient.builder()
  .asyncConfiguration(
    b -> b.advancedOption(SdkAdvancedAsyncClientOption
      .FUTURE_COMPLETION_EXECUTOR,
      executor
    )
  )
  .build();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
