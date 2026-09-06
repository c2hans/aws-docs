---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ResourceMapping.html
---

# ResourceMapping
<a name="API_ResourceMapping"></a>

Specifies the current source of the resource and the destination of where it will be moved to.

## Contents
<a name="API_ResourceMapping_Contents"></a>

 ** Destination **
The destination stack `StackName` and `LogicalResourceId` for the resource being refactored.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: Yes

 ** Source **
The source stack `StackName` and `LogicalResourceId` for the resource being refactored.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: Yes

## See Also
<a name="API_ResourceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceMapping)
