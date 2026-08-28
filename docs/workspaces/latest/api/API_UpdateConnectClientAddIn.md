---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateConnectClientAddIn.html
---

# UpdateConnectClientAddIn
<a name="API_UpdateConnectClientAddIn"></a>

Updates a Connect Customer client add-in. Use this action to update the name and endpoint URL of a Connect Customer client add-in.

## Request Syntax
<a name="API_UpdateConnectClientAddIn_RequestSyntax"></a>

```
{
   "AddInId": "{{string}}",
   "Name": "{{string}}",
   "ResourceId": "{{string}}",
   "URL": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateConnectClientAddIn_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AddInId](#API_UpdateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectClientAddIn-request-AddInId"></a>
The identifier of the client add-in to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [Name](#API_UpdateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectClientAddIn-request-Name"></a>
The name of the client add-in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.*$`
Required: No

 ** [ResourceId](#API_UpdateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectClientAddIn-request-ResourceId"></a>
The directory identifier for which the client add-in is configured.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [URL](#API_UpdateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-UpdateConnectClientAddIn-request-URL"></a>
The endpoint URL of the Connect Customer client add-in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(http|https)\://\S+`
Required: No

## Response Elements
<a name="API_UpdateConnectClientAddIn_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConnectClientAddIn_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnectClientAddIn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/UpdateConnectClientAddIn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/UpdateConnectClientAddIn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
