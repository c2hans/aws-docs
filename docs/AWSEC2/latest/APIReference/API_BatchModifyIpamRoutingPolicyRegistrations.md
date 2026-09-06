---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BatchModifyIpamRoutingPolicyRegistrations.html
---

# BatchModifyIpamRoutingPolicyRegistrations
<a name="API_BatchModifyIpamRoutingPolicyRegistrations"></a>

Modifies multiple routing policy registrations in a single operation. You can create, update, or delete Route Origin Authorizations (ROAs) in batch.

## Request Parameters
<a name="API_BatchModifyIpamRoutingPolicyRegistrations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation ignores the request, but does not return an error.
Type: String
Required: No

 **DeltaJson**
The batch modifications to apply, in JSON format.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces the batch modification even if individual changes conflict with announced routes. Default: `false`.
Type: Boolean
Required: No

 **IpamInternetRegistryAssociationId**
The ID of the IPAM internet registry association.
Type: String
Required: Yes

## Response Elements
<a name="API_BatchModifyIpamRoutingPolicyRegistrations_ResponseElements"></a>

The following elements are returned by the service.

 **ipamRoutingPolicyRegistrationDelta**
Information about the routing policy registration delta created by this batch operation.
Type: [IpamRoutingPolicyRegistrationDelta](API_IpamRoutingPolicyRegistrationDelta.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_BatchModifyIpamRoutingPolicyRegistrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchModifyIpamRoutingPolicyRegistrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BatchModifyIpamRoutingPolicyRegistrations)
