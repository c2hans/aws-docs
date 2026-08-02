---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.html
---

# RegisterSlackWorkspaceForOrganization
<a name="API_RegisterSlackWorkspaceForOrganization"></a>

Registers a Slack workspace for your AWS account. To call this API, your account must be part of an organization in AWS Organizations.

If you're the *management account* and you want to register Slack workspaces for your organization, you must complete the following tasks:

1. Sign in to the [AWS Support Center](https://console.aws.amazon.com/support/app) and authorize the Slack workspaces where you want your organization to have access to. See [Authorize a Slack workspace](https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html) in the * AWS Support User Guide*.

1. Call the `RegisterSlackWorkspaceForOrganization` API to authorize each Slack workspace for the organization.

After the management account authorizes the Slack workspace, member accounts can call this API to authorize the same Slack workspace for their individual accounts. Member accounts don't need to authorize the Slack workspace manually through the [AWS Support Center](https://console.aws.amazon.com/support/app).

To use the Support App, each account must then complete the following tasks:
+ Create an AWS Identity and Access Management (IAM) role with the required permission. For more information, see [Managing access to the Support App](https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html).
+ Configure a Slack channel to use the Support App for support cases for that account. For more information, see [Configuring a Slack channel](https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html).

## Request Syntax
<a name="API_RegisterSlackWorkspaceForOrganization_RequestSyntax"></a>

```
POST /control/register-slack-workspace-for-organization HTTP/1.1
Content-type: application/json

{
   "teamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterSlackWorkspaceForOrganization_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterSlackWorkspaceForOrganization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [teamId](#API_RegisterSlackWorkspaceForOrganization_RequestSyntax) **   <a name="supportapp-RegisterSlackWorkspaceForOrganization-request-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`. Specify the Slack workspace that you want to use for your organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_RegisterSlackWorkspaceForOrganization_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountType": "string",
   "teamId": "string",
   "teamName": "string"
}
```

## Response Elements
<a name="API_RegisterSlackWorkspaceForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountType](#API_RegisterSlackWorkspaceForOrganization_ResponseSyntax) **   <a name="supportapp-RegisterSlackWorkspaceForOrganization-response-accountType"></a>
Whether the AWS account is a management or member account that's part of an organization in AWS Organizations.
Type: String
Valid Values: `management | member`

 ** [teamId](#API_RegisterSlackWorkspaceForOrganization_ResponseSyntax) **   <a name="supportapp-RegisterSlackWorkspaceForOrganization-response-teamId"></a>
The team ID in Slack. This ID uniquely identifies a Slack workspace, such as `T012ABCDEFG`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [teamName](#API_RegisterSlackWorkspaceForOrganization_ResponseSyntax) **   <a name="supportapp-RegisterSlackWorkspaceForOrganization-response-teamName"></a>
The name of the Slack workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.+`

## Errors
<a name="API_RegisterSlackWorkspaceForOrganization_Errors"></a>

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
<a name="API_RegisterSlackWorkspaceForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/RegisterSlackWorkspaceForOrganization)
