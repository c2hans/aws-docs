---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DataTransferApi.html
---

# DataTransferApi
<a name="API_DataTransferApi"></a>

The API of the connector application that Amazon AppFlow uses to transfer your data.

## Contents
<a name="API_DataTransferApi_Contents"></a>

 ** Name **   <a name="appflow-Type-DataTransferApi-Name"></a>
The name of the connector application API.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\w/-]+`
Required: No

 ** Type **   <a name="appflow-Type-DataTransferApi-Type"></a>
You can specify one of the following types:
AUTOMATIC
The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.
SYNC
A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.
ASYNC
An asynchronous API. This type of API optimizes a flow for large datasets.
Type: String
Valid Values: `SYNC | ASYNC | AUTOMATIC`
Required: No

## See Also
<a name="API_DataTransferApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DataTransferApi)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DataTransferApi)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DataTransferApi)
