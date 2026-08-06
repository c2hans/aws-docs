---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ObjectIdentifierAndLinkNameTuple.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ObjectIdentifierAndLinkNameTuple
<a name="API_ObjectIdentifierAndLinkNameTuple"></a>

A pair of ObjectIdentifier and LinkName.

## Contents
<a name="API_ObjectIdentifierAndLinkNameTuple_Contents"></a>

 ** LinkName **   <a name="amazoncds-Type-ObjectIdentifierAndLinkNameTuple-LinkName"></a>
The name of the link between the parent and the child object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`
Required: No

 ** ObjectIdentifier **   <a name="amazoncds-Type-ObjectIdentifierAndLinkNameTuple-ObjectIdentifier"></a>
The ID that is associated with the object.
Type: String
Required: No

## See Also
<a name="API_ObjectIdentifierAndLinkNameTuple_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ObjectIdentifierAndLinkNameTuple)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ObjectIdentifierAndLinkNameTuple)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ObjectIdentifierAndLinkNameTuple)
