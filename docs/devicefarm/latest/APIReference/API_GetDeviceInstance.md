---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDeviceInstance.html
---

# GetDeviceInstance
<a name="API_GetDeviceInstance"></a>

Returns information about a device instance that belongs to a private device fleet.

## Request Syntax
<a name="API_GetDeviceInstance_RequestSyntax"></a>

```
{
   "arn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeviceInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_GetDeviceInstance_RequestSyntax) **   <a name="devicefarm-GetDeviceInstance-request-arn"></a>
The Amazon Resource Name (ARN) of the instance you're requesting information about.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

## Response Syntax
<a name="API_GetDeviceInstance_ResponseSyntax"></a>

```
{
   "deviceInstance": {
      "arn": "string",
      "deviceArn": "string",
      "instanceProfile": {
         "arn": "string",
         "description": "string",
         "excludeAppPackagesFromCleanup": [ "string" ],
         "name": "string",
         "packageCleanup": boolean,
         "rebootAfterUse": boolean
      },
      "labels": [ "string" ],
      "status": "string",
      "udid": "string"
   }
}
```

## Response Elements
<a name="API_GetDeviceInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deviceInstance](#API_GetDeviceInstance_ResponseSyntax) **   <a name="devicefarm-GetDeviceInstance-response-deviceInstance"></a>
An object that contains information about your device instance.
Type: [DeviceInstance](API_DeviceInstance.md) object

## Errors
<a name="API_GetDeviceInstance_Errors"></a>

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
<a name="API_GetDeviceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetDeviceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetDeviceInstance)
