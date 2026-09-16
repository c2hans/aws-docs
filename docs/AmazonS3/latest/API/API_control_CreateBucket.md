---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html
---

# CreateBucket
<a name="API_control_CreateBucket"></a>

**Note**
This action creates an Amazon S3 on Outposts bucket. To create an S3 bucket, see [Create Bucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) in the *Amazon S3 API Reference*.

Creates a new Outposts bucket. By creating the bucket, you become the bucket owner. To create an Outposts bucket, you must have S3 on Outposts. For more information, see [Using Amazon S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in *Amazon S3 User Guide*.

Not every string is an acceptable bucket name. For information on bucket naming restrictions, see [Working with Amazon S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules).

S3 on Outposts buckets support:
+ Tags
+ LifecycleConfigurations for deleting expired objects

For a complete list of restrictions and Amazon S3 feature limitations on S3 on Outposts, see [ Amazon S3 on Outposts Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OnOutpostsRestrictionsLimitations.html).

For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and `x-amz-outpost-id` in your API request, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html#API_control_CreateBucket_Examples) section.

The following actions are related to `CreateBucket` for Amazon S3 on Outposts:
+  [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+  [GetBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html)
+  [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html)
+  [CreateAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html)
+  [PutAccessPointPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html)

## Request Syntax
<a name="API_control_CreateBucket_RequestSyntax"></a>

```
PUT /v20180820/bucket/{{name}} HTTP/1.1
Host: {{Bucket}}.s3-control.amazonaws.com
x-amz-acl: {{ACL}}
x-amz-grant-full-control: {{GrantFullControl}}
x-amz-grant-read: {{GrantRead}}
x-amz-grant-read-acp: {{GrantReadACP}}
x-amz-grant-write: {{GrantWrite}}
x-amz-grant-write-acp: {{GrantWriteACP}}
x-amz-bucket-object-lock-enabled: {{ObjectLockEnabledForBucket}}
x-amz-outpost-id: {{OutpostId}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <LocationConstraint>{{string}}</LocationConstraint>
</CreateBucketConfiguration>
```

## URI Request Parameters
<a name="API_control_CreateBucket_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-Bucket"></a>
The name of the bucket.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-acl](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-ACL"></a>
The canned ACL to apply to the bucket.
This is not supported by Amazon S3 on Outposts buckets.
Valid Values: `private | public-read | public-read-write | authenticated-read`

 ** [x-amz-bucket-object-lock-enabled](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-ObjectLockEnabledForBucket"></a>
Specifies whether you want S3 Object Lock to be enabled for the new bucket.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-grant-full-control](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-GrantFullControl"></a>
Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-grant-read](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-GrantRead"></a>
Allows grantee to list the objects in the bucket.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-grant-read-acp](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-GrantReadACP"></a>
Allows grantee to read the bucket ACL.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-grant-write](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-GrantWrite"></a>
Allows grantee to create, overwrite, and delete any object in the bucket.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-grant-write-acp](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-GrantWriteACP"></a>
Allows grantee to write the ACL for the applicable bucket.
This is not supported by Amazon S3 on Outposts buckets.

 ** [x-amz-outpost-id](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-header-OutpostId"></a>
The ID of the Outposts where the bucket is being created.
This ID is required by Amazon S3 on Outposts buckets.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_control_CreateBucket_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateBucketConfiguration](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-CreateBucketConfiguration"></a>
Root level tag for the CreateBucketConfiguration parameters.
Required: Yes

 ** [LocationConstraint](#API_control_CreateBucket_RequestSyntax) **   <a name="AmazonS3-control_CreateBucket-request-LocationConstraint"></a>
Specifies the Region where the bucket will be created. If you are creating a bucket on the US East (N. Virginia) Region (us-east-1), you do not need to specify the location.
This is not supported by Amazon S3 on Outposts buckets.
Type: String
Valid Values: `EU | eu-west-1 | us-west-1 | us-west-2 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | sa-east-1 | cn-north-1 | eu-central-1`
Required: No

## Response Syntax
<a name="API_control_CreateBucket_ResponseSyntax"></a>

```
HTTP/1.1 200
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketResult>
   <BucketArn>string</BucketArn>
</CreateBucketResult>
```

## Response Elements
<a name="API_control_CreateBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [Location](#API_control_CreateBucket_ResponseSyntax) **   <a name="AmazonS3-control_CreateBucket-response-header-Location"></a>
The location of the bucket.

The following data is returned in XML format by the service.

 ** [CreateBucketResult](#API_control_CreateBucket_ResponseSyntax) **   <a name="AmazonS3-control_CreateBucket-response-CreateBucketResult"></a>
Root level tag for the CreateBucketResult parameters.
Required: Yes

 ** [BucketArn](#API_control_CreateBucket_ResponseSyntax) **   <a name="AmazonS3-control_CreateBucket-response-BucketArn"></a>
The Amazon Resource Name (ARN) of the bucket.
For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.
For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.

## Errors
<a name="API_control_CreateBucket_Errors"></a>

 ** BucketAlreadyExists **
The requested Outposts bucket name is not available. The bucket namespace is shared by all users of the AWS Outposts in this Region. Select a different name and try again.
HTTP Status Code: 400

 ** BucketAlreadyOwnedByYou **
The Outposts bucket you tried to create already exists, and you own it.
HTTP Status Code: 400

## Examples
<a name="API_control_CreateBucket_Examples"></a>

### Sample request to create an Amazon S3 on Outposts bucket
<a name="API_control_CreateBucket_Example_1"></a>

This request creates an Outposts bucket named `example-outpost-bucket`.

```
            PUT /v20180820/bucket/example-outpost-bucket/  HTTP/1.1
            Host:s3-outposts.<Region>.amazonaws.com
            x-amz-outpost-id: op-01ac5d28a6a232904
            Content-Length:
            Date: Wed, 01 Mar  2006 12:00:00 GMT
            Authorization: authorization string
```

## See Also
<a name="API_control_CreateBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateBucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateBucket)
