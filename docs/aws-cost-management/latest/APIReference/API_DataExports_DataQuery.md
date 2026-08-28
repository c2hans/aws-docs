---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_DataQuery.html
---

# DataQuery
<a name="API_DataExports_DataQuery"></a>

The SQL query of column selections and row filters from the data table you want.

## Contents
<a name="API_DataExports_DataQuery_Contents"></a>

 ** QueryStatement **   <a name="awscostmanagement-Type-DataExports_DataQuery-QueryStatement"></a>
The query statement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36000.
Pattern: `[\S\s]*`
Required: Yes

 ** TableConfigurations **   <a name="awscostmanagement-Type-DataExports_DataQuery-TableConfigurations"></a>
The table configuration.
Type: String to string to string map map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Value Length Constraints: Minimum length of 0. Maximum length of 16384.
Value Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_DataExports_DataQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/DataQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/DataQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/DataQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
