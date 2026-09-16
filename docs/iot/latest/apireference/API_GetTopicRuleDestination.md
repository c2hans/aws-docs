---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetTopicRuleDestination.html
---

# GetTopicRuleDestination
<a name="API_GetTopicRuleDestination"></a>

Gets information about a topic rule destination.

Requires permission to access the [GetTopicRuleDestination](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetTopicRuleDestination_RequestSyntax"></a>

```
GET /destinations/{{arn+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTopicRuleDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetTopicRuleDestination_RequestSyntax) **   <a name="iot-GetTopicRuleDestination-request-uri-arn"></a>
The ARN of the topic rule destination.
Required: Yes

## Request Body
<a name="API_GetTopicRuleDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTopicRuleDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "topicRuleDestination": {
      "arn": "string",
      "createdAt": number,
      "httpUrlProperties": {
         "confirmationUrl": "string"
      },
      "lastUpdatedAt": number,
      "status": "string",
      "statusReason": "string",
      "vpcProperties": {
         "roleArn": "string",
         "securityGroups": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetTopicRuleDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [topicRuleDestination](#API_GetTopicRuleDestination_ResponseSyntax) **   <a name="iot-GetTopicRuleDestination-response-topicRuleDestination"></a>
The topic rule destination.
Type: [TopicRuleDestination](API_TopicRuleDestination.md) object

## Errors
<a name="API_GetTopicRuleDestination_Errors"></a>

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
<a name="API_GetTopicRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetTopicRuleDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetTopicRuleDestination)
