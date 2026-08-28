---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/search-groups.html
---

# SearchGroups
<a name="search-groups"></a>

Use the `SearchGroups` operation to search groups in a specified Quick Sight namespace using the supplied filters.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

CLI Input:

```
aws quicksight search-groups
    --region {{us-west-2}}
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
    --filters "[{\"{{Operator}}\": \"StringLike\", \"Name\": \"GROUP_NAME\", \"Value\": \"Mar\"}]"
```

------

For more information about the `SearchGroups` API operation, see [SearchGroups](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchGroups.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
