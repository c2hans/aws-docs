---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetChannel.html
---

# GetChannel
<a name="API_GetChannel"></a>

Gets the channel configuration for the specified channel ARN. See also [BatchGetChannel](API_BatchGetChannel.md).

## Request Syntax
<a name="API_GetChannel_RequestSyntax"></a>

```
POST /GetChannel HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetChannel_RequestSyntax) **   <a name="ivs-GetChannel-request-arn"></a>
ARN of the channel for which the configuration is to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetChannel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channel": {
      "adConfigurationArn": "string",
      "arn": "string",
      "authorized": boolean,
      "containerFormat": "string",
      "ingestEndpoint": "string",
      "insecureIngest": boolean,
      "latencyMode": "string",
      "multitrackInputConfiguration": {
         "enabled": boolean,
         "maximumResolution": "string",
         "policy": "string"
      },
      "name": "string",
      "playbackRestrictionPolicyArn": "string",
      "playbackUrl": "string",
      "preset": "string",
      "recordingConfigurationArn": "string",
      "srt": {
         "endpoint": "string",
         "passphrase": "string"
      },
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channel](#API_GetChannel_ResponseSyntax) **   <a name="ivs-GetChannel-response-channel"></a>

Type: [Channel](API_Channel.md) object

## Errors
<a name="API_GetChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/GetChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/GetChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/GetChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/GetChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/GetChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/GetChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/GetChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/GetChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/GetChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/GetChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
