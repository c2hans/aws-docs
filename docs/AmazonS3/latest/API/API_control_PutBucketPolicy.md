---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html
---

# PutBucketPolicy
<a name="API_control_PutBucketPolicy"></a>

**Note**
This action puts a bucket policy to an Amazon S3 on Outposts bucket. To put a policy on an S3 bucket, see [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html) in the *Amazon S3 API Reference*.

Applies an Amazon S3 bucket policy to an Outposts bucket. For more information, see [Using Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide*.

If you are using an identity other than the root user of the AWS account that owns the Outposts bucket, the calling identity must have the `PutBucketPolicy` permissions on the specified Outposts bucket and belong to the bucket owner's account in order to use this action.

If you don't have `PutBucketPolicy` permissions, Amazon S3 returns a `403 Access Denied` error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not Allowed` error.

**Important**
 As a security precaution, the root user of the AWS account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action.

For more information about bucket policies, see [Using Bucket Policies and User Policies](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html).

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html#API_control_PutBucketPolicy_Examples) section.

The following actions are related to `PutBucketPolicy`:
+  [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html)
+  [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html)

## Request Syntax
<a name="API_control_PutBucketPolicy_RequestSyntax"></a>

```
PUT /v20180820/bucket/{{name}}/policy HTTP/1.1
Host: {{Bucket}}.s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
x-amz-confirm-remove-self-bucket-access: {{ConfirmRemoveSelfBucketAccess}}
<?xml version="1.0" encoding="UTF-8"?>
<PutBucketPolicyRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Policy>{{string}}</Policy>
</PutBucketPolicyRequest>
```

## URI Request Parameters
<a name="API_control_PutBucketPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutBucketPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutBucketPolicy-request-header-Bucket"></a>
Specifies the bucket.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_PutBucketPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutBucketPolicy-request-header-AccountId"></a>
The AWS account ID of the Outposts bucket.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

 ** [x-amz-confirm-remove-self-bucket-access](#API_control_PutBucketPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutBucketPolicy-request-header-ConfirmRemoveSelfBucketAccess"></a>
Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.
This is not supported by Amazon S3 on Outposts buckets.

## Request Body
<a name="API_control_PutBucketPolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutBucketPolicyRequest](#API_control_PutBucketPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutBucketPolicy-request-PutBucketPolicyRequest"></a>
Root level tag for the PutBucketPolicyRequest parameters.
Required: Yes

 ** [Policy](#API_control_PutBucketPolicy_RequestSyntax) **   <a name="AmazonS3-control_PutBucketPolicy-request-Policy"></a>
The bucket policy as a JSON document.
Type: String
Required: Yes

## Response Syntax
<a name="API_control_PutBucketPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutBucketPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_control_PutBucketPolicy_Examples"></a>

### Sample request for putting a bucket policy in an Amazon S3 on Outposts bucket
<a name="API_control_PutBucketPolicy_Example_1"></a>

The following request shows the PUT an individual policy request for the Outposts bucket `example-outpost-bucket`.

```
PUT v20180820/bucket/example-outpost-bucket/policy HTTP/1.1
Host: s3-outposts.<Region>.amazonaws.com
Date: Tue, 04 Apr 2010 20:34:56 GMT
Authorization: authorization string
x-amz-account-id: example-account-id
x-amz-outpost-id: op-01ac5d28a6a232904
{
   "Version":"2012-10-17",
   "Id":"exampleS3OnOutpostBucketPolicy",
   "Statement":[
      {
         "Sid":"st1",
         "Effect":"Allow",
         "Principal":{
            "AWS":"example-account-id"
         },
         "Action":"s3-outposts:*",
         "Resource":"arn:aws:s3-outposts:<your-region>:example-account-id:outpost/op-01ac5d28a6a232904/bucket/example-outpost-bucket"
      }
   ]
}
```

## See Also
<a name="API_control_PutBucketPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketPolicy)
