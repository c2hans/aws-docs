---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_TestCaseScenario.html
---

# TestCaseScenario
<a name="API_iotdeviceadvisor_TestCaseScenario"></a>

Provides test case scenario.

## Contents
<a name="API_iotdeviceadvisor_TestCaseScenario_Contents"></a>

 ** failure **   <a name="iot-Type-iotdeviceadvisor_TestCaseScenario-failure"></a>
Provides test case scenario failure result.
Type: String
Required: No

 ** status **   <a name="iot-Type-iotdeviceadvisor_TestCaseScenario-status"></a>
Provides the test case scenario status. Status is one of the following:
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

 ** systemMessage **   <a name="iot-Type-iotdeviceadvisor_TestCaseScenario-systemMessage"></a>
Provides test case scenario system messages if any.
Type: String
Required: No

 ** testCaseScenarioId **   <a name="iot-Type-iotdeviceadvisor_TestCaseScenario-testCaseScenarioId"></a>
Provides test case scenario ID.
Type: String
Required: No

 ** testCaseScenarioType **   <a name="iot-Type-iotdeviceadvisor_TestCaseScenario-testCaseScenarioType"></a>
Provides test case scenario type. Type is one of the following:
+ Advanced
+ Basic
Type: String
Valid Values: `Advanced | Basic`
Required: No

## See Also
<a name="API_iotdeviceadvisor_TestCaseScenario_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/TestCaseScenario)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/TestCaseScenario)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/TestCaseScenario)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
