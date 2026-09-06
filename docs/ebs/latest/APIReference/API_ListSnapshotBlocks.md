---
source_url: https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListSnapshotBlocks.html
---

# ListSnapshotBlocks
<a name="API_ListSnapshotBlocks"></a>

Returns information about the blocks in an Amazon Elastic Block Store snapshot.

**Note**
You should always retry requests that receive server (`5xx`) error responses, and `ThrottlingException` and `RequestThrottledException` client error responses. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Syntax
<a name="API_ListSnapshotBlocks_RequestSyntax"></a>

```
GET /snapshots/{{snapshotId}}/blocks?maxResults={{MaxResults}}&pageToken={{NextToken}}&startingBlockIndex={{StartingBlockIndex}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSnapshotBlocks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListSnapshotBlocks_RequestSyntax) **   <a name="ebs-ListSnapshotBlocks-request-uri-MaxResults"></a>
The maximum number of blocks to be returned by the request.
Even if additional blocks can be retrieved from the snapshot, the request can return less blocks than **MaxResults** or an empty array of blocks.
To retrieve the next set of blocks from the snapshot, make another request with the returned **NextToken** value. The value of **NextToken** is `null` when there are no more blocks to return.
Valid Range: Minimum value of 100. Maximum value of 10000.

 ** [NextToken](#API_ListSnapshotBlocks_RequestSyntax) **   <a name="ebs-ListSnapshotBlocks-request-uri-NextToken"></a>
The token to request the next page of results.
If you specify **NextToken**, then **StartingBlockIndex** is ignored.
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`

 ** [snapshotId](#API_ListSnapshotBlocks_RequestSyntax) **   <a name="ebs-ListSnapshotBlocks-request-uri-SnapshotId"></a>
The ID of the snapshot from which to get block indexes and block tokens.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^snap-[0-9a-f]+$`
Required: Yes

 ** [StartingBlockIndex](#API_ListSnapshotBlocks_RequestSyntax) **   <a name="ebs-ListSnapshotBlocks-request-uri-StartingBlockIndex"></a>
The block index from which the list should start. The list in the response will start from this block index or the next valid block index in the snapshot.
If you specify **NextToken**, then **StartingBlockIndex** is ignored.
Valid Range: Minimum value of 0.

## Request Body
<a name="API_ListSnapshotBlocks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSnapshotBlocks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Blocks": [
      {
         "BlockIndex": number,
         "BlockToken": "string"
      }
   ],
   "BlockSize": number,
   "ExpiryTime": number,
   "NextToken": "string",
   "VolumeSize": number
}
```

## Response Elements
<a name="API_ListSnapshotBlocks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blocks](#API_ListSnapshotBlocks_ResponseSyntax) **   <a name="ebs-ListSnapshotBlocks-response-Blocks"></a>
An array of objects containing information about the blocks.
Type: Array of [Block](API_Block.md) objects

 ** [BlockSize](#API_ListSnapshotBlocks_ResponseSyntax) **   <a name="ebs-ListSnapshotBlocks-response-BlockSize"></a>
The size of the blocks in the snapshot, in bytes.
Type: Integer

 ** [ExpiryTime](#API_ListSnapshotBlocks_ResponseSyntax) **   <a name="ebs-ListSnapshotBlocks-response-ExpiryTime"></a>
The time when the `BlockToken` expires.
Type: Timestamp

 ** [NextToken](#API_ListSnapshotBlocks_ResponseSyntax) **   <a name="ebs-ListSnapshotBlocks-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[A-Za-z0-9+/=]+$`

 ** [VolumeSize](#API_ListSnapshotBlocks_ResponseSyntax) **   <a name="ebs-ListSnapshotBlocks-response-VolumeSize"></a>
The size of the volume in GB.
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_ListSnapshotBlocks_Errors"></a>

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
<a name="API_ListSnapshotBlocks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ebs-2019-11-02/ListSnapshotBlocks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ebs-2019-11-02/ListSnapshotBlocks)
