---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_MaximumAllowedResources.html
---

# MaximumAllowedResources
<a name="API_MaximumAllowedResources"></a>

The maximum allowed cumulative resources for an application. No new resources will be created once the limit is hit.

## Contents
<a name="API_MaximumAllowedResources_Contents"></a>

 ** cpu **   <a name="emrserverless-Type-MaximumAllowedResources-cpu"></a>
The maximum allowed CPU for an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(vCPU|vcpu|VCPU)?`
Required: Yes

 ** memory **   <a name="emrserverless-Type-MaximumAllowedResources-memory"></a>
The maximum allowed resources for an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)?`
Required: Yes

 ** disk **   <a name="emrserverless-Type-MaximumAllowedResources-disk"></a>
The maximum allowed disk for an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)`
Required: No

## See Also
<a name="API_MaximumAllowedResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/MaximumAllowedResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/MaximumAllowedResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/MaximumAllowedResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
