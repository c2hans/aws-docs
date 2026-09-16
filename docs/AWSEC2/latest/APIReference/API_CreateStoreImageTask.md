---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html
---

# CreateStoreImageTask
<a name="API_CreateStoreImageTask"></a>

Stores an AMI as a single object in an Amazon S3 bucket.

To use this API, you must have the required permissions. For more information, see [Permissions for storing and restoring AMIs using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-ami-store-restore.html#ami-s3-permissions) in the *Amazon EC2 User Guide*.

For more information, see [Store and restore an AMI using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateStoreImageTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Bucket**
The name of the Amazon S3 bucket in which the AMI object will be stored. The bucket must be in the Region in which the request is being made. The AMI object appears in the bucket only after the upload task has completed.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

 **S3ObjectTag.N**
The tags to apply to the AMI object that will be stored in the Amazon S3 bucket.
Type: Array of [S3ObjectTag](API_S3ObjectTag.md) objects
Required: No

## Response Elements
<a name="API_CreateStoreImageTask_ResponseElements"></a>

The following elements are returned by the service.

 **objectKey**
The name of the stored AMI object in the S3 bucket.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateStoreImageTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateStoreImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateStoreImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateStoreImageTask)
