---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/flow-language-actions-parameter-restrictions.html
---

# Parameter restrictions for actions in the Connect Customer Flow language
<a name="flow-language-actions-parameter-restrictions"></a>

There are several restrictions on parameters. Here's what they mean:
+ Must be defined statically. This means that JSONPath cannot be used at all in this value.
+ Must be defined statically or as a single valid JSONPath identifier.

  If JSONPath is used, it must be the entirety of the value; you can't specify an input of "My name is $.Name". Further, the JSONPath must be valid - $.Attributes.stuff is okay, $.BadValue is not okay because there's no "BadValue" path on the object used by flows.
+ May be defined statically or dynamically. Anything goes. A value of "My name is $.Name" is fine here, as well as a fully static value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
