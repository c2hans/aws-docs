---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_DatasourcePackageUsageInfo.html
---

# DatasourcePackageUsageInfo
<a name="API_DatasourcePackageUsageInfo"></a>

Information on the usage of a data source package in the behavior graph.

## Contents
<a name="API_DatasourcePackageUsageInfo_Contents"></a>

 ** VolumeUsageInBytes **   <a name="detective-Type-DatasourcePackageUsageInfo-VolumeUsageInBytes"></a>
Total volume of data in bytes per day ingested for a given data source package.
Type: Long
Required: No

 ** VolumeUsageUpdateTime **   <a name="detective-Type-DatasourcePackageUsageInfo-VolumeUsageUpdateTime"></a>
The data and time when the member account data volume was last updated. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

## See Also
<a name="API_DatasourcePackageUsageInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/DatasourcePackageUsageInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/DatasourcePackageUsageInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/DatasourcePackageUsageInfo)
