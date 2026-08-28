---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ContactListDestination.html
---

# ContactListDestination
<a name="API_ContactListDestination"></a>

An object that contains details about the action of a contact list.

## Contents
<a name="API_ContactListDestination_Contents"></a>

 ** ContactListImportAction **   <a name="SES-Type-ContactListDestination-ContactListImportAction"></a>
>The type of action to perform on the addresses. The following are the possible values:
+ PUT: add the addresses to the contact list. If the record already exists, it will override it with the new value.
+ DELETE: remove the addresses from the contact list.
Type: String
Valid Values: `DELETE | PUT`
Required: Yes

 ** ContactListName **   <a name="SES-Type-ContactListDestination-ContactListName"></a>
The name of the contact list.
Type: String
Required: Yes

## See Also
<a name="API_ContactListDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ContactListDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ContactListDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ContactListDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
