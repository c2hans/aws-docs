---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DeleteRuleset.html
---

# DeleteRuleset
<a name="API_DeleteRuleset"></a>

Deletes a ruleset.

## Request Syntax
<a name="API_DeleteRuleset_RequestSyntax"></a>

```
DELETE /rulesets/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRuleset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteRuleset_RequestSyntax) **   <a name="databrew-DeleteRuleset-request-uri-Name"></a>
The name of the ruleset to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_DeleteRuleset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRuleset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "string"
}
```

## Response Elements
<a name="API_DeleteRuleset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DeleteRuleset_ResponseSyntax) **   <a name="databrew-DeleteRuleset-response-Name"></a>
The name of the deleted ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_DeleteRuleset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRuleset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/DeleteRuleset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DeleteRuleset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
