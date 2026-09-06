---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_GetDevicePoolCompatibility.html
---

# GetDevicePoolCompatibility
<a name="API_GetDevicePoolCompatibility"></a>

Gets information about compatibility with a device pool.

## Request Syntax
<a name="API_GetDevicePoolCompatibility_RequestSyntax"></a>

```
{
   "appArn": "{{string}}",
   "configuration": {
      "auxiliaryApps": [ "{{string}}" ],
      "billingMethod": "{{string}}",
      "customerArtifactPaths": {
         "androidPaths": [ "{{string}}" ],
         "deviceHostPaths": [ "{{string}}" ],
         "iosPaths": [ "{{string}}" ]
      },
      "deviceProxy": {
         "host": "{{string}}",
         "port": {{number}}
      },
      "environmentVariables": [
         {
            "name": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "executionRoleArn": "{{string}}",
      "extraDataPackageArn": "{{string}}",
      "insightsTypes": [ "{{string}}" ],
      "locale": "{{string}}",
      "location": {
         "latitude": {{number}},
         "longitude": {{number}}
      },
      "networkProfileArn": "{{string}}",
      "radios": {
         "bluetooth": {{boolean}},
         "gps": {{boolean}},
         "nfc": {{boolean}},
         "wifi": {{boolean}}
      },
      "vpceConfigurationArns": [ "{{string}}" ]
   },
   "devicePoolArn": "{{string}}",
   "projectArn": "{{string}}",
   "test": {
      "filter": "{{string}}",
      "parameters": {
         "{{string}}" : "{{string}}"
      },
      "testPackageArn": "{{string}}",
      "testSpecArn": "{{string}}",
      "type": "{{string}}"
   },
   "testType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDevicePoolCompatibility_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [appArn](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-appArn"></a>
The ARN of the app that is associated with the specified device pool.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [configuration](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-configuration"></a>
An object that contains information about the settings for a run.
Type: [ScheduleRunConfiguration](API_ScheduleRunConfiguration.md) object
Required: No

 ** [devicePoolArn](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-devicePoolArn"></a>
The device pool's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [projectArn](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-projectArn"></a>
The ARN of the project for which you want to check device pool compatibility.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [test](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-test"></a>
Information about the uploaded test to be run against the device pool.
Type: [ScheduleRunTest](API_ScheduleRunTest.md) object
Required: No

 ** [testType](#API_GetDevicePoolCompatibility_RequestSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-request-testType"></a>
The test type for the specified device pool.
Allowed values include the following:
+ BUILTIN\_FUZZ.
+ APPIUM\_JAVA\_JUNIT.
+ APPIUM\_JAVA\_TESTNG.
+ APPIUM\_PYTHON.
+ APPIUM\_NODE.
+ APPIUM\_RUBY.
+ APPIUM\_WEB\_JAVA\_JUNIT.
+ APPIUM\_WEB\_JAVA\_TESTNG.
+ APPIUM\_WEB\_PYTHON.
+ APPIUM\_WEB\_NODE.
+ APPIUM\_WEB\_RUBY.
+ INSTRUMENTATION.
+ XCTEST.
+ XCTEST\_UI.
Type: String
Valid Values: `BUILTIN_FUZZ | APPIUM_JAVA_JUNIT | APPIUM_JAVA_TESTNG | APPIUM_PYTHON | APPIUM_NODE | APPIUM_RUBY | APPIUM_WEB_JAVA_JUNIT | APPIUM_WEB_JAVA_TESTNG | APPIUM_WEB_PYTHON | APPIUM_WEB_NODE | APPIUM_WEB_RUBY | INSTRUMENTATION | XCTEST | XCTEST_UI`
Required: No

## Response Syntax
<a name="API_GetDevicePoolCompatibility_ResponseSyntax"></a>

```
{
   "compatibleDevices": [
      {
         "compatible": boolean,
         "device": {
            "arn": "string",
            "availability": "string",
            "carrier": "string",
            "cpu": {
               "architecture": "string",
               "clock": number,
               "frequency": "string"
            },
            "fleetName": "string",
            "fleetType": "string",
            "formFactor": "string",
            "heapSize": number,
            "image": "string",
            "instances": [
               {
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
            ],
            "manufacturer": "string",
            "memory": number,
            "model": "string",
            "modelId": "string",
            "name": "string",
            "os": "string",
            "platform": "string",
            "radio": "string",
            "remoteAccessEnabled": boolean,
            "remoteDebugEnabled": boolean,
            "resolution": {
               "height": number,
               "width": number
            }
         },
         "incompatibilityMessages": [
            {
               "message": "string",
               "type": "string"
            }
         ]
      }
   ],
   "incompatibleDevices": [
      {
         "compatible": boolean,
         "device": {
            "arn": "string",
            "availability": "string",
            "carrier": "string",
            "cpu": {
               "architecture": "string",
               "clock": number,
               "frequency": "string"
            },
            "fleetName": "string",
            "fleetType": "string",
            "formFactor": "string",
            "heapSize": number,
            "image": "string",
            "instances": [
               {
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
            ],
            "manufacturer": "string",
            "memory": number,
            "model": "string",
            "modelId": "string",
            "name": "string",
            "os": "string",
            "platform": "string",
            "radio": "string",
            "remoteAccessEnabled": boolean,
            "remoteDebugEnabled": boolean,
            "resolution": {
               "height": number,
               "width": number
            }
         },
         "incompatibilityMessages": [
            {
               "message": "string",
               "type": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetDevicePoolCompatibility_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [compatibleDevices](#API_GetDevicePoolCompatibility_ResponseSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-response-compatibleDevices"></a>
Information about compatible devices.
Type: Array of [DevicePoolCompatibilityResult](API_DevicePoolCompatibilityResult.md) objects

 ** [incompatibleDevices](#API_GetDevicePoolCompatibility_ResponseSyntax) **   <a name="devicefarm-GetDevicePoolCompatibility-response-incompatibleDevices"></a>
Information about incompatible devices.
Type: Array of [DevicePoolCompatibilityResult](API_DevicePoolCompatibilityResult.md) objects

## Errors
<a name="API_GetDevicePoolCompatibility_Errors"></a>

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
<a name="API_GetDevicePoolCompatibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/GetDevicePoolCompatibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/GetDevicePoolCompatibility)
