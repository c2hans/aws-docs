---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/pagination.html
---

# Using paginated results in the AWS SDK for Java 2.x
<a name="pagination"></a>

Many AWS operations return paginated results when the response object is too large to return in a single response. In the AWS SDK for Java 1.0, the response contains a token you use to retrieve the next page of results. In contrast, the AWS SDK for Java 2.x has autopagination methods that make multiple service calls to get the next page of results for you automatically. You only have to write code that processes the results. Autopagination is available for both synchronous and asynchronous clients.

**Note**
These code snippets assume that you understand [the basics of using the SDK](using.md), and have configured your environment with [single sign-on access](get-started-auth.md#setup-credentials).

## Synchronous pagination
<a name="synchronous-pagination"></a>

The following examples demonstrate synchronous pagination methods to list objects in an Amazon S3 bucket.

### Iterate over pages
<a name="iterate-pages"></a>

The first example demonstrates the use of a `listRes` paginator object, a [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/paginators/ListObjectsV2Iterable.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/paginators/ListObjectsV2Iterable.html) instance, to iterate through all the response pages with the `stream` method. The code streams over the response pages, converts the response stream to a stream of `[S3Object](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/model/S3Object.html)` content, and then processes the content of the Amazon S3 object.

The following imports apply to all examples in this synchronous pagination section.

#### Imports
<a name="synchronous-pagination-ex-import"></a>

```
import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.Random;

import software.amazon.awssdk.core.waiters.WaiterResponse;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.paginators.ListObjectsV2Iterable;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.model.S3Exception;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.DeleteObjectRequest;
import software.amazon.awssdk.services.s3.model.DeleteBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateMultipartUploadRequest;
import software.amazon.awssdk.services.s3.model.CreateMultipartUploadResponse;
import software.amazon.awssdk.services.s3.model.CompletedMultipartUpload;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CompletedPart;
import software.amazon.awssdk.services.s3.model.CreateBucketConfiguration;
import software.amazon.awssdk.services.s3.model.UploadPartRequest;
import software.amazon.awssdk.services.s3.model.CompleteMultipartUploadRequest;
import software.amazon.awssdk.services.s3.waiters.S3Waiter;
import software.amazon.awssdk.services.s3.model.HeadBucketRequest;
import software.amazon.awssdk.services.s3.model.HeadBucketResponse;
```

```
        ListObjectsV2Request listReq = ListObjectsV2Request.builder()
            .bucket(bucketName)
            .maxKeys(1)
            .build();

        ListObjectsV2Iterable listRes = s3.listObjectsV2Paginator(listReq);
        // Process response pages
        listRes.stream()
            .flatMap(r -> r.contents().stream())
            .forEach(content -> System.out
                .println(" Key: " + content.key() + " size = " + content.size()));
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/s3/src/main/java/com/example/s3/S3ObjectOperations.java#L112) on GitHub.

### Iterate over objects
<a name="iterate-objects"></a>

The following examples show ways to iterate over the objects returned in the response instead of the pages of the response. The `contents` method of `ListObjectsV2Iterable` class returns an [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/pagination/sync/SdkIterable.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/pagination/sync/SdkIterable.html) that provides several methods to process the underlying content elements.

#### Use a stream
<a name="use-a-stream"></a>

The following snippet uses the `stream` method on the response content to iterate over the paginated item collection.

```
        // Helper method to work with paginated collection of items directly.
        listRes.contents().stream()
            .forEach(content -> System.out
                .println(" Key: " + content.key() + " size = " + content.size()));
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/s3/src/main/java/com/example/s3/S3ObjectOperations.java#L127) on GitHub.

#### Use a for-each loop
<a name="for-loop"></a>

Since `SdkIterable` extends the `Iterable` interface, you can process the contents like any `Iterable`. The following snippet uses standard `for-each` loop to iterate through the contents of the response.

```
        for (S3Object content : listRes.contents()) {
            System.out.println(" Key: " + content.key() + " size = " + content.size());
        }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/s3/src/main/java/com/example/s3/S3ObjectOperations.java#L133) on GitHub.

### Manual pagination
<a name="manual-pagination"></a>

If your use case requires it, manual pagination is still available. Use the next token in the response object for the subsequent requests. The following example uses a `while` loop.

```
        ListObjectsV2Request listObjectsReqManual = ListObjectsV2Request.builder()
            .bucket(bucketName)
            .maxKeys(1)
            .build();

        boolean done = false;
        while (!done) {
            ListObjectsV2Response listObjResponse = s3.listObjectsV2(listObjectsReqManual);
            for (S3Object content : listObjResponse.contents()) {
                System.out.println(content.key());
            }

            if (listObjResponse.nextContinuationToken() == null) {
                done = true;
            }

            listObjectsReqManual = listObjectsReqManual.toBuilder()
                .continuationToken(listObjResponse.nextContinuationToken())
                .build();
        }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/s3/src/main/java/com/example/s3/S3ObjectOperations.java#L90) on GitHub.

## Asynchronous pagination
<a name="asynchronous-pagination"></a>

The following examples demonstrate asynchronous pagination methods to list DynamoDB tables.

### Iterate over pages of table names
<a name="iterate-pages-async"></a>

The following two examples use an asynchronous DynamoDB client that call the `listTablesPaginator` method with a request to get a [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/paginators/ListTablesPublisher.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/paginators/ListTablesPublisher.html). `ListTablesPublisher` implements two interfaces, which provides many options to process responses. We'll look at methods of each interface.

#### Use a `Subscriber`
<a name="use-a-subscriber"></a>

The following code example demonstrates how to process paginated results by using the `org.reactivestreams.Publisher` interface implemented by `ListTablesPublisher`. To learn more about the reactive streams model, see the [Reactive Streams GitHub repo](https://github.com/reactive-streams/reactive-streams-jvm/blob/v1.0.2/README.md).

The following imports apply to all examples in this asynchronous pagination section.

##### Imports
<a name="use-a-subscriber-ex-imports"></a>

```
import io.reactivex.rxjava3.core.Flowable;
import org.reactivestreams.Subscriber;
import org.reactivestreams.Subscription;
import reactor.core.publisher.Flux;
import software.amazon.awssdk.core.async.SdkPublisher;
import software.amazon.awssdk.services.dynamodb.DynamoDbAsyncClient;
import software.amazon.awssdk.services.dynamodb.model.ListTablesRequest;
import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;
import software.amazon.awssdk.services.dynamodb.paginators.ListTablesPublisher;

import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
```

The following code acquires a `ListTablesPublisher` instance.

```
        // Creates a default client with credentials and region loaded from the
        // environment.
        final DynamoDbAsyncClient asyncClient = DynamoDbAsyncClient.create();

        ListTablesRequest listTablesRequest = ListTablesRequest.builder().limit(3).build();
        ListTablesPublisher publisher = asyncClient.listTablesPaginator(listTablesRequest);
```

The following code uses an anonymous implementation of `org.reactivestreams.Subscriber` to process the results for each page.

The `onSubscribe` method calls the `Subscription.request` method to initiate requests for data from the publisher. This method must be called to start getting data from the publisher.

The subscriber's `onNext` method processes a response page by accessing all the table names and printing out each one. After the page is processed, another page is requested from the publisher. This method that is called repeatedly until all pages are retrieved.

The `onError` method is triggered if an error occurs while retrieving data. Finally, the `onComplete` method is called when all pages have been requested.

```
        // A Subscription represents a one-to-one life-cycle of a Subscriber subscribing
        // to a Publisher.
        publisher.subscribe(new Subscriber<ListTablesResponse>() {
            // Maintain a reference to the subscription object, which is required to request
            // data from the publisher.
            private Subscription subscription;

            @Override
            public void onSubscribe(Subscription s) {
                subscription = s;
                // Request method should be called to demand data. Here we request a single
                // page.
                subscription.request(1);
            }

            @Override
            public void onNext(ListTablesResponse response) {
                response.tableNames().forEach(System.out::println);
                // After you process the current page, call the request method to signal that
                // you are ready for next page.
                subscription.request(1);
            }

            @Override
            public void onError(Throwable t) {
                // Called when an error has occurred while processing the requests.
            }

            @Override
            public void onComplete() {
                // This indicates all the results are delivered and there are no more pages
                // left.
            }
        });
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/dynamodbasync/src/main/java/com/example/dynamodbasync/AsyncPagination.java#L83) on GitHub.

#### Use a `Consumer`
<a name="id1pagination"></a>

The `SdkPublisher` interface that `ListTablesPublisher` implements has a `subscribe` method that takes a `Consumer` and returns a `CompletableFuture<Void>`.

The `subscribe` method from this interface can be used for simple use cases when an `org.reactivestreams.Subscriber` might be too much overhead. As the code below consumes each page, it calls the `tableNames` method on each. The `tableNames` method returns a `java.util.List` of DynamoDB table names that are processed with the `forEach` method.

```
        // Use a Consumer for simple use cases.
        CompletableFuture<Void> future = publisher.subscribe(
                response -> response.tableNames()
                        .forEach(System.out::println));
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/dynamodbasync/src/main/java/com/example/dynamodbasync/AsyncPagination.java#L96) on GitHub.

### Iterate over table names
<a name="iterate-objects-async"></a>

The following examples show ways to iterate over the objects returned in the response instead of the pages of the response. Similar to the synchronous Amazon S3 example previously shown with its `contents` method, the DynamoDB asynchronous result class, `ListTablesPublisher` has the `tableNames` convenience method to interact with the underlying item collection. The return type of the `tableNames` method is an [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/SdkPublisher.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/core/async/SdkPublisher.html) that can be used to request items across all pages.

#### Use a `Subscriber`
<a name="id2"></a>

The following code acquires an `SdkPublisher` of the underlying collection of table names.

```
        // Create a default client with credentials and region loaded from the
        // environment.
        final DynamoDbAsyncClient asyncClient = DynamoDbAsyncClient.create();

        ListTablesRequest listTablesRequest = ListTablesRequest.builder().limit(3).build();
        ListTablesPublisher listTablesPublisher = asyncClient.listTablesPaginator(listTablesRequest);
        SdkPublisher<String> publisher = listTablesPublisher.tableNames();
```

The following code uses an anonymous implementation of `org.reactivestreams.Subscriber` to process the results for each page.

The subscriber's `onNext` method processes an individual element of the collection. In this case, it's a table name. After the table name is processed, another table name is requested from the publisher. This method that is called repeatedly until all table names are retrieved.

```
        // Use a Subscriber.
        publisher.subscribe(new Subscriber<String>() {
            private Subscription subscription;

            @Override
            public void onSubscribe(Subscription s) {
                subscription = s;
                subscription.request(1);
            }

            @Override
            public void onNext(String tableName) {
                System.out.println(tableName);
                subscription.request(1);
            }

            @Override
            public void onError(Throwable t) {
            }

            @Override
            public void onComplete() {
            }
        });
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/dynamodbasync/src/main/java/com/example/dynamodbasync/AsyncPagination.java#L147) on GitHub.

#### Use a `Consumer`
<a name="for-loop-async"></a>

The following example uses the `subscribe` method of `SdkPublisher` that takes a `Consumer` to process each item.

```
        // Use a Consumer.
        CompletableFuture<Void> future = publisher.subscribe(System.out::println);
        future.get();
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/dynamodbasync/src/main/java/com/example/dynamodbasync/AsyncPagination.java#L161) on GitHub.

### Use third-party library
<a name="use-third-party-library"></a>

You can use other third party libraries instead of implementing a custom subscriber. This example demonstrates the use of RxJava, but any library that implements the reactive stream interfaces can be used. See the [RxJava wiki page on GitHub](https://github.com/ReactiveX/RxJava/wiki) for more information on that library.

To use the library, add it as a dependency. If using Maven, the example shows the POM snippet to use.

 **POM Entry**

```
<dependency>
      <groupId>io.reactivex.rxjava3</groupId>
      <artifactId>rxjava</artifactId>
      <version>3.1.6</version>
</dependency>
```

 **Code**

```
        DynamoDbAsyncClient asyncClient = DynamoDbAsyncClient.create();
        ListTablesPublisher publisher = asyncClient.listTablesPaginator(ListTablesRequest.builder()
                .build());

        // The Flowable class has many helper methods that work with
        // an implementation of an org.reactivestreams.Publisher.
        List<String> tables = Flowable.fromPublisher(publisher)
                .flatMapIterable(ListTablesResponse::tableNames)
                .toList()
                .blockingGet();
        System.out.println(tables);
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/f807d60010caf3d14fe4cd0801b842fb8e9511ca/javav2/example_code/dynamodbasync/src/main/java/com/example/dynamodbasync/AsyncPagination.java#L198) on GitHub.
