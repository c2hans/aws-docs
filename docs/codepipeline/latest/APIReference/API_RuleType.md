---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RuleType.html
---

# RuleType
<a name="API_RuleType"></a>

The rule type, which is made up of the combined values for category, owner, provider, and version.

## Contents
<a name="API_RuleType_Contents"></a>

 ** id **   <a name="CodePipeline-Type-RuleType-id"></a>
Represents information about a rule type.
Type: [RuleTypeId](API_RuleTypeId.md) object
Required: Yes

 ** inputArtifactDetails **   <a name="CodePipeline-Type-RuleType-inputArtifactDetails"></a>
Returns information about the details of an artifact.
Type: [ArtifactDetails](API_ArtifactDetails.md) object
Required: Yes

 ** ruleConfigurationProperties **   <a name="CodePipeline-Type-RuleType-ruleConfigurationProperties"></a>
The configuration properties for the rule type.
Type: Array of [RuleConfigurationProperty](API_RuleConfigurationProperty.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** settings **   <a name="CodePipeline-Type-RuleType-settings"></a>
Returns information about the settings for a rule type.
Type: [RuleTypeSettings](API_RuleTypeSettings.md) object
Required: No

## See Also
<a name="API_RuleType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
