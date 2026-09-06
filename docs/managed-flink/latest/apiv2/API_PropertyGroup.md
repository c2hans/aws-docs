---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_PropertyGroup.html
---

# PropertyGroup
<a name="API_PropertyGroup"></a>

Property key-value pairs passed into an application.

## Contents
<a name="API_PropertyGroup_Contents"></a>

 ** PropertyGroupId **   <a name="APIReference-Type-PropertyGroup-PropertyGroupId"></a>
Describes the key of an application execution property key-value pair.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** PropertyMap **   <a name="APIReference-Type-PropertyGroup-PropertyMap"></a>
Describes the value of an application execution property key-value pair.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_PropertyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/PropertyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/PropertyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/PropertyGroup)
