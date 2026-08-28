---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_ExpenseGroupProperty.html
---

# ExpenseGroupProperty
<a name="API_ExpenseGroupProperty"></a>

Shows the group that a certain key belongs to. This helps differentiate between names and addresses for different organizations, that can be hard to determine via JSON response.

## Contents
<a name="API_ExpenseGroupProperty_Contents"></a>

 ** Id **   <a name="Textract-Type-ExpenseGroupProperty-Id"></a>
Provides a group Id number, which will be the same for each in the group.
Type: String
Required: No

 ** Types **   <a name="Textract-Type-ExpenseGroupProperty-Types"></a>
Informs you on whether the expense group is a name or an address.
Type: Array of strings
Required: No

## See Also
<a name="API_ExpenseGroupProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/ExpenseGroupProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/ExpenseGroupProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/ExpenseGroupProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
