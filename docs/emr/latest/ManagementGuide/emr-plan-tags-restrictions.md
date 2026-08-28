---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags-restrictions.html
---

# Restrictions that apply to tagging resources in Amazon EMR
<a name="emr-plan-tags-restrictions"></a>

The following basic restrictions apply to tags:
+ Restrictions that apply to Amazon EC2 resources apply to Amazon EMR as well. For more information, see [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions).
+ Do not use the `aws:` prefix in tag names and values because it is reserved for AWS use. In addition, you cannot edit or delete tag names or values with this prefix.
+ You cannot change or edit tags on a terminated cluster.
+ A tag value can be an empty string, but not null. In addition, a tag key cannot be an empty string.
+ Keys and values can contain any alphabetic character in any language, any numeric character, white spaces, invisible separators, and the following symbols: \_ . : / = \+ - @

For more information about tagging using the AWS Management Console, see [Working with tags in the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_Console) in the *Amazon EC2 User Guide*. For more information about tagging using the Amazon EC2API or command line, see [API and CLI overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
