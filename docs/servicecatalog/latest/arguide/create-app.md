---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-app.html
---

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Managing applications
<a name="create-app"></a>

 This section describes how to create and manage applications in AppRegistry. After you define an application by specifying its name, description, and share configuration, you can perform the following actions:
+  Associate resources with the application. For more information, see [Managing application definitions](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-resource.html).
+  Associate attribute groups with the application. For more information, see [Managing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attributes.html).
+  Associate tags with the application. For more information, see [Managing tags](https://docs.aws.amazon.com/servicecatalog/latest/arguide/add-tags.html).
+  Share the application with accounts, organizations, and organizational units. For more information, see [Sharing resources with accounts in your organization](https://docs.aws.amazon.com/servicecatalog/latest/arguide/sharing-definitions.html).

**Note**
 When you create an application, AppRegistry vends an AWS user tag called the `awsApplication` tag. The `awsApplication` tag identifies resources associated with an application. For more information, see [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags).

**Topics**
+ [Creating applications](create-apps.md)
+ [Using Application details](access-app-details.md)
+ [Editing applications](edit-apps.md)
+ [Deleting applications](delete-app-details.md)
+ [Managing application resources](associate-resource.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
