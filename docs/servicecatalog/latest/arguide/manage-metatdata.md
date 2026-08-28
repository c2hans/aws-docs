---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/arguide/manage-metatdata.html
---

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Viewing attribute group metadata
<a name="manage-metatdata"></a>

 An attribute group is an open JSON object where you define the metadata for a resource. Metadata is data that describes other data. For more information, see [Attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#attr-groups) on [Overview of AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html).

**To view attribute group metadata**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/)

1.  From the navigation pane, choose **AppRegistry**, and then choose **Attribute groups**. You're directed to the **Attribute groups** screen where you can view all of your attribute groups.

1.  On **Attribute groups**, choose the name of the attribute groups that you want to view. Or select the attribute group that you want to edit, and then choose **View**. You're directed to the **Attribute group details** screen.

1.  On **Attribute group details**, choose **Metadata**.

 **Example: Attribute group metadata**

```
{
 "Team" : "WebTeam",
 "Department": "10006",
 "ParentDept": "Research",
 "ContactAlias": "research@team.com"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
