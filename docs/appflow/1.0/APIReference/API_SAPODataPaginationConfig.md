---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SAPODataPaginationConfig.html
---

# SAPODataPaginationConfig
<a name="API_SAPODataPaginationConfig"></a>

Sets the page size for each *concurrent process* that transfers OData records from your SAP instance. A concurrent process is query that retrieves a batch of records as part of a flow run. Amazon AppFlow can run multiple concurrent processes in parallel to transfer data faster.

## Contents
<a name="API_SAPODataPaginationConfig_Contents"></a>

 ** maxPageSize **   <a name="appflow-Type-SAPODataPaginationConfig-maxPageSize"></a>
The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application. For transfers of OData records, the maximum page size is 3,000. For transfers of data that comes from an ODP provider, the maximum page size is 10,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

## See Also
<a name="API_SAPODataPaginationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SAPODataPaginationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SAPODataPaginationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SAPODataPaginationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
