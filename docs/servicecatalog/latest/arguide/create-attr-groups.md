---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html
---

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Creating attribute groups
<a name="create-attr-groups"></a>

 With AppRegistry, you create attribute groups to store AWS application metadata.

**To create an attribute group**

1.  Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/)

1.  From the navigation pane, choose **AppRegistry**, and then choose **Attribute groups**. You're directed to the **Attribute groups** screen.

1.  On **Attribute groups**, choose **Create attribute group**.

1.  Under **Create attribute group**, enter a name and description for your attribute group, and provide the JSON schema that captures your metadata taxonomy.

1.  (Optional) Under **Attribute group share configuration**, choose **Turn on cross-account sharing** to share the attribute groups's visibility with your organizational structure. For more information, see [Sharing resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html).

1.  (Optional) Under **Assign attribute group to an application**, select one or more applications to associate to the attribute group. For more information, see [Managing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-app.html).

1.  (Optional) Under **Add tags**, create tags using key/value pairs to assign metadata to the attribute group. For more information, see [Managing tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html).

1.  Choose **Create attribute group**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
