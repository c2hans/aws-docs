---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_KmsKey.html
---

# KmsKey
<a name="API_KmsKey"></a>

KMS key info.

## Contents
<a name="API_KmsKey_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kmsAliasArn **   <a name="groundstation-Type-KmsKey-kmsAliasArn"></a>
KMS Alias Arn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-zA-Z-]{0,16}:kms:[-a-z0-9]{1,50}:[0-9]{12}:((alias/[a-zA-Z0-9:/_-]{1,256}))`
Required: No

 ** kmsAliasName **   <a name="groundstation-Type-KmsKey-kmsAliasName"></a>
KMS Alias Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `alias/[a-zA-Z0-9:/_-]+`
Required: No

 ** kmsKeyArn **   <a name="groundstation-Type-KmsKey-kmsKeyArn"></a>
KMS Key Arn.
Type: String
Required: No

## See Also
<a name="API_KmsKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/KmsKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/KmsKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/KmsKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
