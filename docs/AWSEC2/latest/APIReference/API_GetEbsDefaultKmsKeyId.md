---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetEbsDefaultKmsKeyId.html
---

# GetEbsDefaultKmsKeyId
<a name="API_GetEbsDefaultKmsKeyId"></a>

Describes the default AWS KMS key for EBS encryption by default for your account in this Region.

For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_GetEbsDefaultKmsKeyId_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetEbsDefaultKmsKeyId_ResponseElements"></a>

The following elements are returned by the service.

 **kmsKeyId**
The Amazon Resource Name (ARN) of the default KMS key for encryption by default.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetEbsDefaultKmsKeyId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetEbsDefaultKmsKeyId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetEbsDefaultKmsKeyId)
