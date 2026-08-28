---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateRemoteAccessSession.html
---

# CreateRemoteAccessSession
<a name="API_CreateRemoteAccessSession"></a>

Specifies and starts a remote access session.

## Request Syntax
<a name="API_CreateRemoteAccessSession_RequestSyntax"></a>

```
{
   "appArn": "{{string}}",
   "configuration": {
      "auxiliaryApps": [ "{{string}}" ],
      "billingMethod": "{{string}}",
      "deviceProxy": {
         "host": "{{string}}",
         "port": {{number}}
      },
      "vpceConfigurationArns": [ "{{string}}" ]
   },
   "deviceArn": "{{string}}",
   "instanceArn": "{{string}}",
   "interactionMode": "{{string}}",
   "name": "{{string}}",
   "projectArn": "{{string}}",
   "skipAppResign": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateRemoteAccessSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [appArn](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-appArn"></a>
The Amazon Resource Name (ARN) of the app to create the remote access session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [configuration](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-configuration"></a>
The configuration information for the remote access session request.
Type: [CreateRemoteAccessSessionConfiguration](API_CreateRemoteAccessSessionConfiguration.md) object
Required: No

 ** [deviceArn](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-deviceArn"></a>
The ARN of the device for which you want to create a remote access session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [instanceArn](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-instanceArn"></a>
The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [interactionMode](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-interactionMode"></a>
 *This parameter has been deprecated.*
The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Valid Values: `INTERACTIVE | NO_VIDEO | VIDEO_ONLY`
Required: No

 ** [name](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-name"></a>
The name of the remote access session to create.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [projectArn](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-projectArn"></a>
The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [skipAppResign](#API_CreateRemoteAccessSession_RequestSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-request-skipAppResign"></a>
When set to `true`, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information on how Device Farm modifies your uploads during tests, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/)
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateRemoteAccessSession_ResponseSyntax"></a>

```
{
   "remoteAccessSession": {
      "appUpload": "string",
      "arn": "string",
      "billingMethod": "string",
      "created": number,
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
      "deviceMinutes": {
         "metered": number,
         "total": number,
         "unmetered": number
      },
      "deviceProxy": {
         "host": "string",
         "port": number
      },
      "deviceUdid": "string",
      "endpoint": "string",
      "endpoints": {
         "interactiveEndpoint": "string",
         "remoteDriverEndpoint": "string"
      },
      "instanceArn": "string",
      "interactionMode": "string",
      "message": "string",
      "name": "string",
      "result": "string",
      "skipAppResign": boolean,
      "started": number,
      "status": "string",
      "stopped": number,
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateRemoteAccessSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [remoteAccessSession](#API_CreateRemoteAccessSession_ResponseSyntax) **   <a name="devicefarm-CreateRemoteAccessSession-response-remoteAccessSession"></a>
A container that describes the remote access session when the request to create a remote access session is sent.
Type: [RemoteAccessSession](API_RemoteAccessSession.md) object

## Errors
<a name="API_CreateRemoteAccessSession_Errors"></a>

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
<a name="API_CreateRemoteAccessSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateRemoteAccessSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateRemoteAccessSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
