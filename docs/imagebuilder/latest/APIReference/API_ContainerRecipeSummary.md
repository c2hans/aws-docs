---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerRecipeSummary.html
---

# ContainerRecipeSummary
<a name="API_ContainerRecipeSummary"></a>

A summary of a container recipe.

## Contents
<a name="API_ContainerRecipeSummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-ContainerRecipeSummary-arn"></a>
The Amazon Resource Name (ARN) of the container recipe.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** containerType **   <a name="imagebuilder-Type-ContainerRecipeSummary-containerType"></a>
Specifies the type of container, such as "Docker".
Type: String
Valid Values: `DOCKER`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ContainerRecipeSummary-dateCreated"></a>
The date when this container recipe was created.
Type: String
Required: No

 ** instanceImage **   <a name="imagebuilder-Type-ContainerRecipeSummary-instanceImage"></a>
The base image for a container build and test instance. This can contain an AMI ID or it can specify an AWS Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:`, followed by the parameter name or ARN.
If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-ContainerRecipeSummary-name"></a>
The name of the container recipe.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-ContainerRecipeSummary-owner"></a>
The owner of the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** parentImage **   <a name="imagebuilder-Type-ContainerRecipeSummary-parentImage"></a>
The base image for the container recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ContainerRecipeSummary-platform"></a>
The system platform for the container. Container recipes support only the Linux and Windows platforms.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** tags **   <a name="imagebuilder-Type-ContainerRecipeSummary-tags"></a>
Tags that are attached to the container recipe.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ContainerRecipeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ContainerRecipeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ContainerRecipeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ContainerRecipeSummary)
