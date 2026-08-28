---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/tagging-restrictions.html
---

# Tagging limitations
<a name="tagging-restrictions"></a>

The following basic limitations apply to tags:
+ Each resource can have a maximum of 50 user-created tags.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ The maximum key length is 128 Unicode characters in UTF-8.
+ The maximum value length is 256 Unicode characters in UTF-8.
+ Allowed characters are letters, numbers, spaces representable in UTF-8, and the following characters: \_ . : / = \+ - @.
+ A tag key cannot be an empty string. A tag value can be an empty string, but not null.
+ Tag keys and values are case sensitive.
+ Do not use `AWS:` or any upper or lowercase combination of such as a prefix for either keys or values. These are reserved only for AWS use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
