---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityScanConfigurationSummary.html
---

# CodeSecurityScanConfigurationSummary
<a name="API_CodeSecurityScanConfigurationSummary"></a>

A summary of information about a code security scan configuration.

## Contents
<a name="API_CodeSecurityScanConfigurationSummary_Contents"></a>

 ** name **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-name"></a>
The name of the scan configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[a-zA-Z0-9-_$:.]*`
Required: Yes

 ** ownerAccountId **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-ownerAccountId"></a>
The AWS account ID that owns the scan configuration.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `.*(^\d{12}$)|(^o-[a-z0-9]{10,32}$).*`
Required: Yes

 ** ruleSetCategories **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-ruleSetCategories"></a>
The categories of security rules applied during the scan.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `SAST | IAC | SCA`
Required: Yes

 ** scanConfigurationArn **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-scanConfigurationArn"></a>
The Amazon Resource Name (ARN) of the scan configuration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/codesecurity-configuration/[a-f0-9-]{36}`
Required: Yes

 ** continuousIntegrationScanSupportedEvents **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-continuousIntegrationScanSupportedEvents"></a>
The repository events that trigger continuous integration scans.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `PULL_REQUEST | PUSH`
Required: No

 ** frequencyExpression **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-frequencyExpression"></a>
The schedule expression for periodic scans, in cron format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** periodicScanFrequency **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-periodicScanFrequency"></a>
The frequency at which periodic scans are performed.
Type: String
Valid Values: `WEEKLY | MONTHLY | NEVER`
Required: No

 ** scopeSettings **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-scopeSettings"></a>
The scope settings that define which repositories will be scanned. If the `ScopeSetting` parameter is `ALL` the scan configuration applies to all existing and future projects imported into Amazon Inspector.
Type: [ScopeSettings](API_ScopeSettings.md) object
Required: No

 ** tags **   <a name="inspector2-Type-CodeSecurityScanConfigurationSummary-tags"></a>
The tags associated with the scan configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CodeSecurityScanConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSecurityScanConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSecurityScanConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSecurityScanConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
