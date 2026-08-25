---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamRoutingPolicyRegistration.html
---

# CreateIpamRoutingPolicyRegistration
<a name="API_CreateIpamRoutingPolicyRegistration"></a>

Creates a routing policy registration and publishes Route Origin Authorizations (ROAs) to the RPKI for the specified CIDR prefix and ASNs.

## Request Parameters
<a name="API_CreateIpamRoutingPolicyRegistration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Asn.N**
The Autonomous System Numbers (ASNs) authorized to originate the prefix.
Type: Array of strings
Required: Yes

 **Cidr**
The IP address prefix in CIDR notation to authorize in the ROA.
Type: String
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.
Type: String
Required: No

 **Description**
A description for the routing policy registration.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces the creation of the routing policy registration even if it conflicts with an announced route. Default: `false`.
Type: Boolean
Required: No

 **IpamInternetRegistryAssociationId**
The ID of the IPAM internet registry association.
Type: String
Required: Yes

 **MaxLength**
The maximum prefix length that the ASNs are authorized to announce. Must be greater than or equal to the prefix length of the CIDR. If not specified, defaults to the prefix length of the CIDR (exact match only).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 48.
Required: No

 **PermitMoreSpecificAnnouncements**
Specifies whether to permit more specific route announcements than the CIDR prefix. When enabled, ASNs can announce sub-prefixes of the authorized CIDR up to the specified maximum length. Default: `false`.
Type: Boolean
Required: No

## Response Elements
<a name="API_CreateIpamRoutingPolicyRegistration_ResponseElements"></a>

The following elements are returned by the service.

 **ipamRoutingPolicyRegistrationDelta**
Information about the routing policy registration delta created by this operation.
Type: [IpamRoutingPolicyRegistrationDelta](API_IpamRoutingPolicyRegistrationDelta.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamRoutingPolicyRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamRoutingPolicyRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamRoutingPolicyRegistration)
