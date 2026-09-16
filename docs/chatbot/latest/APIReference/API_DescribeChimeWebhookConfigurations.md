---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeChimeWebhookConfigurations.html
---

# DescribeChimeWebhookConfigurations
<a name="API_DescribeChimeWebhookConfigurations"></a>

Lists Amazon Chime webhook configurations optionally filtered by ChatConfigurationArn.

## Request Syntax
<a name="API_DescribeChimeWebhookConfigurations_RequestSyntax"></a>

```
POST /describe-chime-webhook-configurations HTTP/1.1
Content-type: application/json

{
   "ChatConfigurationArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeChimeWebhookConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeChimeWebhookConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfigurationArn](#API_DescribeChimeWebhookConfigurations_RequestSyntax) **   <a name="qdevinchatapps-DescribeChimeWebhookConfigurations-request-ChatConfigurationArn"></a>
An optional Amazon Resource Name (ARN) of a ChimeWebhookConfiguration to describe.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

 ** [MaxResults](#API_DescribeChimeWebhookConfigurations_RequestSyntax) **   <a name="qdevinchatapps-DescribeChimeWebhookConfigurations-request-MaxResults"></a>
The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeChimeWebhookConfigurations_RequestSyntax) **   <a name="qdevinchatapps-DescribeChimeWebhookConfigurations-request-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`
Required: No

## Response Syntax
<a name="API_DescribeChimeWebhookConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "WebhookConfigurations": [
      {
         "ChatConfigurationArn": "string",
         "ConfigurationName": "string",
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
         "WebhookDescription": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeChimeWebhookConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeChimeWebhookConfigurations_ResponseSyntax) **   <a name="qdevinchatapps-DescribeChimeWebhookConfigurations-response-NextToken"></a>
An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1276.
Pattern: `[a-zA-Z0-9=\/+_.\-,#:\\"{}]{4,1276}`

 ** [WebhookConfigurations](#API_DescribeChimeWebhookConfigurations_ResponseSyntax) **   <a name="qdevinchatapps-DescribeChimeWebhookConfigurations-response-WebhookConfigurations"></a>
A list of Amazon Chime webhooks associated with the account.
Type: Array of [ChimeWebhookConfiguration](API_ChimeWebhookConfiguration.md) objects

## Errors
<a name="API_DescribeChimeWebhookConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DescribeChimeWebhookConfigurationsException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

## See Also
<a name="API_DescribeChimeWebhookConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DescribeChimeWebhookConfigurations)
