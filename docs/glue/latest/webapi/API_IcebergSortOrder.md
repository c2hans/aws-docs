---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergSortOrder.html
---

# IcebergSortOrder
<a name="API_IcebergSortOrder"></a>

Defines the sort order specification for an Iceberg table, determining how data should be ordered within partitions to optimize query performance.

## Contents
<a name="API_IcebergSortOrder_Contents"></a>

 ** Fields **   <a name="Glue-Type-IcebergSortOrder-Fields"></a>
The list of fields and their sort directions that define the ordering criteria for the Iceberg table data.
Type: Array of [IcebergSortField](API_IcebergSortField.md) objects
Required: Yes

 ** OrderId **   <a name="Glue-Type-IcebergSortOrder-OrderId"></a>
The unique identifier for this sort order specification within the Iceberg table's metadata.
Type: Integer
Required: Yes

## See Also
<a name="API_IcebergSortOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergSortOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergSortOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergSortOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
