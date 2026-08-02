---
source_url: https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackChannelConfigurations.html
---

# ListSlackChannelConfigurations
<a name="API_ListSlackChannelConfigurations"></a>

Lists the Slack channel configurations for an AWS account.

## Request Syntax
<a name="API_ListSlackChannelConfigurations_RequestSyntax"></a>

```
POST /control/list-slack-channel-configurations HTTP/1.1
Content-type: application/json

{
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSlackChannelConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSlackChannelConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListSlackChannelConfigurations_RequestSyntax) **   <a name="supportapp-ListSlackChannelConfigurations-request-nextToken"></a>
If the results of a search are large, the API only returns a portion of the results and includes a `nextToken` pagination token in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When the API returns the last set of results, the response doesn't include a pagination token value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListSlackChannelConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "slackChannelConfigurations": [
      {
         "channelId": "string",
         "channelName": "string",
         "channelRoleArn": "string",
         "notifyOnAddCorrespondenceToCase": boolean,
         "notifyOnCaseSeverity": "string",
         "notifyOnCreateOrReopenCase": boolean,
         "notifyOnResolveCase": boolean,
         "teamId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSlackChannelConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSlackChannelConfigurations_ResponseSyntax) **   <a name="supportapp-ListSlackChannelConfigurations-response-nextToken"></a>
The point where pagination should resume when the response returns only partial results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`

 ** [slackChannelConfigurations](#API_ListSlackChannelConfigurations_ResponseSyntax) **   <a name="supportapp-ListSlackChannelConfigurations-response-slackChannelConfigurations"></a>
The configurations for a Slack channel.
Type: Array of [SlackChannelConfiguration](API_SlackChannelConfiguration.md) objects

## Errors
<a name="API_ListSlackChannelConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_ListSlackChannelConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-app-2021-08-20/ListSlackChannelConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-app-2021-08-20/ListSlackChannelConfigurations)
