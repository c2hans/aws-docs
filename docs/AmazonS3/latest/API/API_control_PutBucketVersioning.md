---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html
---

# PutBucketVersioning
<a name="API_control_PutBucketVersioning"></a>

**Note**
This operation sets the versioning state for S3 on Outposts buckets only. To set the versioning state for an S3 bucket, see [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) in the *Amazon S3 API Reference*.

Sets the versioning state for an S3 on Outposts bucket. With S3 Versioning, you can save multiple distinct copies of your objects and recover from unintended user actions and application failures.

You can set the versioning state to one of the following:
+  **Enabled** - Enables versioning for the objects in the bucket. All objects added to the bucket receive a unique version ID.
+  **Suspended** - Suspends versioning for the objects in the bucket. All objects added to the bucket receive the version ID `null`.

If you've never set versioning on your bucket, it has no versioning state. In that case, a [ GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html) request does not return a versioning state value.

When you enable S3 Versioning, for each object in your bucket, you have a current version and zero or more noncurrent versions. You can configure your bucket S3 Lifecycle rules to expire noncurrent versions after a specified time period. For more information, see [ Creating and managing a lifecycle configuration for your S3 on Outposts bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsLifecycleManaging.html) in the *Amazon S3 User Guide*.

If you have an object expiration lifecycle configuration in your non-versioned bucket and you want to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent expiration policy. The noncurrent expiration lifecycle configuration will manage the deletes of the noncurrent object versions in the version-enabled bucket. For more information, see [Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) in the *Amazon S3 User Guide*.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html#API_control_PutBucketVersioning_Examples) section.

The following operations are related to `PutBucketVersioning` for S3 on Outposts.
+  [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html)
+  [PutBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html)
+  [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html)

## Request Syntax
<a name="API_control_PutBucketVersioning_RequestSyntax"></a>

```
PUT /v20180820/bucket/{{name}}/versioning HTTP/1.1
Host: {{Bucket}}.s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
x-amz-mfa: {{MFA}}
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <MfaDelete>{{string}}</MfaDelete>
   <Status>{{string}}</Status>
</VersioningConfiguration>
```

## URI Request Parameters
<a name="API_control_PutBucketVersioning_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-header-Bucket"></a>
The S3 on Outposts bucket to set the versioning state for.
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** [x-amz-account-id](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-header-AccountId"></a>
The AWS account ID of the S3 on Outposts bucket.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

 ** [x-amz-mfa](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-header-MFA"></a>
The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

## Request Body
<a name="API_control_PutBucketVersioning_RequestBody"></a>

The request accepts the following data in XML format.

 ** [VersioningConfiguration](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-VersioningConfiguration"></a>
Root level tag for the VersioningConfiguration parameters.
Required: Yes

 ** [MFADelete](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-MFADelete"></a>
Specifies whether MFA delete is enabled or disabled in the bucket versioning configuration for the S3 on Outposts bucket.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [Status](#API_control_PutBucketVersioning_RequestSyntax) **   <a name="AmazonS3-control_PutBucketVersioning-request-Status"></a>
Sets the versioning state of the S3 on Outposts bucket.
Type: String
Valid Values: `Enabled | Suspended`
Required: No

## Response Syntax
<a name="API_control_PutBucketVersioning_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutBucketVersioning_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Examples
<a name="API_control_PutBucketVersioning_Examples"></a>

### Sample PutBucketVersioning request on an Amazon S3 on Outposts bucket
<a name="API_control_PutBucketVersioning_Example_1"></a>

This request sets the versioning state on an S3 on Outposts bucket that's named `example-outpost-bucket`.

```
            PUT /v20180820/bucket/example-outpost-bucket/?versioning HTTP/1.1
            Host:s3-outposts.region-code.amazonaws.com
            x-amz-account-id: example-account-id
            x-amz-outpost-id: op-01ac5d28a6a232904
            Content-Length: 0
            Date: Wed, 25 May  2022 12:00:00 GMT
            Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
            Authorization: authorization string
            Content-Length: 214

           <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Status>Enabled</Status>
           </VersioningConfiguration>
```

## See Also
<a name="API_control_PutBucketVersioning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutBucketVersioning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutBucketVersioning)
