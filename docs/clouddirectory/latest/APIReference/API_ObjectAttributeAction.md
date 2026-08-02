---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ObjectAttributeAction.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ObjectAttributeAction
<a name="API_ObjectAttributeAction"></a>

The action to take on the object attribute.

## Contents
<a name="API_ObjectAttributeAction_Contents"></a>

 ** ObjectAttributeActionType **   <a name="amazoncds-Type-ObjectAttributeAction-ObjectAttributeActionType"></a>
A type that can be either `Update` or `Delete`.
Type: String
Valid Values: `CREATE_OR_UPDATE | DELETE`
Required: No

 ** ObjectAttributeUpdateValue **   <a name="amazoncds-Type-ObjectAttributeAction-ObjectAttributeUpdateValue"></a>
The value that you want to update to.
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

## See Also
<a name="API_ObjectAttributeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ObjectAttributeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ObjectAttributeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ObjectAttributeAction)
