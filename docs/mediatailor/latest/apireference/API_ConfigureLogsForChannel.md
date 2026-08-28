---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ConfigureLogsForChannel.html
---

# ConfigureLogsForChannel
<a name="API_ConfigureLogsForChannel"></a>

Configures Amazon CloudWatch log settings for a channel.

## Request Syntax
<a name="API_ConfigureLogsForChannel_RequestSyntax"></a>

```
PUT /configureLogs/channel HTTP/1.1
Content-type: application/json

{
   "ChannelName": "{{string}}",
   "LogTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ConfigureLogsForChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ConfigureLogsForChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelName](#API_ConfigureLogsForChannel_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForChannel-request-ChannelName"></a>
The name of the channel.
Type: String
Required: Yes

 ** [LogTypes](#API_ConfigureLogsForChannel_RequestSyntax) **   <a name="mediatailor-ConfigureLogsForChannel-request-LogTypes"></a>
The types of logs to collect.
Type: Array of strings
Valid Values: `AS_RUN`
Required: Yes

## Response Syntax
<a name="API_ConfigureLogsForChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChannelName": "string",
   "LogTypes": [ "string" ]
}
```

## Response Elements
<a name="API_ConfigureLogsForChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelName](#API_ConfigureLogsForChannel_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForChannel-response-ChannelName"></a>
The name of the channel.
Type: String

 ** [LogTypes](#API_ConfigureLogsForChannel_ResponseSyntax) **   <a name="mediatailor-ConfigureLogsForChannel-response-LogTypes"></a>
The types of logs collected.
Type: Array of strings
Valid Values: `AS_RUN`

## Errors
<a name="API_ConfigureLogsForChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ConfigureLogsForChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/ConfigureLogsForChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ConfigureLogsForChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
