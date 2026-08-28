---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CoverageSortCriteria.html
---

# CoverageSortCriteria
<a name="API_CoverageSortCriteria"></a>

Information about the sorting criteria used in the coverage statistics.

## Contents
<a name="API_CoverageSortCriteria_Contents"></a>

 ** attributeName **   <a name="guardduty-Type-CoverageSortCriteria-attributeName"></a>
Represents the field name used to sort the coverage details.
Replace the enum value `CLUSTER_NAME` with `EKS_CLUSTER_NAME`. `CLUSTER_NAME` has been deprecated.
Type: String
Valid Values: `ACCOUNT_ID | COVERAGE_STATUS | ISSUE | ADDON_VERSION | UPDATED_AT | CLUSTER_NAME | EKS_CLUSTER_NAME | ECS_CLUSTER_NAME | INSTANCE_ID`
Required: No

 ** orderBy **   <a name="guardduty-Type-CoverageSortCriteria-orderBy"></a>
The order in which the sorted findings are to be displayed.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_CoverageSortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CoverageSortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CoverageSortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CoverageSortCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
