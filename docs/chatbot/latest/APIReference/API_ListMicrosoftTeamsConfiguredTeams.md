---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsConfiguredTeams.html
---

# ListMicrosoftTeamsConfiguredTeams
<a name="API_ListMicrosoftTeamsConfiguredTeams"></a>

Lists all authorized Microsoft Teams for an AWS Account

## Request Syntax
<a name="API_ListMicrosoftTeamsConfiguredTeams_RequestSyntax"></a>

```
POST /list-ms-teams-configured-teams HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMicrosoftTeamsConfiguredTeams_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMicrosoftTeamsConfiguredTeams_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMicrosoftTeamsConfiguredTeams_RequestSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsConfiguredTeams-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMicrosoftTeamsConfiguredTeams_RequestSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsConfiguredTeams-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`
Required: No

## Response Syntax
<a name="API_ListMicrosoftTeamsConfiguredTeams_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfiguredTeams": [
      {
         "State": "string",
         "StateReason": "string",
         "TeamId": "string",
         "TeamName": "string",
         "TenantId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMicrosoftTeamsConfiguredTeams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfiguredTeams](#API_ListMicrosoftTeamsConfiguredTeams_ResponseSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsConfiguredTeams-response-ConfiguredTeams"></a>
A list of teams in Microsoft Teams that are configured with Amazon Q Developer.
Type: Array of [ConfiguredTeam](API_ConfiguredTeam.md) objects

 ** [NextToken](#API_ListMicrosoftTeamsConfiguredTeams_ResponseSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsConfiguredTeams-response-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`

## Errors
<a name="API_ListMicrosoftTeamsConfiguredTeams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ListMicrosoftTeamsConfiguredTeamsException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_ListMicrosoftTeamsConfiguredTeams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/ListMicrosoftTeamsConfiguredTeams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
