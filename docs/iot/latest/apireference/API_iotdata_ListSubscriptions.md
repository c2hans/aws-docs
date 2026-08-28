---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListSubscriptions.html
---

# ListSubscriptions
<a name="API_iotdata_ListSubscriptions"></a>

Returns a list of all subscriptions for MQTT clients with active sessions, including offline clients with persistent sessions.

Requires permission to access the [ListSubscriptions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdata_ListSubscriptions_RequestSyntax"></a>

```
GET /connections/{{clientId}}/subscriptions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_ListSubscriptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientId](#API_iotdata_ListSubscriptions_RequestSyntax) **   <a name="iot-iotdata_ListSubscriptions-request-uri-clientId"></a>
The unique identifier of the MQTT client to list subscriptions for. The client ID can't start with a dollar sign ($).
MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[^$].*`
Required: Yes

 ** [maxResults](#API_iotdata_ListSubscriptions_RequestSyntax) **   <a name="iot-iotdata_ListSubscriptions-request-uri-maxResults"></a>
The maximum number of subscriptions to return in a single request. By default, this is set to 20.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_iotdata_ListSubscriptions_RequestSyntax) **   <a name="iot-iotdata_ListSubscriptions-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

## Request Body
<a name="API_iotdata_ListSubscriptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_ListSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "subscriptions": [
      {
         "qos": number,
         "topicFilter": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iotdata_ListSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_iotdata_ListSubscriptions_ResponseSyntax) **   <a name="iot-iotdata_ListSubscriptions-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

 ** [subscriptions](#API_iotdata_ListSubscriptions_ResponseSyntax) **   <a name="iot-iotdata_ListSubscriptions-response-subscriptions"></a>
A list of topic filters and their associated Quality of Service (QoS) levels that the client is subscribed to.
Type: Array of [SubscriptionSummary](API_iotdata_SubscriptionSummary.md) objects

## Errors
<a name="API_iotdata_ListSubscriptions_Errors"></a>

 ** ForbiddenException **
The caller isn't authorized to make the request.
HTTP Status Code: 403

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 429

## See Also
<a name="API_iotdata_ListSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/ListSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/ListSubscriptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
