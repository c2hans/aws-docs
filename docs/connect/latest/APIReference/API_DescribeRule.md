---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRule.html
---

# DescribeRule
<a name="API_DescribeRule"></a>

Describes a rule for the specified Connect Customer instance.

## Request Syntax
<a name="API_DescribeRule_RequestSyntax"></a>

```
GET /rules/{{InstanceId}}/{{RuleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeRule_RequestSyntax) **   <a name="connect-DescribeRule-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [RuleId](#API_DescribeRule_RequestSyntax) **   <a name="connect-DescribeRule-request-uri-RuleId"></a>
A unique identifier for the rule.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_DescribeRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Rule": {
      "Actions": [
         {
            "ActionType": "string",
            "AssignContactCategoryAction": {
            },
            "AssignSlaAction": {
               "CaseSlaConfiguration": {
                  "FieldId": "string",
                  "Name": "string",
                  "TargetFieldValues": [
                     {
                        "BooleanValue": boolean,
                        "DoubleValue": number,
                        "EmptyValue": {
                        },
                        "StringValue": "string"
                     }
                  ],
                  "TargetSlaMinutes": number,
                  "Type": "string"
               },
               "SlaAssignmentType": "string"
            },
            "CreateCaseAction": {
               "Fields": [
                  {
                     "Id": "string",
                     "Value": {
                        "BooleanValue": boolean,
                        "DoubleValue": number,
                        "EmptyValue": {
                        },
                        "StringValue": "string"
                     }
                  }
               ],
               "TemplateId": "string"
            },
            "EndAssociatedTasksAction": {
            },
            "EventBridgeAction": {
               "Name": "string"
            },
            "ExtractInformationAction": {
               "RulesExtractionDefinitions": [
                  {
                     "Identifier": "string"
                  }
               ]
            },
            "SendInAppNotificationAction": {
               "Content": {
                  "string" : "string"
               },
               "Exclusion": {
                  "UserIds": [ "string" ],
                  "UserTags": {
                     "string" : "string"
                  }
               },
               "Priority": "string",
               "Recipient": {
                  "UserIds": [ "string" ],
                  "UserTags": {
                     "string" : "string"
                  }
               }
            },
            "SendNotificationAction": {
               "Content": "string",
               "ContentType": "string",
               "DeliveryMethod": "string",
               "Exclusion": {
                  "UserIds": [ "string" ],
                  "UserTags": {
                     "string" : "string"
                  }
               },
               "Recipient": {
                  "UserIds": [ "string" ],
                  "UserTags": {
                     "string" : "string"
                  }
               },
               "Subject": "string"
            },
            "SubmitAutoEvaluationAction": {
               "EvaluationFormId": "string"
            },
            "TaskAction": {
               "ContactFlowId": "string",
               "Description": "string",
               "Name": "string",
               "References": {
                  "string" : {
                     "Arn": "string",
                     "Status": "string",
                     "StatusReason": "string",
                     "Type": "string",
                     "Value": "string"
                  }
               }
            },
            "UpdateCaseAction": {
               "Fields": [
                  {
                     "Id": "string",
                     "Value": {
                        "BooleanValue": boolean,
                        "DoubleValue": number,
                        "EmptyValue": {
                        },
                        "StringValue": "string"
                     }
                  }
               ]
            }
         }
      ],
      "CreatedTime": number,
      "Function": "string",
      "LastUpdatedBy": "string",
      "LastUpdatedTime": number,
      "Name": "string",
      "PreEvaluationFilters": {
         "AndConditions": [
            {
               "FilterKey": "string",
               "FilterType": "string",
               "FilterValue": "string",
               "Operator": "string",
               "ResourceType": "string"
            }
         ]
      },
      "PublishStatus": "string",
      "RuleArn": "string",
      "RuleCapabilityTiers": [ "string" ],
      "RuleId": "string",
      "Tags": {
         "string" : "string"
      },
      "TriggerEventSource": {
         "EventSourceName": "string",
         "IntegrationAssociationId": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Rule](#API_DescribeRule_ResponseSyntax) **   <a name="connect-DescribeRule-response-Rule"></a>
Information about the rule.
Type: [Rule](API_Rule.md) object

## Errors
<a name="API_DescribeRule_Errors"></a>

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
<a name="API_DescribeRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeRule)
