---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateAutomationRule.html
---

# CreateAutomationRule
<a name="API_CreateAutomationRule"></a>

 Creates an automation rule based on input parameters.

## Request Syntax
<a name="API_CreateAutomationRule_RequestSyntax"></a>

```
POST /automationrules/create HTTP/1.1
Content-type: application/json

{
   "Actions": [
      {
         "FindingFieldsUpdate": {
            "Confidence": {{number}},
            "Criticality": {{number}},
            "Note": {
               "Text": "{{string}}",
               "UpdatedBy": "{{string}}"
            },
            "RelatedFindings": [
               {
                  "Id": "{{string}}",
                  "ProductArn": "{{string}}"
               }
            ],
            "Severity": {
               "Label": "{{string}}",
               "Normalized": {{number}},
               "Product": {{number}}
            },
            "Types": [ "{{string}}" ],
            "UserDefinedFields": {
               "{{string}}" : "{{string}}"
            },
            "VerificationState": "{{string}}",
            "Workflow": {
               "Status": "{{string}}"
            }
         },
         "Type": "{{string}}"
      }
   ],
   "Criteria": {
      "AwsAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "AwsAccountName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "CompanyName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceAssociatedStandardsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceSecurityControlId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ComplianceStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Confidence": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "CreatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "Criticality": [
         {
            "Eq": {{number}},
            "Gt": {{number}},
            "Gte": {{number}},
            "Lt": {{number}},
            "Lte": {{number}}
         }
      ],
      "Description": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "FirstObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "GeneratorId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Id": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "LastObservedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "NoteText": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "NoteUpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "NoteUpdatedBy": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ProductName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RecordState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "RelatedFindingsProductArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationArn": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceApplicationName": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceDetailsOther": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerAccountId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceOwnerOrgId": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourcePartition": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceProvider": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceRegion": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceTags": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceType": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SeverityLabel": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SourceUrl": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Title": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Type": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "UpdatedAt": [
         {
            "DateRange": {
               "Comparison": "{{string}}",
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "End": "{{string}}",
            "Start": "{{string}}"
         }
      ],
      "UserDefinedFields": [
         {
            "Comparison": "{{string}}",
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "VerificationState": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "WorkflowStatus": [
         {
            "Comparison": "{{string}}",
            "Value": "{{string}}"
         }
      ]
   },
   "Description": "{{string}}",
   "IsTerminal": {{boolean}},
   "RuleName": "{{string}}",
   "RuleOrder": {{number}},
   "RuleStatus": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAutomationRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAutomationRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-Actions"></a>
 One or more actions to update finding fields if a finding matches the conditions specified in `Criteria`.
Type: Array of [AutomationRulesAction](API_AutomationRulesAction.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [Criteria](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-Criteria"></a>
 A set of ASFF finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding.
Type: [AutomationRulesFindingFilters](API_AutomationRulesFindingFilters.md) object
Required: Yes

 ** [Description](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-Description"></a>
 A description of the rule.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [IsTerminal](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-IsTerminal"></a>
Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
Type: Boolean
Required: No

 ** [RuleName](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-RuleName"></a>
 The name of the rule.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [RuleOrder](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-RuleOrder"></a>
An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** [RuleStatus](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-RuleStatus"></a>
 Whether the rule is active after it is created. If this parameter is equal to `ENABLED`, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use [`BatchUpdateAutomationRules`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Tags](#API_CreateAutomationRule_RequestSyntax) **   <a name="securityhub-CreateAutomationRule-request-Tags"></a>
 User-defined tags associated with an automation rule.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAutomationRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "string"
}
```

## Response Elements
<a name="API_CreateAutomationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleArn](#API_CreateAutomationRule_ResponseSyntax) **   <a name="securityhub-CreateAutomationRule-response-RuleArn"></a>
 The Amazon Resource Name (ARN) of the automation rule that you created.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_CreateAutomationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateAutomationRule)
