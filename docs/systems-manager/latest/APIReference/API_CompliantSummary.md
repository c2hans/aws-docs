---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CompliantSummary.html
---

# CompliantSummary
<a name="API_CompliantSummary"></a>

A summary of resources that are compliant. The summary is organized according to the resource count for each compliance type.

## Contents
<a name="API_CompliantSummary_Contents"></a>

 ** CompliantCount **   <a name="systemsmanager-Type-CompliantSummary-CompliantCount"></a>
The total number of resources that are compliant.
Type: Integer
Required: No

 ** SeveritySummary **   <a name="systemsmanager-Type-CompliantSummary-SeveritySummary"></a>
A summary of the compliance severity by compliance type.
Type: [SeveritySummary](API_SeveritySummary.md) object
Required: No

## See Also
<a name="API_CompliantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CompliantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CompliantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CompliantSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
