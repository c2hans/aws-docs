---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SourceEndpointFilter.html
---

# SourceEndpointFilter
<a name="API_SourceEndpointFilter"></a>

A filter to apply when listing source endpoints. This is a union type, so exactly one of its members is set.

## Contents
<a name="API_SourceEndpointFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** nameContains **   <a name="mediaconnect-Type-SourceEndpointFilter-nameContains"></a>
Filters the results to source endpoints whose names contain the specified strings.
Type: Array of strings
Required: No

 ** regionNames **   <a name="mediaconnect-Type-SourceEndpointFilter-regionNames"></a>
Filters the results to source endpoints in the specified AWS Regions.
Type: Array of strings
Required: No

 ** sourceTypes **   <a name="mediaconnect-Type-SourceEndpointFilter-sourceTypes"></a>
Filters the results to source endpoints of the specified types.
Type: Array of strings
Valid Values: `STANDARD | ROUTER_OUTPUT`
Required: No

## See Also
<a name="API_SourceEndpointFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SourceEndpointFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SourceEndpointFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SourceEndpointFilter)
