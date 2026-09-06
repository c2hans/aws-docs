---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListChannels.html
---

# ListChannels
<a name="API_ListChannels"></a>

Gets summary information about all channels in your account, in the AWS region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).

## Request Syntax
<a name="API_ListChannels_RequestSyntax"></a>

```
POST /ListChannels HTTP/1.1
Content-type: application/json

{
   "filterByAdConfigurationArn": "{{string}}",
   "filterByName": "{{string}}",
   "filterByPlaybackRestrictionPolicyArn": "{{string}}",
   "filterByRecordingConfigurationArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListChannels_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListChannels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterByAdConfigurationArn](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-filterByAdConfigurationArn"></a>
Filters the channel list to match the specified ad configuration ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:ad-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [filterByName](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-filterByName"></a>
Filters the channel list to match the specified name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [filterByPlaybackRestrictionPolicyArn](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-filterByPlaybackRestrictionPolicyArn"></a>
Filters the channel list to match the specified policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-restriction-policy/[a-zA-Z0-9-]+$`
Required: No

 ** [filterByRecordingConfigurationArn](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-filterByRecordingConfigurationArn"></a>
Filters the channel list to match the specified recording-configuration ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+$`
Required: No

 ** [maxResults](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-maxResults"></a>
Maximum number of channels to return. Default: 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListChannels_RequestSyntax) **   <a name="ivs-ListChannels-request-nextToken"></a>
The first channel to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListChannels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channels": [
      {
         "adConfigurationArn": "string",
         "arn": "string",
         "authorized": boolean,
         "insecureIngest": boolean,
         "latencyMode": "string",
         "name": "string",
         "playbackRestrictionPolicyArn": "string",
         "preset": "string",
         "recordingConfigurationArn": "string",
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channels](#API_ListChannels_ResponseSyntax) **   <a name="ivs-ListChannels-response-channels"></a>
List of the matching channels.
Type: Array of [ChannelSummary](API_ChannelSummary.md) objects

 ** [nextToken](#API_ListChannels_ResponseSyntax) **   <a name="ivs-ListChannels-response-nextToken"></a>
If there are more channels than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

## Errors
<a name="API_ListChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListChannels)
