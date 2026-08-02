---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateIpamExternalResourceVerificationToken.html
---

# CreateIpamExternalResourceVerificationToken
<a name="API_CreateIpamExternalResourceVerificationToken"></a>

Create a verification token.

A verification token is an AWS-generated random value that you can use to prove ownership of an external resource. For example, you can use a verification token to validate that you control a public IP address range when you bring an IP address range to AWS (BYOIP).

## Request Parameters
<a name="API_CreateIpamExternalResourceVerificationToken_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM that will create the token.
Type: String
Required: Yes

 **TagSpecification.N**
Token tags.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateIpamExternalResourceVerificationToken_ResponseElements"></a>

The following elements are returned by the service.

 **ipamExternalResourceVerificationToken**
The verification token.
Type: [IpamExternalResourceVerificationToken](API_IpamExternalResourceVerificationToken.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateIpamExternalResourceVerificationToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateIpamExternalResourceVerificationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateIpamExternalResourceVerificationToken)
