---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/tag-restrictions.html
---

# Tagging restrictions
<a name="tag-restrictions"></a>

The following basic restrictions apply to tags on Amazon Braket resources:
+ Maximum number of tags that you can assign to a resource: 50
+ Maximum key length: 128 Unicode characters
+ Maximum value length: 256 Unicode characters
+ Valid characters for key and value: `a-z, A-Z, 0-9, space`, and these characters: `_ . : / = + -` and `@`
+ Keys and values are case sensitive.
+ Don't use `aws` as a prefix for keys; it's reserved for AWS use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
