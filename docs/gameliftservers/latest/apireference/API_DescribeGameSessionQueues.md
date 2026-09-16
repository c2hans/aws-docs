---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionQueues.html
---

# DescribeGameSessionQueues
<a name="API_DescribeGameSessionQueues"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. When specifying a list of queues, objects are returned only for queues that currently exist in the Region.

 **Learn more**

 [ View Your Queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-console.html)

## Request Syntax
<a name="API_DescribeGameSessionQueues_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGameSessionQueues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_DescribeGameSessionQueues_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionQueues-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages. You can request up to 50 results.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Names](#API_DescribeGameSessionQueues_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionQueues-request-Names"></a>
A list of queue names to retrieve information for. You can use either the queue ID or ARN value. To request settings for all queues, leave this parameter empty.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+|^arn:.*:gamesessionqueue\/[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_DescribeGameSessionQueues_RequestSyntax) **   <a name="gameliftservers-DescribeGameSessionQueues-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeGameSessionQueues_ResponseSyntax"></a>

```
{
   "GameSessionQueues": [
      {
         "CustomEventData": "string",
         "Destinations": [
            {
               "DestinationArn": "string"
            }
         ],
         "FilterConfiguration": {
            "AllowedLocations": [ "string" ]
         },
         "GameSessionQueueArn": "string",
         "Name": "string",
         "NotificationTarget": "string",
         "PlayerLatencyPolicies": [
            {
               "MaximumIndividualPlayerLatencyMilliseconds": number,
               "PolicyDurationSeconds": number
            }
         ],
         "PriorityConfiguration": {
            "LocationOrder": [ "string" ],
            "PriorityOrder": [ "string" ]
         },
         "TimeoutInSeconds": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeGameSessionQueues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionQueues](#API_DescribeGameSessionQueues_ResponseSyntax) **   <a name="gameliftservers-DescribeGameSessionQueues-response-GameSessionQueues"></a>
A collection of objects that describe the requested game session queues.
Type: Array of [GameSessionQueue](API_GameSessionQueue.md) objects

 ** [NextToken](#API_DescribeGameSessionQueues_ResponseSyntax) **   <a name="gameliftservers-DescribeGameSessionQueues-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeGameSessionQueues_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_DescribeGameSessionQueues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeGameSessionQueues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeGameSessionQueues)
