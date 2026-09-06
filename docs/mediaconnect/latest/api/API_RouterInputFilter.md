---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputFilter.html
---

# RouterInputFilter
<a name="API_RouterInputFilter"></a>

A filter that can be used to retrieve a list of router inputs.

## Contents
<a name="API_RouterInputFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inputTypes **   <a name="mediaconnect-Type-RouterInputFilter-inputTypes"></a>
The types of router inputs to include in the filter.
Type: Array of strings
Valid Values: `STANDARD | FAILOVER | MERGE | MEDIACONNECT_FLOW | MEDIALIVE_CHANNEL`
Required: No

 ** nameContains **   <a name="mediaconnect-Type-RouterInputFilter-nameContains"></a>
The names of the router inputs to include in the filter.
Type: Array of strings
Required: No

 ** networkInterfaceArns **   <a name="mediaconnect-Type-RouterInputFilter-networkInterfaceArns"></a>
The Amazon Resource Names (ARNs) of the network interfaces associated with the router inputs to include in the filter.
Type: Array of strings
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: No

 ** regionNames **   <a name="mediaconnect-Type-RouterInputFilter-regionNames"></a>
The AWS Regions of the router inputs to include in the filter.
Type: Array of strings
Required: No

 ** routingScopes **   <a name="mediaconnect-Type-RouterInputFilter-routingScopes"></a>
Filter criteria to list router inputs based on their routing scope (REGIONAL or GLOBAL).
Type: Array of strings
Valid Values: `REGIONAL | GLOBAL`
Required: No

## See Also
<a name="API_RouterInputFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputFilter)
