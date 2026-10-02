---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateRule.html
---

# UpdateRule
<a name="API_UpdateRule"></a>

Updates a rule for the specified Connect Customer instance.

Use the [Rules Function language](https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html) to code conditions for the rule.

## Request Syntax
<a name="API_UpdateRule_RequestSyntax"></a>

```
PUT /rules/{{InstanceId}}/{{RuleId}} HTTP/1.1
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
         "SendInAppNotificationAction": {
            "Content": {
               "{{string}}" : "{{string}}"
            },
            "Exclusion": {
               "UserIds": [ "{{string}}" ],
               "UserTags": {
                  "{{string}}" : "{{string}}"
               }
            },
            "Priority": "{{string}}",
            "Recipient": {
               "UserIds": [ "{{string}}" ],
               "UserTags": {
                  "{{string}}" : "{{string}}"
               }
            }
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
   "Function": "{{string}}",
   "Name": "{{string}}",
   "PreEvaluationFilters": {
      "AndConditions": [
         {
            "FilterKey": "{{string}}",
            "FilterType": "{{string}}",
            "FilterValue": "{{string}}",
            "Operator": "{{string}}",
            "ResourceType": "{{string}}"
         }
      ]
   },
   "PublishStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [RuleId](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-uri-RuleId"></a>
A unique identifier for the rule.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-Actions"></a>
A list of actions to be run when the rule is triggered.
Type: Array of [RuleAction](API_RuleAction.md) objects
Required: Yes

 ** [Function](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-Function"></a>
The conditions of the rule.
Type: String
Required: Yes

 ** [Name](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-Name"></a>
The name of the rule. You can change the name only if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` \| `OnZendeskTicketStatusUpdate` \| `OnSalesforceCaseCreate`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^[0-9a-zA-Z._-]+`
Required: Yes

 ** [PreEvaluationFilters](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-PreEvaluationFilters"></a>
The pre-evaluation filters for the rule, that restrict the rule to be applied to only certain resources based on the resource's attributes, such as tags assigned to a contact. The pre-evaluation filters are applied even before rule conditions are evaluated and are used to enforce tag-based-access-control while applying rules.
Type: [PreEvaluationFilters](API_PreEvaluationFilters.md) object
Required: No

 ** [PublishStatus](#API_UpdateRule_RequestSyntax) **   <a name="connect-UpdateRule-request-PublishStatus"></a>
The publish status of the rule.
Type: String
Valid Values: `DRAFT | PUBLISHED`
Required: Yes

## Response Syntax
<a name="API_UpdateRule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateRule_Errors"></a>

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateRule)
