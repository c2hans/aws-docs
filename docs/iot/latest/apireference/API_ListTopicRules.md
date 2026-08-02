---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListTopicRules.html
---

# ListTopicRules
<a name="API_ListTopicRules"></a>

Lists the rules for the specific topic.

Requires permission to access the [ListTopicRules](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListTopicRules_RequestSyntax"></a>

```
GET /rules?maxResults={{maxResults}}&nextToken={{nextToken}}&ruleDisabled={{ruleDisabled}}&topic={{topic}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTopicRules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListTopicRules_RequestSyntax) **   <a name="iot-ListTopicRules-request-uri-maxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [nextToken](#API_ListTopicRules_RequestSyntax) **   <a name="iot-ListTopicRules-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [ruleDisabled](#API_ListTopicRules_RequestSyntax) **   <a name="iot-ListTopicRules-request-uri-ruleDisabled"></a>
Specifies whether the rule is disabled.

 ** [topic](#API_ListTopicRules_RequestSyntax) **   <a name="iot-ListTopicRules-request-uri-topic"></a>
The topic.

## Request Body
<a name="API_ListTopicRules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTopicRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "rules": [
      {
         "createdAt": number,
         "ruleArn": "string",
         "ruleDisabled": boolean,
         "ruleName": "string",
         "topicPattern": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTopicRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTopicRules_ResponseSyntax) **   <a name="iot-ListTopicRules-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

 ** [rules](#API_ListTopicRules_ResponseSyntax) **   <a name="iot-ListTopicRules-response-rules"></a>
The rules.
Type: Array of [TopicRuleListItem](API_TopicRuleListItem.md) objects

## Errors
<a name="API_ListTopicRules_Errors"></a>

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
<a name="API_ListTopicRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListTopicRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListTopicRules)
