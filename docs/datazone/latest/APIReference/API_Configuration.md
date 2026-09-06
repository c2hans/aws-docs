---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Configuration.html
---

# Configuration
<a name="API_Configuration"></a>

The configuration of a connection.

## Contents
<a name="API_Configuration_Contents"></a>

 ** classification **   <a name="datazone-Type-Configuration-classification"></a>
The classification of the connection configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[\w][\w\.\-\_]*`
Required: No

 ** properties **   <a name="datazone-Type-Configuration-properties"></a>
The properties of the connection configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Configuration)
