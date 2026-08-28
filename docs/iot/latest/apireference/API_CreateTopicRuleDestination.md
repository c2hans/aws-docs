---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRuleDestination.html
---

# CreateTopicRuleDestination
<a name="API_CreateTopicRuleDestination"></a>

Creates a topic rule destination. The destination must be confirmed prior to use.

Requires permission to access the [CreateTopicRuleDestination](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateTopicRuleDestination_RequestSyntax"></a>

```
POST /destinations HTTP/1.1
Content-type: application/json

{
   "destinationConfiguration": {
      "httpUrlConfiguration": {
         "confirmationUrl": "{{string}}"
      },
      "vpcConfiguration": {
         "roleArn": "{{string}}",
         "securityGroups": [ "{{string}}" ],
         "subnetIds": [ "{{string}}" ],
         "vpcId": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_CreateTopicRuleDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTopicRuleDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationConfiguration](#API_CreateTopicRuleDestination_RequestSyntax) **   <a name="iot-CreateTopicRuleDestination-request-destinationConfiguration"></a>
The topic rule destination configuration.
Type: [TopicRuleDestinationConfiguration](API_TopicRuleDestinationConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_CreateTopicRuleDestination_ResponseSyntax"></a>

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
<a name="API_CreateTopicRuleDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [topicRuleDestination](#API_CreateTopicRuleDestination_ResponseSyntax) **   <a name="iot-CreateTopicRuleDestination-response-topicRuleDestination"></a>
The topic rule destination.
Type: [TopicRuleDestination](API_TopicRuleDestination.md) object

## Errors
<a name="API_CreateTopicRuleDestination_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_CreateTopicRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateTopicRuleDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateTopicRuleDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
