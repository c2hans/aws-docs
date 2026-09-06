---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

Creates a rule for the specified Connect Customer instance.

Use the [Rules Function language](https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html) to code conditions for the rule.

## Request Syntax
<a name="API_CreateRule_RequestSyntax"></a>

```
POST /rules/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Actions": [
      {
         "ActionType": "{{string}}",
         "AssignContactCategoryAction": {
         },
         "AssignSlaAction": {
            "CaseSlaConfiguration": {
               "FieldId": "{{string}}",
               "Name": "{{string}}",
               "TargetFieldValues": [
                  {
                     "BooleanValue": {{boolean}},
                     "DoubleValue": {{number}},
                     "EmptyValue": {
                     },
                     "StringValue": "{{string}}"
                  }
               ],
               "TargetSlaMinutes": {{number}},
               "Type": "{{string}}"
            },
            "SlaAssignmentType": "{{string}}"
         },
         "CreateCaseAction": {
            "Fields": [
               {
                  "Id": "{{string}}",
                  "Value": {
                     "BooleanValue": {{boolean}},
                     "DoubleValue": {{number}},
                     "EmptyValue": {
                     },
                     "StringValue": "{{string}}"
                  }
               }
            ],
            "TemplateId": "{{string}}"
         },
         "EndAssociatedTasksAction": {
         },
         "EventBridgeAction": {
            "Name": "{{string}}"
         },
         "ExtractInformationAction": {
            "RulesExtractionDefinitions": [
               {
                  "Identifier": "{{string}}"
               }
            ]
         },
         "SendNotificationAction": {
            "Content": "{{string}}",
            "ContentType": "{{string}}",
            "DeliveryMethod": "{{string}}",
            "Exclusion": {
               "UserIds": [ "{{string}}" ],
               "UserTags": {
                  "{{string}}" : "{{string}}"
               }
            },
            "Recipient": {
               "UserIds": [ "{{string}}" ],
               "UserTags": {
                  "{{string}}" : "{{string}}"
               }
            },
            "Subject": "{{string}}"
         },
         "SubmitAutoEvaluationAction": {
            "EvaluationFormId": "{{string}}"
         },
         "TaskAction": {
            "ContactFlowId": "{{string}}",
            "Description": "{{string}}",
            "Name": "{{string}}",
            "References": {
               "{{string}}" : {
                  "Arn": "{{string}}",
                  "Status": "{{string}}",
                  "StatusReason": "{{string}}",
                  "Type": "{{string}}",
                  "Value": "{{string}}"
               }
            }
         },
         "UpdateCaseAction": {
            "Fields": [
               {
                  "Id": "{{string}}",
                  "Value": {
                     "BooleanValue": {{boolean}},
                     "DoubleValue": {{number}},
                     "EmptyValue": {
                     },
                     "StringValue": "{{string}}"
                  }
               }
            ]
         }
      }
   ],
   "ClientToken": "{{string}}",
   "Function": "{{string}}",
   "Name": "{{string}}",
   "PublishStatus": "{{string}}",
   "TriggerEventSource": {
      "EventSourceName": "{{string}}",
      "IntegrationAssociationId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-Actions"></a>
A list of actions to be run when the rule is triggered.
Type: Array of [RuleAction](API_RuleAction.md) objects
Required: Yes

 ** [ClientToken](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Function](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-Function"></a>
The conditions of the rule.
Type: String
Required: Yes

 ** [Name](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-Name"></a>
A unique name for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** [PublishStatus](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-PublishStatus"></a>
The publish status of the rule.
Type: String
Valid Values: `DRAFT | PUBLISHED`
Required: Yes

 ** [TriggerEventSource](#API_CreateRule_RequestSyntax) **   <a name="connect-CreateRule-request-TriggerEventSource"></a>
The event source to trigger the rule.
Type: [RuleTriggerEventSource](API_RuleTriggerEventSource.md) object
Required: Yes

## Response Syntax
<a name="API_CreateRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "string",
   "RuleId": "string"
}
```

## Response Elements
<a name="API_CreateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleArn](#API_CreateRule_ResponseSyntax) **   <a name="connect-CreateRule-response-RuleArn"></a>
The Amazon Resource Name (ARN) of the rule.
Type: String

 ** [RuleId](#API_CreateRule_ResponseSyntax) **   <a name="connect-CreateRule-response-RuleId"></a>
A unique identifier for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateRule_Errors"></a>

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

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateRule)
