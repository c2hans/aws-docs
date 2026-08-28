---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFilter.html
---

# ContactFilter
<a name="API_ContactFilter"></a>

Filters user data based on the contact information that is associated to the users. It contains a list of [contact states](https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html).

## Contents
<a name="API_ContactFilter_Contents"></a>

 ** ContactStates **   <a name="connect-Type-ContactFilter-ContactStates"></a>
A list of up to 9 [contact states](https://docs.aws.amazon.com/connect/latest/adminguide/about-contact-states.html).
Type: Array of strings
Array Members: Maximum number of 9 items.
Valid Values: `INCOMING | PENDING | CONNECTING | CONNECTED | CONNECTED_ONHOLD | MISSED | ERROR | ENDED | REJECTED`
Required: No

## See Also
<a name="API_ContactFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
