---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateObjectEncryption.html
---

# UpdateObjectEncryption
<a name="API_UpdateObjectEncryption"></a>

**Note**
This operation is not supported for directory buckets or Amazon S3 on Outposts buckets.

 Updates the server-side encryption type of an existing encrypted object in a general purpose bucket. You can use the `UpdateObjectEncryption` operation to change encrypted objects from server-side encryption with Amazon S3 managed keys (SSE-S3) to server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), or to apply S3 Bucket Keys. You can also use the `UpdateObjectEncryption` operation to change the customer-managed KMS key used to encrypt your data so that you can comply with custom key-rotation standards.

Using the `UpdateObjectEncryption` operation, you can atomically update the server-side encryption type of an existing object in a general purpose bucket without any data movement. The `UpdateObjectEncryption` operation uses envelope encryption to re-encrypt the data key used to encrypt and decrypt your object with your newly specified server-side encryption type. In other words, when you use the `UpdateObjectEncryption` operation, your data isn't copied, archived objects in the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes aren't restored, and objects in the S3 Intelligent-Tiering storage class aren't moved between tiers. Additionally, the `UpdateObjectEncryption` operation preserves all object metadata properties, including the storage class, creation date, last modified date, ETag, and checksum properties. For more information, see [ Updating server-side encryption for existing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/update-sse-encryption.html) in the *Amazon S3 User Guide*.

By default, all `UpdateObjectEncryption` requests that specify a customer-managed KMS key are restricted to KMS keys that are owned by the bucket owner's AWS account. If you're using AWS Organizations, you can request the ability to use KMS keys owned by other member accounts within your organization by contacting AWS Support.

**Note**
Source objects that are unencrypted, or encrypted with either dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) or server-side encryption with customer-provided keys (SSE-C) aren't supported by this operation. Additionally, you cannot specify SSE-S3 encryption as the requested new encryption type `UpdateObjectEncryption` request.

Permissions
+ To use the `UpdateObjectEncryption` operation, you must have the following permissions:
  +  `s3:UpdateObjectEncryption`
  +  `kms:Encrypt`
  +  `kms:Decrypt`
  +  `kms:GenerateDataKey`
  +  `kms:ReEncrypt*`
+ If you're using AWS Organizations, to use this operation with customer-managed KMS keys from other AWS accounts within your organization, you must have the `organizations:DescribeAccount` permission.

Errors
+ You might receive an `InvalidRequest` error for several reasons. Depending on the reason for the error, you might receive one of the following messages:
  + The `UpdateObjectEncryption` operation doesn't supported unencrypted source objects. Only source objects encrypted with SSE-S3 or SSE-KMS are supported.
  + The `UpdateObjectEncryption` operation doesn't support source objects with the encryption type DSSE-KMS or SSE-C. Only source objects encrypted with SSE-S3 or SSE-KMS are supported.
  + The `UpdateObjectEncryption` operation doesn't support updating the encryption type to DSSE-KMS or SSE-C. Modify the request to specify SSE-KMS for the updated encryption type, and then try again.
  + Requests that modify an object encryption configuration require AWS Signature Version 4. Modify the request to use AWS Signature Version 4, and then try again.
  + Requests that modify an object encryption configuration require a valid new encryption type. Valid values are `SSEKMS`. Modify the request to specify SSE-KMS for the updated encryption type, and then try again.
  + Requests that modify an object's encryption type to SSE-KMS require an AWS KMS key Amazon Resource Name (ARN). Modify the request to specify a KMS key ARN, and then try again.
  + Requests that modify an object's encryption type to SSE-KMS require a valid AWS KMS key Amazon Resource Name (ARN). Confirm that you have a correctly formatted KMS key ARN in your request, and then try again.
  + The `BucketKeyEnabled` value isn't valid. Valid values are `true` or `false`. Modify the request to specify a valid value, and then try again.
+ You might receive an `AccessDenied` error for several reasons. Depending on the reason for the error, you might receive one of the following messages:
  + The AWS KMS key in the request must be owned by the same account as the bucket. Modify the request to specify a KMS key from the same account, and then try again.
  + The bucket owner's account was approved to make `UpdateObjectEncryption` requests that use any AWS KMS key in their organization, but the bucket owner's account isn't part of an organization in AWS Organizations. Make sure that the bucket owner's account and the specified KMS key belong to the same organization, and then try again.
  + The specified AWS KMS key must be from the same organization in AWS Organizations as the bucket. Specify a KMS key that belongs to the same organization as the bucket, and then try again.
  + The encryption type for the specified object can’t be updated because that object is protected by S3 Object Lock. If the object has a governance-mode retention period or a legal hold, you must first remove the Object Lock status on the object before you issue your `UpdateObjectEncryption` request. You can't use the `UpdateObjectEncryption` operation with objects that have an Object Lock compliance mode retention period applied to them.

## Request Syntax
<a name="API_UpdateObjectEncryption_RequestSyntax"></a>

