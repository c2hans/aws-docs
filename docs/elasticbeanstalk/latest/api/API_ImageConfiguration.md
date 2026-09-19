---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ImageConfiguration.html
---

# ImageConfiguration
<a name="API_ImageConfiguration"></a>

The source of the container image for an application version: an image that you built and pushed to a container registry yourself, or settings for Elastic Beanstalk to build one from your source bundle.

## Contents
<a name="API_ImageConfiguration_Contents"></a>

 ** Build **
Settings that Elastic Beanstalk uses to build a container image from the source bundle of the application version.
If you specify `Build`, also specify the request's `SourceBundle` parameter, and don't specify `Source`.
Type: [ImageBuildConfiguration](API_ImageBuildConfiguration.md) object
Required: No

 ** Source **
The location of a container image that you built and pushed to a container registry yourself. Elastic Beanstalk deploys the image without a build step.
If you specify `Source`, don't specify `Build` or the request's `SourceBundle` parameter.
Type: [ImageSource](API_ImageSource.md) object
Required: No

## See Also
<a name="API_ImageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ImageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ImageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ImageConfiguration)
