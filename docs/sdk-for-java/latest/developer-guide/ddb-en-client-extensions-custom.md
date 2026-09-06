---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-extensions-custom.html
---

# Custom extension example
<a name="ddb-en-client-extensions-custom"></a>

You can create custom extensions by implementing the `DynamoDbEnhancedClientExtension` interface. The following custom extension class shows a `beforeWrite()` method that uses an update expression to set a `registrationDate` attribute if the item in the database doesn't already have one.

```
public final class CustomExtension implements DynamoDbEnhancedClientExtension {

    // 1. In a custom extension, use an UpdateExpression to define what action to take before
    //    an item is updated.
    @Override
    public WriteModification beforeWrite(DynamoDbExtensionContext.BeforeWrite context) {
        if ( context.operationContext().tableName().equals("Customer")
                && context.operationName().equals(OperationName.UPDATE_ITEM)) {
            return WriteModification.builder()
                    .updateExpression(createUpdateExpression())
                    .build();
        }
        return WriteModification.builder().build();  // Return an "empty" WriteModification instance if the extension should not be applied.
                                                     // In this case, if the code is not updating an item on the Customer table.
    }

    private static UpdateExpression createUpdateExpression() {

        // 2. Use a SetAction, a subclass of UpdateAction, to provide the values in the update.
        SetAction setAction =
                SetAction.builder()
                        .path("registrationDate")
                        .value("if_not_exists(registrationDate, :regValue)")
                        .putExpressionValue(":regValue", AttributeValue.fromS(Instant.now().toString()))
                        .build();
        // 3. Build the UpdateExpression with one or more UpdateAction.
        return UpdateExpression.builder()
                .addAction(setAction)
                .build();
    }
}
```
