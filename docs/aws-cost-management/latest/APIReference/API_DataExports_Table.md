---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Table.html
---

# Table
<a name="API_DataExports_Table"></a>

The details for the data export table.

## Contents
<a name="API_DataExports_Table_Contents"></a>

 ** Description **   <a name="awscostmanagement-Type-DataExports_Table-Description"></a>
The description for the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TableName **   <a name="awscostmanagement-Type-DataExports_Table-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** TableProperties **   <a name="awscostmanagement-Type-DataExports_Table-TableProperties"></a>
The properties for the table.
Type: Array of [TablePropertyDescription](API_DataExports_TablePropertyDescription.md) objects
Required: No

## See Also
<a name="API_DataExports_Table_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/Table)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/Table)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/Table)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
