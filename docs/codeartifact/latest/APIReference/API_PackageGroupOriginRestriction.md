---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupOriginRestriction.html
---

# PackageGroupOriginRestriction
<a name="API_PackageGroupOriginRestriction"></a>

Contains information about the configured restrictions of the origin controls of a package group.

## Contents
<a name="API_PackageGroupOriginRestriction_Contents"></a>

 ** effectiveMode **   <a name="codeartifact-Type-PackageGroupOriginRestriction-effectiveMode"></a>
The effective package group origin restriction setting. If the value of `mode` is `ALLOW`, `ALLOW_SPECIFIC_REPOSITORIES`, or `BLOCK`, then the value of `effectiveMode` is the same. Otherwise, when the value of `mode` is `INHERIT`, then the value of `effectiveMode` is the value of `mode` of the first parent group which does not have a value of `INHERIT`.
Type: String
Valid Values: `ALLOW | ALLOW_SPECIFIC_REPOSITORIES | BLOCK | INHERIT`
Required: No

 ** inheritedFrom **   <a name="codeartifact-Type-PackageGroupOriginRestriction-inheritedFrom"></a>
The parent package group that the package group origin restrictions are inherited from.
Type: [PackageGroupReference](API_PackageGroupReference.md) object
Required: No

 ** mode **   <a name="codeartifact-Type-PackageGroupOriginRestriction-mode"></a>
The package group origin restriction setting. If the value of `mode` is `ALLOW`, `ALLOW_SPECIFIC_REPOSITORIES`, or `BLOCK`, then the value of `effectiveMode` is the same. Otherwise, when the value is `INHERIT`, then the value of `effectiveMode` is the value of `mode` of the first parent group which does not have a value of `INHERIT`.
Type: String
Valid Values: `ALLOW | ALLOW_SPECIFIC_REPOSITORIES | BLOCK | INHERIT`
Required: No

 ** repositoriesCount **   <a name="codeartifact-Type-PackageGroupOriginRestriction-repositoriesCount"></a>
The number of repositories in the allowed repository list.
Type: Long
Required: No

## See Also
<a name="API_PackageGroupOriginRestriction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageGroupOriginRestriction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageGroupOriginRestriction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageGroupOriginRestriction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
