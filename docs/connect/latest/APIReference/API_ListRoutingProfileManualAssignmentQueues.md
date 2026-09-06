---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRoutingProfileManualAssignmentQueues.html
---

# ListRoutingProfileManualAssignmentQueues
<a name="API_ListRoutingProfileManualAssignmentQueues"></a>

Lists the manual assignment queues associated with a routing profile.

 **Use cases**

Following are common uses cases for this API:
+ This API returns list of queues where contacts can be manually assigned or picked by an agent who has access to the Worklist app. The user can additionally filter on queues, if they have access to those queues (otherwise a invalid request exception will be thrown).

  For information about how manual contact assignment works in the agent workspace, see the [Access the Worklist app in the Connect Customer agent workspace](https://docs.aws.amazon.com/connect/latest/adminguide/worklist-app.html) in the *Connect Customer Administrator Guide*.

 **Important things to know**
+ This API only returns the manual assignment queues associated with a routing profile. Use the ListRoutingProfileQueues API to list the auto assignment queues for the routing profile.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_ListRoutingProfileManualAssignmentQueues_RequestSyntax"></a>

```
GET /routing-profiles/{{InstanceId}}/{{RoutingProfileId}}/manual-assignment-queues?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRoutingProfileManualAssignmentQueues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListRoutingProfileManualAssignmentQueues_RequestSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListRoutingProfileManualAssignmentQueues_RequestSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListRoutingProfileManualAssignmentQueues_RequestSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [RoutingProfileId](#API_ListRoutingProfileManualAssignmentQueues_RequestSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-request-uri-RoutingProfileId"></a>
The identifier of the routing profile.
Required: Yes

## Request Body
<a name="API_ListRoutingProfileManualAssignmentQueues_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRoutingProfileManualAssignmentQueues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastModifiedRegion": "string",
   "LastModifiedTime": number,
   "NextToken": "string",
   "RoutingProfileManualAssignmentQueueConfigSummaryList": [
      {
         "Channel": "string",
         "QueueArn": "string",
         "QueueId": "string",
         "QueueName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRoutingProfileManualAssignmentQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastModifiedRegion](#API_ListRoutingProfileManualAssignmentQueues_ResponseSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-response-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_ListRoutingProfileManualAssignmentQueues_ResponseSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-response-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp

 ** [NextToken](#API_ListRoutingProfileManualAssignmentQueues_ResponseSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [RoutingProfileManualAssignmentQueueConfigSummaryList](#API_ListRoutingProfileManualAssignmentQueues_ResponseSyntax) **   <a name="connect-ListRoutingProfileManualAssignmentQueues-response-RoutingProfileManualAssignmentQueueConfigSummaryList"></a>
Information about the manual assignment queues associated with the routing profile.
Type: Array of [RoutingProfileManualAssignmentQueueConfigSummary](API_RoutingProfileManualAssignmentQueueConfigSummary.md) objects

## Errors
<a name="API_ListRoutingProfileManualAssignmentQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

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

## Examples
<a name="API_ListRoutingProfileManualAssignmentQueues_Examples"></a>

### Example request to retrieve the manual assignment queues
<a name="API_ListRoutingProfileManualAssignmentQueues_Example_1"></a>

Provide instanceId and routingProfileId for which you want to retrieve the manual assignment queues. You can optionally provide MaxResults parameter.

```
PUT https://connect.us-west-2.amazonaws.com/routing-profiles/{{instance_id}}/{{routingProfileId}}/manual-assignment-queues HTTP/1.1 Content-type: application/json
{
     "MaxResults": 1
}
```

### Example response to list the manual assignment queues
<a name="API_ListRoutingProfileManualAssignmentQueues_Example_2"></a>

 Lists the manual assignment queues associated with the `routingProfileId`. Includes only one result since MaxResults parameter was 1. Also includes a NextToken, which can be used as input to fetch the remaining results.

```
{
    "LastModifiedRegion": "us-west-2",
    "LastModifiedTime": 1.75735455979E9,
    "NextToken": "AQICAHjfUasjUykoODDhNKl2HebKOGiYdLPRfLHRCAwv4m2pxQFto9/8mR5l9ttjq9pNVQmNAAAByzCCAccGCSqGSIb3DQEHBqCCAbgwggG0AgEAMIIBrQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzA10RtjnfHtBRMGfECARCAggF+PluTA4SojLX+eTvUKdEPCmi7jYLeUmMxLLKWWY2Q853Q0Mqd7rnPo1RKs/cILump20rk2lWa0cX894lTJDxNECkZnOh0EaD4MEd4hZ0eDvDOGzDc7IqHX29U9gtEjFc0Z6AZiBhRDqEHOMQB0egAN9m0HibtmcDzn00TPzBME6MWnBoZBCNiwCZEOpxLoFwc/U2/2oXixa3NFogkJAgRrVWcK5IKYx3DPN5e2rsk0mDylOZGneTNILeSt+zQ95m6bJj5Nm+wFbxr+mpxs8ZPTpwRVTjz/vThFmdmlLv42/uZCkXvq4IULyq2le98cq/nwTXnYtr3e3qQdQ4EHOi+Iettbv+p6TT3UxZIG/CETvGf0CP3uu9F64vG+iOWyDPtamaQjPRvZS+Wtb8awprNBVl9h8jkHZsM5C9+PbZoU7U9qqX67w96BSyxIXzsvs+8Oq5myvifbG+c1QxCnQWzlyXyHmKuRdRgE6rttiqOdw9J4DtwBlmFrC40V7FwCA==",
    "RoutingProfileManualAssignmentQueueConfigSummaryList": [
        {
            "Channel": "VOICE",
            "QueueArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/queue/12345678-1234-5678-aabb-123456abcdef",
            "QueueId": "12345678-1234-5678-aabb-123456abcdef",
            "QueueName": "Q_NAME_1"
        }
    ]
}
```

### Example request to fetch the remaining manual assignment queues associated with a routing profile
<a name="API_ListRoutingProfileManualAssignmentQueues_Example_3"></a>

Use NextToken from previous response to fetch the remaining manual assignment queues associated with a routing profile.

```
PUT https://connect.us-west-2.amazonaws.com/routing-profiles/{{instance_id}}/{{routingProfileId}}/manual-assignment-queues HTTP/1.1 Content-type: application/json
{
    "MaxResults": 1,
    "NextToken": "AQICAHjfUasjUykoODDhNKl2HebKOGiYdLPRfLHRCAwv4m2pxQFto9/8mR5l9ttjq9pNVQmNAAAByzCCAccGCSqGSIb3DQEHBqCCAbgwggG0AgEAMIIBrQYJKoZIhvcNAQcBMB4GCWCGSAFlAwQBLjARBAzA10RtjnfHtBRMGfECARCAggF+PluTA4SojLX+eTvUKdEPCmi7jYLeUmMxLLKWWY2Q853Q0Mqd7rnPo1RKs/cILump20rk2lWa0cX894lTJDxNECkZnOh0EaD4MEd4hZ0eDvDOGzDc7IqHX29U9gtEjFc0Z6AZiBhRDqEHOMQB0egAN9m0HibtmcDzn00TPzBME6MWnBoZBCNiwCZEOpxLoFwc/U2/2oXixa3NFogkJAgRrVWcK5IKYx3DPN5e2rsk0mDylOZGneTNILeSt+zQ95m6bJj5Nm+wFbxr+mpxs8ZPTpwRVTjz/vThFmdmlLv42/uZCkXvq4IULyq2le98cq/nwTXnYtr3e3qQdQ4EHOi+Iettbv+p6TT3UxZIG/CETvGf0CP3uu9F64vG+iOWyDPtamaQjPRvZS+Wtb8awprNBVl9h8jkHZsM5C9+PbZoU7U9qqX67w96BSyxIXzsvs+8Oq5myvifbG+c1QxCnQWzlyXyHmKuRdRgE6rttiqOdw9J4DtwBlmFrC40V7FwCA==“
}
```

### Example response to list the remaining manual assignment queues
<a name="API_ListRoutingProfileManualAssignmentQueues_Example_4"></a>

Excludes the manual assignment queues retrieved by previous request.

```
{
    "LastModifiedRegion": "us-west-2",
    "LastModifiedTime": 1.75735455979E9,
    "NextToken": null,
    "RoutingProfileManualAssignmentQueueConfigSummaryList": [
        {
            "Channel": "TASK",
            "QueueArn": "arn:aws:connect:us-west-2:123456789012:instance/12345678-1234-5678-aabb-123456abcdef/queue/12345678-1234-5678-aabb-123456abcdef",
            "QueueId": "12345678-1234-5678-aabb-123456abcdef",
            "QueueName": "Q_NAME_2"
        }
    ]
}
```

## See Also
<a name="API_ListRoutingProfileManualAssignmentQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListRoutingProfileManualAssignmentQueues)
