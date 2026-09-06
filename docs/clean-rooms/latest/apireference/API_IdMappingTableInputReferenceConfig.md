---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_IdMappingTableInputReferenceConfig.html
---

# IdMappingTableInputReferenceConfig
<a name="API_IdMappingTableInputReferenceConfig"></a>

Provides the input reference configuration for the ID mapping table.

## Contents
<a name="API_IdMappingTableInputReferenceConfig_Contents"></a>

 ** inputReferenceArn **   <a name="API-Type-IdMappingTableInputReferenceConfig-inputReferenceArn"></a>
The Amazon Resource Name (ARN) of the referenced resource in AWS Entity Resolution. Valid values are ID mapping workflow ARNs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(idmappingworkflow/.*)`
Required: Yes

 ** manageResourcePolicies **   <a name="API-Type-IdMappingTableInputReferenceConfig-manageResourcePolicies"></a>
When `TRUE`, AWS Clean Rooms manages permissions for the ID mapping table resource.
When `FALSE`, the resource owner manages permissions for the ID mapping table resource.
Type: Boolean
Required: Yes

## See Also
<a name="API_IdMappingTableInputReferenceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/IdMappingTableInputReferenceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/IdMappingTableInputReferenceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/IdMappingTableInputReferenceConfig)
