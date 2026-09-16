---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVerifiedAccessEndpointPolicy.html
---

# ModifyVerifiedAccessEndpointPolicy
<a name="API_ModifyVerifiedAccessEndpointPolicy"></a>

Modifies the specified AWS Verified Access endpoint policy.

## Request Parameters
<a name="API_ModifyVerifiedAccessEndpointPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PolicyDocument**
The Verified Access policy document.
Type: String
Required: No

 **PolicyEnabled**
The status of the Verified Access policy.
Type: Boolean
Required: No

 **SseSpecification**
The options for server side encryption.
Type: [VerifiedAccessSseSpecificationRequest](API_VerifiedAccessSseSpecificationRequest.md) object
Required: No

 **VerifiedAccessEndpointId**
The ID of the Verified Access endpoint.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVerifiedAccessEndpointPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **policyDocument**
The Verified Access policy document.
Type: String

 **policyEnabled**
The status of the Verified Access policy.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

 **sseSpecification**
The options in use for server side encryption.
Type: [VerifiedAccessSseSpecificationResponse](API_VerifiedAccessSseSpecificationResponse.md) object

## Errors
<a name="API_ModifyVerifiedAccessEndpointPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyVerifiedAccessEndpointPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVerifiedAccessEndpointPolicy)
