---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_BlueprintSummary.html
---

# BlueprintSummary

A summary of a blueprint, returned in the results of `ListBlueprints`.

## Contents
<a name="API_BlueprintSummary_Contents"></a>

 ** BlueprintArn **   <a name="Textract-Type-BlueprintSummary-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: Yes

 ** CreationTime **   <a name="Textract-Type-BlueprintSummary-CreationTime"></a>
The date and time that the blueprint was created.
Type: Timestamp
Required: Yes

 ** BlueprintName **   <a name="Textract-Type-BlueprintSummary-BlueprintName"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** BlueprintVersion **   <a name="Textract-Type-BlueprintSummary-BlueprintVersion"></a>
The version of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]*$`
Required: No

 ** LastModifiedTime **   <a name="Textract-Type-BlueprintSummary-LastModifiedTime"></a>
The date and time that the blueprint was last modified.
Type: Timestamp
Required: No

 ** ResourceOwner **   <a name="Textract-Type-BlueprintSummary-ResourceOwner"></a>
Whether the blueprint is owned by your account or provided by Amazon Textract.
Type: String
Valid Values: `ACCOUNT | SERVICE`
Required: No

## See Also
<a name="API_BlueprintSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/BlueprintSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/BlueprintSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/BlueprintSummary)
