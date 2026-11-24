---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_ClusterPeerFilter.html
---

# ClusterPeerFilter

A filter used to restrict the results of describe calls for Amazon FSx for NetApp ONTAP cluster peers.

## Contents
<a name="API_ClusterPeerFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-ClusterPeerFilter-Name"></a>
The name for this filter.
Type: String
Valid Values: `file-system-id`
Required: No

 ** Values **   <a name="FSx-Type-ClusterPeerFilter-Values"></a>
The values of the filter. These are all the values for any of the applied filters.
Type: Array of strings
Array Members: Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`
Required: No

## See Also
<a name="API_ClusterPeerFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/ClusterPeerFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/ClusterPeerFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/ClusterPeerFilter)
