---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteRunConfiguration.html
---

# SuiteRunConfiguration
<a name="API_iotdeviceadvisor_SuiteRunConfiguration"></a>

Gets suite run configuration.

## Contents
<a name="API_iotdeviceadvisor_SuiteRunConfiguration_Contents"></a>

 ** primaryDevice **   <a name="iot-Type-iotdeviceadvisor_SuiteRunConfiguration-primaryDevice"></a>
Sets the primary device for the test suite run. This requires a thing ARN or a certificate ARN.
Type: [DeviceUnderTest](API_iotdeviceadvisor_DeviceUnderTest.md) object
Required: Yes

 ** parallelRun **   <a name="iot-Type-iotdeviceadvisor_SuiteRunConfiguration-parallelRun"></a>
TRUE if multiple test suites run in parallel.
Type: Boolean
Required: No

 ** selectedTestList **   <a name="iot-Type-iotdeviceadvisor_SuiteRunConfiguration-selectedTestList"></a>
Sets test case list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

## See Also
<a name="API_iotdeviceadvisor_SuiteRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/SuiteRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/SuiteRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/SuiteRunConfiguration)
