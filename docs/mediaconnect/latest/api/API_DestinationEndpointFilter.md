---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpointFilter.html
---

# DestinationEndpointFilter
<a name="API_DestinationEndpointFilter"></a>

A filter to apply when listing destination endpoints. This is a union type, so exactly one of its members is set.

## Contents
<a name="API_DestinationEndpointFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** destinationTypes **   <a name="mediaconnect-Type-DestinationEndpointFilter-destinationTypes"></a>
Filters the results to destination endpoints of the specified types.
Type: Array of strings
Valid Values: `STANDARD | ROUTER_INPUT`
Required: No

 ** nameContains **   <a name="mediaconnect-Type-DestinationEndpointFilter-nameContains"></a>
Filters the results to destination endpoints whose names contain the specified strings.
Type: Array of strings
Required: No

 ** regionNames **   <a name="mediaconnect-Type-DestinationEndpointFilter-regionNames"></a>
Filters the results to destination endpoints in the specified AWS Regions.
Type: Array of strings
Required: No

## See Also
<a name="API_DestinationEndpointFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpointFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpointFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpointFilter)
