---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_BatchGetLinkAttributes.html
---

Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# BatchGetLinkAttributes
<a name="API_BatchGetLinkAttributes"></a>

Retrieves attributes that are associated with a typed link inside a [BatchRead](API_BatchRead.md) operation. For more information, see [GetLinkAttributes](API_GetLinkAttributes.md) and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations).

## Contents
<a name="API_BatchGetLinkAttributes_Contents"></a>

 ** AttributeNames **   <a name="amazoncds-Type-BatchGetLinkAttributes-AttributeNames"></a>
A list of attribute names whose values will be retrieved.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 230.
Pattern: `^[a-zA-Z0-9._:-]*$`
Required: Yes

 ** TypedLinkSpecifier **   <a name="amazoncds-Type-BatchGetLinkAttributes-TypedLinkSpecifier"></a>
Allows a typed link specifier to be accepted as input.
Type: [TypedLinkSpecifier](API_TypedLinkSpecifier.md) object
Required: Yes

## See Also
<a name="API_BatchGetLinkAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchGetLinkAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchGetLinkAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchGetLinkAttributes)
