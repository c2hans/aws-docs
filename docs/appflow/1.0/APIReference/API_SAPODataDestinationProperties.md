---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SAPODataDestinationProperties.html
---

# SAPODataDestinationProperties
<a name="API_SAPODataDestinationProperties"></a>

The properties that are applied when using SAPOData as a flow destination

## Contents
<a name="API_SAPODataDestinationProperties_Contents"></a>

 ** objectPath **   <a name="appflow-Type-SAPODataDestinationProperties-objectPath"></a>
The object path specified in the SAPOData flow destination.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** errorHandlingConfig **   <a name="appflow-Type-SAPODataDestinationProperties-errorHandlingConfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

 ** idFieldNames **   <a name="appflow-Type-SAPODataDestinationProperties-idFieldNames"></a>
 A list of field names that can be used as an ID field when performing a write operation.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** successResponseHandlingConfig **   <a name="appflow-Type-SAPODataDestinationProperties-successResponseHandlingConfig"></a>
Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.
For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.
Type: [SuccessResponseHandlingConfig](API_SuccessResponseHandlingConfig.md) object
Required: No

 ** writeOperationType **   <a name="appflow-Type-SAPODataDestinationProperties-writeOperationType"></a>
 The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.
Type: String
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_SAPODataDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SAPODataDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SAPODataDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SAPODataDestinationProperties)
