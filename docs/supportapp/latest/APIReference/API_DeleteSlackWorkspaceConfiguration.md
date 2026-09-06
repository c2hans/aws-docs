---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteSlackWorkspaceConfiguration.html
---

# DeleteSlackWorkspaceConfiguration
<a name="API_DeleteSlackWorkspaceConfiguration"></a>

Deletes a Slack workspace configuration from your AWS account. This operation doesn't delete your Slack workspace.

## Request Syntax
<a name="API_DeleteSlackWorkspaceConfiguration_RequestSyntax"></a>

```
POST /control/delete-slack-workspace-configuration HTTP/1.1
Content-type: application/json

{
   "teamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteSlackWorkspaceConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteSlackWorkspaceConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [teamId](#API_DeleteSlackWorkspaceConfiguration_RequestSyntax) **   <a name="supportapp-DeleteSlackWorkspaceConfiguration-request-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_DeleteSlackWorkspaceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteSlackWorkspaceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSlackWorkspaceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Your request has a conflict. For example, you might receive this error if you try the following:
+ Add, update, or delete a Slack channel configuration before you add a Slack workspace to your AWS account.
+ Add a Slack channel configuration that already exists in your AWS account.
+ Delete a Slack channel configuration for a live chat channel.
+ Delete a Slack workspace from your AWS account that has an active live chat channel.
+ Call the `RegisterSlackWorkspaceForOrganization` API from an AWS account that doesn't belong to an organization.
+ Call the `RegisterSlackWorkspaceForOrganization` API from a member account, but the management account hasn't registered that workspace yet for the organization.
HTTP Status Code: 409

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource is missing or doesn't exist, such as an account alias, Slack channel configuration, or Slack workspace configuration.
HTTP Status Code: 404

 ** ValidationException **
Your request input doesn't meet the constraints that the Support App specifies.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSlackWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/DeleteSlackWorkspaceConfiguration)
