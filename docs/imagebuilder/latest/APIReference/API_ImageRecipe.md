---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageRecipe.html
---

# ImageRecipe
<a name="API_ImageRecipe"></a>

An image recipe.

## Contents
<a name="API_ImageRecipe_Contents"></a>

 ** additionalInstanceConfiguration **   <a name="imagebuilder-Type-ImageRecipe-additionalInstanceConfiguration"></a>
Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.
Type: [AdditionalInstanceConfiguration](API_AdditionalInstanceConfiguration.md) object
Required: No

 ** amiTags **   <a name="imagebuilder-Type-ImageRecipe-amiTags"></a>
Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** amiWatermarks **   <a name="imagebuilder-Type-ImageRecipe-amiWatermarks"></a>
The AMI watermark names attached to the output AMI from this recipe. AMI watermarks are lineage markers that automatically propagate to derivative AMIs when the source AMI is copied or distributed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[A-Za-z0-9()\[\]./'@_\-][A-Za-z0-9 ()\[\]./'@_\-]{1,126}[A-Za-z0-9()\[\]./'@_\-]$`
Required: No

 ** arn **   <a name="imagebuilder-Type-ImageRecipe-arn"></a>
The Amazon Resource Name (ARN) of the image recipe.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** blockDeviceMappings **   <a name="imagebuilder-Type-ImageRecipe-blockDeviceMappings"></a>
The block device mappings to apply when creating images from this recipe.
Type: Array of [InstanceBlockDeviceMapping](API_InstanceBlockDeviceMapping.md) objects
Required: No

 ** components **   <a name="imagebuilder-Type-ImageRecipe-components"></a>
The components that are included in the image recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
Type: Array of [ComponentConfiguration](API_ComponentConfiguration.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-ImageRecipe-dateCreated"></a>
The date on which this image recipe was created.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-ImageRecipe-description"></a>
The description of the image recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-ImageRecipe-name"></a>
The name of the image recipe.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** owner **   <a name="imagebuilder-Type-ImageRecipe-owner"></a>
The owner of the image recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** parentImage **   <a name="imagebuilder-Type-ImageRecipe-parentImage"></a>
The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:
+ AMI ID
+ Image Builder image Amazon Resource Name (ARN)
+  AWS Systems Manager (SSM) Parameter Store Parameter, prefixed by `ssm:`, followed by the parameter name or ARN.
+  AWS Marketplace product ID
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** platform **   <a name="imagebuilder-Type-ImageRecipe-platform"></a>
The platform of the image recipe.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: No

 ** tags **   <a name="imagebuilder-Type-ImageRecipe-tags"></a>
The tags of the image recipe.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** type **   <a name="imagebuilder-Type-ImageRecipe-type"></a>
Specifies which type of image is created by the recipe - an AMI or a container image.
Type: String
Valid Values: `AMI | DOCKER`
Required: No

 ** version **   <a name="imagebuilder-Type-ImageRecipe-version"></a>
The version of the image recipe.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** workingDirectory **   <a name="imagebuilder-Type-ImageRecipe-workingDirectory"></a>
The working directory to be used during build and test workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ImageRecipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageRecipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageRecipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageRecipe)
