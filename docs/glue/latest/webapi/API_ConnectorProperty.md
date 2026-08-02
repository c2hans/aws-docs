---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorProperty.html
---

# ConnectorProperty
<a name="API_ConnectorProperty"></a>

Defines a property configuration for connection types, default values, and where the property should be used in requests.

## Contents
<a name="API_ConnectorProperty_Contents"></a>

 ** Name **   <a name="Glue-Type-ConnectorProperty-Name"></a>
The name of the property.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** PropertyType **   <a name="Glue-Type-ConnectorProperty-PropertyType"></a>
The data type of this property
Type: String
Valid Values: `USER_INPUT | SECRET | READ_ONLY | UNUSED | SECRET_OR_USER_INPUT`
Required: Yes

 ** Required **   <a name="Glue-Type-ConnectorProperty-Required"></a>
Indicates whether the property is required.
Type: Boolean
Required: Yes

 ** AllowedValues **   <a name="Glue-Type-ConnectorProperty-AllowedValues"></a>
A list of `AllowedValue` objects representing the values allowed for the property.
Type: Array of strings
Required: No

 ** DefaultValue **   <a name="Glue-Type-ConnectorProperty-DefaultValue"></a>
The default value for the property.
Type: String
Required: No

 ** KeyOverride **   <a name="Glue-Type-ConnectorProperty-KeyOverride"></a>
A key name to use when sending this property in API requests, if different from the display name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** PropertyLocation **   <a name="Glue-Type-ConnectorProperty-PropertyLocation"></a>
Specifies where this property should be included in REST requests, such as in headers, query parameters, or request body.
Type: String
Valid Values: `HEADER | BODY | QUERY_PARAM | PATH`
Required: No

## See Also
<a name="API_ConnectorProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorProperty)
