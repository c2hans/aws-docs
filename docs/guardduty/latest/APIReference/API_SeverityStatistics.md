---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SeverityStatistics.html
---

# SeverityStatistics
<a name="API_SeverityStatistics"></a>

Information about severity level for each finding type.

## Contents
<a name="API_SeverityStatistics_Contents"></a>

 ** lastGeneratedAt **   <a name="guardduty-Type-SeverityStatistics-lastGeneratedAt"></a>
The timestamp at which a finding type for a specific severity was last generated.
Type: Timestamp
Required: No

 ** severity **   <a name="guardduty-Type-SeverityStatistics-severity"></a>
The severity level associated with each finding type.
Type: Double
Required: No

 ** totalFindings **   <a name="guardduty-Type-SeverityStatistics-totalFindings"></a>
The total number of findings associated with this severity.
Type: Integer
Required: No

## See Also
<a name="API_SeverityStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/SeverityStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/SeverityStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/SeverityStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
