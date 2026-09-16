---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationS3.html
---

# UpdateLocationS3
<a name="API_UpdateLocationS3"></a>

Modifies the following configuration parameters of the Amazon S3 transfer location that you're using with AWS DataSync.

**Important**
Before you begin, make sure that you read the following topics:
 [Storage class considerations with Amazon S3 locations](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes)
 [Evaluating S3 request costs when using DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests)

## Request Syntax
<a name="API_UpdateLocationS3_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}",
   "S3Config": {
      "BucketAccessRoleArn": "{{string}}"
   },
   "S3StorageClass": "{{string}}",
   "Subdirectory": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationS3_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_UpdateLocationS3_RequestSyntax) **   <a name="DataSync-UpdateLocationS3-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the Amazon S3 transfer location that you're updating.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [S3Config](#API_UpdateLocationS3_RequestSyntax) **   <a name="DataSync-UpdateLocationS3-request-S3Config"></a>
Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.
For more information, see [Providing DataSync access to S3 buckets](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-access).
Type: [S3Config](API_S3Config.md) object
Required: No

 ** [S3StorageClass](#API_UpdateLocationS3_RequestSyntax) **   <a name="DataSync-UpdateLocationS3-request-S3StorageClass"></a>
Specifies the storage class that you want your objects to use when Amazon S3 is a transfer destination.
For buckets in AWS Regions, the storage class defaults to `STANDARD`. For buckets on AWS Outposts, the storage class defaults to `OUTPOSTS`.
For more information, see [Storage class considerations with Amazon S3 transfers](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes).
Type: String
Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_INSTANT_RETRIEVAL`
Required: No

 ** [Subdirectory](#API_UpdateLocationS3_RequestSyntax) **   <a name="DataSync-UpdateLocationS3-request-Subdirectory"></a>
Specifies a prefix in the S3 bucket that DataSync reads from or writes to (depending on whether the bucket is a source or destination location).
DataSync can't transfer objects with a prefix that begins with a slash (`/`) or includes `//`, `/./`, or `/../` patterns. For example:
+  `/photos`
+  `photos//2006/January`
+  `photos/./2006/February`
+  `photos/../2006/March`
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
Required: No

## Response Elements
<a name="API_UpdateLocationS3_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationS3_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationS3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationS3)
