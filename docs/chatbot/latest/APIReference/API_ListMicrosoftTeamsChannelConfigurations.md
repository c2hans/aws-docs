---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsChannelConfigurations.html
---

# ListMicrosoftTeamsChannelConfigurations
<a name="API_ListMicrosoftTeamsChannelConfigurations"></a>

Lists all Amazon Q Developer Microsoft Teams channel configurations in an AWS account.

## Request Syntax
<a name="API_ListMicrosoftTeamsChannelConfigurations_RequestSyntax"></a>

```
POST /list-ms-teams-channel-configurations HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TeamId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListMicrosoftTeamsChannelConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListMicrosoftTeamsChannelConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMicrosoftTeamsChannelConfigurations_RequestSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsChannelConfigurations-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMicrosoftTeamsChannelConfigurations_RequestSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsChannelConfigurations-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`
Required: No

 ** [TeamId](#API_ListMicrosoftTeamsChannelConfigurations_RequestSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsChannelConfigurations-request-TeamId"></a>
 The ID of the Microsoft Teams authorized with Amazon Q Developer.
To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the Amazon Q Developer in chat applications console. Then you can copy and paste the team ID from the console. For more information, see [Step 1: Configure a Microsoft Teams client](https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup) in the * Amazon Q Developer Administrator Guide*.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9A-Fa-f]{8}(?:-[0-9A-Fa-f]{4}){3}-[0-9A-Fa-f]{12}`
Required: No

## Response Syntax
<a name="API_ListMicrosoftTeamsChannelConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "TeamChannelConfigurations": [
      {
         "ChannelId": "string",
         "ChannelName": "string",
         "ChatConfigurationArn": "string",
         "ConfigurationName": "string",
         "GuardrailPolicyArns": [ "string" ],
         "IamRoleArn": "string",
         "LoggingLevel": "string",
         "SnsTopicArns": [ "string" ],
         "State": "string",
         "StateReason": "string",
         "Tags": [
            {
               "TagKey": "string",
               "TagValue": "string"
            }
         ],
         "TeamId": "string",
         "TeamName": "string",
         "TenantId": "string",
         "UserAuthorizationRequired": boolean
      }
   ]
}
```

## Response Elements
<a name="API_ListMicrosoftTeamsChannelConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListMicrosoftTeamsChannelConfigurations_ResponseSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsChannelConfigurations-response-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`

 ** [TeamChannelConfigurations](#API_ListMicrosoftTeamsChannelConfigurations_ResponseSyntax) **   <a name="qdevinchatapps-ListMicrosoftTeamsChannelConfigurations-response-TeamChannelConfigurations"></a>
A list of Amazon Q Developer channel configurations for Microsoft Teams.
Type: Array of [TeamsChannelConfiguration](API_TeamsChannelConfiguration.md) objects

## Errors
<a name="API_ListMicrosoftTeamsChannelConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ListTeamsChannelConfigurationsException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_ListMicrosoftTeamsChannelConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/ListMicrosoftTeamsChannelConfigurations)
