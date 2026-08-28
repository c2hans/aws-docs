---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublicKeySummary.html
---

# PublicKeySummary
<a name="API_PublicKeySummary"></a>

Contains information about a public key.

## Contents
<a name="API_PublicKeySummary_Contents"></a>

 ** CreatedTime **   <a name="cloudfront-Type-PublicKeySummary-CreatedTime"></a>
The date and time when the public key was uploaded.
Type: Timestamp
Required: Yes

 ** EncodedKey **   <a name="cloudfront-Type-PublicKeySummary-EncodedKey"></a>
The public key.
Type: String
Required: Yes

 ** Id **   <a name="cloudfront-Type-PublicKeySummary-Id"></a>
The identifier of the public key.
Type: String
Required: Yes

 ** Name **   <a name="cloudfront-Type-PublicKeySummary-Name"></a>
A name to help identify the public key.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-PublicKeySummary-Comment"></a>
A comment to describe the public key. The comment cannot be longer than 128 characters.
Type: String
Required: No

## See Also
<a name="API_PublicKeySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
