---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SalesforceDestinationProperties.html
---

# SalesforceDestinationProperties
<a name="API_SalesforceDestinationProperties"></a>

 The properties that are applied when Salesforce is being used as a destination.

## Contents
<a name="API_SalesforceDestinationProperties_Contents"></a>

 ** object **   <a name="appflow-Type-SalesforceDestinationProperties-object"></a>
 The object specified in the Salesforce flow destination.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** dataTransferApi **   <a name="appflow-Type-SalesforceDestinationProperties-dataTransferApi"></a>
Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data to Salesforce.
AUTOMATIC
The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers to Salesforce. If your flow transfers fewer than 1,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.
Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900 records, and it might use Bulk API 2.0 on the next day to transfer 1,100 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.
By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.
BULKV2
Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.
Note that Bulk API 2.0 does not transfer Salesforce compound fields.
REST\_SYNC
Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail with a timed out error.
Type: String
Valid Values: `AUTOMATIC | BULKV2 | REST_SYNC`
Required: No

 ** errorHandlingConfig **   <a name="appflow-Type-SalesforceDestinationProperties-errorHandlingConfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the Salesforce destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

 ** idFieldNames **   <a name="appflow-Type-SalesforceDestinationProperties-idFieldNames"></a>
 The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update or delete.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** writeOperationType **   <a name="appflow-Type-SalesforceDestinationProperties-writeOperationType"></a>
 This specifies the type of write operation to be performed in Salesforce. When the value is `UPSERT`, then `idFieldNames` is required.
Type: String
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_SalesforceDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SalesforceDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SalesforceDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SalesforceDestinationProperties)
