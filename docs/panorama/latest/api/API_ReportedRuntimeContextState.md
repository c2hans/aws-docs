---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ReportedRuntimeContextState.html
---

# ReportedRuntimeContextState
<a name="API_ReportedRuntimeContextState"></a>

An application instance's state.

## Contents
<a name="API_ReportedRuntimeContextState_Contents"></a>

 ** DesiredState **   <a name="panorama-Type-ReportedRuntimeContextState-DesiredState"></a>
The application's desired state.
Type: String
Valid Values: `RUNNING | STOPPED | REMOVED`
Required: Yes

 ** DeviceReportedStatus **   <a name="panorama-Type-ReportedRuntimeContextState-DeviceReportedStatus"></a>
The application's reported status.
Type: String
Valid Values: `STOPPING | STOPPED | STOP_ERROR | REMOVAL_FAILED | REMOVAL_IN_PROGRESS | STARTING | RUNNING | INSTALL_ERROR | LAUNCHED | LAUNCH_ERROR | INSTALL_IN_PROGRESS`
Required: Yes

 ** DeviceReportedTime **   <a name="panorama-Type-ReportedRuntimeContextState-DeviceReportedTime"></a>
When the device reported the application's state.
Type: Timestamp
Required: Yes

 ** RuntimeContextName **   <a name="panorama-Type-ReportedRuntimeContextState-RuntimeContextName"></a>
The device's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.+`
Required: Yes

## See Also
<a name="API_ReportedRuntimeContextState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ReportedRuntimeContextState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ReportedRuntimeContextState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ReportedRuntimeContextState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
