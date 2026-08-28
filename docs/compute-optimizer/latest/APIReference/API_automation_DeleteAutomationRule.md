---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DeleteAutomationRule.html
---

# DeleteAutomationRule
<a name="API_automation_DeleteAutomationRule"></a>

 Deletes an existing automation rule.

## Request Syntax
<a name="API_automation_DeleteAutomationRule_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "ruleArn": "{{string}}",
   "ruleRevision": {{number}}
}
```

## Request Parameters
<a name="API_automation_DeleteAutomationRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_DeleteAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteAutomationRule-request-clientToken"></a>
 A unique identifier to ensure idempotency of the request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [ruleArn](#API_automation_DeleteAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteAutomationRule-request-ruleArn"></a>
 The ARN of the rule to delete.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`
Required: Yes

 ** [ruleRevision](#API_automation_DeleteAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteAutomationRule-request-ruleRevision"></a>
 The revision number of the rule to delete.
Type: Long
Required: Yes

## Response Elements
<a name="API_automation_DeleteAutomationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_automation_DeleteAutomationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified resource was not found.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_DeleteAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/DeleteAutomationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
