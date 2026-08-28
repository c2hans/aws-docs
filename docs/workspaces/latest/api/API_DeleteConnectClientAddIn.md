---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteConnectClientAddIn.html
---

# DeleteConnectClientAddIn
<a name="API_DeleteConnectClientAddIn"></a>

Deletes a client-add-in for Connect Customer that is configured within a directory.

## Request Syntax
<a name="API_DeleteConnectClientAddIn_RequestSyntax"></a>

```
{
   "AddInId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConnectClientAddIn_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AddInId](#API_DeleteConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-DeleteConnectClientAddIn-request-AddInId"></a>
The identifier of the client add-in to delete.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [ResourceId](#API_DeleteConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-DeleteConnectClientAddIn-request-ResourceId"></a>
The directory identifier for which the client add-in is configured.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

## Response Elements
<a name="API_DeleteConnectClientAddIn_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConnectClientAddIn_Errors"></a>

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
<a name="API_DeleteConnectClientAddIn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DeleteConnectClientAddIn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DeleteConnectClientAddIn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
