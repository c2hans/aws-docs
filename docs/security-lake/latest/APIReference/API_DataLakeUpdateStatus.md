---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeUpdateStatus.html
---

# DataLakeUpdateStatus
<a name="API_DataLakeUpdateStatus"></a>

The status of the last `UpdateDataLake` or `DeleteDataLake` API request. This is set to Completed after the configuration is updated, or removed if deletion of the data lake is successful.

## Contents
<a name="API_DataLakeUpdateStatus_Contents"></a>

 ** exception **   <a name="securitylake-Type-DataLakeUpdateStatus-exception"></a>
The details of the last `UpdateDataLake`or `DeleteDataLake` API request which failed.
Type: [DataLakeUpdateException](API_DataLakeUpdateException.md) object
Required: No

 ** requestId **   <a name="securitylake-Type-DataLakeUpdateStatus-requestId"></a>
The unique ID for the last `UpdateDataLake` or `DeleteDataLake` API request.
Type: String
Required: No

 ** status **   <a name="securitylake-Type-DataLakeUpdateStatus-status"></a>
The status of the last `UpdateDataLake` or `DeleteDataLake` API request that was requested.
Type: String
Valid Values: `INITIALIZED | PENDING | COMPLETED | FAILED`
Required: No

## See Also
<a name="API_DataLakeUpdateStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeUpdateStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeUpdateStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeUpdateStatus)
