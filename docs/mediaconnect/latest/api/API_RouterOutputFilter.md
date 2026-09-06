---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterOutputFilter.html
---

# RouterOutputFilter
<a name="API_RouterOutputFilter"></a>

A filter that can be used to retrieve a list of router outputs.

## Contents
<a name="API_RouterOutputFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** nameContains **   <a name="mediaconnect-Type-RouterOutputFilter-nameContains"></a>
The names of the router outputs to include in the filter.
Type: Array of strings
Required: No

 ** networkInterfaceArns **   <a name="mediaconnect-Type-RouterOutputFilter-networkInterfaceArns"></a>
The Amazon Resource Names (ARNs) of the network interfaces associated with the router outputs to include in the filter.
Type: Array of strings
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: No

 ** outputTypes **   <a name="mediaconnect-Type-RouterOutputFilter-outputTypes"></a>
The types of router outputs to include in the filter.
Type: Array of strings
Valid Values: `STANDARD | MEDIACONNECT_FLOW | MEDIALIVE_INPUT`
Required: No

 ** regionNames **   <a name="mediaconnect-Type-RouterOutputFilter-regionNames"></a>
The AWS Regions of the router outputs to include in the filter.
Type: Array of strings
Required: No

 ** routedInputArns **   <a name="mediaconnect-Type-RouterOutputFilter-routedInputArns"></a>
The ARNs of the router inputs associated with the router outputs to include in the filter.
Type: Array of strings
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: No

 ** routingScopes **   <a name="mediaconnect-Type-RouterOutputFilter-routingScopes"></a>
Filter criteria to list router outputs based on their routing scope.
Type: Array of strings
Valid Values: `REGIONAL | GLOBAL`
Required: No

## See Also
<a name="API_RouterOutputFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterOutputFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterOutputFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterOutputFilter)
