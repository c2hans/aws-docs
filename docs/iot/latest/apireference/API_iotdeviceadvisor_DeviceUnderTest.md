---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_DeviceUnderTest.html
---

# DeviceUnderTest
<a name="API_iotdeviceadvisor_DeviceUnderTest"></a>

Information of a test device. A thing ARN, certificate ARN or device role ARN is required.

## Contents
<a name="API_iotdeviceadvisor_DeviceUnderTest_Contents"></a>

 ** certificateArn **   <a name="iot-Type-iotdeviceadvisor_DeviceUnderTest-certificateArn"></a>
Lists device's certificate ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** deviceRoleArn **   <a name="iot-Type-iotdeviceadvisor_DeviceUnderTest-deviceRoleArn"></a>
Lists device's role ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** thingArn **   <a name="iot-Type-iotdeviceadvisor_DeviceUnderTest-thingArn"></a>
Lists device's thing ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_iotdeviceadvisor_DeviceUnderTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/DeviceUnderTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/DeviceUnderTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/DeviceUnderTest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
