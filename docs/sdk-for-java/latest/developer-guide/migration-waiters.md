---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-waiters.html
---

# Changes in Waiters from version 1 to version 2
<a name="migration-waiters"></a>

This topic details the changes in the functionality of Waiters from version 1 (v1) to version 2 (v2).

The following tables demonstrate the difference for DynamoDB waiters specifically. Waiters for other services follow the same pattern.

## High-level changes
<a name="migration-waiters-api-changes"></a>

Waiters classes are in the same Maven artifact as the service.

| Change | v1 | v2 |
| --- | --- | --- |
|  <br />Maven dependencies |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>com.amazonaws</groupId><br />            <artifactId>aws-java-sdk-bom</artifactId><br />            <version>{{1.12.6801}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>com.amazonaws</groupId><br />        <artifactId>dynamodb</artifactId><br />    </dependency><br /></dependencies><br /></pre>  |  <pre><dependencyManagement><br />    <dependencies><br />        <dependency><br />            <groupId>software.amazon.awssdk</groupId><br />            <artifactId>bom</artifactId><br />            <version>{{2.27.102}}</version><br />            <type>pom</type><br />            <scope>import</scope><br />        </dependency><br />    </dependencies><br /></dependencyManagement><br /><dependencies><br />    <dependency><br />        <groupId>software.amazon.awssdk</groupId><br />        <artifactId>dynamodb</artifactId><br />    </dependency><br /></dependencies></pre>  |
| Package name | com.amazonaws.services.dynamodbv2.waiters | software.amazon.awssdk.services.dynamodb.waiters |
| Class names | `[AmazonDynamoDBWaiters](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/waiters/AmazonDynamoDBWaiters.html)` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-waiters.html)  |

1 [Latest version](https://central.sonatype.com/artifact/com.amazonaws/aws-java-sdk-bom). 2 [Latest version](https://central.sonatype.com/artifact/software.amazon.awssdk/bom).

## API changes
<a name="migration-cf-presign-behavior-changes"></a>

| Change | v1 | v2 |
| --- | --- | --- |
| Create a waiter |  <pre>AmazonDynamoDB client = AmazonDynamoDBClientBuilder <br />                            .standard().build();<br />AmazonDynamoDBWaiters waiter = client.waiters();</pre>  | Synchronous:<pre>DynamoDbClient client = DynamoDbClient.create();<br />DynamoDbWaiter waiter = client.waiter();</pre>Asynchronous:<pre>DynamoDbAsyncClient asyncClient = <br />        DynamoDbAsyncClient.create();<br />DynamoDbAsyncWaiter waiter = asyncClient.waiter();</pre> |
| Wait until a table exists | Synchronous:<pre>waiter.tableExists()<br />    .run(new WaiterParameters<>(<br />        new DescribeTableRequest(tableName)));</pre>Asynchronous:<pre>waiter.tableExists()<br />    .runAsync(new WaiterParameters()<br />      .withRequest(new DescribeTableRequest(tableName)),<br />          new WaiterHandler() {<br />              @Override<br />              public void onWaitSuccess(<br />                  AmazonWebServiceRequest amazonWebServiceRequest) {<br />                    System.out.println("Table creation succeeded");<br />              }<br /><br />              @Override<br />              public void onWaitFailure(Exception e) {<br />                  e.printStackTrace();<br />              }<br />          }).get();</pre> | Synchronous:<pre>WaiterResponse<DescribeTableResponse> waiterResponse =<br />    waiter.waitUntilTableExists(<br />        r -> r.tableName("myTable"));<br />waiterResponse.matched().response()<br />       .ifPresent(System.out::println);</pre><br />Asynchronous:<pre>waiter.waitUntilTableExists(r -> r.tableName(tableName))<br />           .whenComplete((r, t) -> {<br />               if (t != null) {<br />                   t.printStackTrace();<br />               } else {<br />                   System.out.println(<br />                        "Table creation succeeded");<br />               }<br />           }).join();</pre> |

## Configuration changes
<a name="migration-waiters-config"></a>

| Change | v1 | v2 |
| --- | --- | --- |
| Polling Strategy (max attempts and fixed delay) |  <pre>MaxAttemptsRetryStrategy maxAttemptsRetryStrategy = <br />        new MaxAttemptsRetryStrategy(10);<br /><br />FixedDelayStrategy fixedDelayStrategy = <br />        new FixedDelayStrategy(3);<br /><br />PollingStrategy pollingStrategy = <br />        new PollingStrategy(maxAttemptsRetryStrategy, <br />                fixedDelayStrategy);<br /><br />waiter.tableExists().run(<br />        new WaiterParameters<>(<br />            new DescribeTableRequest(tableName)), <br />                pollingStrategy);</pre>  |  <pre><br />FixedDelayBackoffStrategy fixedDelayBackoffStrategy = <br />        FixedDelayBackoffStrategy<br />            .create(Duration.ofSeconds(3));<br /><br />waiter.waitUntilTableExists(r -> r.tableName(tableName),<br />        c -> c.maxAttempts(10)<br />                .backoffStrategy(fixedDelayBackoffStrategy));</pre>  |
