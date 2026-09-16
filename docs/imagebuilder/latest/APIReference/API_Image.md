---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

An Image Builder image resource that keeps track of all of the settings used to create, configure, and distribute output for that image. You must specify exactly one recipe for the image – either a container recipe (`containerRecipe`), which creates a container image, or an image recipe (`imageRecipe`), which creates an AMI.

## Contents
<a name="API_Image_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-Image-arn"></a>
The Amazon Resource Name (ARN) of the image.
Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:

1. Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.

1. Version ARNs have only the first three nodes: <major>.<minor>.<patch>

1. Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** buildType **   <a name="imagebuilder-Type-Image-buildType"></a>
Indicates the type of build that created this image. The build can be initiated in the following ways:
+  **USER\_INITIATED** – A manual pipeline build request.
+  **SCHEDULED** – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.
+  **IMPORT** – A VM import created the image to use as the base image for the recipe.
+  **IMPORT\_ISO** – An ISO disk import created the image.
Type: String
Valid Values: `USER_INITIATED | SCHEDULED | IMPORT | IMPORT_ISO`
Required: No

 ** containerRecipe **   <a name="imagebuilder-Type-Image-containerRecipe"></a>
For container images, this is the container recipe that Image Builder used to create the image. For images that distribute an AMI, this is empty.
Type: [ContainerRecipe](API_ContainerRecipe.md) object
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-Image-dateCreated"></a>
The date on which Image Builder created this image.
Type: String
Required: No

 ** deprecationTime **   <a name="imagebuilder-Type-Image-deprecationTime"></a>
The time when deprecation occurs for an image resource. This can be a past or future date.
Type: Timestamp
Required: No

 ** distributionConfiguration **   <a name="imagebuilder-Type-Image-distributionConfiguration"></a>
The distribution configuration that Image Builder used to create this image.
Type: [DistributionConfiguration](API_DistributionConfiguration.md) object
Required: No

 ** enhancedImageMetadataEnabled **   <a name="imagebuilder-Type-Image-enhancedImageMetadataEnabled"></a>
Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.
Type: Boolean
Required: No

 ** executionRole **   <a name="imagebuilder-Type-Image-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** imageRecipe **   <a name="imagebuilder-Type-Image-imageRecipe"></a>
For images that distribute an AMI, this is the image recipe that Image Builder used to create the image. For container images, this is empty.
Type: [ImageRecipe](API_ImageRecipe.md) object
Required: No

 ** imageScanningConfiguration **   <a name="imagebuilder-Type-Image-imageScanningConfiguration"></a>
Contains settings for vulnerability scans.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** imageSource **   <a name="imagebuilder-Type-Image-imageSource"></a>
The origin of the base image that Image Builder used to build this image.
Type: String
Valid Values: `AMAZON_MANAGED | AWS_MARKETPLACE | IMPORTED | CUSTOM`
Required: No

 ** imageTestsConfiguration **   <a name="imagebuilder-Type-Image-imageTestsConfiguration"></a>
The image tests that ran when that Image Builder created this image.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** infrastructureConfiguration **   <a name="imagebuilder-Type-Image-infrastructureConfiguration"></a>
The infrastructure that Image Builder used to create this image.
Type: [InfrastructureConfiguration](API_InfrastructureConfiguration.md) object
Required: No

 ** lifecycleExecutionId **   <a name="imagebuilder-Type-Image-lifecycleExecutionId"></a>
Identifies the last runtime instance of the lifecycle policy to take action on the image.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** loggingConfiguration **   <a name="imagebuilder-Type-Image-loggingConfiguration"></a>
The logging configuration that's defined for the image. Image Builder uses the defined settings to direct execution log output during image creation.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** name **   <a name="imagebuilder-Type-Image-name"></a>
The name of the image.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** osVersion **   <a name="imagebuilder-Type-Image-osVersion"></a>
The operating system version for instances that launch from this image. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** outputResources **   <a name="imagebuilder-Type-Image-outputResources"></a>
The output resources that Image Builder produces for this image.
Type: [OutputResources](API_OutputResources.md) object
Required: No

 ** platform **   <a name="imagebuilder-Type-Image-platform"></a>
The image operating system platform, such as Linux or Windows.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** scanState **   <a name="imagebuilder-Type-Image-scanState"></a>
Contains information about the current state of scans for this image.
Type: [ImageScanState](API_ImageScanState.md) object
Required: No

 ** sourcePipelineArn **   <a name="imagebuilder-Type-Image-sourcePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that created this image.
Type: String
Required: No

 ** sourcePipelineName **   <a name="imagebuilder-Type-Image-sourcePipelineName"></a>
The name of the image pipeline that created this image.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** state **   <a name="imagebuilder-Type-Image-state"></a>
The state of the image.
Type: [ImageState](API_ImageState.md) object
Required: No

 ** tags **   <a name="imagebuilder-Type-Image-tags"></a>
The tags that apply to this image.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-Image-type"></a>
Specifies whether this image produces an AMI or a container image.
Type: String
Valid Values: `AMI | DOCKER`
Required: No

 ** version **   <a name="imagebuilder-Type-Image-version"></a>
The semantic version of the image.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
 **Filtering:** You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** workflows **   <a name="imagebuilder-Type-Image-workflows"></a>
Contains the build and test workflows that are associated with the image.
Type: Array of [WorkflowConfiguration](API_WorkflowConfiguration.md) objects
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/Image)
