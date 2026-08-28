---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html
---

# BatchUpdateAutomationRules
<a name="API_BatchUpdateAutomationRules"></a>

 Updates one or more automation rules based on rule Amazon Resource Names (ARNs) and input parameters.

## Request Syntax
<a name="API_BatchUpdateAutomationRules_RequestSyntax"></a>

```
PATCH /automationrules/update HTTP/1.1
Content-type: application/json

{
   "UpdateAutomationRulesRequestItems": [
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
         "RuleArn": "{{string}}",
         "RuleName": "{{string}}",
         "RuleOrder": {{number}},
         "RuleStatus": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchUpdateAutomationRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchUpdateAutomationRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UpdateAutomationRulesRequestItems](#API_BatchUpdateAutomationRules_RequestSyntax) **   <a name="securityhub-BatchUpdateAutomationRules-request-UpdateAutomationRulesRequestItems"></a>
 An array of ARNs for the rules that are to be updated. Optionally, you can also include `RuleStatus` and `RuleOrder`.
Type: Array of [UpdateAutomationRulesRequestItem](API_UpdateAutomationRulesRequestItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateAutomationRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProcessedAutomationRules": [ "string" ],
   "UnprocessedAutomationRules": [
      {
         "ErrorCode": number,
         "ErrorMessage": "string",
         "RuleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateAutomationRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessedAutomationRules](#API_BatchUpdateAutomationRules_ResponseSyntax) **   <a name="securityhub-BatchUpdateAutomationRules-response-ProcessedAutomationRules"></a>
 A list of properly processed rule ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`

 ** [UnprocessedAutomationRules](#API_BatchUpdateAutomationRules_ResponseSyntax) **   <a name="securityhub-BatchUpdateAutomationRules-response-UnprocessedAutomationRules"></a>
 A list of objects containing `RuleArn`, `ErrorCode`, and `ErrorMessage`. This parameter tells you which automation rules the request didn't update and why.
Type: Array of [UnprocessedAutomationRule](API_UnprocessedAutomationRule.md) objects

## Errors
<a name="API_BatchUpdateAutomationRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_BatchUpdateAutomationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchUpdateAutomationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateAutomationRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
