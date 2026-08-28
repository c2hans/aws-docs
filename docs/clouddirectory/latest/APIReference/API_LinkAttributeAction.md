---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_LinkAttributeAction.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# LinkAttributeAction
<a name="API_LinkAttributeAction"></a>

The action to take on a typed link attribute value. Updates are only supported for attributes which don’t contribute to link identity.

## Contents
<a name="API_LinkAttributeAction_Contents"></a>

 ** AttributeActionType **   <a name="amazoncds-Type-LinkAttributeAction-AttributeActionType"></a>
A type that can be either `UPDATE_OR_CREATE` or `DELETE`.
Type: String
Valid Values: `CREATE_OR_UPDATE | DELETE`
Required: No

 ** AttributeUpdateValue **   <a name="amazoncds-Type-LinkAttributeAction-AttributeUpdateValue"></a>
The value that you want to update to.
Type: [TypedAttributeValue](API_TypedAttributeValue.md) object
Required: No

## See Also
<a name="API_LinkAttributeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/LinkAttributeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/LinkAttributeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/LinkAttributeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
