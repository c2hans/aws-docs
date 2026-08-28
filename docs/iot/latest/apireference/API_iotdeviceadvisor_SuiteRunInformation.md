---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_SuiteRunInformation.html
---

# SuiteRunInformation
<a name="API_iotdeviceadvisor_SuiteRunInformation"></a>

Information about the suite run.

Requires permission to access the [SuiteRunInformation](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Contents
<a name="API_iotdeviceadvisor_SuiteRunInformation_Contents"></a>

 ** createdAt **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-createdAt"></a>
Date (in Unix epoch time) when the suite run was created.
Type: Timestamp
Required: No

 ** endAt **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-endAt"></a>
Date (in Unix epoch time) when the suite run ended.
Type: Timestamp
Required: No

 ** failed **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-failed"></a>
Number of test cases that failed in the suite run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 500.
Required: No

 ** passed **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-passed"></a>
Number of test cases that passed in the suite run.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 500.
Required: No

 ** startedAt **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-startedAt"></a>
Date (in Unix epoch time) when the suite run was started.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-status"></a>
Status of the suite run.
Type: String
Valid Values: `PASS | FAIL | CANCELED | PENDING | RUNNING | STOPPING | STOPPED | PASS_WITH_WARNINGS | ERROR`
Required: No

 ** suiteDefinitionId **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-suiteDefinitionId"></a>
Suite definition ID of the suite run.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

 ** suiteDefinitionName **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-suiteDefinitionName"></a>
Suite definition name of the suite run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** suiteDefinitionVersion **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-suiteDefinitionVersion"></a>
Suite definition version of the suite run.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.
Required: No

 ** suiteRunId **   <a name="iot-Type-iotdeviceadvisor_SuiteRunInformation-suiteRunId"></a>
Suite run ID of the suite run.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: No

## See Also
<a name="API_iotdeviceadvisor_SuiteRunInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/SuiteRunInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/SuiteRunInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/SuiteRunInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
