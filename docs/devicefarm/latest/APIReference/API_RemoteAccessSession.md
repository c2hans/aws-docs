---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_RemoteAccessSession.html
---

# RemoteAccessSession
<a name="API_RemoteAccessSession"></a>

Represents information about the remote access session.

## Contents
<a name="API_RemoteAccessSession_Contents"></a>

 ** appUpload **   <a name="devicefarm-Type-RemoteAccessSession-appUpload"></a>
The ARN for the app to be installed onto your device.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** arn **   <a name="devicefarm-Type-RemoteAccessSession-arn"></a>
The Amazon Resource Name (ARN) of the remote access session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** billingMethod **   <a name="devicefarm-Type-RemoteAccessSession-billingMethod"></a>
The billing method of the remote access session. Possible values include `METERED` or `UNMETERED`. For more information about metered devices, see [AWS Device Farm terminology](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology).
Type: String
Valid Values: `METERED | UNMETERED`
Required: No

 ** created **   <a name="devicefarm-Type-RemoteAccessSession-created"></a>
The date and time the remote access session was created.
Type: Timestamp
Required: No

 ** device **   <a name="devicefarm-Type-RemoteAccessSession-device"></a>
The device (phone or tablet) used in the remote access session.
Type: [Device](API_Device.md) object
Required: No

 ** deviceMinutes **   <a name="devicefarm-Type-RemoteAccessSession-deviceMinutes"></a>
The number of minutes a device is used in a remote access session (including setup and teardown minutes).
Type: [DeviceMinutes](API_DeviceMinutes.md) object
Required: No

 ** deviceProxy **   <a name="devicefarm-Type-RemoteAccessSession-deviceProxy"></a>
The device proxy configured for the remote access session.
Type: [DeviceProxy](API_DeviceProxy.md) object
Required: No

 ** deviceUdid **   <a name="devicefarm-Type-RemoteAccessSession-deviceUdid"></a>
Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.
Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html).
Type: String
Required: No

 ** endpoint **   <a name="devicefarm-Type-RemoteAccessSession-endpoint"></a>
The endpoint for the remote access session. This field is deprecated, and is replaced by the new `endpoints.interactiveEndpoint` field.
Type: String
Required: No

 ** endpoints **   <a name="devicefarm-Type-RemoteAccessSession-endpoints"></a>
Represents the remote endpoints for viewing and controlling a device during a remote access session.
Type: [RemoteAccessEndpoints](API_RemoteAccessEndpoints.md) object
Required: No

 ** instanceArn **   <a name="devicefarm-Type-RemoteAccessSession-instanceArn"></a>
The ARN of the instance.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** interactionMode **   <a name="devicefarm-Type-RemoteAccessSession-interactionMode"></a>
 *This member has been deprecated.*
The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Valid Values: `INTERACTIVE | NO_VIDEO | VIDEO_ONLY`
Required: No

 ** message **   <a name="devicefarm-Type-RemoteAccessSession-message"></a>
A message about the remote access session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** name **   <a name="devicefarm-Type-RemoteAccessSession-name"></a>
The name of the remote access session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** result **   <a name="devicefarm-Type-RemoteAccessSession-result"></a>
The result of the remote access session. Can be any of the following:
+ PENDING.
+ PASSED.
+ WARNED.
+ FAILED.
+ SKIPPED.
+ ERRORED.
+ STOPPED.
Type: String
Valid Values: `PENDING | PASSED | WARNED | FAILED | SKIPPED | ERRORED | STOPPED`
Required: No

 ** skipAppResign **   <a name="devicefarm-Type-RemoteAccessSession-skipAppResign"></a>
When set to `true`, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs*.
Type: Boolean
Required: No

 ** started **   <a name="devicefarm-Type-RemoteAccessSession-started"></a>
The date and time the remote access session was started.
Type: Timestamp
Required: No

 ** status **   <a name="devicefarm-Type-RemoteAccessSession-status"></a>
The status of the remote access session. Can be any of the following:
+ PENDING.
+ PENDING\_CONCURRENCY.
+ PENDING\_DEVICE.
+ PROCESSING.
+ SCHEDULING.
+ PREPARING.
+ RUNNING.
+ COMPLETED.
+ STOPPING.
Type: String
Valid Values: `PENDING | PENDING_CONCURRENCY | PENDING_DEVICE | PROCESSING | SCHEDULING | PREPARING | RUNNING | COMPLETED | STOPPING`
Required: No

 ** stopped **   <a name="devicefarm-Type-RemoteAccessSession-stopped"></a>
The date and time the remote access session was stopped.
Type: Timestamp
Required: No

 ** vpcConfig **   <a name="devicefarm-Type-RemoteAccessSession-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## See Also
<a name="API_RemoteAccessSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/RemoteAccessSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/RemoteAccessSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/RemoteAccessSession)
