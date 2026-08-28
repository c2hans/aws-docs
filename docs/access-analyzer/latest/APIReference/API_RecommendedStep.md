---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_RecommendedStep.html
---

# RecommendedStep
<a name="API_RecommendedStep"></a>

Contains information about a recommended step for an unused access analyzer finding.

## Contents
<a name="API_RecommendedStep_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** unusedPermissionsRecommendedStep **   <a name="accessanalyzer-Type-RecommendedStep-unusedPermissionsRecommendedStep"></a>
A recommended step for an unused permissions finding.
Type: [UnusedPermissionsRecommendedStep](API_UnusedPermissionsRecommendedStep.md) object
Required: No

## See Also
<a name="API_RecommendedStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/RecommendedStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/RecommendedStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/RecommendedStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
