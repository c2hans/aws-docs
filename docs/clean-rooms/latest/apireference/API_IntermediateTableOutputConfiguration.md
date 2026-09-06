---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IntermediateTableOutputConfiguration.html
---

# IntermediateTableOutputConfiguration
<a name="API_IntermediateTableOutputConfiguration"></a>

Contains the output configuration of an intermediate table when a protected query populates it.

## Contents
<a name="API_IntermediateTableOutputConfiguration_Contents"></a>

 ** arn **   <a name="API-Type-IntermediateTableOutputConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the intermediate table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership\/[\d\w-]+\/intermediatetable\/[\d\w-]+`
Required: Yes

 ** id **   <a name="API-Type-IntermediateTableOutputConfiguration-id"></a>
The unique identifier of the intermediate table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-IntermediateTableOutputConfiguration-name"></a>
The name of the intermediate table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_IntermediateTableOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IntermediateTableOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IntermediateTableOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IntermediateTableOutputConfiguration)
