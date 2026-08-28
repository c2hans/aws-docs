---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptRuleSetMetadata.html
---

# ReceiptRuleSetMetadata
<a name="API_ReceiptRuleSetMetadata"></a>

Information about a receipt rule set.

A receipt rule set is a collection of rules that specify what Amazon SES should do with mail it receives on behalf of your account's verified domains.

For information about setting up receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules).

## Contents
<a name="API_ReceiptRuleSetMetadata_Contents"></a>

 ** CreatedTimestamp **
The date and time the receipt rule set was created.
Type: Timestamp
Required: No

 ** Name **
The name of the receipt rule set. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Start and end with a letter or number.
+ Contain 64 characters or fewer.
Type: String
Required: No

## See Also
<a name="API_ReceiptRuleSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ReceiptRuleSetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ReceiptRuleSetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ReceiptRuleSetMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
