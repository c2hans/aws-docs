---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html
---

# PackageGroupDescription
<a name="API_PackageGroupDescription"></a>

 The description of the package group.

## Contents
<a name="API_PackageGroupDescription_Contents"></a>

 ** arn **   <a name="codeartifact-Type-PackageGroupDescription-arn"></a>
 The ARN of the package group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** contactInfo **   <a name="codeartifact-Type-PackageGroupDescription-contactInfo"></a>
 The contact information of the package group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** createdTime **   <a name="codeartifact-Type-PackageGroupDescription-createdTime"></a>
A timestamp that represents the date and time the package group was created.
Type: Timestamp
Required: No

 ** description **   <a name="codeartifact-Type-PackageGroupDescription-description"></a>
 The description of the package group.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** domainName **   <a name="codeartifact-Type-PackageGroupDescription-domainName"></a>
 The name of the domain that contains the package group.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: No

 ** domainOwner **   <a name="codeartifact-Type-PackageGroupDescription-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** originConfiguration **   <a name="codeartifact-Type-PackageGroupDescription-originConfiguration"></a>
The package group origin configuration that determines how package versions can enter repositories.
Type: [PackageGroupOriginConfiguration](API_PackageGroupOriginConfiguration.md) object
Required: No

 ** parent **   <a name="codeartifact-Type-PackageGroupDescription-parent"></a>
 The direct parent package group of the package group.
Type: [PackageGroupReference](API_PackageGroupReference.md) object
Required: No

 ** pattern **   <a name="codeartifact-Type-PackageGroupDescription-pattern"></a>
 The pattern of the package group. The pattern determines which packages are associated with the package group.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 520.
Pattern: `[^\p{C}\p{IsWhitespace}]+`
Required: No

## See Also
<a name="API_PackageGroupDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/PackageGroupDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/PackageGroupDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/PackageGroupDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
