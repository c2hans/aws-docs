---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_AuditFinding.html
---

# AuditFinding
<a name="API_AuditFinding"></a>

A structure that contains information about an audit finding, which represents an automated analysis result about service behavior, performance issues, or potential problems identified through heuristic algorithms.

## Contents
<a name="API_AuditFinding_Contents"></a>

 ** KeyAttributes **   <a name="applicationsignals-Type-AuditFinding-KeyAttributes"></a>
The key attributes that identify the service or entity this audit finding relates to. This is a string-to-string map that includes fields like Type, Name, and Environment.
Type: String to string map
Map Entries: Maximum number of 4 items.
Key Pattern: `[a-zA-Z]{1,50}`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `[ -~]*[!-~]+[ -~]*`
Required: Yes

 ** AuditorResults **   <a name="applicationsignals-Type-AuditFinding-AuditorResults"></a>
An array of auditor results that contain the specific findings, descriptions, and severity levels identified by different auditing algorithms.
Type: Array of [AuditorResult](API_AuditorResult.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** DependencyGraph **   <a name="applicationsignals-Type-AuditFinding-DependencyGraph"></a>
A structure containing nodes and edges that represent the dependency relationships relevant to this audit finding, helping to understand the context and potential impact.
Type: [DependencyGraph](API_DependencyGraph.md) object
Required: No

 ** MetricGraph **   <a name="applicationsignals-Type-AuditFinding-MetricGraph"></a>
A structure containing metric data queries and time range information that provides context for the audit finding through relevant performance metrics.
Type: [MetricGraph](API_MetricGraph.md) object
Required: No

 ** Operation **   <a name="applicationsignals-Type-AuditFinding-Operation"></a>
The name of the operation associated with this audit finding, if the finding is specific to a particular service operation.
Type: String
Required: No

 ** Type **   <a name="applicationsignals-Type-AuditFinding-Type"></a>
The type of audit finding.
Type: String
Required: No

## See Also
<a name="API_AuditFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/AuditFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/AuditFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/AuditFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
