---
source_url: https://docs.aws.amazon.com/inspector/latest/user/tagging-fundamentals.html
---

# Tagging fundamentals
<a name="tagging-fundamentals"></a>

 A tag consists of a key-value pair. The tag key is a general label. The tag value is a description of the tag key. This topic descibes the fundamentals of tagging Amazon Inspector resources. When tagging Amazon Inspector resources, consider the following:
+  You can tag [suppression rules](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-supression-rules.html) and [CIS scan configurations](https://docs.aws.amazon.com/inspector/latest/user/scanning-cis-create-cis-scan-configuration.html).
+  You can add as many as 50 tags to each of your Amazon Inspector resources.
+  Tag keys must be unique.
+  A tag key can only have one tag value.
+  Tag keys and tag values can have a maximum of 128 UTF-8 characters. The characters can be letters, numbers, spaces, or the following symbols: `_` `.` `:` `/` `=` `+` `-` `@`.
+  You cannot use the `aws` prefix in any of your tags or modify tags with this prefix. Tags with the `aws` prefix are reserved for use by AWS.
+  Tags assigned to an Amazon Inspector resource are only available in your AWS account and in the AWS Region where you created them.
+  When you delete a resource, all tags associated with it are deleted, too.

 For more information about tags, see [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *Tagging AWS Resources and Tag Editor User Guide*.

**Note**
 Tags are not intended to store confidential or sensitive information. Never use tags to store this type of data. Tags can be accessible from other AWS services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
