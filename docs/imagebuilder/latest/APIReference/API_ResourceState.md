---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ResourceState.html
---

# ResourceState
<a name="API_ResourceState"></a>

The state to apply to the image resource in a resource state update request.

## Contents
<a name="API_ResourceState_Contents"></a>

 ** status **   <a name="imagebuilder-Type-ResourceState-status"></a>
The status to which you want to move the image resource. Set the status to `AVAILABLE` to restore an image that's currently deprecated or disabled.
Type: String
Valid Values: `AVAILABLE | DELETED | DEPRECATED | DISABLED`
Required: No

## See Also
<a name="API_ResourceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ResourceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ResourceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ResourceState)
