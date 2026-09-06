---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ManagedThingSummary.html
---

# ManagedThingSummary
<a name="API_ManagedThingSummary"></a>

Structure representing one managed thing.

## Contents
<a name="API_ManagedThingSummary_Contents"></a>

 ** ActivatedAt **   <a name="managedintegrations-Type-ManagedThingSummary-ActivatedAt"></a>
The timestampe value of when the managed thing was activated at.
Type: Timestamp
Required: No

 ** AdvertisedProductId **   <a name="managedintegrations-Type-ManagedThingSummary-AdvertisedProductId"></a>
The id of the advertised product.
Type: String
Length Constraints: Fixed length of 5.
Pattern: `([A-Za-z0-9!#$%&()*\+\-;<=>?@^_`{|}~])+`
Required: No

 ** Arn **   <a name="managedintegrations-Type-ManagedThingSummary-Arn"></a>
The Amazon Resource Name (ARN) of the managed thing.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:managed-thing/([0-9a-zA-Z:_-])+`
Required: No

 ** Brand **   <a name="managedintegrations-Type-ManagedThingSummary-Brand"></a>
The brand of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** Classification **   <a name="managedintegrations-Type-ManagedThingSummary-Classification"></a>
The classification of the managed thing such as light bulb or thermostat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ConnectorDestinationId **   <a name="managedintegrations-Type-ManagedThingSummary-ConnectorDestinationId"></a>
The identifier of the connector destination associated with this managed thing, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** ConnectorDeviceId **   <a name="managedintegrations-Type-ManagedThingSummary-ConnectorDeviceId"></a>
The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** ConnectorPolicyId **   <a name="managedintegrations-Type-ManagedThingSummary-ConnectorPolicyId"></a>
 *This member has been deprecated.*
The id of the connector policy.
This parameter is used for cloud-to-cloud devices only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** CreatedAt **   <a name="managedintegrations-Type-ManagedThingSummary-CreatedAt"></a>
The timestamp value of when the device creation request occurred.
Type: Timestamp
Required: No

 ** CredentialLockerId **   <a name="managedintegrations-Type-ManagedThingSummary-CredentialLockerId"></a>
The identifier of the credential locker for the managed thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** Id **   <a name="managedintegrations-Type-ManagedThingSummary-Id"></a>
The id of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`
Required: No

 ** Model **   <a name="managedintegrations-Type-ManagedThingSummary-Model"></a>
The model of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** Name **   <a name="managedintegrations-Type-ManagedThingSummary-Name"></a>
The name of the managed thing representing the physical device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** Owner **   <a name="managedintegrations-Type-ManagedThingSummary-Owner"></a>
Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.,@-]+`
Required: No

 ** ParentControllerId **   <a name="managedintegrations-Type-ManagedThingSummary-ParentControllerId"></a>
Id of the controller device used for the discovery job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9]+`
Required: No

 ** ProvisioningStatus **   <a name="managedintegrations-Type-ManagedThingSummary-ProvisioningStatus"></a>
The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see [Device Provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html).
Type: String
Valid Values: `UNASSOCIATED | PRE_ASSOCIATED | DISCOVERED | ACTIVATED | DELETION_FAILED | DELETE_IN_PROGRESS | ISOLATED | DELETED`
Required: No

 ** Role **   <a name="managedintegrations-Type-ManagedThingSummary-Role"></a>
The type of device used. This will be the AWS hub controller, cloud device, or AWS IoT device.
Type: String
Valid Values: `CONTROLLER | DEVICE`
Required: No

 ** SerialNumber **   <a name="managedintegrations-Type-ManagedThingSummary-SerialNumber"></a>
The serial number of the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** UpdatedAt **   <a name="managedintegrations-Type-ManagedThingSummary-UpdatedAt"></a>
The timestamp value of when the managed thing was last updated at.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedThingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ManagedThingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ManagedThingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ManagedThingSummary)
