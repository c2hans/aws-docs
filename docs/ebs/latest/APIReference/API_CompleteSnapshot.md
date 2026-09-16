---
source_url: https://docs.aws.amazon.com/ebs/latest/APIReference/API_CompleteSnapshot.html
---

# CompleteSnapshot
<a name="API_CompleteSnapshot"></a>

Seals and completes the snapshot after all of the required blocks of data have been written to it. Completing the snapshot changes the status to `completed`. You cannot write new blocks to a snapshot after it has been completed.

**Note**
You should always retry requests that receive server (`5xx`) error responses, and `ThrottlingException` and `RequestThrottledException` client error responses. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Syntax
<a name="API_CompleteSnapshot_RequestSyntax"></a>

```
POST /snapshots/completion/{{snapshotId}} HTTP/1.1
x-amz-ChangedBlocksCount: {{ChangedBlocksCount}}
x-amz-Checksum: {{Checksum}}
x-amz-Checksum-Algorithm: {{ChecksumAlgorithm}}
x-amz-Checksum-Aggregation-Method: {{ChecksumAggregationMethod}}
```

## URI Request Parameters
<a name="API_CompleteSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChangedBlocksCount](#API_CompleteSnapshot_RequestSyntax) **   <a name="ebs-CompleteSnapshot-request-ChangedBlocksCount"></a>
The number of blocks that were written to the snapshot.
Valid Range: Minimum value of 0.
Required: Yes

 ** [Checksum](#API_CompleteSnapshot_RequestSyntax) **   <a name="ebs-CompleteSnapshot-request-Checksum"></a>
An aggregated Base-64 SHA256 checksum based on the checksums of each written block.
To generate the aggregated checksum using the linear aggregation method, arrange the checksums for each written block in ascending order of their block index, concatenate them to form a single string, and then generate the checksum on the entire string using the SHA256 algorithm.
Length Constraints: Maximum length of 64.
Pattern: `^[A-Za-z0-9+/=]+$`

 ** [ChecksumAggregationMethod](#API_CompleteSnapshot_RequestSyntax) **   <a name="ebs-CompleteSnapshot-request-ChecksumAggregationMethod"></a>
The aggregation method used to generate the checksum. Currently, the only supported aggregation method is `LINEAR`.
Length Constraints: Maximum length of 32.
Pattern: `^[A-Za-z0-9]+$`
Valid Values: `LINEAR`

 ** [ChecksumAlgorithm](#API_CompleteSnapshot_RequestSyntax) **   <a name="ebs-CompleteSnapshot-request-ChecksumAlgorithm"></a>
The algorithm used to generate the checksum. Currently, the only supported algorithm is `SHA256`.
Length Constraints: Maximum length of 32.
Pattern: `^[A-Za-z0-9]+$`
Valid Values: `SHA256`

 ** [snapshotId](#API_CompleteSnapshot_RequestSyntax) **   <a name="ebs-CompleteSnapshot-request-uri-SnapshotId"></a>
The ID of the snapshot.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^snap-[0-9a-f]+$`
Required: Yes

## Request Body
<a name="API_CompleteSnapshot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CompleteSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "Status": "string"
}
```

## Response Elements
<a name="API_CompleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_CompleteSnapshot_ResponseSyntax) **   <a name="ebs-CompleteSnapshot-response-Status"></a>
The status of the snapshot.
Type: String
Length Constraints: Maximum length of 32.
Valid Values: `completed | pending | error`

## Errors
<a name="API_CompleteSnapshot_Errors"></a>

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
<a name="API_CompleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ebs-2019-11-02/CompleteSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ebs-2019-11-02/CompleteSnapshot)
