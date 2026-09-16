---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerRecipe.html
---

# ContainerRecipe
<a name="API_ContainerRecipe"></a>

A container recipe.

## Contents
<a name="API_ContainerRecipe_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ContainerRecipe-arn"></a>
The Amazon Resource Name (ARN) of the container recipe.
Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:

1. Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.

1. Version ARNs have only the first three nodes: <major>.<minor>.<patch>

1. Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** components **   <a name="imagebuilder-Type-ContainerRecipe-components"></a>
Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
Type: Array of [ComponentConfiguration](API_ComponentConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** containerType **   <a name="imagebuilder-Type-ContainerRecipe-containerType"></a>
Specifies the type of container, such as Docker.
Type: String
Valid Values: `DOCKER`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ContainerRecipe-dateCreated"></a>
The date when this container recipe was created.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-ContainerRecipe-description"></a>
The description of the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** dockerfileTemplateData **   <a name="imagebuilder-Type-ContainerRecipe-dockerfileTemplateData"></a>
Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
Type: String
Required: No

 ** encrypted **   <a name="imagebuilder-Type-ContainerRecipe-encrypted"></a>
A flag that indicates if the target container is encrypted.
Type: Boolean
Required: No

 ** instanceConfiguration **   <a name="imagebuilder-Type-ContainerRecipe-instanceConfiguration"></a>
A group of options that can be used to configure an instance for building and testing container images.
Type: [InstanceConfiguration](API_InstanceConfiguration.md) object
Required: No

 ** kmsKeyId **   <a name="imagebuilder-Type-ContainerRecipe-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the container image for distribution to the target Region. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-ContainerRecipe-name"></a>
The name of the container recipe.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-ContainerRecipe-owner"></a>
The owner of the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** parentImage **   <a name="imagebuilder-Type-ContainerRecipe-parentImage"></a>
The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example `amazonlinux:latest`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ContainerRecipe-platform"></a>
The system platform for the container, such as Windows or Linux.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** tags **   <a name="imagebuilder-Type-ContainerRecipe-tags"></a>
Tags that are attached to the container recipe.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** targetRepository **   <a name="imagebuilder-Type-ContainerRecipe-targetRepository"></a>
The destination repository for the container image.
Type: [TargetContainerRepository](API_TargetContainerRepository.md) object
Required: No

 ** version **   <a name="imagebuilder-Type-ContainerRecipe-version"></a>
The semantic version of the container recipe.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
 **Filtering:** You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** workingDirectory **   <a name="imagebuilder-Type-ContainerRecipe-workingDirectory"></a>
The working directory for use during build and test workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ContainerRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ContainerRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ContainerRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ContainerRecipe)
