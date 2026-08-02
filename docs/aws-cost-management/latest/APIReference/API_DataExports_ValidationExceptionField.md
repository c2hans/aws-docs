---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ValidationExceptionField.html
---

# ValidationExceptionField
<a name="API_DataExports_ValidationExceptionField"></a>

The input failed to meet the constraints specified by the AWS service in a specified field.

## Contents
<a name="API_DataExports_ValidationExceptionField_Contents"></a>

 ** Message **   <a name="awscostmanagement-Type-DataExports_ValidationExceptionField-Message"></a>
A message with the reason for the validation exception error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** Name **   <a name="awscostmanagement-Type-DataExports_ValidationExceptionField-Name"></a>
The field name where the invalid entry was detected.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_DataExports_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ValidationExceptionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ValidationExceptionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ValidationExceptionField)
