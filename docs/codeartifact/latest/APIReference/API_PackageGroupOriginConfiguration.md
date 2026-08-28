---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupOriginConfiguration.html
---

# PackageGroupOriginConfiguration
<a name="API_PackageGroupOriginConfiguration"></a>

The package group origin configuration that determines how package versions can enter repositories.

## Contents
<a name="API_PackageGroupOriginConfiguration_Contents"></a>

 ** restrictions **   <a name="codeartifact-Type-PackageGroupOriginConfiguration-restrictions"></a>
The origin configuration settings that determine how package versions can enter repositories.
Type: String to [PackageGroupOriginRestriction](API_PackageGroupOriginRestriction.md) object map
Valid Keys: `EXTERNAL_UPSTREAM | INTERNAL_UPSTREAM | PUBLISH`
Required: No

## See Also
<a name="API_PackageGroupOriginConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageGroupOriginConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageGroupOriginConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageGroupOriginConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
