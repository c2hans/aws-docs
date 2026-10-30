---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeReplicationBackfillResults.html
---

# DescribeReplicationBackfillResults
<a name="API_DescribeReplicationBackfillResults"></a>

Returns the status, progress, and per-image results for a replication backfill. The backfill to describe is identified by the `replicationBackfillId` returned by the [StartReplicationBackfill](API_StartReplicationBackfill.md) operation.

**Note**
The per-image results are available only after the replication backfill reaches a terminal status.

## Request Syntax
<a name="API_DescribeReplicationBackfillResults_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "replicationBackfillId": "{{string}}",
   "resultStatusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReplicationBackfillResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeReplicationBackfillResults_RequestSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-request-maxResults"></a>
The maximum number of replication backfill results returned by `DescribeReplicationBackfillResults` in paginated output. When this parameter is used, `DescribeReplicationBackfillResults` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeReplicationBackfillResults` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `DescribeReplicationBackfillResults` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeReplicationBackfillResults_RequestSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeReplicationBackfillResults` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_DescribeReplicationBackfillResults_RequestSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-request-registryId"></a>
The AWS account ID associated with the registry that contains the replication backfill to describe. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [replicationBackfillId](#API_DescribeReplicationBackfillResults_RequestSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-request-replicationBackfillId"></a>
The ID of the replication backfill to describe.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [resultStatusFilter](#API_DescribeReplicationBackfillResults_RequestSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-request-resultStatusFilter"></a>
The status used to filter the returned results. Each result has a status of `COMPLETE` or `FAILED`. If you omit this parameter, results with both statuses are returned.
Type: String
Valid Values: `COMPLETE | FAILED`
Required: No

## Response Syntax
<a name="API_DescribeReplicationBackfillResults_ResponseSyntax"></a>

```
{
   "destination": {
      "region": "string",
      "registryId": "string"
   },
   "endedAt": number,
   "failureCode": "string",
   "nextToken": "string",
   "progress": {
      "completedReplicationCount": number,
      "failedReplicationCount": number,
      "failureCodes": [ "string" ],
      "totalReplicationCount": number
   },
   "registryId": "string",
   "replicationBackfillId": "string",
   "results": [
      {
         "failureCode": "string",
         "imageId": {
            "imageDigest": "string",
            "imageTag": "string"
         },
         "repositoryName": "string",
         "status": "string",
         "subImageFailureCodes": [ "string" ]
      }
   ],
   "startedAt": number,
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeReplicationBackfillResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destination](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-destination"></a>
The destination Region and registry to which the images are replicated.
Type: [ReplicationDestination](API_ReplicationDestination.md) object

 ** [endedAt](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-endedAt"></a>
The date and time, in JavaScript date format, when the replication backfill ended. This value is `null` while the replication backfill is still in progress.
Type: Timestamp

 ** [failureCode](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-failureCode"></a>
The failure code for a replication backfill that has failed.
Type: String

 ** [nextToken](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeReplicationBackfillResults` request. When the results of a `DescribeReplicationBackfillResults` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [progress](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-progress"></a>
The progress of the replication backfill, including the total, completed, and failed replication counts. This value is `null` until the replication backfill finishes preparing the set of images to replicate. It is therefore `null` while the replication backfill is `PREPARING`, and remains `null` if the replication backfill is stopped before preparation completes.
Type: [ReplicationBackfillProgress](API_ReplicationBackfillProgress.md) object

 ** [registryId](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [replicationBackfillId](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-replicationBackfillId"></a>
The ID of the replication backfill.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [results](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-results"></a>
The per-image results for the replication backfill. Results are available only after the replication backfill reaches a terminal status.
Type: Array of [ReplicationBackfillResult](API_ReplicationBackfillResult.md) objects

 ** [startedAt](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-startedAt"></a>
The date and time, in JavaScript date format, when the replication backfill was started.
Type: Timestamp

 ** [status](#API_DescribeReplicationBackfillResults_ResponseSyntax) **   <a name="ECR-DescribeReplicationBackfillResults-response-status"></a>
The current status of the replication backfill.
Type: String
Valid Values: `PREPARING | IN_PROGRESS | COMPLETE | FAILED | STOPPING | STOPPED`

## Errors
<a name="API_DescribeReplicationBackfillResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ReplicationBackfillNotFoundException **
The specified replication backfill could not be found. Check the specified replication backfill ID and ensure that you are operating on the correct registry.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeReplicationBackfillResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribeReplicationBackfillResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribeReplicationBackfillResults)
