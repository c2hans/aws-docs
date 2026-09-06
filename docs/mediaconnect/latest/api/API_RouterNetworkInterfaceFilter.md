---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterNetworkInterfaceFilter.html
---

# RouterNetworkInterfaceFilter
<a name="API_RouterNetworkInterfaceFilter"></a>

A filter that can be used to retrieve a list of router network interfaces.

## Contents
<a name="API_RouterNetworkInterfaceFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** nameContains **   <a name="mediaconnect-Type-RouterNetworkInterfaceFilter-nameContains"></a>
The names of the router network interfaces to include in the filter.
Type: Array of strings
Required: No

 ** networkInterfaceTypes **   <a name="mediaconnect-Type-RouterNetworkInterfaceFilter-networkInterfaceTypes"></a>
The types of router network interfaces to include in the filter.
Type: Array of strings
Valid Values: `PUBLIC | VPC`
Required: No

 ** regionNames **   <a name="mediaconnect-Type-RouterNetworkInterfaceFilter-regionNames"></a>
The AWS Regions of the router network interfaces to include in the filter.
Type: Array of strings
Required: No

## See Also
<a name="API_RouterNetworkInterfaceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterNetworkInterfaceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterNetworkInterfaceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterNetworkInterfaceFilter)
