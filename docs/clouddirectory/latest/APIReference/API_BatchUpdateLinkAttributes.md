---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchUpdateLinkAttributes.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchUpdateLinkAttributes
<a name="API_BatchUpdateLinkAttributes"></a>

Updates a given typed link’s attributes inside a [BatchRead](API_BatchRead.md) operation. Attributes to be updated must not contribute to the typed link’s identity, as defined by its `IdentityAttributeOrder`. For more information, see [UpdateLinkAttributes](API_UpdateLinkAttributes.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchUpdateLinkAttributes_Contents"></a>

 ** AttributeUpdates **   <a name="amazoncds-Type-BatchUpdateLinkAttributes-AttributeUpdates"></a>
The attributes update structure.
Type: Array of [LinkAttributeUpdate](API_LinkAttributeUpdate.md) objects
Required: Yes

 ** TypedLinkSpecifier **   <a name="amazoncds-Type-BatchUpdateLinkAttributes-TypedLinkSpecifier"></a>
Allows a typed link specifier to be accepted as input.
Type: [TypedLinkSpecifier](API_TypedLinkSpecifier.md) object
Required: Yes

## See Also
<a name="API_BatchUpdateLinkAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchUpdateLinkAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchUpdateLinkAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchUpdateLinkAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
