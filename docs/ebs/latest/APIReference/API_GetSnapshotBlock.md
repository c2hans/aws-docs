---
source_url: https://docs.aws.amazon.com/ebs/latest/APIReference/API_GetSnapshotBlock.html
---

# GetSnapshotBlock
<a name="API_GetSnapshotBlock"></a>

Returns the data in a block in an Amazon Elastic Block Store snapshot.

**Note**
You should always retry requests that receive server (`5xx`) error responses, and `ThrottlingException` and `RequestThrottledException` client error responses. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Syntax
<a name="API_GetSnapshotBlock_RequestSyntax"></a>

```
GET /snapshots/{{snapshotId}}/blocks/{{blockIndex}}?blockToken={{BlockToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSnapshotBlock_RequestParameters"></a>

The request uses the following URI parameters.

 ** [blockIndex](#API_GetSnapshotBlock_RequestSyntax) **   <a name="ebs-GetSnapshotBlock-request-uri-BlockIndex"></a>
The block index of the block in which to read the data. A block index is a logical index in units of `512` KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data/`524288`). The logical offset of the data must be `512` KiB aligned.
Valid Range: Minimum value of 0.
Required: Yes

 ** [BlockToken](#API_GetSnapshotBlock_RequestSyntax) **   <a name="ebs-GetSnapshotBlock-request-uri-BlockToken"></a>
The block token of the block from which to get data. You can obtain the `BlockToken` by running the `ListChangedBlocks` or `ListSnapshotBlocks` operations.
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`
Required: Yes

 ** [snapshotId](#API_GetSnapshotBlock_RequestSyntax) **   <a name="ebs-GetSnapshotBlock-request-uri-SnapshotId"></a>
The ID of the snapshot containing the block from which to get data.
If the specified snapshot is encrypted, you must have permission to use the KMS key that was used to encrypt the snapshot. For more information, see [ Using encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html) in the *Amazon Elastic Compute Cloud User Guide*.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^snap-[0-9a-f]+$`
Required: Yes

## Request Body
<a name="API_GetSnapshotBlock_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSnapshotBlock_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-Data-Length: {{DataLength}}
x-amz-Checksum: {{Checksum}}
x-amz-Checksum-Algorithm: {{ChecksumAlgorithm}}

{{BlockData}}
```

## Response Elements
<a name="API_GetSnapshotBlock_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [Checksum](#API_GetSnapshotBlock_ResponseSyntax) **   <a name="ebs-GetSnapshotBlock-response-Checksum"></a>
The checksum generated for the block, which is Base64 encoded.
Length Constraints: Maximum length of 64.
Pattern: `^[A-Za-z0-9+/=]+$`

 ** [ChecksumAlgorithm](#API_GetSnapshotBlock_ResponseSyntax) **   <a name="ebs-GetSnapshotBlock-response-ChecksumAlgorithm"></a>
The algorithm used to generate the checksum for the block, such as SHA256.
Length Constraints: Maximum length of 32.
Pattern: `^[A-Za-z0-9]+$`
Valid Values: `SHA256`

 ** [DataLength](#API_GetSnapshotBlock_ResponseSyntax) **   <a name="ebs-GetSnapshotBlock-response-DataLength"></a>
The size of the data in the block.

The response returns the following as the HTTP body.

 ** [BlockData](#API_GetSnapshotBlock_ResponseSyntax) **   <a name="ebs-GetSnapshotBlock-response-BlockData"></a>
The data content of the block.

## Errors
<a name="API_GetSnapshotBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the exception.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html).
HTTP Status Code: 500

 ** RequestThrottledException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html).
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** Reason **
The reason for the exception.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Your current service quotas do not allow you to perform this action.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints of the EBS direct APIs.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetSnapshotBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ebs-2019-11-02/GetSnapshotBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ebs-2019-11-02/GetSnapshotBlock)
