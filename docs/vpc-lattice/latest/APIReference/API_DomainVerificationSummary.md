---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DomainVerificationSummary.html
---

# DomainVerificationSummary
<a name="API_DomainVerificationSummary"></a>

 Summary information about a domain verification.

## Contents
<a name="API_DomainVerificationSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-DomainVerificationSummary-arn"></a>
 The Amazon Resource Name (ARN) of the domain verification.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:domainverification/dv-[a-fA-F0-9]{17}`
Required: Yes

 ** createdAt **   <a name="vpclattice-Type-DomainVerificationSummary-createdAt"></a>
 The date and time that the domain verification was created, in ISO-8601 format.
Type: Timestamp
Required: Yes

 ** domainName **   <a name="vpclattice-Type-DomainVerificationSummary-domainName"></a>
 The domain name being verified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: Yes

 ** id **   <a name="vpclattice-Type-DomainVerificationSummary-id"></a>
 The ID of the domain verification.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`
Required: Yes

 ** status **   <a name="vpclattice-Type-DomainVerificationSummary-status"></a>
 The current status of the domain verification process.
Type: String
Valid Values: `VERIFIED | PENDING | VERIFICATION_TIMED_OUT`
Required: Yes

 ** lastVerifiedTime **   <a name="vpclattice-Type-DomainVerificationSummary-lastVerifiedTime"></a>
 The date and time that the domain was last successfully verified, in ISO-8601 format.
Type: Timestamp
Required: No

 ** tags **   <a name="vpclattice-Type-DomainVerificationSummary-tags"></a>
 The tags associated with the domain verification.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** txtMethodConfig **   <a name="vpclattice-Type-DomainVerificationSummary-txtMethodConfig"></a>
 The TXT record configuration used for domain verification.
Type: [TxtMethodConfig](API_TxtMethodConfig.md) object
Required: No

## See Also
<a name="API_DomainVerificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DomainVerificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DomainVerificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DomainVerificationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
