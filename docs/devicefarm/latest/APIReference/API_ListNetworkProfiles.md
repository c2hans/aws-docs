---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListNetworkProfiles.html
---

# ListNetworkProfiles
<a name="API_ListNetworkProfiles"></a>

Returns the list of available network profiles.

## Request Syntax
<a name="API_ListNetworkProfiles_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}",
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNetworkProfiles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListNetworkProfiles_RequestSyntax) **   <a name="devicefarm-ListNetworkProfiles-request-arn"></a>
The Amazon Resource Name (ARN) of the project for which you want to list network profiles.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListNetworkProfiles_RequestSyntax) **   <a name="devicefarm-ListNetworkProfiles-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** [type](#API_ListNetworkProfiles_RequestSyntax) **   <a name="devicefarm-ListNetworkProfiles-request-type"></a>
The type of network profile to return information about. Valid values are listed here.
Type: String
Valid Values: `CURATED | PRIVATE`
Required: No

## Response Syntax
<a name="API_ListNetworkProfiles_ResponseSyntax"></a>

```
{
   "networkProfiles": [
      {
         "arn": "string",
         "description": "string",
         "downlinkBandwidthBits": number,
         "downlinkDelayMs": number,
         "downlinkJitterMs": number,
         "downlinkLossPercent": number,
         "name": "string",
         "type": "string",
         "uplinkBandwidthBits": number,
         "uplinkDelayMs": number,
         "uplinkJitterMs": number,
         "uplinkLossPercent": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNetworkProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkProfiles](#API_ListNetworkProfiles_ResponseSyntax) **   <a name="devicefarm-ListNetworkProfiles-response-networkProfiles"></a>
A list of the available network profiles.
Type: Array of [NetworkProfile](API_NetworkProfile.md) objects

 ** [nextToken](#API_ListNetworkProfiles_ResponseSyntax) **   <a name="devicefarm-ListNetworkProfiles-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListNetworkProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListNetworkProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListNetworkProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListNetworkProfiles)
