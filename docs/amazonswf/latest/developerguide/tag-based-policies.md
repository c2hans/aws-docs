---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/tag-based-policies.html
---

# Tag-based Policies
<a name="tag-based-policies"></a>

Amazon SWF supports policies based on tags. For instance, you could restrict Amazon SWF domains that include a tag with the key `environment` and the value `production` with the following condition:

```
"Condition": {
    "StringEquals": {"aws:ResourceTag/environment": "production"}
}
```

For more information on tagging, see:
+ [Tags in Amazon SWF](swf-dev-adv-tags.md)
+ [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
