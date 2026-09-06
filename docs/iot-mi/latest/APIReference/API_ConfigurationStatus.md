---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ConfigurationStatus.html
---

# ConfigurationStatus
<a name="API_ConfigurationStatus"></a>

Provides the status of the default encryption configuration for an AWS account.

## Contents
<a name="API_ConfigurationStatus_Contents"></a>

 ** state **   <a name="managedintegrations-Type-ConfigurationStatus-state"></a>
The status state describing the default encryption configuration update.
Type: String
Valid Values: `ENABLED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** error **   <a name="managedintegrations-Type-ConfigurationStatus-error"></a>
The error details describing a failed default encryption configuration update.
Type: [ConfigurationError](API_ConfigurationError.md) object
Required: No

## See Also
<a name="API_ConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ConfigurationStatus)
