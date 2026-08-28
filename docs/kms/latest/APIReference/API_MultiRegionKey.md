---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_MultiRegionKey.html
---

# MultiRegionKey
<a name="API_MultiRegionKey"></a>

Describes the primary or replica key in a multi-Region key.

## Contents
<a name="API_MultiRegionKey_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="KMS-Type-MultiRegionKey-Arn"></a>
Displays the key ARN of a primary or replica key of a multi-Region key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Region **   <a name="KMS-Type-MultiRegionKey-Region"></a>
Displays the AWS Region of a primary or replica key in a multi-Region key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-z]+-){2,3}\d+$`
Required: No

## See Also
<a name="API_MultiRegionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/MultiRegionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/MultiRegionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/MultiRegionKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
