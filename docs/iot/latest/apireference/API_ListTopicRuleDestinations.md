---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRuleDestinations.html
---

# ListTopicRuleDestinations
<a name="API_ListTopicRuleDestinations"></a>

Lists all the topic rule destinations in your AWS account.

Requires permission to access the [ListTopicRuleDestinations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListTopicRuleDestinations_RequestSyntax"></a>

```
GET /destinations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTopicRuleDestinations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTopicRuleDestinations_RequestSyntax) **   <a name="iot-ListTopicRuleDestinations-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListTopicRuleDestinations_RequestSyntax) **   <a name="iot-ListTopicRuleDestinations-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

## Request Body
<a name="API_ListTopicRuleDestinations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTopicRuleDestinations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destinationSummaries": [
      {
         "arn": "string",
         "createdAt": number,
         "httpUrlSummary": {
            "confirmationUrl": "string"
         },
         "lastUpdatedAt": number,
         "status": "string",
         "statusReason": "string",
         "vpcDestinationSummary": {
            "roleArn": "string",
            "securityGroups": [ "string" ],
            "subnetIds": [ "string" ],
            "vpcId": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListTopicRuleDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinationSummaries](#API_ListTopicRuleDestinations_ResponseSyntax) **   <a name="iot-ListTopicRuleDestinations-response-destinationSummaries"></a>
Information about a topic rule destination.
Type: Array of [TopicRuleDestinationSummary](API_TopicRuleDestinationSummary.md) objects

 ** [nextToken](#API_ListTopicRuleDestinations_ResponseSyntax) **   <a name="iot-ListTopicRuleDestinations-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListTopicRuleDestinations_Errors"></a>

 ** InternalException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_ListTopicRuleDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListTopicRuleDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListTopicRuleDestinations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
