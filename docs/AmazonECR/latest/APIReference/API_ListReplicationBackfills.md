---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListReplicationBackfills.html
---

# ListReplicationBackfills
<a name="API_ListReplicationBackfills"></a>

Lists the replication backfills for a registry, including their status and progress.

**Note**
Replication backfills that have reached a terminal status are retained for 90 days after they end, after which they are no longer returned.

## Request Syntax
<a name="API_ListReplicationBackfills_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReplicationBackfills_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListReplicationBackfills_RequestSyntax) **   <a name="ECR-ListReplicationBackfills-request-maxResults"></a>
The maximum number of replication backfill results returned by `ListReplicationBackfills` in paginated output. When this parameter is used, `ListReplicationBackfills` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListReplicationBackfills` request with the returned `nextToken` value. This value can be between 1 and 50. If this parameter is not used, then `ListReplicationBackfills` returns up to 25 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListReplicationBackfills_RequestSyntax) **   <a name="ECR-ListReplicationBackfills-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListReplicationBackfills` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_ListReplicationBackfills_RequestSyntax) **   <a name="ECR-ListReplicationBackfills-request-registryId"></a>
The AWS account ID associated with the registry for which to list replication backfills. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_ListReplicationBackfills_ResponseSyntax"></a>

```
{
   "backfills": [
      {
         "destination": {
            "region": "string",
            "registryId": "string"
         },
         "endedAt": number,
         "failureCode": "string",
         "progress": {
            "completedReplicationCount": number,
            "failedReplicationCount": number,
            "failureCodes": [ "string" ],
            "totalReplicationCount": number
         },
         "replicationBackfillId": "string",
         "startedAt": number,
         "status": "string"
      }
   ],
   "nextToken": "string",
   "registryId": "string"
}
```

## Response Elements
<a name="API_ListReplicationBackfills_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [backfills](#API_ListReplicationBackfills_ResponseSyntax) **   <a name="ECR-ListReplicationBackfills-response-backfills"></a>
A list of the replication backfills for the registry.
Type: Array of [ReplicationBackfillSummary](API_ReplicationBackfillSummary.md) objects

 ** [nextToken](#API_ListReplicationBackfills_ResponseSyntax) **   <a name="ECR-ListReplicationBackfills-response-nextToken"></a>
The `nextToken` value to include in a future `ListReplicationBackfills` request. When the results of a `ListReplicationBackfills` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [registryId](#API_ListReplicationBackfills_ResponseSyntax) **   <a name="ECR-ListReplicationBackfills-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

## Errors
<a name="API_ListReplicationBackfills_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
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
<a name="API_ListReplicationBackfills_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/ListReplicationBackfills)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ListReplicationBackfills)
