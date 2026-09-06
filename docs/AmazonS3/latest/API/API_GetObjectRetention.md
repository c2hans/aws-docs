---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html
---

# GetObjectRetention
<a name="API_GetObjectRetention"></a>

**Note**
This operation is not supported for directory buckets.

Retrieves an object's retention settings. For more information, see [Locking Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html).

This functionality is not supported for Amazon S3 on Outposts.

The following action is related to `GetObjectRetention`:
+  [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetObjectRetention_RequestSyntax"></a>

```
GET /{Key+}?retention&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetObjectRetention_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetObjectRetention_RequestSyntax) **   <a name="AmazonS3-GetObjectRetention-request-header-Bucket"></a>
The bucket name containing the object whose retention settings you want to retrieve.
 **Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [Key](#API_GetObjectRetention_RequestSyntax) **   <a name="AmazonS3-GetObjectRetention-request-uri-uri-Key"></a>
The key name for the object whose retention settings you want to retrieve.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_GetObjectRetention_RequestSyntax) **   <a name="AmazonS3-GetObjectRetention-request-uri-querystring-VersionId"></a>
The version ID for the object whose retention settings you want to retrieve.

 ** [x-amz-expected-bucket-owner](#API_GetObjectRetention_RequestSyntax) **   <a name="AmazonS3-GetObjectRetention-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-request-payer](#API_GetObjectRetention_RequestSyntax) **   <a name="AmazonS3-GetObjectRetention-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Request Body
<a name="API_GetObjectRetention_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetObjectRetention_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Retention>
   <Mode>string</Mode>
   <RetainUntilDate>timestamp</RetainUntilDate>
</Retention>
```

## Response Elements
<a name="API_GetObjectRetention_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [Retention](#API_GetObjectRetention_ResponseSyntax) **   <a name="AmazonS3-GetObjectRetention-response-Retention"></a>
Root level tag for the Retention parameters.
Required: Yes

 ** [Mode](#API_GetObjectRetention_ResponseSyntax) **   <a name="AmazonS3-GetObjectRetention-response-Mode"></a>
Indicates the Retention mode for the specified object.
Type: String
Valid Values: `GOVERNANCE | COMPLIANCE`

 ** [RetainUntilDate](#API_GetObjectRetention_ResponseSyntax) **   <a name="AmazonS3-GetObjectRetention-response-RetainUntilDate"></a>
The date on which this Object Lock Retention will expire.
Type: Timestamp

## See Also
<a name="API_GetObjectRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetObjectRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetObjectRetention)
