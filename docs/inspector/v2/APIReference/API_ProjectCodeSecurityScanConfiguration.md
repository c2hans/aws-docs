---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ProjectCodeSecurityScanConfiguration.html
---

# ProjectCodeSecurityScanConfiguration
<a name="API_ProjectCodeSecurityScanConfiguration"></a>

Contains the scan configuration settings applied to a specific project in a code repository.

## Contents
<a name="API_ProjectCodeSecurityScanConfiguration_Contents"></a>

 ** continuousIntegrationScanConfigurations **   <a name="inspector2-Type-ProjectCodeSecurityScanConfiguration-continuousIntegrationScanConfigurations"></a>
The continuous integration scan configurations applied to the project.
Type: Array of [ProjectContinuousIntegrationScanConfiguration](API_ProjectContinuousIntegrationScanConfiguration.md) objects
Required: No

 ** periodicScanConfigurations **   <a name="inspector2-Type-ProjectCodeSecurityScanConfiguration-periodicScanConfigurations"></a>
The periodic scan configurations applied to the project.
Type: Array of [ProjectPeriodicScanConfiguration](API_ProjectPeriodicScanConfiguration.md) objects
Required: No

## See Also
<a name="API_ProjectCodeSecurityScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ProjectCodeSecurityScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ProjectCodeSecurityScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ProjectCodeSecurityScanConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
