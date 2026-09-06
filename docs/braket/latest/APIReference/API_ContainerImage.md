---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_ContainerImage.html
---

# ContainerImage
<a name="API_ContainerImage"></a>

The container image used to create an Amazon Braket hybrid job.

## Contents
<a name="API_ContainerImage_Contents"></a>

 ** uri **   <a name="braket-Type-ContainerImage-uri"></a>
The URI locating the container image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\d{10,14}\.dkr\.ecr.[a-z0-9-]+\.amazonaws\.com\/.+(@sha256)?:.+`
Required: Yes

## See Also
<a name="API_ContainerImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/ContainerImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/ContainerImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/ContainerImage)
