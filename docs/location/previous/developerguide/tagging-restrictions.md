---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tagging-restrictions.html
---

# Amazon Location tagging restrictions
<a name="tagging-restrictions"></a>

Tagging allows you to organize and manage your resources more effectively. This page outlines the specific rules and constraints that govern the use of tags within Amazon Location Service. By understanding these tagging restrictions, you can ensure compliance with best practices and avoid potential issues when implementing tagging strategies for your location-based resources and applications.

The following basic restrictions apply to tags:
+ Maximum tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
**Note**
If you add a new tag with the same tag key as an existing tag, the new tag overwrites the existing tag.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ The `aws:` prefix is reserved for AWS use. If a tag has a tag key with this prefix, then you can't edit or delete the tag's key or value. Tags with the `aws:` prefix don't count against your tags per resource limit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
