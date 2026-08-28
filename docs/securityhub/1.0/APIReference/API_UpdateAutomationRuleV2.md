---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateAutomationRuleV2.html
---

# UpdateAutomationRuleV2
<a name="API_UpdateAutomationRuleV2"></a>

Updates a V2 automation rule.

## Request Syntax
<a name="API_UpdateAutomationRuleV2_RequestSyntax"></a>

```
PATCH /automationrulesv2/{{Identifier}} HTTP/1.1
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
   "Criteria": { ... },
   "Description": "{{string}}",
   "RuleName": "{{string}}",
   "RuleOrder": {{number}},
   "RuleStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAutomationRuleV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-uri-Identifier"></a>
The ARN of the automation rule.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateAutomationRuleV2_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Actions](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-Actions"></a>
A list of actions to be performed when the rule criteria is met.
Type: Array of [AutomationRulesActionV2](API_AutomationRulesActionV2.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [Criteria](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-Criteria"></a>
The filtering type and configuration of the automation rule.
Type: [Criteria](API_Criteria.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Description](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-Description"></a>
A description of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [RuleName](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-RuleName"></a>
The name of the automation rule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** [RuleOrder](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-RuleOrder"></a>
Represents a value for the rule priority.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 1000.0.
Required: No

 ** [RuleStatus](#API_UpdateAutomationRuleV2_RequestSyntax) **   <a name="securityhub-UpdateAutomationRuleV2-request-RuleStatus"></a>
The status of the automation rule.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## Response Syntax
<a name="API_UpdateAutomationRuleV2_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAutomationRuleV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAutomationRuleV2_Errors"></a>

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAutomationRuleV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateAutomationRuleV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateAutomationRuleV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
