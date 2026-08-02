---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CustomConnectorSourceProperties.html
---

# CustomConnectorSourceProperties
<a name="API_CustomConnectorSourceProperties"></a>

The properties that are applied when the custom connector is being used as a source.

## Contents
<a name="API_CustomConnectorSourceProperties_Contents"></a>

 ** entityName **   <a name="appflow-Type-CustomConnectorSourceProperties-entityName"></a>
The entity specified in the custom connector as a source in the flow.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** customProperties **   <a name="appflow-Type-CustomConnectorSourceProperties-customProperties"></a>
Custom properties that are required to use the custom connector as a source.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `\S+`
Required: No

 ** dataTransferApi **   <a name="appflow-Type-CustomConnectorSourceProperties-dataTransferApi"></a>
The API of the connector application that Amazon AppFlow uses to transfer your data.
Type: [DataTransferApi](API_DataTransferApi.md) object
Required: No

## See Also
<a name="API_CustomConnectorSourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CustomConnectorSourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CustomConnectorSourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CustomConnectorSourceProperties)
