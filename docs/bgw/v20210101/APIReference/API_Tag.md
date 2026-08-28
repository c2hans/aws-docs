---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

A key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, and the following characters: \+ - = . \_ : /. Spaces are not allowed in tag values.

## Contents
<a name="API_Tag_Contents"></a>

 ** Key **   <a name="bgw-Type-Tag-Key"></a>
The key part of a tag's key-value pair. The key can't start with `aws:`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: Yes

 ** Value **   <a name="bgw-Type-Tag-Value"></a>
The value part of a tag's key-value pair.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\x00]*`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
