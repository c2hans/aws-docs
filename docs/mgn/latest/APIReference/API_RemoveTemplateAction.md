---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_RemoveTemplateAction.html
---

# RemoveTemplateAction
<a name="API_RemoveTemplateAction"></a>

Remove template post migration custom action.

## Request Syntax
<a name="API_RemoveTemplateAction_RequestSyntax"></a>

```
POST /RemoveTemplateAction HTTP/1.1
Content-type: application/json

{
   "actionID": "{{string}}",
   "launchConfigurationTemplateID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RemoveTemplateAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RemoveTemplateAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionID](#API_RemoveTemplateAction_RequestSyntax) **   <a name="mgn-RemoveTemplateAction-request-actionID"></a>
Template post migration custom action ID to remove.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`
Required: Yes

 ** [launchConfigurationTemplateID](#API_RemoveTemplateAction_RequestSyntax) **   <a name="mgn-RemoveTemplateAction-request-launchConfigurationTemplateID"></a>
Launch configuration template ID of the post migration custom action to remove.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_RemoveTemplateAction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_RemoveTemplateAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_RemoveTemplateAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_RemoveTemplateAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/RemoveTemplateAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/RemoveTemplateAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
