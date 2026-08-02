---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_PrefixConfig.html
---

# PrefixConfig
<a name="API_PrefixConfig"></a>

Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.

## Contents
<a name="API_PrefixConfig_Contents"></a>

 ** pathPrefixHierarchy **   <a name="appflow-Type-PrefixConfig-pathPrefixHierarchy"></a>
Specifies whether the destination file path includes either or both of the following elements:
EXECUTION\_ID
The ID that Amazon AppFlow assigns to the flow run.
SCHEMA\_VERSION
The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:
+ Source-to-destination field mappings
+ Field data types
+ Partition keys
Type: Array of strings
Valid Values: `EXECUTION_ID | SCHEMA_VERSION`
Required: No

 ** prefixFormat **   <a name="appflow-Type-PrefixConfig-prefixFormat"></a>
Determines the level of granularity for the date and time that's included in the prefix.
Type: String
Valid Values: `YEAR | MONTH | DAY | HOUR | MINUTE`
Required: No

 ** prefixType **   <a name="appflow-Type-PrefixConfig-prefixType"></a>
Determines the format of the prefix, and whether it applies to the file name, file path, or both.
Type: String
Valid Values: `FILENAME | PATH | PATH_AND_FILENAME`
Required: No

## See Also
<a name="API_PrefixConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/PrefixConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/PrefixConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/PrefixConfig)
