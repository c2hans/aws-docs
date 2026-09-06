---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html
---

# DataflowEndpoint
<a name="API_DataflowEndpoint"></a>

Information about a dataflow endpoint.

## Contents
<a name="API_DataflowEndpoint_Contents"></a>

 ** address **   <a name="groundstation-Type-DataflowEndpoint-address"></a>
Socket address of a dataflow endpoint.
Type: [SocketAddress](API_SocketAddress.md) object
Required: No

 ** mtu **   <a name="groundstation-Type-DataflowEndpoint-mtu"></a>
Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.
Type: Integer
Valid Range: Minimum value of 1400. Maximum value of 1500.
Required: No

 ** name **   <a name="groundstation-Type-DataflowEndpoint-name"></a>
Name of a dataflow endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[ a-zA-Z0-9_:-]{1,256}`
Required: No

 ** status **   <a name="groundstation-Type-DataflowEndpoint-status"></a>
Status of a dataflow endpoint.
Type: String
Valid Values: `created | creating | deleted | deleting | failed`
Required: No

## See Also
<a name="API_DataflowEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/DataflowEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/DataflowEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/DataflowEndpoint)
