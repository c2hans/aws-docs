---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CrossRegionS3RestoreSourcesAccess.html
---

# CrossRegionS3RestoreSourcesAccess
<a name="API_CrossRegionS3RestoreSourcesAccess"></a>

The configuration access for the cross-Region Amazon S3 database restore source for the ODB network.

## Contents
<a name="API_CrossRegionS3RestoreSourcesAccess_Contents"></a>

 ** ipv4Addresses **   <a name="odb-Type-CrossRegionS3RestoreSourcesAccess-ipv4Addresses"></a>
The IPv4 addresses allowed for cross-Region Amazon S3 restore access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** region **   <a name="odb-Type-CrossRegionS3RestoreSourcesAccess-region"></a>
The AWS Region for cross-Region Amazon S3 restore access.
Type: String
Required: No

 ** status **   <a name="odb-Type-CrossRegionS3RestoreSourcesAccess-status"></a>
The current status of the cross-Region Amazon S3 restore access configuration.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: No

## See Also
<a name="API_CrossRegionS3RestoreSourcesAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CrossRegionS3RestoreSourcesAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CrossRegionS3RestoreSourcesAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CrossRegionS3RestoreSourcesAccess)
