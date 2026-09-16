---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessEndpoint.html
---

# ModifyVerifiedAccessEndpoint
<a name="API_ModifyVerifiedAccessEndpoint"></a>

Modifies the configuration of the specified AWS Verified Access endpoint.

## Request Parameters
<a name="API_ModifyVerifiedAccessEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrOptions**
The CIDR options.
Type: [ModifyVerifiedAccessEndpointCidrOptions](API_ModifyVerifiedAccessEndpointCidrOptions.md) object
Required: No

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the Verified Access endpoint.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **LoadBalancerOptions**
The load balancer details if creating the Verified Access endpoint as `load-balancer`type.
Type: [ModifyVerifiedAccessEndpointLoadBalancerOptions](API_ModifyVerifiedAccessEndpointLoadBalancerOptions.md) object
Required: No

 **NetworkInterfaceOptions**
The network interface options.
Type: [ModifyVerifiedAccessEndpointEniOptions](API_ModifyVerifiedAccessEndpointEniOptions.md) object
Required: No

 **RdsOptions**
The RDS options.
Type: [ModifyVerifiedAccessEndpointRdsOptions](API_ModifyVerifiedAccessEndpointRdsOptions.md) object
Required: No

 **VerifiedAccessEndpointId**
The ID of the Verified Access endpoint.
Type: String
Required: Yes

 **VerifiedAccessGroupId**
The ID of the Verified Access group.
Type: String
Required: No

## Response Elements
<a name="API_ModifyVerifiedAccessEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **verifiedAccessEndpoint**
Details about the Verified Access endpoint.
Type: [VerifiedAccessEndpoint](API_VerifiedAccessEndpoint.md) object

## Errors
<a name="API_ModifyVerifiedAccessEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyVerifiedAccessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVerifiedAccessEndpoint)
