---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamInternetRegistryAssociation.html
---

# CreateIpamInternetRegistryAssociation
<a name="API_CreateIpamInternetRegistryAssociation"></a>

Creates an association between an IPAM and a Regional Internet Registry (RIR) for Resource Public Key Infrastructure (RPKI) management. You can use this association to create Route Origin Authorizations (ROAs) for IP address prefixes registered with the internet registry. Your IPAM must be in the Advanced tier to use this feature.

## Request Parameters
<a name="API_CreateIpamInternetRegistryAssociation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.
Type: String
Required: No

 **Description**
A description for the internet registry association.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM to associate with the internet registry.
Type: String
Required: Yes

 **OrganizationHandle**
The organization handle at the internet registry (for example, a RIPE NCC organization ID or ARIN Org ID).
Type: String
Required: Yes

 **Rir**
The Regional Internet Registry to associate with. Possible values:
+  `ripe` - RIPE NCC (Europe, the Middle East, and Central Asia).
+  `apnic` - APNIC (Asia Pacific).
+  `arin` - ARIN (North America).
+  `lacnic` - LACNIC (Latin America and the Caribbean).
Type: String
Valid Values: `ripe | apnic | arin | lacnic`
Required: Yes

 **TagSpecification.N**
The tags to assign to the internet registry association.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamInternetRegistryAssociation_ResponseElements"></a>

The following elements are returned by the service.

 **ipamInternetRegistryAssociation**
Information about the internet registry association.
Type: [IpamInternetRegistryAssociation](API_IpamInternetRegistryAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamInternetRegistryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamInternetRegistryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamInternetRegistryAssociation)
