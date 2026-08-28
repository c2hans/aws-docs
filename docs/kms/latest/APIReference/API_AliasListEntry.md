---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_AliasListEntry.html
---

# AliasListEntry
<a name="API_AliasListEntry"></a>

Contains information about an alias.

## Contents
<a name="API_AliasListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AliasArn **   <a name="KMS-Type-AliasListEntry-AliasArn"></a>
String that contains the key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AliasName **   <a name="KMS-Type-AliasListEntry-AliasName"></a>
String that contains the alias. This value begins with `alias/`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: No

 ** CreationDate **   <a name="KMS-Type-AliasListEntry-CreationDate"></a>
Date and time that the alias was most recently created in the account and Region. Formatted as Unix time.
Type: Timestamp
Required: No

 ** LastUpdatedDate **   <a name="KMS-Type-AliasListEntry-LastUpdatedDate"></a>
Date and time that the alias was most recently associated with a KMS key in the account and Region. Formatted as Unix time.
Type: Timestamp
Required: No

 ** TargetKeyId **   <a name="KMS-Type-AliasListEntry-TargetKeyId"></a>
String that contains the key identifier of the KMS key associated with the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_AliasListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/AliasListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/AliasListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/AliasListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
