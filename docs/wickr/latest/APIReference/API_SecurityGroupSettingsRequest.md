---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroupSettingsRequest.html
---

# SecurityGroupSettingsRequest
<a name="API_SecurityGroupSettingsRequest"></a>

Contains the security group configuration settings that can be specified when creating or updating a security group. This is a subset of SecurityGroupSettings containing only the modifiable federation and security settings.

## Contents
<a name="API_SecurityGroupSettingsRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** enableGuestFederation **   <a name="wickr-Type-SecurityGroupSettingsRequest-enableGuestFederation"></a>
Guest users let you work with people outside your organization that only have limited access to Wickr. Only valid when federationMode is set to Global.
Type: Boolean
Required: No

 ** enableRestrictedGlobalFederation **   <a name="wickr-Type-SecurityGroupSettingsRequest-enableRestrictedGlobalFederation"></a>
Enables restricted global federation to limit communication to specific permitted networks only. Requires globalFederation to be enabled.
Type: Boolean
Required: No

 ** federationMode **   <a name="wickr-Type-SecurityGroupSettingsRequest-federationMode"></a>
The local federation mode. Values: 0 (none), 1 (federated - all networks), 2 (restricted - only permitted networks).
Type: Integer
Required: No

 ** globalFederation **   <a name="wickr-Type-SecurityGroupSettingsRequest-globalFederation"></a>
Allow users to securely federate with all AWS Wickr networks and AWS Enterprise networks.
Type: Boolean
Required: No

 ** lockoutThreshold **   <a name="wickr-Type-SecurityGroupSettingsRequest-lockoutThreshold"></a>
The number of failed password attempts before a user account is locked out.
Type: Integer
Required: No

 ** permittedNetworks **   <a name="wickr-Type-SecurityGroupSettingsRequest-permittedNetworks"></a>
A list of network IDs that are permitted for local federation when federation mode is set to restricted.
Type: Array of strings
Length Constraints: Fixed length of 8.
Pattern: `[0-9]{8}`
Required: No

 ** permittedWickrAwsNetworks **   <a name="wickr-Type-SecurityGroupSettingsRequest-permittedWickrAwsNetworks"></a>
A list of permitted AWS Wickr networks for restricted global federation.
Type: Array of [WickrAwsNetworks](API_WickrAwsNetworks.md) objects
Required: No

 ** permittedWickrEnterpriseNetworks **   <a name="wickr-Type-SecurityGroupSettingsRequest-permittedWickrEnterpriseNetworks"></a>
A list of permitted Wickr Enterprise networks for restricted global federation.
Type: Array of [PermittedWickrEnterpriseNetwork](API_PermittedWickrEnterpriseNetwork.md) objects
Required: No

## See Also
<a name="API_SecurityGroupSettingsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/SecurityGroupSettingsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/SecurityGroupSettingsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/SecurityGroupSettingsRequest)
