---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyDefinitionRequest.html
---

# PropertyDefinitionRequest
<a name="API_PropertyDefinitionRequest"></a>

An object that sets information about a property.

## Contents
<a name="API_PropertyDefinitionRequest_Contents"></a>

 ** configuration **   <a name="tm-Type-PropertyDefinitionRequest-configuration"></a>
A mapping that specifies configuration information about the property. Use this field to specify information that you read from and write to an external source.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Value Pattern: `.*`
Required: No

 ** dataType **   <a name="tm-Type-PropertyDefinitionRequest-dataType"></a>
An object that contains information about the data type.
Type: [DataType](API_DataType.md) object
Required: No

 ** defaultValue **   <a name="tm-Type-PropertyDefinitionRequest-defaultValue"></a>
An object that contains the default value.
Type: [DataValue](API_DataValue.md) object
Required: No

 ** displayName **   <a name="tm-Type-PropertyDefinitionRequest-displayName"></a>
A friendly name for the property.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*[^\u0000-\u001F\u007F]*.*`
Required: No

 ** isExternalId **   <a name="tm-Type-PropertyDefinitionRequest-isExternalId"></a>
A Boolean value that specifies whether the property ID comes from an external data store.
Type: Boolean
Required: No

 ** isRequiredInEntity **   <a name="tm-Type-PropertyDefinitionRequest-isRequiredInEntity"></a>
A Boolean value that specifies whether the property is required.
Type: Boolean
Required: No

 ** isStoredExternally **   <a name="tm-Type-PropertyDefinitionRequest-isStoredExternally"></a>
A Boolean value that specifies whether the property is stored externally.
Type: Boolean
Required: No

 ** isTimeSeries **   <a name="tm-Type-PropertyDefinitionRequest-isTimeSeries"></a>
A Boolean value that specifies whether the property consists of time series data.
Type: Boolean
Required: No

## See Also
<a name="API_PropertyDefinitionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/PropertyDefinitionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/PropertyDefinitionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/PropertyDefinitionRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
