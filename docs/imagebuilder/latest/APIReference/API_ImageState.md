---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageState.html
---

# ImageState
<a name="API_ImageState"></a>

Image status and the reason for that status.

## Contents
<a name="API_ImageState_Contents"></a>

 ** failureContext **   <a name="imagebuilder-Type-ImageState-failureContext"></a>
The details about the failure, for images that failed to complete. Image Builder only sets this property when the image status is `FAILED`.
Type: [ImageFailureContext](API_ImageFailureContext.md) object
Required: No

 ** reason **   <a name="imagebuilder-Type-ImageState-reason"></a>
The reason for the status of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** status **   <a name="imagebuilder-Type-ImageState-status"></a>
The status of the image. A new image moves through build, test, and distribution statuses during creation, and ends in the `AVAILABLE`, `FAILED`, or `CANCELLED` state. The `DEPRECATED`, `DISABLED`, and `DELETED` statuses come from later resource management actions.
Type: String
Valid Values: `PENDING | CREATING | BUILDING | TESTING | DISTRIBUTING | INTEGRATING | AVAILABLE | CANCELLED | FAILED | DEPRECATED | DELETED | DISABLED`
Required: No

## See Also
<a name="API_ImageState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageState)
