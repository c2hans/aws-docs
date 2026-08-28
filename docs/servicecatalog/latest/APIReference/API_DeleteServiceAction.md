---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeleteServiceAction.html
---

# DeleteServiceAction
<a name="API_DeleteServiceAction"></a>

Deletes a self-service action.

## Request Syntax
<a name="API_DeleteServiceAction_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}",
   "IdempotencyToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteServiceAction_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DeleteServiceAction_RequestSyntax) **   <a name="servicecatalog-DeleteServiceAction-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DeleteServiceAction_RequestSyntax) **   <a name="servicecatalog-DeleteServiceAction-request-Id"></a>
The self-service action identifier. For example, `act-fs7abcd89wxyz`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [IdempotencyToken](#API_DeleteServiceAction_RequestSyntax) **   <a name="servicecatalog-DeleteServiceAction-request-IdempotencyToken"></a>
A unique identifier that you provide to ensure idempotency. If multiple requests from the same AWS account use the same idempotency token, the same response is returned for each repeated request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

## Response Elements
<a name="API_DeleteServiceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteServiceAction_Errors"></a>

 ** ResourceInUseException **
A resource that is currently in use. Ensure that the resource is not in use and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteServiceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DeleteServiceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteServiceAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
