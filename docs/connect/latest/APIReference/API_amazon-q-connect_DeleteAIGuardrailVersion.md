---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_DeleteAIGuardrailVersion.html
---

# DeleteAIGuardrailVersion
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion"></a>

Delete and Amazon Q in Connect AI Guardrail version.

## Request Syntax
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_RequestSyntax"></a>

```
DELETE /assistants/{{assistantId}}/aiguardrails/{{aiGuardrailId}}/versions/{{versionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aiGuardrailId](#API_amazon-q-connect_DeleteAIGuardrailVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_DeleteAIGuardrailVersion-request-uri-aiGuardrailId"></a>
The identifier of the Amazon Q in Connect AI Guardrail.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** [assistantId](#API_amazon-q-connect_DeleteAIGuardrailVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_DeleteAIGuardrailVersion-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [versionNumber](#API_amazon-q-connect_DeleteAIGuardrailVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_DeleteAIGuardrailVersion-request-uri-versionNumber"></a>
The version number of the AI Guardrail version to be deleted.
Valid Range: Minimum value of 1.
Required: Yes

## Request Body
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_ResponseSyntax"></a>

```
HTTP/1.1 202
```

## Response Elements
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response with an empty HTTP body.

## Errors
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_DeleteAIGuardrailVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/DeleteAIGuardrailVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/DeleteAIGuardrailVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
