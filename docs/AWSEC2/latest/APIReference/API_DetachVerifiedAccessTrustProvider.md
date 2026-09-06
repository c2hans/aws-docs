---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVerifiedAccessTrustProvider.html
---

# DetachVerifiedAccessTrustProvider
<a name="API_DetachVerifiedAccessTrustProvider"></a>

Detaches the specified AWS Verified Access trust provider from the specified AWS Verified Access instance.

## Request Parameters
<a name="API_DetachVerifiedAccessTrustProvider_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VerifiedAccessInstanceId**
The ID of the Verified Access instance.
Type: String
Required: Yes

 **VerifiedAccessTrustProviderId**
The ID of the Verified Access trust provider.
Type: String
Required: Yes

## Response Elements
<a name="API_DetachVerifiedAccessTrustProvider_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **verifiedAccessInstance**
Details about the Verified Access instance.
Type: [VerifiedAccessInstance](API_VerifiedAccessInstance.md) object

 **verifiedAccessTrustProvider**
Details about the Verified Access trust provider.
Type: [VerifiedAccessTrustProvider](API_VerifiedAccessTrustProvider.md) object

## Errors
<a name="API_DetachVerifiedAccessTrustProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DetachVerifiedAccessTrustProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DetachVerifiedAccessTrustProvider)
