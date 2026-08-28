---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-migrate-optimstic-locking.html
---

# Optimistic locking differences between version 1 and version 2 of the SDK for Java
<a name="dynamodb-migrate-optimstic-locking"></a>

Both V1 and V2 implement optimistic locking with an attribute annotation that marks one property on your bean class to store the version number.

**Differences in optimistic locking behavior**

|  | V1 | V2 |
| --- | --- | --- |
| Bean class annotation | @DynamoDBVersionAttribute | @DynamoDbVersionAttribute (note that V2 uses a lowercase "b") |
| Initial save | Version number attribute set to 1. | The starting value for the version attribute set with `@DynamoDbVersionAttribute(startAt = {{X}})`. Default value is 0. |
| Update | The version number attribute is incremented by 1 if the conditional check verifies that the version number of the object being updated matches the number in the database. | The version number attribute is incremented if the conditional check verifies that the version number of the object being updated matches the number in the database.<br />The version number attribute incremented by the `incrementBy` option set with `@DynamoDbVersionAttribute(incrementBy = {{X}})`. Default value is 1. |
| Delete | DynamoDBMapper adds a conditional check that the version number of the object being deleted matches the version number in the database. | V2 does not does not automatically add conditions for the delete operations. You must add condition expressions manually if you want to control the delete behavior.<br />In the following example `recordVersion` is the bean's version attribute.<pre>// 1. Read the item and get its current version.<br />Customer item = customerTable.getItem(Key.builder().partitionValue("someId").build());<br />AttributeValue currentVersion = item.getRecordVersion();<br /><br />// 2. Create conditional delete with the `currentVersion` value.<br />DeleteItemEnhancedRequest deleteItemRequest =<br />    DeleteItemEnhancedRequest.builder()<br />       .key(KEY)<br />       .conditionExpression(Expression.builder()<br />           .expression("recordVersion = :current_version_value")<br />           .putExpressionValue(":current_version_value", currentVersion)<br />           .build()).build();<br /><br />customerTable.deleteItem(deleteItemRequest);</pre> |
| Transactional Write with a Condition Check | You cannot use a bean class that is annotated with @DynamoDBVersionAttribute in an addConditionCheck method. | You can use a bean class with the @DynamoDbVersionAttribute annotation in an addConditionCheck builder method for a transactWriteItems request. |
| Disable | Disable optimistic locking by changing the DynamoDBMapperConfig.SaveBehavior enumeration value from UPDATE to CLOBBER. | Do not use the `@DynamoDbVersionAttribute` annotation. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
