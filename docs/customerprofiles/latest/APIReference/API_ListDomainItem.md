---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListDomainItem.html
---

# ListDomainItem
<a name="API_connect-customer-profiles_ListDomainItem"></a>

An object in a list that represents a domain.

## Contents
<a name="API_connect-customer-profiles_ListDomainItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_ListDomainItem-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp
Required: Yes

 ** DomainName **   <a name="connect-Type-connect-customer-profiles_ListDomainItem-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListDomainItem-LastUpdatedAt"></a>
The timestamp of when the domain was most recently edited.
Type: Timestamp
Required: Yes

 ** Tags **   <a name="connect-Type-connect-customer-profiles_ListDomainItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_ListDomainItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListDomainItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListDomainItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListDomainItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
