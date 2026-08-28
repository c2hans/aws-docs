---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectContinuousIntegrationScanConfiguration.html
---

# ProjectContinuousIntegrationScanConfiguration
<a name="API_ProjectContinuousIntegrationScanConfiguration"></a>

Contains the continuous integration scan configuration settings applied to a specific project.

## Contents
<a name="API_ProjectContinuousIntegrationScanConfiguration_Contents"></a>

 ** ruleSetCategories **   <a name="inspector2-Type-ProjectContinuousIntegrationScanConfiguration-ruleSetCategories"></a>
The categories of security rules applied during continuous integration scans for the project.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `SAST | IAC | SCA`
Required: No

 ** supportedEvent **   <a name="inspector2-Type-ProjectContinuousIntegrationScanConfiguration-supportedEvent"></a>
The repository event that triggers continuous integration scans for the project.
Type: String
Valid Values: `PULL_REQUEST | PUSH`
Required: No

## See Also
<a name="API_ProjectContinuousIntegrationScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ProjectContinuousIntegrationScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ProjectContinuousIntegrationScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ProjectContinuousIntegrationScanConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
