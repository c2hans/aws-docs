---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityScanConfiguration.html
---

# CodeSecurityScanConfiguration
<a name="API_CodeSecurityScanConfiguration"></a>

Contains the configuration settings for code security scans.

## Contents
<a name="API_CodeSecurityScanConfiguration_Contents"></a>

 ** ruleSetCategories **   <a name="inspector2-Type-CodeSecurityScanConfiguration-ruleSetCategories"></a>
The categories of security rules to be applied during the scan.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `SAST | IAC | SCA`
Required: Yes

 ** continuousIntegrationScanConfiguration **   <a name="inspector2-Type-CodeSecurityScanConfiguration-continuousIntegrationScanConfiguration"></a>
Configuration settings for continuous integration scans that run automatically when code changes are made.
Type: [ContinuousIntegrationScanConfiguration](API_ContinuousIntegrationScanConfiguration.md) object
Required: No

 ** periodicScanConfiguration **   <a name="inspector2-Type-CodeSecurityScanConfiguration-periodicScanConfiguration"></a>
Configuration settings for periodic scans that run on a scheduled basis.
Type: [PeriodicScanConfiguration](API_PeriodicScanConfiguration.md) object
Required: No

## See Also
<a name="API_CodeSecurityScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSecurityScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSecurityScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSecurityScanConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
