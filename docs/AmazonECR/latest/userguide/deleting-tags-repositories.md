---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/deleting-tags-repositories.html
---

# Deleting tags from a private repository in Amazon ECR
<a name="deleting-tags-repositories"></a>

You can delete tags from a private repository.

## To delete a tag from a private repository (AWS Management Console)
<a name="deleting-tags-repositories-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, select the region to use.

1. On the **Repositories** page, select the check box next to the repository you want to remove a tag from.

1. From the **Action** menu, select **Repository tags**.

1. On the **Repository tags** page, select **Edit**.

1. On the **Edit repository tags** page, select **Remove** for each tag you want to delete, and choose **Save**.

## To delete a tag from a private repository (AWS CLI)
<a name="deleting-tags-repositories-cli"></a>

You can delete one or more tags by using the AWS CLI or an API.
+ AWS CLI - [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/ecr/untag-resource.html)
+ API action - [UntagResource](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UntagResource.html)

The following example shows how to delete a tag from a repository using the AWS CLI.

```
aws ecr untag-resource \
     --resource-arn arn:aws:ecr:{{region}}:{{account_id}}:repository/{{repository_name}} \
     --tag-keys {{tag_key}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
