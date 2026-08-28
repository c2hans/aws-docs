---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_PhysicalTable.html
---

# PhysicalTable
<a name="API_PhysicalTable"></a>

A view of a data source that contains information about the shape of the data in the underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_PhysicalTable_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CustomSql **   <a name="QS-Type-PhysicalTable-CustomSql"></a>
A physical table type built from the results of the custom SQL query.
Type: [CustomSql](API_CustomSql.md) object
Required: No

 ** FileSource **   <a name="QS-Type-PhysicalTable-FileSource"></a>
A physical table type for a file data source.
Type: [FileSource](API_FileSource.md) object
Required: No

 ** RelationalTable **   <a name="QS-Type-PhysicalTable-RelationalTable"></a>
A physical table type for relational data sources.
Type: [RelationalTable](API_RelationalTable.md) object
Required: No

 ** S3Source **   <a name="QS-Type-PhysicalTable-S3Source"></a>
A physical table type for an S3 data source.
Type: [S3Source](API_S3Source.md) object
Required: No

 ** SaaSTable **   <a name="QS-Type-PhysicalTable-SaaSTable"></a>
A physical table type for Software-as-a-Service (SaaS) sources.
Type: [SaaSTable](API_SaaSTable.md) object
Required: No

## See Also
<a name="API_PhysicalTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/PhysicalTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/PhysicalTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/PhysicalTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
