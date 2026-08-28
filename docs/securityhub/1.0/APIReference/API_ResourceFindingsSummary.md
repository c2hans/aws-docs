---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceFindingsSummary.html
---

# ResourceFindingsSummary
<a name="API_ResourceFindingsSummary"></a>

A list of summaries for all finding types on a resource.

## Contents
<a name="API_ResourceFindingsSummary_Contents"></a>

 ** FindingType **   <a name="securityhub-Type-ResourceFindingsSummary-FindingType"></a>
The category or classification of the security finding.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ProductName **   <a name="securityhub-Type-ResourceFindingsSummary-ProductName"></a>
The name of the product associated with the security finding.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** TotalFindings **   <a name="securityhub-Type-ResourceFindingsSummary-TotalFindings"></a>
The total count of security findings.
Type: Integer
Required: Yes

 ** Severities **   <a name="securityhub-Type-ResourceFindingsSummary-Severities"></a>
A breakdown of security findings by their severity levels.
Type: [ResourceSeverityBreakdown](API_ResourceSeverityBreakdown.md) object
Required: No

## See Also
<a name="API_ResourceFindingsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceFindingsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceFindingsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceFindingsSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
