---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_TagResource.html
---

# TagResource
<a name="API_automation_TagResource"></a>

 Adds tags to the specified resource.

## Request Syntax
<a name="API_automation_TagResource_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "resourceArn": "{{string}}",
   "ruleRevision": {{number}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_automation_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_TagResource_RequestSyntax) **   <a name="computeoptimizer-automation_TagResource-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [resourceArn](#API_automation_TagResource_RequestSyntax) **   <a name="computeoptimizer-automation_TagResource-request-resourceArn"></a>
 The ARN of the resource to tag.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`
Required: Yes

 ** [ruleRevision](#API_automation_TagResource_RequestSyntax) **   <a name="computeoptimizer-automation_TagResource-request-ruleRevision"></a>
The revision number of the automation rule to tag. This ensures you're tagging the correct version of the rule.
Type: Long
Required: Yes

 ** [tags](#API_automation_TagResource_RequestSyntax) **   <a name="computeoptimizer-automation_TagResource-request-tags"></a>
 The tags to add to the resource.
Type: Array of [Tag](API_automation_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_automation_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_automation_TagResource_Errors"></a>

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
<a name="API_automation_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/TagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
