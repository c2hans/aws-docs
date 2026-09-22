---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageVersion.html
---

# ImageVersion
<a name="API_ImageVersion"></a>

The defining characteristics of a specific version of an Image Builder image.

## Contents
<a name="API_ImageVersion_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ImageVersion-arn"></a>
The Amazon Resource Name (ARN) of a specific version of an Image Builder image.
Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:

1. Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.

1. Version ARNs have only the first three nodes: <major>.<minor>.<patch>

1. Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** buildType **   <a name="imagebuilder-Type-ImageVersion-buildType"></a>
Indicates the type of build that created this image. The build can be initiated in the following ways:
+  **USER\_INITIATED** – A manual pipeline build request.
+  **SCHEDULED** – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.
+  **IMPORT** – A VM import created the image to use as the base image for the recipe.
+  **IMPORT\_ISO** – An ISO disk import created the image.
Type: String
Valid Values: `USER_INITIATED | SCHEDULED | IMPORT | IMPORT_ISO`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ImageVersion-dateCreated"></a>
The date on which this specific version of the Image Builder image was created.
Type: String
Required: No

 ** imageSource **   <a name="imagebuilder-Type-ImageVersion-imageSource"></a>
The origin of the base image that Image Builder used to build this image.
Type: String
Valid Values: `AMAZON_MANAGED | AWS_MARKETPLACE | IMPORTED | CUSTOM`
Required: No

 ** name **   <a name="imagebuilder-Type-ImageVersion-name"></a>
The name of this specific version of an Image Builder image.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** osVersion **   <a name="imagebuilder-Type-ImageVersion-osVersion"></a>
The operating system version of the image. For example, Amazon Linux 2023 or Microsoft Windows Server 2022.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** owner **   <a name="imagebuilder-Type-ImageVersion-owner"></a>
The owner of the image version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ImageVersion-platform"></a>
The operating system platform of the image version, for example "Windows" or "Linux".
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** type **   <a name="imagebuilder-Type-ImageVersion-type"></a>
Specifies whether this image produces an AMI or a container image.
Type: String
Valid Values: `AMI | DOCKER`
Required: No

 ** version **   <a name="imagebuilder-Type-ImageVersion-version"></a>
The semantic version of the image. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
 **Filtering:** You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

## See Also
<a name="API_ImageVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageVersion)
