---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVerifiedAccessInstance.html
---

# CreateVerifiedAccessInstance
<a name="API_CreateVerifiedAccessInstance"></a>

An AWS Verified Access instance is a regional entity that evaluates application requests and grants access only when your security requirements are met.

## Request Parameters
<a name="API_CreateVerifiedAccessInstance_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CidrEndpointsCustomSubDomain**
The custom subdomain.
Type: String
Required: No

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **Description**
A description for the Verified Access instance.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FIPSEnabled**
Enable or disable support for Federal Information Processing Standards (FIPS) on the instance.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to assign to the Verified Access instance.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateVerifiedAccessInstance_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **verifiedAccessInstance**
Details about the Verified Access instance.
Type: [VerifiedAccessInstance](API_VerifiedAccessInstance.md) object

## Errors
<a name="API_CreateVerifiedAccessInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateVerifiedAccessInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVerifiedAccessInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVerifiedAccessInstance)
