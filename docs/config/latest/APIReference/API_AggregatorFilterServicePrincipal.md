---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregatorFilterServicePrincipal.html
---

# AggregatorFilterServicePrincipal
<a name="API_AggregatorFilterServicePrincipal"></a>

An object to filter service-linked configuration recorders in an aggregator based on the linked AWS service.

## Contents
<a name="API_AggregatorFilterServicePrincipal_Contents"></a>

 ** Type **   <a name="config-Type-AggregatorFilterServicePrincipal-Type"></a>
The type of service principal filter to apply. `INCLUDE` specifies that the list of service principals in the `Value` field will be aggregated and no other service principals will be filtered.
Type: String
Valid Values: `INCLUDE`
Required: No

 ** Value **   <a name="config-Type-AggregatorFilterServicePrincipal-Value"></a>
Comma-separated list of service principals for the linked AWS services to filter your aggregated service-linked configuration recorders.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_AggregatorFilterServicePrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregatorFilterServicePrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregatorFilterServicePrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregatorFilterServicePrincipal)
