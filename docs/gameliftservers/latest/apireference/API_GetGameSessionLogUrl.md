---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetGameSessionLogUrl.html
---

# GetGameSessionLogUrl
<a name="API_GetGameSessionLogUrl"></a>

 **This API works with the following fleet types:** EC2

Retrieves the location of stored game session logs for a specified game session on Amazon GameLift Servers managed fleets. When a game session is terminated, Amazon GameLift Servers automatically stores the logs in Amazon S3 and retains them for 14 days. Use this URL to download the logs.

**Note**
See the [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_gamelift) page for maximum log file sizes. Log files that exceed this limit are not saved.

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_GetGameSessionLogUrl_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetGameSessionLogUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_GetGameSessionLogUrl_RequestSyntax) **   <a name="gameliftservers-GetGameSessionLogUrl-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions to get logs for. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

## Response Syntax
<a name="API_GetGameSessionLogUrl_ResponseSyntax"></a>

```
{
   "PreSignedUrl": "string"
}
```

## Response Elements
<a name="API_GetGameSessionLogUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PreSignedUrl](#API_GetGameSessionLogUrl_ResponseSyntax) **   <a name="gameliftservers-GetGameSessionLogUrl-response-PreSignedUrl"></a>
Location of the requested game session logs, available for download. This URL is valid for 15 minutes, after which S3 will reject any download request using this URL. You can request a new URL any time within the 14-day period that the logs are retained.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetGameSessionLogUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## See Also
<a name="API_GetGameSessionLogUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/GetGameSessionLogUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GetGameSessionLogUrl)
