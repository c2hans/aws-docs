---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html
---

# Configuration
<a name="API_Configuration"></a>

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

## Contents
<a name="API_Configuration_Contents"></a>

 ** classification **   <a name="emrserverless-Type-Configuration-classification"></a>
The classification within a configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** configurations **   <a name="emrserverless-Type-Configuration-configurations"></a>
A list of additional configurations to apply within a configuration object.
Type: Array of [Configuration](#API_Configuration) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** properties **   <a name="emrserverless-Type-Configuration-properties"></a>
A set of properties specified within a configuration classification.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/Configuration)
