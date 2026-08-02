---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteDefinitionInformation.html
---

# SuiteDefinitionInformation
<a name="API_iotdeviceadvisor_SuiteDefinitionInformation"></a>

Information about the suite definition.

## Contents
<a name="API_iotdeviceadvisor_SuiteDefinitionInformation_Contents"></a>

 ** createdAt **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-createdAt"></a>
Date (in Unix epoch time) when the test suite was created.
Type: Timestamp
Required: No

 ** defaultDevices **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-defaultDevices"></a>
Specifies the devices that are under test for the test suite.
Type: Array of [DeviceUnderTest](API_iotdeviceadvisor_DeviceUnderTest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

 ** intendedForQualification **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-intendedForQualification"></a>
Specifies if the test suite is intended for qualification.
Type: Boolean
Required: No

 ** isLongDurationTest **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-isLongDurationTest"></a>
Verifies if the test suite is a long duration test.
Type: Boolean
Required: No

 ** protocol **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-protocol"></a>
Gets the MQTT protocol that is configured in the suite definition.
Type: String
Valid Values: `MqttV3_1_1 | MqttV5 | MqttV3_1_1_OverWebSocket | MqttV5_OverWebSocket`
Required: No

 ** suiteDefinitionId **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-suiteDefinitionId"></a>
Suite definition ID of the test suite.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

 ** suiteDefinitionName **   <a name="iot-Type-iotdeviceadvisor_SuiteDefinitionInformation-suiteDefinitionName"></a>
Suite name of the test suite.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_iotdeviceadvisor_SuiteDefinitionInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/SuiteDefinitionInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/SuiteDefinitionInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/SuiteDefinitionInformation)
