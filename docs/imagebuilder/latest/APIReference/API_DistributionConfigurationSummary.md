---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionConfigurationSummary.html
---

# DistributionConfigurationSummary
<a name="API_DistributionConfigurationSummary"></a>

A high-level overview of a distribution configuration.

## Contents
<a name="API_DistributionConfigurationSummary_Contents"></a>

 ** arn **   <a name="imagebuilder-Type-DistributionConfigurationSummary-arn"></a>
The Amazon Resource Name (ARN) of the distribution configuration.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):(?:image-recipe|container-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline|lifecycle-policy|workflow\/(?:build|test|distribution))/[a-z0-9-_]+(?:/(?:(?:x|[0-9]+)\.(?:x|[0-9]+)\.(?:x|[0-9]+))(?:/[0-9]+)?)?$`
Required: No

 ** dateCreated **   <a name="imagebuilder-Type-DistributionConfigurationSummary-dateCreated"></a>
The date on which the distribution configuration was created.
Type: String
Required: No

 ** dateUpdated **   <a name="imagebuilder-Type-DistributionConfigurationSummary-dateUpdated"></a>
The date on which the distribution configuration was updated.
Type: String
Required: No

 ** description **   <a name="imagebuilder-Type-DistributionConfigurationSummary-description"></a>
The description of the distribution configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** name **   <a name="imagebuilder-Type-DistributionConfigurationSummary-name"></a>
The name of the distribution configuration.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: No

 ** regions **   <a name="imagebuilder-Type-DistributionConfigurationSummary-regions"></a>
A list of Regions where the container image is distributed to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** tags **   <a name="imagebuilder-Type-DistributionConfigurationSummary-tags"></a>
The tags associated with the distribution configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DistributionConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/DistributionConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/DistributionConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/DistributionConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
