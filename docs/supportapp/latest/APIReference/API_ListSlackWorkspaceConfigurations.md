---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackWorkspaceConfigurations.html
---

# ListSlackWorkspaceConfigurations
<a name="API_ListSlackWorkspaceConfigurations"></a>

Lists the Slack workspace configurations for an AWS account.

## Request Syntax
<a name="API_ListSlackWorkspaceConfigurations_RequestSyntax"></a>

```
POST /control/list-slack-workspace-configurations HTTP/1.1
Content-type: application/json

{
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSlackWorkspaceConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSlackWorkspaceConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListSlackWorkspaceConfigurations_RequestSyntax) **   <a name="supportapp-ListSlackWorkspaceConfigurations-request-nextToken"></a>
If the results of a search are large, the API only returns a portion of the results and includes a `nextToken` pagination token in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When the API returns the last set of results, the response doesn't include a pagination token value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListSlackWorkspaceConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "slackWorkspaceConfigurations": [
      {
         "allowOrganizationMemberAccount": boolean,
         "teamId": "string",
         "teamName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSlackWorkspaceConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSlackWorkspaceConfigurations_ResponseSyntax) **   <a name="supportapp-ListSlackWorkspaceConfigurations-response-nextToken"></a>
The point where pagination should resume when the response returns only partial results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [slackWorkspaceConfigurations](#API_ListSlackWorkspaceConfigurations_ResponseSyntax) **   <a name="supportapp-ListSlackWorkspaceConfigurations-response-slackWorkspaceConfigurations"></a>
The configurations for a Slack workspace.
Type: Array of [SlackWorkspaceConfiguration](API_SlackWorkspaceConfiguration.md) objects

## Errors
<a name="API_ListSlackWorkspaceConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_ListSlackWorkspaceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/ListSlackWorkspaceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/ListSlackWorkspaceConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support App in Slack. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportapp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
