---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html
---

# GetObjectLegalHold
<a name="API_GetObjectLegalHold"></a>

**Note**
This operation is not supported for directory buckets.

Gets an object's current legal hold status. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

This functionality is not supported for Amazon S3 on Outposts.

The following action is related to `GetObjectLegalHold`:
+  [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetObjectLegalHold_RequestSyntax"></a>

```
GET /{Key+}?legal-hold&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetObjectLegalHold_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetObjectLegalHold_RequestSyntax) **   <a name="AmazonS3-GetObjectLegalHold-request-header-Bucket"></a>
The bucket name containing the object whose legal hold status you want to retrieve.
 **Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [Key](#API_GetObjectLegalHold_RequestSyntax) **   <a name="AmazonS3-GetObjectLegalHold-request-uri-uri-Key"></a>
The key name for the object whose legal hold status you want to retrieve.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_GetObjectLegalHold_RequestSyntax) **   <a name="AmazonS3-GetObjectLegalHold-request-uri-querystring-VersionId"></a>
The version ID of the object whose legal hold status you want to retrieve.

 ** [x-amz-expected-bucket-owner](#API_GetObjectLegalHold_RequestSyntax) **   <a name="AmazonS3-GetObjectLegalHold-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-request-payer](#API_GetObjectLegalHold_RequestSyntax) **   <a name="AmazonS3-GetObjectLegalHold-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Request Body
<a name="API_GetObjectLegalHold_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetObjectLegalHold_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<LegalHold>
   <Status>string</Status>
</LegalHold>
```

## Response Elements
<a name="API_GetObjectLegalHold_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [LegalHold](#API_GetObjectLegalHold_ResponseSyntax) **   <a name="AmazonS3-GetObjectLegalHold-response-LegalHold"></a>
Root level tag for the LegalHold parameters.
Required: Yes

 ** [Status](#API_GetObjectLegalHold_ResponseSyntax) **   <a name="AmazonS3-GetObjectLegalHold-response-Status"></a>
Indicates whether the specified object has a legal hold in place.
Type: String
Valid Values: `ON | OFF`

## See Also
<a name="API_GetObjectLegalHold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectLegalHold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectLegalHold)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
