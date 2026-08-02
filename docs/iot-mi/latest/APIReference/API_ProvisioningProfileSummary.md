---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ProvisioningProfileSummary.html
---

# ProvisioningProfileSummary
<a name="API_ProvisioningProfileSummary"></a>

Structure describing a provisioning profile.

## Contents
<a name="API_ProvisioningProfileSummary_Contents"></a>

 ** Arn **   <a name="managedintegrations-Type-ProvisioningProfileSummary-Arn"></a>
The Amazon Resource Name (ARN) of the provisioning profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:provisioning-profile/[0-9a-zA-Z]+`
Required: No

 ** Id **   <a name="managedintegrations-Type-ProvisioningProfileSummary-Id"></a>
The identifier of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Name **   <a name="managedintegrations-Type-ProvisioningProfileSummary-Name"></a>
The name of the provisioning profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[0-9A-Za-z_-]+`
Required: No

 ** ProvisioningType **   <a name="managedintegrations-Type-ProvisioningProfileSummary-ProvisioningType"></a>
The type of provisioning workflow the device uses for onboarding to IoT managed integrations.
Type: String
Valid Values: `FLEET_PROVISIONING | JITR`
Required: No

 ** Status **   <a name="managedintegrations-Type-ProvisioningProfileSummary-Status"></a>
The status of a provisioning profile.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

## See Also
<a name="API_ProvisioningProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ProvisioningProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ProvisioningProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ProvisioningProfileSummary)
