---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Batch.html
---

# Batch
<a name="API_connect-customer-profiles_Batch"></a>

Batch defines the boundaries for ingestion for each step in `APPFLOW_INTEGRATION` workflow. `APPFLOW_INTEGRATION` workflow splits ingestion based on these boundaries.

## Contents
<a name="API_connect-customer-profiles_Batch_Contents"></a>

 ** EndTime **   <a name="connect-Type-connect-customer-profiles_Batch-EndTime"></a>
End time of batch to split ingestion.
Type: Timestamp
Required: Yes

 ** StartTime **   <a name="connect-Type-connect-customer-profiles_Batch-StartTime"></a>
Start time of batch to split ingestion.
Type: Timestamp
Required: Yes

## See Also
<a name="API_connect-customer-profiles_Batch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Batch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Batch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Batch)
