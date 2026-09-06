---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsEncryptionByDefault.html
---

# GetEbsEncryptionByDefault
<a name="API_GetEbsEncryptionByDefault"></a>

Describes whether EBS encryption by default is enabled for your account in the current Region.

For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_GetEbsEncryptionByDefault_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetEbsEncryptionByDefault_ResponseElements"></a>

The following elements are returned by the service.

 **ebsEncryptionByDefault**
Indicates whether encryption by default is enabled.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

 **sseType**
Reserved for future use.
Type: String
Valid Values: `sse-ebs | sse-kms | none`

## Errors
<a name="API_GetEbsEncryptionByDefault_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetEbsEncryptionByDefault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetEbsEncryptionByDefault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetEbsEncryptionByDefault)
