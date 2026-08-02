---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ZendeskDestinationProperties.html
---

# ZendeskDestinationProperties
<a name="API_ZendeskDestinationProperties"></a>

The properties that are applied when Zendesk is used as a destination.

## Contents
<a name="API_ZendeskDestinationProperties_Contents"></a>

 ** object **   <a name="appflow-Type-ZendeskDestinationProperties-object"></a>
The object specified in the Zendesk flow destination.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** errorHandlingConfig **   <a name="appflow-Type-ZendeskDestinationProperties-errorHandlingConfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

 ** idFieldNames **   <a name="appflow-Type-ZendeskDestinationProperties-idFieldNames"></a>
 A list of field names that can be used as an ID field when performing a write operation.
Type: Array of strings
Array Members: Minimum number of 0 items.
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** writeOperationType **   <a name="appflow-Type-ZendeskDestinationProperties-writeOperationType"></a>
 The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.
Type: String
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_ZendeskDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ZendeskDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ZendeskDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ZendeskDestinationProperties)