```
PUT /{Key+}?encryption&versionId={{VersionId}} HTTP/1.1
Host: {{Bucket}}.s3.amazonaws.com
x-amz-request-payer: {{RequestPayer}}
x-amz-expected-bucket-owner: {{ExpectedBucketOwner}}
Content-MD5: {{ContentMD5}}
x-amz-sdk-checksum-algorithm: {{ChecksumAlgorithm}}
<?xml version="1.0" encoding="UTF-8"?>
<ObjectEncryption xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <SSE-KMS>
      <BucketKeyEnabled>{{boolean}}</BucketKeyEnabled>
      <KMSKeyArn>{{string}}</KMSKeyArn>
   </SSE-KMS>
</ObjectEncryption>
```

## URI Request Parameters
<a name="API_UpdateObjectEncryption_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Bucket](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-header-Bucket"></a>
 The name of the general purpose bucket that contains the specified object key name.
When you use this operation with an access point attached to a general purpose bucket, you must either provide the alias of the access point in place of the bucket name or you must specify the access point Amazon Resource Name (ARN). When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form ` AccessPointName-AccountId.s3-accesspoint.Region.amazonaws.com`. When using this operation with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [ Referencing access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-naming.html) in the *Amazon S3 User Guide*.
Required: Yes

 ** [Content-MD5](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-header-ContentMD5"></a>
 The MD5 hash for the request body. For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.

 ** [Key](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-uri-uri-Key"></a>
 The key name of the object that you want to update the server-side encryption type for.
Length Constraints: Minimum length of 1.
Required: Yes

 ** [versionId](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-uri-querystring-VersionId"></a>
 The version ID of the object that you want to update the server-side encryption type for.

 ** [x-amz-expected-bucket-owner](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-header-ExpectedBucketOwner"></a>
 The account ID of the expected bucket owner. If the account ID that you provide doesn't match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

 ** [x-amz-request-payer](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-header-RequestPayer"></a>
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. If either the source or destination S3 bucket has Requester Pays enabled, the requester will pay for the corresponding charges. For information about downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the *Amazon S3 User Guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

 ** [x-amz-sdk-checksum-algorithm](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-header-ChecksumAlgorithm"></a>
 Indicates the algorithm used to create the checksum for the object when you use an AWS SDK. This header doesn't provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more information, see [ Checking object integrity ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm` parameter.
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`

## Request Body
<a name="API_UpdateObjectEncryption_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ObjectEncryption](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-ObjectEncryption"></a>
Root level tag for the ObjectEncryption parameters.
Required: Yes

 ** [SSEKMS](#API_UpdateObjectEncryption_RequestSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-request-SSEKMS"></a>
 Specifies to update the object encryption type to server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS).
Type: [SSEKMSEncryption](API_SSEKMSEncryption.md) data type
Required: No

## Response Syntax
<a name="API_UpdateObjectEncryption_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-request-charged: {{RequestCharged}}
```

## Response Elements
<a name="API_UpdateObjectEncryption_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [x-amz-request-charged](#API_UpdateObjectEncryption_ResponseSyntax) **   <a name="AmazonS3-UpdateObjectEncryption-response-header-RequestCharged"></a>
If present, indicates that the requester was successfully charged for the request. For more information, see [Using Requester Pays buckets for storage transfers and usage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html) in the *Amazon Simple Storage Service user guide*.
This functionality is not supported for directory buckets.
Valid Values: `requester`

## Errors
<a name="API_UpdateObjectEncryption_Errors"></a>

 ** AccessDenied **
 You might receive this error for several reasons. For details, see the description of this API operation.
HTTP Status Code: 403

 ** InvalidRequest **
A parameter or header in your request isn't valid. For details, see the description of this API operation.
HTTP Status Code: 400

 ** NoSuchKey **
The specified key does not exist.
HTTP Status Code: 404

## Examples
<a name="API_UpdateObjectEncryption_Examples"></a>

### Sample Request: Updating encryption type to SSE-KMS with S3 Bucket Keys enabled
<a name="API_UpdateObjectEncryption_Example_1"></a>

The following example request illustrates updating the server-side encryption type of the `example.txt` object in the `amzn-s3-demo-bucket` bucket to SSE-KMS with S3 Bucket Keys enabled.

```
PUT /example.txt?encryption&versionId=VersionId HTTP/1.1
Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
x-amz-request-payer: <RequestPayer>
x-amz-expected-bucket-owner: <ExpectedBucketOwner>
Content-MD5: <ContentMD5>
x-amz-sdk-checksum-algorithm: <ChecksumAlgorithm>
<?xml version="1.0" encoding="UTF-8"?>
<ObjectEncryption xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <SSE-KMS>
      <BucketKeyEnabled>true</BucketKeyEnabled>
      <KMSKeyArn>arn:aws:kms:<Region>:<AccountId>:key/<KeyID></KMSKeyArn>
   </SSE-KMS>
</ObjectEncryption>
```

## See Also
<a name="API_UpdateObjectEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateObjectEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateObjectEncryption)
