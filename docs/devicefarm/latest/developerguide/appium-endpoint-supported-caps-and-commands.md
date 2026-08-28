---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/appium-endpoint-supported-caps-and-commands.html
---

# Supported Appium capabilities and commands
<a name="appium-endpoint-supported-caps-and-commands"></a>

Device Farm's Appium endpoint supports most of the same commands and desired capabilities that you use on local devices, with a few exceptions. The following lists show which capabilities and commands are currently not supported. If your tests are unable to run as expected due to a restricted capability, please open a support case for additional guidance.

## Supported capabilities
<a name="appium-endpoint-unsupported-capabilities"></a>

When creating an Appium session on Device Farm, we recommend having a distinct set of capabilities which exclude any capabilities specific to your local device. On Device Farm, session creation may fail if certain unsupported capabilities are set. This includes device-specific capabilities like `udid` and `platformVersion`. Additionally, certain capabilities related to ChromeDriver on Android and WebDriverAgent on iOS aren't supported, as well as capabilities that are only supported on emulators and simulators.

## Supported commands
<a name="appium-endpoint-unsupported-commands"></a>

Most Appium commands that run properly on real Android and iOS devices will run as-expected on Device Farm, with the following exclusions:

### Appium device commands (`/appium/device`)
<a name="appium-endpoint-unsupported-device-commands"></a>
+ `install_app`
+ `finger_print`
+ `send_sms`
+ `gsm_call`
+ `gsm_signal`
+ `gsm_voice`
+ `power_ac`
+ `power_capacity`
+ `network_speed`
+ `shake`

### Appium execute methods and scripts (`/execute`)
<a name="appium-endpoint-unsupported-execute-methods"></a>
+ `installApp`
+ `execEmuConsoleCommand`
+ `fingerprint`
+ `gsmCall`
+ `gsmSignal`
+ `sendSms`
+ `gsmVoice`
+ `powerAC`
+ `powerCapacity`
+ `networkSpeed`
+ `sensorSet`
+ `injectEmulatorCameraImage`
+ `isGpsEnabled`
+ `shake`
+ `clearApp`
+ `clearKeychains`
+ `configureLocalization`
+ `enrollBiometric`
+ `getPasteboard`
+ `installXCTestBundle`
+ `listXCTestBundles`
+ `listXCTestsInTestBundle`
+ `runXCTest`
+ `sendBiometricMatch`
+ `setPasteboard`
+ `setPermission`
+ `startAudioRecording`
+ `startLogsBroadcast`
+ `startRecordingScreen`
+ `startScreenStreaming`
+ `startXCTestScreenRecording`
+ `stopAudioRecording`
+ `stopLogsBroadcast`
+ `stopRecordingScreen`
+ `stopScreenStreaming`
+ `stopXCTestScreenRecording`
+ `updateSafariPreferences`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
