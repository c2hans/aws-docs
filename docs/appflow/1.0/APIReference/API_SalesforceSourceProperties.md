---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SalesforceSourceProperties.html
---

# SalesforceSourceProperties
<a name="API_SalesforceSourceProperties"></a>

 The properties that are applied when Salesforce is being used as a source.

## Contents
<a name="API_SalesforceSourceProperties_Contents"></a>

 ** object **   <a name="appflow-Type-SalesforceSourceProperties-object"></a>
 The object specified in the Salesforce flow source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** dataTransferApi **   <a name="appflow-Type-SalesforceSourceProperties-dataTransferApi"></a>
Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data from Salesforce.
AUTOMATIC
The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers from Salesforce. If your flow transfers fewer than 1,000,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.
Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900,000 records, and it might use Bulk API 2.0 on the next day to transfer 1,100,000 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.
By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.
BULKV2
Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.
Note that Bulk API 2.0 does not transfer Salesforce compound fields.
REST\_SYNC
Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail wituh a timed out error.
Type: String
Valid Values: `AUTOMATIC | BULKV2 | REST_SYNC`
Required: No

 ** enableDynamicFieldUpdate **   <a name="appflow-Type-SalesforceSourceProperties-enableDynamicFieldUpdate"></a>
 The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.
Type: Boolean
Required: No

 ** includeDeletedRecords **   <a name="appflow-Type-SalesforceSourceProperties-includeDeletedRecords"></a>
 Indicates whether Amazon AppFlow includes deleted files in the flow run.
Type: Boolean
Required: No

## See Also
<a name="API_SalesforceSourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SalesforceSourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SalesforceSourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SalesforceSourceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
