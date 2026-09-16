---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpamRoutingPolicyRegistration.html
---

# DeleteIpamRoutingPolicyRegistration
<a name="API_DeleteIpamRoutingPolicyRegistration"></a>

Deletes a routing policy registration for a specified CIDR prefix.

## Request Parameters
<a name="API_DeleteIpamRoutingPolicyRegistration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
The IP address prefix in CIDR notation identifying the routing policy registration to delete.
Type: String
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces the deletion even if it conflicts with an announced route. Default: `false`.
Type: Boolean
Required: No

 **IpamInternetRegistryAssociationId**
The ID of the IPAM internet registry association.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteIpamRoutingPolicyRegistration_ResponseElements"></a>

The following elements are returned by the service.

 **ipamRoutingPolicyRegistrationDelta**
Information about the routing policy registration delta created by this deletion.
Type: [IpamRoutingPolicyRegistrationDelta](API_IpamRoutingPolicyRegistrationDelta.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteIpamRoutingPolicyRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteIpamRoutingPolicyRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteIpamRoutingPolicyRegistration)
