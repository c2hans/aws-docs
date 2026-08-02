---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DocumentParameter.html
---

# DocumentParameter
<a name="API_DocumentParameter"></a>

A map of key-value pairs containing the patterns that need to be replaced in a managed template job document schema. You can use the description of each key as a guidance to specify the inputs during runtime when creating a job.

**Note**
 `documentParameters` can only be used when creating jobs from AWS managed templates. This parameter can't be used with custom job templates or to create jobs from them.

## Contents
<a name="API_DocumentParameter_Contents"></a>

 ** description **   <a name="iot-Type-DocumentParameter-description"></a>
Description of the map field containing the patterns that need to be replaced in a managed template job document schema.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** example **   <a name="iot-Type-DocumentParameter-example"></a>
An example illustrating a pattern that need to be replaced in a managed template job document schema.
Type: String
Pattern: `[^\p{C}]+`
Required: No

 ** key **   <a name="iot-Type-DocumentParameter-key"></a>
Key of the map field containing the patterns that need to be replaced in a managed template job document schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** optional **   <a name="iot-Type-DocumentParameter-optional"></a>
Specifies whether a pattern that needs to be replaced in a managed template job document schema is optional or required.
Type: Boolean
Required: No

 ** regex **   <a name="iot-Type-DocumentParameter-regex"></a>
A regular expression of the patterns that need to be replaced in a managed template job document schema.
Type: String
Required: No

## See Also
<a name="API_DocumentParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DocumentParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DocumentParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DocumentParameter)
