---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceNetworksRequestFilters.html
---

# DescribeSourceNetworksRequestFilters
<a name="API_DescribeSourceNetworksRequestFilters"></a>

A set of filters by which to return Source Networks.

## Contents
<a name="API_DescribeSourceNetworksRequestFilters_Contents"></a>

 ** originAccountID **   <a name="drs-Type-DescribeSourceNetworksRequestFilters-originAccountID"></a>
Filter Source Networks by account ID containing the protected VPCs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** originRegion **   <a name="drs-Type-DescribeSourceNetworksRequestFilters-originRegion"></a>
Filter Source Networks by the region containing the protected VPCs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9]`
Required: No

 ** sourceNetworkIDs **   <a name="drs-Type-DescribeSourceNetworksRequestFilters-sourceNetworkIDs"></a>
An array of Source Network IDs that should be returned. An empty array means all Source Networks.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_DescribeSourceNetworksRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeSourceNetworksRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeSourceNetworksRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeSourceNetworksRequestFilters)
