---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CreateConnectClientAddIn.html
---

# CreateConnectClientAddIn
<a name="API_CreateConnectClientAddIn"></a>

Creates a client-add-in for Connect Customer within a directory. You can create only one Connect Customer client add-in within a directory.

This client add-in allows WorkSpaces users to seamlessly connect to Connect Customer.

## Request Syntax
<a name="API_CreateConnectClientAddIn_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "ResourceId": "{{string}}",
   "URL": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateConnectClientAddIn_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-CreateConnectClientAddIn-request-Name"></a>
The name of the client add-in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^.*$`
Required: Yes

 ** [ResourceId](#API_CreateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-CreateConnectClientAddIn-request-ResourceId"></a>
The directory identifier for which to configure the client add-in.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: Yes

 ** [URL](#API_CreateConnectClientAddIn_RequestSyntax) **   <a name="WorkSpaces-CreateConnectClientAddIn-request-URL"></a>
The endpoint URL of the Connect Customer client add-in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(http|https)\://\S+`
Required: Yes

## Response Syntax
<a name="API_CreateConnectClientAddIn_ResponseSyntax"></a>

```
{
   "AddInId": "string"
}
```

## Response Elements
<a name="API_CreateConnectClientAddIn_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddInId](#API_CreateConnectClientAddIn_ResponseSyntax) **   <a name="WorkSpaces-CreateConnectClientAddIn-response-AddInId"></a>
The client add-in identifier.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateConnectClientAddIn_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceCreationFailedException **
The resource could not be created.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_CreateConnectClientAddIn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/CreateConnectClientAddIn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CreateConnectClientAddIn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
