---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-tags.html
---

# Working with tags using the AWS CLI and the Amazon EMR Serverless API
<a name="using-tags"></a>

Use the following AWS CLI commands or Amazon EMR Serverless API operations to add, update, list, and delete the tags for your resources.

**CLI commands and API operations for tags**

| Resource | Supports tags | Supports tag propagation |
| --- | --- | --- |
| Add or overwrite one or more tags | tag-resource | TagResource |
| List tags for a resource | list-tags-for-resource | ListTagsForResource |
| Delete one or more tags | untag-resource | UntagResource |

The following examples demonstrate how to tag or untag resources using the AWS CLI.

**Tag an existing application**

The following command tags an existing application.

```
aws emr-serverless tag-resource --resource-arn resource_ARN --tags team=devs
```

**Untag an existing application**

The following command deletes a tag from an existing application.

```
aws emr-serverless untag-resource --resource-arn resource_ARN --tag-keys tag_key
```

**List tags for a resource**

The following command lists the tags associated with an existing resource.

```
aws emr-serverless list-tags-for-resource --resource-arn resource_ARN
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
