---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateAutomationRuleV2.html
---

# CreateAutomationRuleV2
<a name="API_CreateAutomationRuleV2"></a>

Creates a V2 automation rule.

## Request Syntax
<a name="API_CreateAutomationRuleV2_RequestSyntax"></a>

```
POST /automationrulesv2/create HTTP/1.1
Content-type: application/json

{
   "Actions": [
      {
         "ExternalIntegrationConfiguration": {
            "ConnectorArn": "{{string}}"
         },
         "FindingFieldsUpdate": {
            "Comment": "{{string}}",
            "SeverityId": {{number}},
            "StatusId": {{number}}
         },
         "Type": "{{string}}"
      }
   ],
   "ClientToken": "{{string}}",
   "Criteria": { ... },
   "Description": "{{string}}",
   "RuleName": "{{string}}",
   "RuleOrder": {{number}},
   "RuleStatus": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAutomationRuleV2_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAutomationRuleV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-Actions"></a>
A list of actions to be performed when the rule criteria is met.
Type: Array of [AutomationRulesActionV2](API_AutomationRulesActionV2.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [ClientToken](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-ClientToken"></a>
A unique identifier used to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[\x21-\x7E]{1,64}$`
Required: No

 ** [Criteria](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-Criteria"></a>
The filtering type and configuration of the automation rule.
Type: [Criteria](API_Criteria.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-Description"></a>
A description of the V2 automation rule.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [RuleName](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-RuleName"></a>
The name of the V2 automation rule.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [RuleOrder](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-RuleOrder"></a>
The value for the rule priority.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 1000.0.
Required: Yes

 ** [RuleStatus](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-RuleStatus"></a>
The status of the V2 automation rule.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [Tags](#API_CreateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-CreateAutomationRuleV2-request-Tags"></a>
A list of key-value pairs associated with the V2 automation rule.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAutomationRuleV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RuleArn": "string",
   "RuleId": "string"
}
```

## Response Elements
<a name="API_CreateAutomationRuleV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleArn](#API_CreateAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-CreateAutomationRuleV2-response-RuleArn"></a>
The ARN of the V2 automation rule.
Type: String
Pattern: `.*\S.*`

 ** [RuleId](#API_CreateAutomationRuleV2_ResponseSyntax) **   <a name="securityhub-CreateAutomationRuleV2-response-RuleId"></a>
The ID of the V2 automation rule.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_CreateAutomationRuleV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed the service quota limit.
HTTP Status Code: 402

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_CreateAutomationRuleV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateAutomationRuleV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateAutomationRuleV2)
