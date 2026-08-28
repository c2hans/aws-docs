---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-ddbtable.html
---

# Create a DynamoDB table if needed
<a name="ddb-en-client-gs-ddbtable"></a>

After you have created a `DynamoDbTable` instance, use it to perform a *one-time* creation of a table in DynamoDB.

## Create table example code
<a name="ddb-en-client-gs-ddbtable-createex"></a>

The following example creates a DynamoDB table based on the `Customer` data class.

This example creates a DynamoDB table with the name `Customer`—identical to the class name—but the table name can be something else. Whatever you name the table, you must use this name in additional applications to work with the table. Supply this name to the `table()` method anytime you create another `DynamoDbTable` object in order to work with the underlying DynamoDB table.

The Java lambda parameter, `builder`, passed to the `createTable` method lets you [customize the table](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/CreateTableEnhancedRequest.Builder.html). In this example, [provisioned throughput](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.ProvisionedThroughput.Manual) is configured. If you want to use default settings when you create a table, skip the builder as shown in the following snippet.

```
customerTable.createTable();
```

When default settings are used, values for provisioned throughput are not set. Instead, the billing mode for the table is set to [on-demand](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html#HowItWorks.OnDemand).

The example also uses a `[DynamoDbWaiter](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/waiters/DynamoDbWaiter.html)` before attempting to print out the table name received in the response. The creation of a table takes some time. Therefore, using a waiter means you don't have to write logic that polls the DynamoDB service to see if the table exists before using the table.

### Imports
<a name="ddb-en-client-gs-ddbtable-imports"></a>

```
import com.example.dynamodb.Customer;
import software.amazon.awssdk.core.internal.waiters.ResponseOrException;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbEnhancedClient;
import software.amazon.awssdk.enhanced.dynamodb.DynamoDbTable;
import software.amazon.awssdk.enhanced.dynamodb.TableSchema;
import software.amazon.awssdk.enhanced.dynamodb.model.CreateTableEnhancedRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeTableResponse;
import software.amazon.awssdk.services.dynamodb.waiters.DynamoDbWaiter;
```

### Code
<a name="ddb-en-client-gs-ddbtable-code"></a>

```
 public static void createCustomerTable(DynamoDbTable<Customer> customerTable, DynamoDbClient standardClient) {
     // Create the DynamoDB table using the 'customerTable' DynamoDbTable instance.
     customerTable.createTable(builder -> builder
             .provisionedThroughput(b -> b
                     .readCapacityUnits(10L)
                     .writeCapacityUnits(10L)
                     .build())
     );
     // The DynamoDbClient instance (named 'standardClient') passed to the builder for the DynamoDbWaiter is the same instance
     // that was passed to the builder of the DynamoDbEnhancedClient instance that we created previously.
     // By using the same instance, it ensures that the same Region that was configured on the standard DynamoDbClient
     // instance is used for other service clients that accept a DynamoDbClient during construction.
     try (DynamoDbWaiter waiter = DynamoDbWaiter.builder().client(standardClient).build()) { // DynamoDbWaiter is Autocloseable
         ResponseOrException<DescribeTableResponse> response = waiter
                 .waitUntilTableExists(builder -> builder.tableName("Customer").build())
                 .matched();
         DescribeTableResponse tableDescription = response.response().orElseThrow(
                 () -> new RuntimeException("Customer table was not created."));
         // The actual error can be inspected in response.exception()
         logger.info("Customer table was created.");
     }
 }
```

**Note**
A DynamoDB table's attribute names begin with a lowercase letter when the table is generated from a data class. If you want the table's attribute name to begin with an uppercase letter, use the [`@DynamoDbAttribute({{NAME}})` annotation](ddb-en-client-adv-features-inex-attr.md) and provide the name you want as a parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
