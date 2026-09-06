---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_DomainSummary"></a>

 Information about a domain, including its name, Amazon Resource Name (ARN), and status. The [ListDomains](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html) operation returns a list of `DomainSummary` objects.

## Contents
<a name="API_DomainSummary_Contents"></a>

 ** arn **   <a name="codeartifact-Type-DomainSummary-arn"></a>
 The ARN of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** createdTime **   <a name="codeartifact-Type-DomainSummary-createdTime"></a>
 A timestamp that contains the date and time the domain was created.
Type: Timestamp
Required: No

 ** encryptionKey **   <a name="codeartifact-Type-DomainSummary-encryptionKey"></a>
 The key used to encrypt the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** name **   <a name="codeartifact-Type-DomainSummary-name"></a>
 The name of the domain.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: No

 ** owner **   <a name="codeartifact-Type-DomainSummary-owner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** status **   <a name="codeartifact-Type-DomainSummary-status"></a>
 A string that contains the status of the domain.
Type: String
Valid Values: `Active | Deleted`
Required: No

## See Also
<a name="API_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/DomainSummary)
