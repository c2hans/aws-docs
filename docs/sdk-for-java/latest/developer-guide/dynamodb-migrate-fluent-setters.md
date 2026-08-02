---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migrate-fluent-setters.html
---

# Fluent setters differences between version 1 and version 2 of the SDK for Java
<a name="dynamodb-migrate-fluent-setters"></a>

You can use POJOs with fluent setters in the DynamoDB mapping API for V1 and with V2 since version 2.30.29.

For example, the following POJO returns a `Customer` instance from the `setName` method:

```
// V1

@DynamoDBTable(tableName ="Customer")
public class Customer{
  private String name;
  // Other attributes and methods not shown.
  public Customer setName(String name){
     this.name = name;
     return this;
  }
}
```

However, if you use a version of V2 prior to 2.30.29, `setName` returns a `Customer` instance with a `name` value of `null`.

```
// V2 prior to version 2.30.29.

@DynamoDbBean
public class Customer{
  private String name;
  // Other attributes and methods not shown.
  public Customer setName(String name){
     this.name = name;
     return this;  // Bug: returns this instance with a `name` value of `null`.
  }
}
```

```
// Available in V2 since version 2.30.29.

@DynamoDbBean
public class Customer{
  private String name;
  // Other attributes and methods not shown.
  public Customer setName(String name){
     this.name = name;
     return this;  // Returns this instance for method chaining with the `name` value set.
  }
}
```
