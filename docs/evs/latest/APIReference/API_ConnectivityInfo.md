---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ConnectivityInfo.html
---

# ConnectivityInfo
<a name="API_ConnectivityInfo"></a>

The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.

**Note**
Not supported when `vcfVersion` is `SELF_DEPLOYED`.

## Contents
<a name="API_ConnectivityInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** privateRouteServerPeerings **   <a name="evs-Type-ConnectivityInfo-privateRouteServerPeerings"></a>
The unique IDs for private route server peers.
Type: Array of strings
Array Members: Fixed number of 2 items.
Length Constraints: Minimum length of 3. Maximum length of 21.
Required: Yes

## See Also
<a name="API_ConnectivityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ConnectivityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ConnectivityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ConnectivityInfo)
