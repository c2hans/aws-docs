---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageSummary.html
---

# ImageSummary
<a name="API_ImageSummary"></a>

An image summary.

## Contents
<a name="API_ImageSummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ImageSummary-arn"></a>
The Amazon Resource Name (ARN) of the image.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** buildType **   <a name="imagebuilder-Type-ImageSummary-buildType"></a>
Indicates the type of build that created this image. The build can be initiated in the following ways:
+  **USER\_INITIATED** – A manual pipeline build request.
+  **SCHEDULED** – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.
+  **IMPORT** – A VM import created the image to use as the base image for the recipe.
+  **IMPORT\_ISO** – An ISO disk import created the image.
Type: String
Valid Values: `USER_INITIATED | SCHEDULED | IMPORT | IMPORT_ISO`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ImageSummary-dateCreated"></a>
The date on which Image Builder created this image.
Type: String
Required: No

 ** deprecationTime **   <a name="imagebuilder-Type-ImageSummary-deprecationTime"></a>
The time when deprecation occurs for an image resource. This can be a past or future date.
Type: Timestamp
Required: No

 ** imageSource **   <a name="imagebuilder-Type-ImageSummary-imageSource"></a>
The origin of the base image that Image Builder used to build this image.
Type: String
Valid Values: `AMAZON_MANAGED | AWS_MARKETPLACE | IMPORTED | CUSTOM`
Required: No

 ** lifecycleExecutionId **   <a name="imagebuilder-Type-ImageSummary-lifecycleExecutionId"></a>
Identifies the last runtime instance of the lifecycle policy to take action on the image.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** loggingConfiguration **   <a name="imagebuilder-Type-ImageSummary-loggingConfiguration"></a>
The logging configuration that's defined for the image.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** name **   <a name="imagebuilder-Type-ImageSummary-name"></a>
The name of the image.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** osVersion **   <a name="imagebuilder-Type-ImageSummary-osVersion"></a>
The operating system version of the instances that launch from this image. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** outputResources **   <a name="imagebuilder-Type-ImageSummary-outputResources"></a>
The output resources that Image Builder produced when it created this image.
Type: [OutputResources](API_OutputResources.md) object
Required: No

 ** owner **   <a name="imagebuilder-Type-ImageSummary-owner"></a>
The owner of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ImageSummary-platform"></a>
The image operating system platform, such as Linux or Windows.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** state **   <a name="imagebuilder-Type-ImageSummary-state"></a>
The state of the image.
Type: [ImageState](API_ImageState.md) object
Required: No

 ** tags **   <a name="imagebuilder-Type-ImageSummary-tags"></a>
The tags that apply to this image.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-ImageSummary-type"></a>
Specifies whether this image produces an AMI or a container image.
Type: String
Valid Values: `AMI | DOCKER`
Required: No

 ** version **   <a name="imagebuilder-Type-ImageSummary-version"></a>
The version of the image.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+(?:/[0-9]+)?$`
Required: No

## See Also
<a name="API_ImageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageSummary)
