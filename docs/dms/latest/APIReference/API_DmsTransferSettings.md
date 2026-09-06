---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DmsTransferSettings.html
---

# DmsTransferSettings
<a name="API_DmsTransferSettings"></a>

 The settings in JSON format for the DMS Transfer type source endpoint.

## Contents
<a name="API_DmsTransferSettings_Contents"></a>

 ** BucketName **   <a name="DMS-Type-DmsTransferSettings-BucketName"></a>
 The name of the S3 bucket to use.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-DmsTransferSettings-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.
Type: String
Required: No

## See Also
<a name="API_DmsTransferSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DmsTransferSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DmsTransferSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DmsTransferSettings)
