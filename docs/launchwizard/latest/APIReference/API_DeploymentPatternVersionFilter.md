---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeploymentPatternVersionFilter.html
---

# DeploymentPatternVersionFilter
<a name="API_DeploymentPatternVersionFilter"></a>

A filter for deployment pattern versions. Use this filter to specify criteria for querying deployment pattern versions in AWS Launch Wizard.

## Contents
<a name="API_DeploymentPatternVersionFilter_Contents"></a>

 ** name **   <a name="launchwizard-Type-DeploymentPatternVersionFilter-name"></a>
The name of the filter attribute. Specifies which attribute to filter on when querying deployment pattern versions.
Type: String
Valid Values: `updateFromVersion`
Required: Yes

 ** values **   <a name="launchwizard-Type-DeploymentPatternVersionFilter-values"></a>
The values to filter by. Contains the specific values to match against when filtering deployment pattern versions.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)`
Required: Yes

## See Also
<a name="API_DeploymentPatternVersionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/DeploymentPatternVersionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/DeploymentPatternVersionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/DeploymentPatternVersionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
