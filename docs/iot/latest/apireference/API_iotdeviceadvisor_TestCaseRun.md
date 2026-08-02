---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TestCaseRun.html
---

# TestCaseRun
<a name="API_iotdeviceadvisor_TestCaseRun"></a>

Provides the test case run.

## Contents
<a name="API_iotdeviceadvisor_TestCaseRun_Contents"></a>

 ** endTime **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-endTime"></a>
Provides test case run end time.
Type: Timestamp
Required: No

 ** failure **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-failure"></a>
Provides test case run failure result.
Type: String
Required: No

 ** logUrl **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-logUrl"></a>
Provides test case run log URL.
Type: String
Required: No

 ** startTime **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-startTime"></a>
Provides test case run start time.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-status"></a>
Provides the test case run status. Status is one of the following:
+  `PASS`: Test passed.
+  `FAIL`: Test failed.
+  `PENDING`: Test has not started running but is scheduled.
+  `RUNNING`: Test is running.
+  `STOPPING`: Test is performing cleanup steps. You will see this status only if you stop a suite run.
+  `STOPPED` Test is stopped. You will see this status only if you stop a suite run.
+  `PASS_WITH_WARNINGS`: Test passed with warnings.
+  `ERORR`: Test faced an error when running due to an internal issue.
Type: String
Valid Values: `PASS | FAIL | CANCELED | PENDING | RUNNING | STOPPING | STOPPED | PASS_WITH_WARNINGS | ERROR`
Required: No

 ** testCaseDefinitionId **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-testCaseDefinitionId"></a>
Provides the test case run definition ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

 ** testCaseDefinitionName **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-testCaseDefinitionName"></a>
Provides the test case run definition name.
Type: String
Required: No

 ** testCaseRunId **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-testCaseRunId"></a>
Provides the test case run ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

 ** testScenarios **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-testScenarios"></a>
 Provides the test scenarios for the test case run.
Type: Array of [TestCaseScenario](API_iotdeviceadvisor_TestCaseScenario.md) objects
Required: No

 ** warnings **   <a name="iot-Type-iotdeviceadvisor_TestCaseRun-warnings"></a>
Provides test case run warnings.
Type: String
Required: No

## See Also
<a name="API_iotdeviceadvisor_TestCaseRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/TestCaseRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/TestCaseRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/TestCaseRun)
