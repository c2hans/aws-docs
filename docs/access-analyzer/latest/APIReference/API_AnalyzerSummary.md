---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzerSummary.html
---

# AnalyzerSummary
<a name="API_AnalyzerSummary"></a>

Contains information about the analyzer.

## Contents
<a name="API_AnalyzerSummary_Contents"></a>

 ** arn **   <a name="accessanalyzer-Type-AnalyzerSummary-arn"></a>
The ARN of the analyzer.
Type: String
Pattern: `[^:]*:[^:]*:[^:]*:[^:]*:[^:]*:analyzer/.{1,255}`
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-AnalyzerSummary-createdAt"></a>
A timestamp for the time at which the analyzer was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="accessanalyzer-Type-AnalyzerSummary-name"></a>
The name of the analyzer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][A-Za-z0-9_.-]*`
Required: Yes

 ** status **   <a name="accessanalyzer-Type-AnalyzerSummary-status"></a>
The status of the analyzer. An `Active` analyzer successfully monitors supported resources and generates new findings. The analyzer is `Disabled` when a user action, such as removing trusted access for AWS Identity and Access Management Access Analyzer from AWS Organizations, causes the analyzer to stop generating new findings. The status is `Creating` when the analyzer creation is in progress and `Failed` when the analyzer creation has failed.
Type: String
Valid Values: `ACTIVE | CREATING | DISABLED | FAILED`
Required: Yes

 ** type **   <a name="accessanalyzer-Type-AnalyzerSummary-type"></a>
The type represents the zone of trust or scope for the analyzer.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ORGANIZATION_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS`
Required: Yes

 ** configuration **   <a name="accessanalyzer-Type-AnalyzerSummary-configuration"></a>
Specifies if the analyzer is an external access, unused access, or internal access analyzer. The [GetAnalyzer](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_GetAnalyzer.html) action includes this property in its response if a configuration is specified, while the [ListAnalyzers](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ListAnalyzers.html) action omits it.
Type: [AnalyzerConfiguration](API_AnalyzerConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** lastResourceAnalyzed **   <a name="accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzed"></a>
The resource that was most recently analyzed by the analyzer.
Type: String
Required: No

 ** lastResourceAnalyzedAt **   <a name="accessanalyzer-Type-AnalyzerSummary-lastResourceAnalyzedAt"></a>
The time at which the most recently analyzed resource was analyzed.
Type: Timestamp
Required: No

 ** statusReason **   <a name="accessanalyzer-Type-AnalyzerSummary-statusReason"></a>
The `statusReason` provides more details about the current status of the analyzer. For example, if the creation for the analyzer fails, a `Failed` status is returned. For an analyzer with organization as the type, this failure can be due to an issue with creating the service-linked roles required in the member accounts of the AWS organization.
Type: [StatusReason](API_StatusReason.md) object
Required: No

 ** tags **   <a name="accessanalyzer-Type-AnalyzerSummary-tags"></a>
An array of key-value pairs applied to the analyzer. The key-value pairs consist of the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.
The tag key is a value that is 1 to 128 characters in length and cannot be prefixed with `aws:`.
The tag value is a value that is 0 to 256 characters in length.
Type: String to string map
Required: No

## See Also
<a name="API_AnalyzerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
