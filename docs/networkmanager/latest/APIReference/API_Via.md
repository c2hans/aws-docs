---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Via.html
---

# Via
<a name="API_Via"></a>

The list of network function groups and edge overrides for the service insertion action. Used for both the `send-to` and `send-via` actions.

## Contents
<a name="API_Via_Contents"></a>

 ** NetworkFunctionGroups **   <a name="networkmanager-Type-Via-NetworkFunctionGroups"></a>
The list of network function groups associated with the service insertion action.
Type: Array of [NetworkFunctionGroup](API_NetworkFunctionGroup.md) objects
Required: No

 ** WithEdgeOverrides **   <a name="networkmanager-Type-Via-WithEdgeOverrides"></a>
Describes any edge overrides. An edge override is a specific edge to be used for traffic.
Type: Array of [EdgeOverride](API_EdgeOverride.md) objects
Required: No

## See Also
<a name="API_Via_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Via)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Via)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Via)
