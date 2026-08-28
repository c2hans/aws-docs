---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_DeleteLifecyclePolicy.html
---

# DeleteLifecyclePolicy
<a name="API_DeleteLifecyclePolicy"></a>

Deletes the specified lifecycle policy and halts the automated operations that the policy specified.

For more information about deleting a policy, see [Delete lifecycle policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-modify-delete.html#delete).

## Request Syntax
<a name="API_DeleteLifecyclePolicy_RequestSyntax"></a>

```
DELETE /policies/{{policyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteLifecyclePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyId](#API_DeleteLifecyclePolicy_RequestSyntax) **   <a name="dlm-DeleteLifecyclePolicy-request-uri-PolicyId"></a>
The identifier of the lifecycle policy.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteLifecyclePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteLifecyclePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteLifecyclePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteLifecyclePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service failed in an unexpected way.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because a limit was exceeded.
 ** ResourceType **
Value is the type of resource for which a limit was exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource was not found.
 ** ResourceIds **
Value is a list of resource IDs that were not found.
 ** ResourceType **
Value is the type of resource that was not found.
HTTP Status Code: 404

## See Also
<a name="API_DeleteLifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/DeleteLifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/DeleteLifecyclePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
