---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnectorFilters.html
---

# GatewayConnectorFilters
<a name="API_GatewayConnectorFilters"></a>

The filters that determine which gateway ingress paths a connector applies to.

## Contents
<a name="API_GatewayConnectorFilters_Contents"></a>

 ** accessTypes **   <a name="ECS-Type-GatewayConnectorFilters-accessTypes"></a>
The access types of the gateway ingress paths that the connector applies to.
The access type can be one of the following values:
+  `PUBLIC` - The ingress path is publicly accessible.
+  `PRIVATE` - The ingress path is only accessible privately.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `PUBLIC | PRIVATE`
Required: No

## See Also
<a name="API_GatewayConnectorFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnectorFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnectorFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnectorFilters)
