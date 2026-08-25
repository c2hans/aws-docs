---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_Update.html
---

# Update
<a name="API_Update"></a>

An object representing an asynchronous update.

## Contents
<a name="API_Update_Contents"></a>

 ** cancellation **   <a name="AmazonEKS-Type-Update-cancellation"></a>
The latest cancellation information for the update. This field is present only if any cancellation is attempted for the update.
Type: [Cancellation](API_Cancellation.md) object
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-Update-createdAt"></a>
The Unix epoch timestamp at object creation.
Type: Timestamp
Required: No

 ** errors **   <a name="AmazonEKS-Type-Update-errors"></a>
Any errors associated with a `Failed` update.
Type: Array of [ErrorDetail](API_ErrorDetail.md) objects
Required: No

 ** id **   <a name="AmazonEKS-Type-Update-id"></a>
A UUID that is used to track the update.
Type: String
Required: No

 ** params **   <a name="AmazonEKS-Type-Update-params"></a>
A key-value map that contains the parameters associated with the update.
Type: Array of [UpdateParam](API_UpdateParam.md) objects
Required: No

 ** status **   <a name="AmazonEKS-Type-Update-status"></a>
The current status of the update.
Type: String
Valid Values: `InProgress | Failed | Cancelled | Successful`
Required: No

 ** type **   <a name="AmazonEKS-Type-Update-type"></a>
The type of the update.
Type: String
Valid Values: `VersionUpdate | EndpointAccessUpdate | LoggingUpdate | ConfigUpdate | AssociateIdentityProviderConfig | DisassociateIdentityProviderConfig | AssociateEncryptionConfig | AddonUpdate | VpcConfigUpdate | AccessConfigUpdate | UpgradePolicyUpdate | ZonalShiftConfigUpdate | AutoModeUpdate | RemoteNetworkConfigUpdate | DeletionProtectionUpdate | CapabilityUpdate | ControlPlaneScalingConfigUpdate | VendedLogsUpdate | ControlPlaneEgressUpdate | VersionRollback | ControlPlaneComponentConfigUpdate | CertificateAuthorityUpdate`
Required: No

## See Also
<a name="API_Update_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Update)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Update)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Update)
