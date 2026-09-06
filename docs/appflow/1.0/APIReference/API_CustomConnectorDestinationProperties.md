---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CustomConnectorDestinationProperties.html
---

# CustomConnectorDestinationProperties
<a name="API_CustomConnectorDestinationProperties"></a>

The properties that are applied when the custom connector is being used as a destination.

## Contents
<a name="API_CustomConnectorDestinationProperties_Contents"></a>

 ** entityName **   <a name="appflow-Type-CustomConnectorDestinationProperties-entityName"></a>
The entity specified in the custom connector as a destination in the flow.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** customProperties **   <a name="appflow-Type-CustomConnectorDestinationProperties-customProperties"></a>
The custom properties that are specific to the connector when it's used as a destination in the flow.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `\S+`
Required: No

 ** errorHandlingConfig **   <a name="appflow-Type-CustomConnectorDestinationProperties-errorHandlingConfig"></a>
The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

 ** idFieldNames **   <a name="appflow-Type-CustomConnectorDestinationProperties-idFieldNames"></a>
The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** writeOperationType **   <a name="appflow-Type-CustomConnectorDestinationProperties-writeOperationType"></a>
Specifies the type of write operation to be performed in the custom connector when it's used as destination.
Type: String
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_CustomConnectorDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/CustomConnectorDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/CustomConnectorDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/CustomConnectorDestinationProperties)
