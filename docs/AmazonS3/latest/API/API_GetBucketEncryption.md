---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html
---

# GetBucketEncryption
<a name="API_GetBucketEncryption"></a>

Returns the default encryption configuration for an Amazon S3 bucket. By default, all buckets have a default encryption configuration that uses server-side encryption with Amazon S3 managed keys (SSE-S3). This operation also returns the [BucketKeyEnabled](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html#AmazonS3-Type-ServerSideEncryptionRule-BucketKeyEnabled) and [BlockedEncryptionTypes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ServerSideEncryptionRule.html#AmazonS3-Type-ServerSideEncryptionRule-BlockedEncryptionTypes) statuses.

**Note**
 **General purpose buckets** - For information about the bucket default encryption feature, see [Amazon S3 Bucket Default Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the *Amazon S3 User Guide*.
 **Directory buckets** - For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS. For information about the default encryption configuration in directory buckets, see [Setting default server-side encryption behavior for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html).

Permissions
+  **General purpose bucket permissions** - The `s3:GetEncryptionConfiguration` permission is required in a policy. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources) and [Managing Access Permissions to Your Amazon S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).
+  **Directory bucket permissions** - To grant access to this API operation, you must have the `s3express:GetEncryptionConfiguration` permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn't supported. This operation can only be performed by the AWS account that owns the resource. For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

HTTP Host header syntax
 **Directory buckets ** - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

The following operations are related to `GetBucketEncryption`:
+  [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+  [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)

**Important**
You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

## Request Syntax
<a name="API_GetBucketEncryption_RequestSyntax"></a>

```
GET /?encryption HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
```

## URI Request Parameters
<a name="API_GetBucketEncryption_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_GetBucketEncryption_RequestSyntax) **   <a name="AmazonS3-GetBucketEncryption-request-header-Bucket"></a>
The name of the bucket from which the server-side encryption configuration is retrieved.
 **Directory buckets ** - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name `. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format ` bucket-base-name--zone-id--x-s3` (for example, ` DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*
Required: Yes

 ** [x-amz-expected-bucket-owner](#API_GetBucketEncryption_RequestSyntax) **   <a name="AmazonS3-GetBucketEncryption-request-header-ExpectedBucketOwner"></a>
The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).
For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code `501 Not Implemented`.

## Request Body
<a name="API_GetBucketEncryption_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBucketEncryption_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ServerSideEncryptionConfiguration>
   <Rule>
      <ApplyServerSideEncryptionByDefault>
         <KMSMasterKeyID>string</KMSMasterKeyID>
         <SSEAlgorithm>string</SSEAlgorithm>
      </ApplyServerSideEncryptionByDefault>
      <BlockedEncryptionTypes>
         <EncryptionType>string</EncryptionType>
         ...
      </BlockedEncryptionTypes>
      <BucketKeyEnabled>boolean</BucketKeyEnabled>
   </Rule>
   ...
</ServerSideEncryptionConfiguration>
```

## Response Elements
<a name="API_GetBucketEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ServerSideEncryptionConfiguration](#API_GetBucketEncryption_ResponseSyntax) **   <a name="AmazonS3-GetBucketEncryption-response-ServerSideEncryptionConfiguration"></a>
Root level tag for the ServerSideEncryptionConfiguration parameters.
Required: Yes

 ** [Rule](#API_GetBucketEncryption_ResponseSyntax) **   <a name="AmazonS3-GetBucketEncryption-response-Rules"></a>
Container for information about a particular server-side encryption configuration rule.
Type: Array of [ServerSideEncryptionRule](API_ServerSideEncryptionRule.md) data types

## Examples
<a name="API_GetBucketEncryption_Examples"></a>

### Sample Request: Retrieve the encryption configuration for an S3 general purpose bucket
<a name="API_GetBucketEncryption_Example_1"></a>

The following example shows a GET /?encryption request.

```
GET /?encryption HTTP/1.1
  Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
  Date: Wed, 06 Sep 2017 12:00:00 GMT
  Authorization: authorization string
  Content-Length: length
```

### Sample Response for a general purpose bucket
<a name="API_GetBucketEncryption_Example_2"></a>

This example illustrates one usage of `GetBucketEncryption`.

```
HTTP/1.1 200 OK
  x-amz-id-2: kDmqsuw5FDmgLmxQaUkd9A4NJ/PIiE0c1rAU/ue2Yp60toXs4I5k5fqlwZsA6fV+wJQCzRRwygQ=
  x-amz-request-id: 5D8706FCB2673B7D
  Date: Wed, 19 Nov 2025 12:00:00 GMT
  Transfer-Encoding: chunked
  Server: AmazonS3

  <ServerSideEncryptionConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
      <ApplyServerSideEncryptionByDefault>
          <SSEAlgorithm>aws:kms</SSEAlgorithm>
          <KMSKeyID>arn:aws:kms:us-east-1:1234/5678example</KMSKeyID>
      </ApplyServerSideEncryptionByDefault>
      <BlockedEncryptionTypes>
        <EncryptionType>SSE-C</EncryptionType>
      </BlockedEncryptionTypes>
  </Rule>
  </ServerSideEncryptionConfiguration>
```

## See Also
<a name="API_GetBucketEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketEncryption)
