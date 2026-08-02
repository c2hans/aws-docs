---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InfrastructureConfigurationSummary.html
---

# InfrastructureConfigurationSummary
<a name="API_InfrastructureConfigurationSummary"></a>

The infrastructure used when building Amazon EC2 AMIs.

## Contents
<a name="API_InfrastructureConfigurationSummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-arn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-dateCreated"></a>
The date on which the infrastructure configuration was created.
Type: String
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-dateUpdated"></a>
The date on which the infrastructure configuration was last updated.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-description"></a>
The description of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** instanceProfileName **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-instanceProfileName"></a>
The instance profile of the infrastructure configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@-]+$`
Required: No

 ** instanceTypes **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-instanceTypes"></a>
The instance types of the infrastructure configuration.
Type: Array of strings
Required: No

 ** name **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-name"></a>
The name of the infrastructure configuration.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** placement **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-placement"></a>
The instance placement settings that define where the instances that are launched from your image will run.
Type: [Placement](API_Placement.md) object
Required: No

 ** resourceTags **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-resourceTags"></a>
The tags attached to the image created by Image Builder.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** tags **   <a name="imagebuilder-Type-InfrastructureConfigurationSummary-tags"></a>
The tags of the infrastructure configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_InfrastructureConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InfrastructureConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InfrastructureConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InfrastructureConfigurationSummary)
