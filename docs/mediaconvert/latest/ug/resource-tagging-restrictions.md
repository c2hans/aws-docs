---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/resource-tagging-restrictions.html
---

# Restrictions for tags on AWS Elemental MediaConvert resources
<a name="resource-tagging-restrictions"></a>

The following basic restrictions apply to tags:
+ Maximum number of tags per resource – 50.
+ Maximum **Key** length – 128 Unicode characters.
+ Maximum **Value** length – 256 Unicode characters.
+ Valid values for **Key** and **Value** – Uppercase and lowercase letters in the UTF-8 character set, numbers, space, and the following characters: \_ . : / = \+ - and @.
+ Tag keys and values are case sensitive.
+ Don't use the `aws:` prefix for either keys or values. It's reserved for AWS use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
