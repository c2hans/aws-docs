---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteDefinitionConfiguration.html
---

# SuiteDefinitionConfiguration
<a name="API_iotdeviceadvisor_SuiteDefinitionConfiguration"></a>

Gets the suite definition configuration.

## Contents
<a name="API_iotdeviceadvisor_SuiteDefinitionConfiguration_Contents"></a>

 ** devicePermissionRoleArn **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-devicePermissionRoleArn"></a>
Gets the device permission ARN. This is a required parameter.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** rootGroup **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-rootGroup"></a>
Gets the test suite root group. This is a required parameter. For updating or creating the latest qualification suite, if `intendedForQualification` is set to true, `rootGroup` can be an empty string. If `intendedForQualification` is false, `rootGroup` cannot be an empty string. If `rootGroup` is empty, and `intendedForQualification` is set to true, all the qualification tests are included, and the configuration is default.
 For a qualification suite, the minimum length is 0, and the maximum is 2048. For a non-qualification suite, the minimum length is 1, and the maximum is 2048.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** suiteDefinitionName **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-suiteDefinitionName"></a>
Gets the suite definition name. This is a required parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** devices **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-devices"></a>
Gets the devices configured.
Type: Array of [DeviceUnderTest](API_iotdeviceadvisor_DeviceUnderTest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** intendedForQualification **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-intendedForQualification"></a>
Gets the tests intended for qualification in a suite.
Type: Boolean
Required: No

 ** isLongDurationTest **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-isLongDurationTest"></a>
Verifies if the test suite is a long duration test.
Type: Boolean
Required: No

 ** protocol **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionConfiguration-protocol"></a>
Sets the MQTT protocol that is configured in the suite definition.
Type: String
Valid Values: `MqttV3_1_1 | MqttV5 | MqttV3_1_1_OverWebSocket | MqttV5_OverWebSocket`
Required: No

## See Also
<a name="API_iotdeviceadvisor_SuiteDefinitionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/SuiteDefinitionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/SuiteDefinitionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/SuiteDefinitionConfiguration)
