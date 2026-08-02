---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetNetworkProfile.html
---

# GetNetworkProfile
<a name="API_GetNetworkProfile"></a>

Returns information about a network profile.

## Request Syntax
<a name="API_GetNetworkProfile_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetNetworkProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_GetNetworkProfile_RequestSyntax) **   <a name="devicefarm-GetNetworkProfile-request-arn"></a>
The ARN of the network profile to return information about.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_GetNetworkProfile_ResponseSyntax"></a>

```
{
   "networkProfile": {
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
}
```

## Response Elements
<a name="API_GetNetworkProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [networkProfile](#API_GetNetworkProfile_ResponseSyntax) **   <a name="devicefarm-GetNetworkProfile-response-networkProfile"></a>
The network profile.
Type: [NetworkProfile](API_NetworkProfile.md) object

## Errors
<a name="API_GetNetworkProfile_Errors"></a>

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
<a name="API_GetNetworkProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetNetworkProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetNetworkProfile)
