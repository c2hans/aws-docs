---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddressList.html
---

# AddressList
<a name="API_AddressList"></a>

An address list contains a list of emails and domains that are used in MailManager Ingress endpoints and Rules for email management.

## Contents
<a name="API_AddressList_Contents"></a>

 ** AddressListArn **   <a name="sesmailmanager-Type-AddressList-AddressListArn"></a>
The Amazon Resource Name (ARN) of the address list.
Type: String
Required: Yes

 ** AddressListId **   <a name="sesmailmanager-Type-AddressList-AddressListId"></a>
The identifier of the address list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** AddressListName **   <a name="sesmailmanager-Type-AddressList-AddressListName"></a>
The user-friendly name of the address list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** CreatedTimestamp **   <a name="sesmailmanager-Type-AddressList-CreatedTimestamp"></a>
The timestamp of when the address list was created.
Type: Timestamp
Required: Yes

 ** LastUpdatedTimestamp **   <a name="sesmailmanager-Type-AddressList-LastUpdatedTimestamp"></a>
The timestamp of when the address list was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AddressList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/AddressList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/AddressList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/AddressList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
