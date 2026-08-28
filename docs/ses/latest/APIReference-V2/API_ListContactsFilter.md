---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListContactsFilter.html
---

# ListContactsFilter
<a name="API_ListContactsFilter"></a>

A filter that can be applied to a list of contacts.

## Contents
<a name="API_ListContactsFilter_Contents"></a>

 ** FilteredStatus **   <a name="SES-Type-ListContactsFilter-FilteredStatus"></a>
The status by which you are filtering: `OPT_IN` or `OPT_OUT`.
Type: String
Valid Values: `OPT_IN | OPT_OUT`
Required: No

 ** TopicFilter **   <a name="SES-Type-ListContactsFilter-TopicFilter"></a>
Used for filtering by a specific topic preference.
Type: [TopicFilter](API_TopicFilter.md) object
Required: No

## See Also
<a name="API_ListContactsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListContactsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListContactsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListContactsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
