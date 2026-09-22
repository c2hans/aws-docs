---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionConfiguration.html
---

# DistributionConfiguration
<a name="API_DistributionConfiguration"></a>

Defines how Image Builder distributes the output of an image build. You can configure:
+ The Regions to distribute the image to.
+ The Region-specific settings to apply, such as output AMI names, launch permissions for other AWS accounts, and target container repositories.

## Contents
<a name="API_DistributionConfiguration_Contents"></a>

 ** timeoutMinutes **   <a name="imagebuilder-Type-DistributionConfiguration-timeoutMinutes"></a>
A property that Image Builder doesn't use. You can't set this property when you create or update a distribution configuration, and it has no effect on distribution behavior.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 720.
Required: Yes

 ** arn **   <a name="imagebuilder-Type-DistributionConfiguration-arn"></a>
The Amazon Resource Name (ARN) of the distribution configuration.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-DistributionConfiguration-dateCreated"></a>
The date on which this distribution configuration was created.
Type: String
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-DistributionConfiguration-dateUpdated"></a>
The date on which this distribution configuration was last updated.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-DistributionConfiguration-description"></a>
The description of the distribution configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** distributions **   <a name="imagebuilder-Type-DistributionConfiguration-distributions"></a>
The distribution objects that apply Region-specific settings for the deployment of the image to targeted Regions.
Type: Array of [Distribution](API_Distribution.md) objects
Required: No

 ** name **   <a name="imagebuilder-Type-DistributionConfiguration-name"></a>
The name of the distribution configuration.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** tags **   <a name="imagebuilder-Type-DistributionConfiguration-tags"></a>
The tags of the distribution configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DistributionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DistributionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DistributionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DistributionConfiguration)
