---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListReplicationFindings.html
---

# ListReplicationFindings
<a name="API_ListReplicationFindings"></a>

Lists replication findings for resources of a specified resource type in a specified Connect Customer instance. A replication finding describes a single resource whose replication to one or more Regions is incomplete or has encountered an error. Results are returned in pages. This operation is available only for instances that are set up for Global Resiliency.

## Request Syntax
<a name="API_ListReplicationFindings_RequestSyntax"></a>

```
GET /replication-findings/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReplicationFindings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListReplicationFindings_RequestSyntax) **   <a name="connect-ListReplicationFindings-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can provide either the instance ID or the full instance ARN. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_ListReplicationFindings_RequestSyntax) **   <a name="connect-ListReplicationFindings-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListReplicationFindings_RequestSyntax) **   <a name="connect-ListReplicationFindings-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 100000.

 ** [ResourceType](#API_ListReplicationFindings_RequestSyntax) **   <a name="connect-ListReplicationFindings-request-uri-ResourceType"></a>
The type of resource to list replication findings for. The following values are currently supported: `AGENT`, `AGENT_GROUP`, `AGENT_GROUP_LEVEL`, `AGENT_STATE`, `ATTRIBUTE`, `CONTACT_FLOW`, `DATA_TABLE`, `DATA_TABLE_ATTRIBUTE`, `DATA_TABLE_RECORD`, `DATA_TABLE_VALUE`, `FLOW_MODULE`, `FLOW_MODULE_ALIAS`, `FLOW_MODULE_VERSION`, `METRIC`, `NOTIFICATION`, `OPERATING_HOURS`, `PHONE_NUMBER`, `PROMPT`, `QUEUE`, `REPORT`, `ROUTING_PROFILE`, `SECURITY_PROFILE`, `TASK_TEMPLATE`, `TEST_CASE`, `TRANSFER_DESTINATION`, `VIEW`, and `WORKSPACE`. Additional resource types can be supported over time. Specifying a value that is not currently supported returns an `InvalidRequestException`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_ListReplicationFindings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReplicationFindings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateDriftedResourceCounts": [
      {
         "Count": number,
         "Region": "string",
         "Timestamp": number
      }
   ],
   "NextToken": "string",
   "ReplicationFindingsList": [
      {
         "Arn": "string",
         "Id": "string",
         "Message": "string",
         "Name": "string",
         "Operation": "string",
         "ReferenceCode": "string",
         "Region": "string",
         "ResourceType": "string"
      }
   ],
   "ResourceReplicationStatuses": [
      {
         "Region": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReplicationFindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateDriftedResourceCounts](#API_ListReplicationFindings_ResponseSyntax) **   <a name="connect-ListReplicationFindings-response-ApproximateDriftedResourceCounts"></a>
The approximate number of resources of the requested type that are not yet in sync, reported per AWS Region. This count is independent of `ReplicationFindingsList` and can be higher than the number of findings returned. It is eventually consistent and can lag the current state of the instance. Each entry is the `ApproximateDriftedResourceCount` for one Region; a Region appears only when its count has been computed.
Type: Array of [ApproximateDriftedResourceCount](API_ApproximateDriftedResourceCount.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [NextToken](#API_ListReplicationFindings_ResponseSyntax) **   <a name="connect-ListReplicationFindings-response-NextToken"></a>
If there are additional results, this is the token for retrieving the next page of `ReplicationFindingsList`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

 ** [ReplicationFindingsList](#API_ListReplicationFindings_ResponseSyntax) **   <a name="connect-ListReplicationFindings-response-ReplicationFindingsList"></a>
A list of replication findings for the requested resource type. Only findings that require your action are returned, so this list can be empty even when a drift count is nonzero. Results are paginated.
Type: Array of [ReplicationFinding](API_ReplicationFinding.md) objects

 ** [ResourceReplicationStatuses](#API_ListReplicationFindings_ResponseSyntax) **   <a name="connect-ListReplicationFindings-response-ResourceReplicationStatuses"></a>
The replication status of the requested resource type in each AWS Region across which the Connect Customer instance is deployed for Global Resiliency, with one entry per Region. This set describes the overall replication state for the request and is returned in full on every page of results, so it does not change as you paginate.
Type: Array of [ResourceReplicationStatus](API_ResourceReplicationStatus.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

## Errors
<a name="API_ListReplicationFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListReplicationFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListReplicationFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListReplicationFindings)
