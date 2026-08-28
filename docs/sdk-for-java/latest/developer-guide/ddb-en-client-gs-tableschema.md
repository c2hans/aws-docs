---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-gs-tableschema.html
---

# Generate a `TableSchema` from a data class
<a name="ddb-en-client-gs-tableschema"></a>

A `[TableSchema](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/TableSchema.html)` enables the enhanced client to map DynamoDB attribute values to and from your client-side classes. In this tutorial, you learn about `TableSchema`s derived from a static data class and generated from code by using a builder.

## Use an annotated data class
<a name="ddb-en-client-gs-tableschema-anno-bean"></a>

The SDK for Java 2.x includes a [set of annotations](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/mapper/annotations/package-summary.html) that you can use with a data class to quickly generate a `TableSchema` for mapping your classes to tables.

Start by creating a data class that conforms to the [JavaBean specification](https://download.oracle.com/otn-pub/jcp/7224-javabeans-1.01-fr-spec-oth-JSpec/beans.101.pdf). The specification requires that a class has a no-argument public constructor and has getters and setters for each attribute in the class. Include a class-level annotation to indicate that the data class is a `DynamoDbBean`. Also, at a minimum, include a `DynamoDbPartitionKey` annotation on the getter or setter for the primary key attribute.

You can apply [attribute-level annotations](ddb-en-client-anno-index.md) to getters or setters, but not both.

**Note**
The term `property` is normally used for a value encapsulated in a JavaBean. However, this guide uses the term `attribute` instead, to be consistent with the terminology used by DynamoDB.

The following `Customer` class uses a composite primary key that consists of a partition key (`id`) and a sort key (`email`). A DynamoDB primary key is either a single partition key attribute or a partition key combined with a sort key. Use the `@DynamoDbPartitionKey` and `@DynamoDbSortKey` annotations to identify the key attributes.

### `Customer` class
<a name="ddb-en-client-gs-tableschema-anno-bean-cust"></a>

```
package org.example.tests.model;

import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey;
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbSortKey;

import java.time.Instant;

@DynamoDbBean
public class Customer {

    private String id;
    private String name;
    private String email;
    private Instant regDate;

    @DynamoDbPartitionKey
    public String getId() { return this.id; }

    public void setId(String id) { this.id = id; }

    public String getCustName() { return this.name; }

    public void setCustName(String name) { this.name = name; }

    @DynamoDbSortKey
    public String getEmail() { return this.email; }

    public void setEmail(String email) { this.email = email; }

    public Instant getRegistrationDate() { return this.regDate; }

    public void setRegistrationDate(Instant registrationDate) { this.regDate = registrationDate; }

    @Override
    public String toString() {
        return "Customer [id=" + id + ", name=" + name + ", email=" + email
                + ", regDate=" + regDate + "]";
    }
}
```

After you have created an annotated data class, use it to create the `TableSchema`, as shown in the following snippet.

```
static final TableSchema<Customer> customerTableSchema = TableSchema.fromBean(Customer.class);
```

A `TableSchema` is designed to be static and immutable. You can usually instantiate it at class-load time.

The static `TableSchema.fromBean()` factory method introspects the bean to generate the mapping of data class attributes (properties) to and from DynamoDB attributes.

For an example of working with a data model made up of several data classes, see the `Person` class in the [Work with attributes that are beans, maps, lists and sets](ddb-en-client-adv-features-nested.md) section.

## Use a builder
<a name="ddb-en-client-gs-tableschema-builder"></a>

You can skip the cost of bean introspection if you define the table schema in code. If you code the schema, your class does not need to follow JavaBean naming standards nor does it need to be annotated. The following example uses a builder and is equivalent to the `Customer` class example that uses annotations.

```
static final TableSchema<Customer> customerTableSchema =
                TableSchema.builder(Customer.class)
                        .newItemSupplier(Customer::new)
                        .addAttribute(String.class, a -> a.name("id")
                                .getter(Customer::getId)
                                .setter(Customer::setId)
                                .tags(StaticAttributeTags.primaryPartitionKey()))
                        .addAttribute(String.class, a -> a.name("email")
                                .getter(Customer::getEmail)
                                .setter(Customer::setEmail)
                                .tags(StaticAttributeTags.primarySortKey()))
                        .addAttribute(String.class, a -> a.name("name")
                                .getter(Customer::getCustName)
                                .setter(Customer::setCustName))
                        .addAttribute(Instant.class, a -> a.name("registrationDate")
                                .getter(Customer::getRegistrationDate)
                                .setter(Customer::setRegistrationDate))
                        .build();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
