---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ColumnClassificationDetails.html
---

# ColumnClassificationDetails
<a name="API_ColumnClassificationDetails"></a>

Contains classification information for data columns, including mappings that specify how columns should be handled during synthetic data generation and privacy analysis.

## Contents
<a name="API_ColumnClassificationDetails_Contents"></a>

 ** columnMapping **   <a name="API-Type-ColumnClassificationDetails-columnMapping"></a>
A mapping that defines the classification of data columns for synthetic data generation and specifies how each column should be handled during the privacy-preserving data synthesis process.
Type: Array of [SyntheticDataColumnProperties](API_SyntheticDataColumnProperties.md) objects
Array Members: Minimum number of 5 items.
Required: Yes

## See Also
<a name="API_ColumnClassificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ColumnClassificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ColumnClassificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ColumnClassificationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
