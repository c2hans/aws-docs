---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html
---

# GetBucketVersioning
<a name="API_GetBucketVersioning"></a>

**Note**
This operation is not supported for directory buckets.

Returns the versioning state of a bucket.

To retrieve the versioning state of a bucket, you must be the bucket owner.

This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete status is `enabled`, the bucket owner must use an authentication device to change the versioning state of the bucket.

The following operations are related to `GetBucketVersioning`:
+  [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html)
+  [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
+  [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketVersioning_RequestSyntax"></a>

```
GET /?versioning HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketVersioning_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketVersioning_RequestSyntax) **   <a name="AmazonS3-GetBucketVersioning-request-header-Bucket"></a>
The name of the bucket for which to get the versioning information.
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketVersioning_RequestSyntax) **   <a name="AmazonS3-GetBucketVersioning-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

## Request Body
<a name="API_GetBucketVersioning_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketVersioning_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration>
   <Status>string</Status>
   <MfaDelete>string</MfaDelete>
</VersioningConfiguration>
```

## Response Elements
<a name="API_GetBucketVersioning_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [VersioningConfiguration](#API_GetBucketVersioning_ResponseSyntax) **   <a name="AmazonS3-GetBucketVersioning-response-GetBucketVersioningOutput"></a>
Root level tag for the VersioningConfiguration parameters.
Required: Yes

 ** [MFADelete](#API_GetBucketVersioning_ResponseSyntax) **   <a name="AmazonS3-GetBucketVersioning-response-MFADelete"></a>
Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.
Type: String
Valid Values: `Enabled | Disabled`

 ** [Status](#API_GetBucketVersioning_ResponseSyntax) **   <a name="AmazonS3-GetBucketVersioning-response-Status"></a>
The versioning state of the bucket.
Type: String
Valid Values: `Enabled | Suspended`

## Examples
<a name="API_GetBucketVersioning_Examples"></a>

### Example
<a name="API_GetBucketVersioning_Example_1"></a>

This example returns the versioning state of `amzn-s3-demo-bucket`.

```
         GET /?versioning HTTP/1.1
         Host:amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
         Date: Wed, 12 Oct 2009 17:50:00 GMT
         Authorization: authorization string
         Content-Type: text/plain
```

### Example
<a name="API_GetBucketVersioning_Example_2"></a>

There are three versioning states:

If you enabled versioning on a bucket, the response is:

```
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Enabled</Status>
     </VersioningConfiguration>
```

### Example
<a name="API_GetBucketVersioning_Example_3"></a>

If you suspended versioning on a bucket, the response is:

```
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
        <Status>Suspended</Status>
     </VersioningConfiguration>
```

### Example
<a name="API_GetBucketVersioning_Example_4"></a>

If you never enabled (or suspended) versioning on a bucket, the response is:

```
     <VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"/>
```

## See Also
<a name="API_GetBucketVersioning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketVersioning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketVersioning)
