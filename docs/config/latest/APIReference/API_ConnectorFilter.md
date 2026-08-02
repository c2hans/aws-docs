---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConnectorFilter.html
---

# ConnectorFilter
<a name="API_ConnectorFilter"></a>

Filters connectors based on the connector provider.

## Contents
<a name="API_ConnectorFilter_Contents"></a>

 ** filterName **   <a name="config-Type-ConnectorFilter-filterName"></a>
The name of the filter. Currently, only `provider` is supported.
Type: String
Valid Values: `provider`
Required: No

 ** filterValues **   <a name="config-Type-ConnectorFilter-filterValues"></a>
The value of the filter. For `provider`, valid values include: `AZURE`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ConnectorFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConnectorFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConnectorFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConnectorFilter)
