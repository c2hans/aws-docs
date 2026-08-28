---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DeleteAutomationRuleV2.html
---

# DeleteAutomationRuleV2
<a name="API_DeleteAutomationRuleV2"></a>

Deletes a V2 automation rule.

## Request Syntax
<a name="API_DeleteAutomationRuleV2_RequestSyntax"></a>

```
DELETE /automationrulesv2/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAutomationRuleV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_DeleteAutomationRuleV2_RequestSyntax) **   <a name="securityhub-DeleteAutomationRuleV2-request-uri-Identifier"></a>
The ARN of the V2 automation rule.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_DeleteAutomationRuleV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAutomationRuleV2_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAutomationRuleV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAutomationRuleV2_Errors"></a>

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
<a name="API_DeleteAutomationRuleV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DeleteAutomationRuleV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DeleteAutomationRuleV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
