---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update.html
---

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Add or update tags for a CodeGuru Reviewer associated repository
<a name="how-to-tag-associated-repository-update"></a>

You can change the value for a tag associated with an associated repository or add a new tag. Keep in mind that there are limits on the characters you can use in the key and value fields. For more information, see [Limits](quotas.md#limits-tags).

**Important**
Updating the value of a tag for an associated repository can impact access to that associated repository. Before you update the value of a tag for an associated repository, make sure to review any IAM policies that might use the value to control access to resources such as associated repositories. For examples of tag-based access policies, see [Using tags to control access to Amazon CodeGuru Reviewer associated repositories](auth-and-access-control-using-tags.md).

**Topics**
+ [Add or update tags for a CodeGuru Reviewer associated repository (console)](how-to-tag-associated-repository-update-console.md)
+ [Add or update tags for a CodeGuru Reviewer associated repository (AWS CLI)](how-to-tag-associated-repository-update-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
