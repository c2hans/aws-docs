---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StopReplicationBackfill.html
---

# StopReplicationBackfill
<a name="API_StopReplicationBackfill"></a>

Stops an in progress replication backfill for a registry. The backfill to stop is identified by the `replicationBackfillId` returned by the [StartReplicationBackfill](API_StartReplicationBackfill.md) operation.

**Note**
Images that have already been replicated are not affected, and replications that are already in progress continue to completion.

## Request Syntax
<a name="API_StopReplicationBackfill_RequestSyntax"></a>

```
{
   "registryId": "{{string}}",
   "replicationBackfillId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopReplicationBackfill_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [registryId](#API_StopReplicationBackfill_RequestSyntax) **   <a name="ECR-StopReplicationBackfill-request-registryId"></a>
The AWS account ID associated with the registry that contains the replication backfill to stop. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [replicationBackfillId](#API_StopReplicationBackfill_RequestSyntax) **   <a name="ECR-StopReplicationBackfill-request-replicationBackfillId"></a>
The ID of the replication backfill to stop.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_StopReplicationBackfill_ResponseSyntax"></a>

```
{
   "destination": {
      "region": "string",
      "registryId": "string"
   },
   "registryId": "string",
   "replicationBackfillId": "string",
   "startedAt": number,
   "status": "string"
}
```

## Response Elements
<a name="API_StopReplicationBackfill_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destination](#API_StopReplicationBackfill_ResponseSyntax) **   <a name="ECR-StopReplicationBackfill-response-destination"></a>
The destination Region and registry to which the images are replicated.
Type: [ReplicationDestination](API_ReplicationDestination.md) object

 ** [registryId](#API_StopReplicationBackfill_ResponseSyntax) **   <a name="ECR-StopReplicationBackfill-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

 ** [replicationBackfillId](#API_StopReplicationBackfill_ResponseSyntax) **   <a name="ECR-StopReplicationBackfill-response-replicationBackfillId"></a>
The ID of the replication backfill.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [startedAt](#API_StopReplicationBackfill_ResponseSyntax) **   <a name="ECR-StopReplicationBackfill-response-startedAt"></a>
The date and time, in JavaScript date format, when the replication backfill was started.
Type: Timestamp

 ** [status](#API_StopReplicationBackfill_ResponseSyntax) **   <a name="ECR-StopReplicationBackfill-response-status"></a>
The current status of the replication backfill. When you stop a replication backfill, its status is `STOPPED` if the backfill is stopped immediately, or `STOPPING` if there are replications still in progress that must complete before the backfill stops.
Type: String
Valid Values: `PREPARING | IN_PROGRESS | COMPLETE | FAILED | STOPPING | STOPPED`

## Errors
<a name="API_StopReplicationBackfill_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** ReplicationBackfillInvalidStatusException **
The requested operation can't be performed on the replication backfill because it is not in a valid status for that operation. For example, you can't stop a replication backfill that has already reached a terminal status. Use the [DescribeReplicationBackfillResults](API_DescribeReplicationBackfillResults.md) operation to check the current status before retrying.
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
<a name="API_StopReplicationBackfill_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/StopReplicationBackfill)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/StopReplicationBackfill)
