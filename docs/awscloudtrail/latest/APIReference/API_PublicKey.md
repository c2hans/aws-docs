---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PublicKey.html
---

# PublicKey
<a name="API_PublicKey"></a>

Contains information about a returned public key.

## Contents
<a name="API_PublicKey_Contents"></a>

 ** Fingerprint **   <a name="awscloudtrail-Type-PublicKey-Fingerprint"></a>
The fingerprint of the public key.
Type: String
Required: No

 ** ValidityEndTime **   <a name="awscloudtrail-Type-PublicKey-ValidityEndTime"></a>
The ending time of validity of the public key.
Type: Timestamp
Required: No

 ** ValidityStartTime **   <a name="awscloudtrail-Type-PublicKey-ValidityStartTime"></a>
The starting time of validity of the public key.
Type: Timestamp
Required: No

 ** Value **   <a name="awscloudtrail-Type-PublicKey-Value"></a>
The DER encoded public key value in PKCS\#1 format.
Type: Base64-encoded binary data object
Required: No

## See Also
<a name="API_PublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/PublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/PublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/PublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
