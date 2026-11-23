---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_BlueprintItem.html
---

# BlueprintItem

Associates a blueprint, and optionally a specific blueprint version, with a project for custom output extraction.

## Contents
<a name="API_BlueprintItem_Contents"></a>

 ** BlueprintArn **   <a name="Textract-Type-BlueprintItem-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: Yes

 ** BlueprintVersion **   <a name="Textract-Type-BlueprintItem-BlueprintVersion"></a>
The version of the blueprint. If omitted, the latest version is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]*$`
Required: No

## See Also
<a name="API_BlueprintItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/BlueprintItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/BlueprintItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/BlueprintItem)
