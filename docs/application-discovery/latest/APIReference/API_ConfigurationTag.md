---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ConfigurationTag.html
---

# ConfigurationTag
<a name="API_ConfigurationTag"></a>

Tags for a configuration item. Tags are metadata that help you categorize IT assets.

## Contents
<a name="API_ConfigurationTag_Contents"></a>

 ** configurationId **   <a name="DiscServ-Type-ConfigurationTag-configurationId"></a>
The configuration ID for the item to tag. You can specify a list of keys and values.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** configurationType **   <a name="DiscServ-Type-ConfigurationTag-configurationType"></a>
A type of IT asset to tag.
Type: String
Valid Values: `SERVER | PROCESS | CONNECTION | APPLICATION`
Required: No

 ** key **   <a name="DiscServ-Type-ConfigurationTag-key"></a>
A type of tag on which to filter. For example, *serverType*.
Type: String
Required: No

 ** timeOfCreation **   <a name="DiscServ-Type-ConfigurationTag-timeOfCreation"></a>
The time the configuration tag was created in Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** value **   <a name="DiscServ-Type-ConfigurationTag-value"></a>
A value on which to filter. For example *key = serverType* and *value = web server*.
Type: String
Required: No

## See Also
<a name="API_ConfigurationTag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ConfigurationTag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ConfigurationTag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ConfigurationTag)
