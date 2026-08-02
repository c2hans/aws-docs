---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_InspectorServiceAttributes.html
---

# InspectorServiceAttributes
<a name="API_InspectorServiceAttributes"></a>

This data type is used in the [Finding](API_Finding.md) data type.

## Contents
<a name="API_InspectorServiceAttributes_Contents"></a>

 ** schemaVersion **   <a name="Inspector-Type-InspectorServiceAttributes-schemaVersion"></a>
The schema version of this data type.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** assessmentRunArn **   <a name="Inspector-Type-InspectorServiceAttributes-assessmentRunArn"></a>
The ARN of the assessment run during which the finding is generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** rulesPackageArn **   <a name="Inspector-Type-InspectorServiceAttributes-rulesPackageArn"></a>
The ARN of the rules package that is used to generate the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_InspectorServiceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/InspectorServiceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/InspectorServiceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/InspectorServiceAttributes)
