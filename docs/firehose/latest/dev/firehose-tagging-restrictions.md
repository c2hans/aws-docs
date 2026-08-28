---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging-restrictions.html
---

# Know tag restrictions
<a name="firehose-tagging-restrictions"></a>

The following restrictions apply to tags in Amazon Data Firehose.

**Basic restrictions**
+ The maximum number of tags per resource (stream) is 50.
+ Tag keys and values are case-sensitive.
+ You can't change or edit tags for a deleted stream.

**Tag key restrictions**
+ Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair.
+ You can't start a tag key with `aws:` because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.
+ Tag keys must be between 1 and 128 Unicode characters in length.
+ Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: `_ . / = + - @`.

**Tag value restrictions**
+ Tag values must be between 0 and 255 Unicode characters in length.
+ Tag values can be blank. Otherwise, they must consist of the following characters: Unicode letters, digits, white space, and any of the following special characters: `_ . / = + - @`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
