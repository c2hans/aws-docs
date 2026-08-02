---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StateCapability.html
---

# StateCapability
<a name="API_StateCapability"></a>

State capabilities added for the managed thing.

## Contents
<a name="API_StateCapability_Contents"></a>

 ** id **   <a name="managedintegrations-Type-StateCapability-id"></a>
The id of the managed thing in the capability report.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+@(\d+\.\d+(\.\d+)?|\$latest)`
Required: Yes

 ** name **   <a name="managedintegrations-Type-StateCapability-name"></a>
Name for the AWS capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[/a-zA-Z0-9\._ -]+`
Required: Yes

 ** version **   <a name="managedintegrations-Type-StateCapability-version"></a>
Version for the AWS capability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(0|[1-9][0-9]*)`
Required: Yes

 ** properties **   <a name="managedintegrations-Type-StateCapability-properties"></a>
Describe the command capability with the properties it supports.
Type: JSON value
Required: No

## See Also
<a name="API_StateCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/StateCapability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/StateCapability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/StateCapability)
