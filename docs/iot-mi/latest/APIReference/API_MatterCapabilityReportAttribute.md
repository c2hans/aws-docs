---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_MatterCapabilityReportAttribute.html
---

# MatterCapabilityReportAttribute
<a name="API_MatterCapabilityReportAttribute"></a>

Matter attribute used in capability report.

## Contents
<a name="API_MatterCapabilityReportAttribute_Contents"></a>

 ** id **   <a name="managedintegrations-Type-MatterCapabilityReportAttribute-id"></a>
The id of the Matter attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 24.
Pattern: `0[xX][0-9a-fA-F]+$|^[0-9]+`
Required: No

 ** name **   <a name="managedintegrations-Type-MatterCapabilityReportAttribute-name"></a>
Name for the AWS Matter capability report attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: No

 ** value **   <a name="managedintegrations-Type-MatterCapabilityReportAttribute-value"></a>
Value for the AWS Matter capability report attribute.
Type: JSON value
Required: No

## See Also
<a name="API_MatterCapabilityReportAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/MatterCapabilityReportAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/MatterCapabilityReportAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/MatterCapabilityReportAttribute)
