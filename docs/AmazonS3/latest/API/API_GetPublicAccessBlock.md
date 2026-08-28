---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html
---

# GetPublicAccessBlock
<a name="API_GetPublicAccessBlock"></a>

**Note**
This operation is not supported for directory buckets.

Retrieves the `PublicAccessBlock` configuration for an Amazon S3 bucket. This operation returns the bucket-level configuration only. To understand the effective public access behavior, you must also consider account-level settings (which may inherit from organization-level policies). To use this operation, you must have the `s3:GetBucketPublicAccessBlock` permission. For more information about Amazon S3 permissions, see [Specifying Permissions in a Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html).

**Important**
When Amazon S3 evaluates the `PublicAccessBlock` configuration for a bucket or an object, it checks the `PublicAccessBlock` configuration for both the bucket (or the bucket that contains the object) and the bucket owner's account. Account-level settings automatically inherit from organization-level policies when present. If the `PublicAccessBlock` settings are different between the bucket and the account, Amazon S3 uses the most restrictive combination of the bucket-level and account-level settings.

For more information about when Amazon S3 considers a bucket or an object public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status).

The following operations are related to `GetPublicAccessBlock`:
+  [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html)
+  [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
+  [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
+  [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetPublicAccessBlock_RequestSyntax"></a>

```
GET /?publicAccessBlock HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetPublicAccessBlock_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-request-header-Bucket"></a>
The name of the Amazon S3 bucket whose `PublicAccessBlock` configuration you want to retrieve.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetPublicAccessBlock_RequestSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetPublicAccessBlock_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPublicAccessBlock_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
   <BlockPublicAcls>boolean</BlockPublicAcls>
   <IgnorePublicAcls>boolean</IgnorePublicAcls>
   <BlockPublicPolicy>boolean</BlockPublicPolicy>
   <RestrictPublicBuckets>boolean</RestrictPublicBuckets>
</PublicAccessBlockConfiguration>
```

## Response Elements
<a name="API_GetPublicAccessBlock_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [PublicAccessBlockConfiguration](#API_GetPublicAccessBlock_ResponseSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-response-PublicAccessBlockConfiguration"></a>
Root level tag for the PublicAccessBlockConfiguration parameters.
Required: Yes

 ** [BlockPublicAcls](#API_GetPublicAccessBlock_ResponseSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-response-BlockPublicAcls"></a>
Specifies whether Amazon S3 should block public access control lists (ACLs) for this bucket and objects in this bucket. Setting this element to `TRUE` causes the following behavior:
+ PUT Bucket ACL and PUT Object ACL calls fail if the specified ACL is public.
+ PUT Object calls fail if the request includes a public ACL.
+ PUT Bucket calls fail if the request includes a public ACL.
Enabling this setting doesn't affect existing policies or ACLs.
Type: Boolean

 ** [BlockPublicPolicy](#API_GetPublicAccessBlock_ResponseSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-response-BlockPublicPolicy"></a>
Specifies whether Amazon S3 should block public bucket policies for this bucket. Setting this element to `TRUE` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.
Enabling this setting doesn't affect existing bucket policies.
Type: Boolean

 ** [IgnorePublicAcls](#API_GetPublicAccessBlock_ResponseSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-response-IgnorePublicAcls"></a>
Specifies whether Amazon S3 should ignore public ACLs for this bucket and objects in this bucket. Setting this element to `TRUE` causes Amazon S3 to ignore all public ACLs on this bucket and objects in this bucket.
Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set.
Type: Boolean

 ** [RestrictPublicBuckets](#API_GetPublicAccessBlock_ResponseSyntax) **   <a name="AmazonS3-GetPublicAccessBlock-response-RestrictPublicBuckets"></a>
Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to `TRUE` restricts access to this bucket to only AWS service principals and authorized users within this account if the bucket has a public policy.
Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.
Type: Boolean

## Examples
<a name="API_GetPublicAccessBlock_Examples"></a>

### Sample Request
<a name="API_GetPublicAccessBlock_Example_1"></a>

The following request gets a bucket `PublicAccessBlock` configuration.

```
            GET /<bucket-name>?publicAccessBlock HTTP/1.1
            Host: <bucket-name>.s3.<Region>.amazonaws.com
            x-amz-date: <Thu, 15 Nov 2016 00:17:21 GMT>
            Authorization: <signatureValue>
```

### Sample Response
<a name="API_GetPublicAccessBlock_Example_2"></a>

This example illustrates one usage of GetPublicAccessBlock.

```
         HTTP/1.1 200 OK
         x-amz-id-2: ITnGT1y4REXAMPLEPi4hklTXouTf0hccUjo0iCPEXAMPLEutBj3M7fPGlWO2SEWp
         x-amz-request-id: 51991EXAMPLE5321
         Date: Thu, 15 Nov 2016 00:17:22 GMT
         Server: AmazonS3
         Content-Length: 0

         <PublicAccessBlockConfiguration>
            <BlockPublicAcls>TRUE</BlockPublicAcls>
            <IgnorePublicAcls>FALSE</IgnorePublicAcls>
            <BlockPublicPolicy>FALSE</BlockPublicPolicy>
            <RestrictPublicBuckets>FALSE</RestrictPublicBuckets>
         </PublicAccessBlockConfiguration>
```

## See Also
<a name="API_GetPublicAccessBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetPublicAccessBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetPublicAccessBlock)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
