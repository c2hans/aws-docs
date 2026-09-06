---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateDevicePool.html
---

# UpdateDevicePool
<a name="API_UpdateDevicePool"></a>

Modifies the name, description, and rules in a device pool given the attributes and the pool ARN. Rule updates are all-or-nothing, meaning they can only be updated as a whole (or not at all).

## Request Syntax
<a name="API_UpdateDevicePool_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "clearMaxDevices": {{boolean}},
   "description": "{{string}}",
   "maxDevices": {{number}},
   "name": "{{string}}",
   "rules": [
      {
         "attribute": "{{string}}",
         "operator": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDevicePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-arn"></a>
The Amazon Resource Name (ARN) of the Device Farm device pool to update.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [clearMaxDevices](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-clearMaxDevices"></a>
Sets whether the `maxDevices` parameter applies to your device pool. If you set this parameter to `true`, the `maxDevices` parameter does not apply, and Device Farm does not limit the number of devices that it adds to your device pool. In this case, Device Farm adds all available devices that meet the criteria specified in the `rules` parameter.
If you use this parameter in your request, you cannot use the `maxDevices` parameter in the same request.
Type: Boolean
Required: No

 ** [description](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-description"></a>
A description of the device pool to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [maxDevices](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-maxDevices"></a>
The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and that meet the criteria that you assign for the `rules` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.
By specifying the maximum number of devices, you can control the costs that you incur by running tests.
If you use this parameter in your request, you cannot use the `clearMaxDevices` parameter in the same request.
Type: Integer
Required: No

 ** [name](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-name"></a>
A string that represents the name of the device pool to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [rules](#API_UpdateDevicePool_RequestSyntax) **   <a name="devicefarm-UpdateDevicePool-request-rules"></a>
Represents the rules to modify for the device pool. Updating rules is optional. If you update rules for your request, the update replaces the existing rules.
Type: Array of [Rule](API_Rule.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDevicePool_ResponseSyntax"></a>

```
{
   "devicePool": {
      "arn": "string",
      "description": "string",
      "maxDevices": number,
      "name": "string",
      "rules": [
         {
            "attribute": "string",
            "operator": "string",
            "value": "string"
         }
      ],
      "type": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDevicePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [devicePool](#API_UpdateDevicePool_ResponseSyntax) **   <a name="devicefarm-UpdateDevicePool-response-devicePool"></a>
The device pool you just updated.
Type: [DevicePool](API_DevicePool.md) object

## Errors
<a name="API_UpdateDevicePool_Errors"></a>

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
<a name="API_UpdateDevicePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateDevicePool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateDevicePool)
