---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationSortCriteria.html
---

# InvestigationSortCriteria
<a name="API_InvestigationSortCriteria"></a>

Contains information about the criteria used for sorting investigations.

## Contents
<a name="API_InvestigationSortCriteria_Contents"></a>

 ** attributeName **   <a name="guardduty-Type-InvestigationSortCriteria-attributeName"></a>
The attribute by which to sort investigations.
Type: String
Valid Values: `START_TIME | END_TIME | STATUS | RISK_LEVEL | CONFIDENCE`
Required: No

 ** orderBy **   <a name="guardduty-Type-InvestigationSortCriteria-orderBy"></a>
The order in which the sorted results are to be displayed.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_InvestigationSortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationSortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationSortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationSortCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
