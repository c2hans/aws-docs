---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageTagMutabilityExclusionFilter.html
---

# ImageTagMutabilityExclusionFilter
<a name="API_ImageTagMutabilityExclusionFilter"></a>

A filter that specifies which image tags should be excluded from the repository's image tag mutability setting.

## Contents
<a name="API_ImageTagMutabilityExclusionFilter_Contents"></a>

 ** filter **   <a name="ECR-Type-ImageTagMutabilityExclusionFilter-filter"></a>
The filter value used to match image tags for exclusion from mutability settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9a-zA-Z._*-]{1,128}$`
Required: Yes

 ** filterType **   <a name="ECR-Type-ImageTagMutabilityExclusionFilter-filterType"></a>
The type of filter to apply for excluding image tags from mutability settings.
Type: String
Valid Values: `WILDCARD`
Required: Yes

## See Also
<a name="API_ImageTagMutabilityExclusionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageTagMutabilityExclusionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageTagMutabilityExclusionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageTagMutabilityExclusionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
