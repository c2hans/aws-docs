---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackWorkspaces.html
---

# DescribeSlackWorkspaces
<a name="API_DescribeSlackWorkspaces"></a>

List all authorized Slack workspaces connected to the AWS Account onboarded with Amazon Q Developer.

## Request Syntax
<a name="API_DescribeSlackWorkspaces_RequestSyntax"></a>

```
POST /describe-slack-workspaces HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeSlackWorkspaces_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeSlackWorkspaces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeSlackWorkspaces_RequestSyntax) **   <a name="qdevinchatapps-DescribeSlackWorkspaces-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeSlackWorkspaces_RequestSyntax) **   <a name="qdevinchatapps-DescribeSlackWorkspaces-request-NextToken"></a>
 An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`
Required: No

## Response Syntax
<a name="API_DescribeSlackWorkspaces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SlackWorkspaces": [
      {
         "SlackTeamId": "string",
         "SlackTeamName": "string",
         "State": "string",
         "StateReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSlackWorkspaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSlackWorkspaces_ResponseSyntax) **   <a name="qdevinchatapps-DescribeSlackWorkspaces-response-NextToken"></a>
 An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`

 ** [SlackWorkspaces](#API_DescribeSlackWorkspaces_ResponseSyntax) **   <a name="qdevinchatapps-DescribeSlackWorkspaces-response-SlackWorkspaces"></a>
A list of Slack workspaces registered with Amazon Q Developer.
Type: Array of [SlackWorkspace](API_SlackWorkspace.md) objects

## Errors
<a name="API_DescribeSlackWorkspaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DescribeSlackWorkspacesException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSlackWorkspaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DescribeSlackWorkspaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DescribeSlackWorkspaces)
