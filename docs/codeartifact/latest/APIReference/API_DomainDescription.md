---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html
---

# DomainDescription
<a name="API_DomainDescription"></a>

 Information about a domain. A domain is a container for repositories. When you create a domain, it is empty until you add one or more repositories.

## Contents
<a name="API_DomainDescription_Contents"></a>

 ** arn **   <a name="codeartifact-Type-DomainDescription-arn"></a>
 The Amazon Resource Name (ARN) of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** assetSizeBytes **   <a name="codeartifact-Type-DomainDescription-assetSizeBytes"></a>
 The total size of all assets in the domain.
Type: Long
Required: No

 ** createdTime **   <a name="codeartifact-Type-DomainDescription-createdTime"></a>
 A timestamp that represents the date and time the domain was created.
Type: Timestamp
Required: No

 ** encryptionKey **   <a name="codeartifact-Type-DomainDescription-encryptionKey"></a>
 The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** name **   <a name="codeartifact-Type-DomainDescription-name"></a>
 The name of the domain.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: No

 ** owner **   <a name="codeartifact-Type-DomainDescription-owner"></a>
 The AWS account ID that owns the domain.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** repositoryCount **   <a name="codeartifact-Type-DomainDescription-repositoryCount"></a>
 The number of repositories in the domain.
Type: Integer
Required: No

 ** s3BucketArn **   <a name="codeartifact-Type-DomainDescription-s3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket that is used to store package assets in the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** status **   <a name="codeartifact-Type-DomainDescription-status"></a>
 The current status of a domain.
Type: String
Valid Values: `Active | Deleted`
Required: No

## See Also
<a name="API_DomainDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DomainDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DomainDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DomainDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
