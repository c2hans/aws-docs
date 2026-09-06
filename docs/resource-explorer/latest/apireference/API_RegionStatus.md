---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_RegionStatus.html
---

# RegionStatus
<a name="API_RegionStatus"></a>

Contains information about the status of Resource Explorer configuration in a specific AWS Region.

## Contents
<a name="API_RegionStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Index **   <a name="resourceexplorer-Type-RegionStatus-Index"></a>
The status information for the Resource Explorer index in this Region.
Type: [IndexStatus](API_IndexStatus.md) object
Required: No

 ** Region **   <a name="resourceexplorer-Type-RegionStatus-Region"></a>
The AWS Region for which this status information applies.
Type: String
Pattern: `[a-z-]+-[a-z]+-[0-9]`
Required: No

 ** View **   <a name="resourceexplorer-Type-RegionStatus-View"></a>
The status information for the Resource Explorer view in this Region.
Type: [ViewStatus](API_ViewStatus.md) object
Required: No

## See Also
<a name="API_RegionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/RegionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/RegionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/RegionStatus)
