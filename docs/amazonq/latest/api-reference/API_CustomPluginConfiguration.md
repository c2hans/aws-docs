---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CustomPluginConfiguration.html
---

# CustomPluginConfiguration
<a name="API_CustomPluginConfiguration"></a>

 Configuration information required to create a custom plugin.

## Contents
<a name="API_CustomPluginConfiguration_Contents"></a>

 ** apiSchemaType **   <a name="qbusiness-Type-CustomPluginConfiguration-apiSchemaType"></a>
The type of OpenAPI schema to use.
Type: String
Valid Values: `OPEN_API_V3`
Required: Yes

 ** description **   <a name="qbusiness-Type-CustomPluginConfiguration-description"></a>
A description for your custom plugin configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** apiSchema **   <a name="qbusiness-Type-CustomPluginConfiguration-apiSchema"></a>
Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.
Type: [APISchema](API_APISchema.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_CustomPluginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CustomPluginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CustomPluginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CustomPluginConfiguration)
