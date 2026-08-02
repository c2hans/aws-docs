---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_DatasourcePackageIngestDetail.html
---

# DatasourcePackageIngestDetail
<a name="API_DatasourcePackageIngestDetail"></a>

Details about the data source packages ingested by your behavior graph.

## Contents
<a name="API_DatasourcePackageIngestDetail_Contents"></a>

 ** DatasourcePackageIngestState **   <a name="detective-Type-DatasourcePackageIngestDetail-DatasourcePackageIngestState"></a>
Details on which data source packages are ingested for a member account.
Type: String
Valid Values: `STARTED | STOPPED | DISABLED`
Required: No

 ** LastIngestStateChange **   <a name="detective-Type-DatasourcePackageIngestDetail-LastIngestStateChange"></a>
The date a data source package was enabled for this account
Type: String to [TimestampForCollection](API_TimestampForCollection.md) object map
Valid Keys: `STARTED | STOPPED | DISABLED`
Required: No

## See Also
<a name="API_DatasourcePackageIngestDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/DatasourcePackageIngestDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/DatasourcePackageIngestDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/DatasourcePackageIngestDetail)
