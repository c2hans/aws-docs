---
source_url: https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_DeleteRule.html
---

# DeleteRule
<a name="API_DeleteRule"></a>

Deletes a Recycle Bin retention rule. For more information, see [ Delete Recycle Bin retention rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-working-with-rules.html#recycle-bin-delete-rule) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Syntax
<a name="API_DeleteRule_RequestSyntax"></a>

```
DELETE /rules/{{identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [identifier](#API_DeleteRule_RequestSyntax) **   <a name="recyclebin-DeleteRule-request-uri-Identifier"></a>
The unique ID of the retention rule.
Pattern: `[0-9a-zA-Z]{11}`
Required: Yes

## Request Body
<a name="API_DeleteRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRule_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The specified retention rule lock request can't be completed.
 ** Reason **
The reason for the exception.
HTTP Status Code: 409

 ** InternalServerException **
The service could not respond to the request due to an internal problem.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Reason **
The reason for the exception.
HTTP Status Code: 404

 ** ValidationException **
One or more of the parameters in the request is not valid.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rbin-2021-06-15/DeleteRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rbin-2021-06-15/DeleteRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Recycle Bin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recyclebin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
