---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/arguide/getting-started-ar.html
---

AWS Service Catalog AppRegistry is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Service Catalog AppRegistry availability change](https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-registry-availability-change.html).

# Getting started with AppRegistry
<a name="getting-started-ar"></a>

 When you create a repository for all of your AWS applications and associated resources, you increase the visibility and governance of these applications, which helps you define and manage application metadata and better understand the AWS applications and resources in your organization.

**Key tasks in AppRegistry**
 The following topics help you get started with AppRegistry.
+  Create an application to group resources and metadata. For more information, see [Creating applications](create-apps.md).
+  Add a user tag called `awsApplication` tag to resources, so you can identify which resources are associated with an application. For more information, see [the `awsApplication` tag](https://docs.aws.amazon.com/servicecatalog/latest/arguide/overview-appreg.html#ar-user-tags).
+  Associate resources with your application. For more information, see [Associating and disassociating application resources.](associate-resources.md)
+  Share your application to other accounts in your organization. For more information, see [Sharing resources with accounts in your organization](sharing-definitions.md).
+  Create and associate an attribute group with your application. For more information, see [Managing attribute groups.](associate-attributes.md)
+  Create tags to organize your application resources. For more information, see [Managing tags](add-tags.md).

**Note**
 This section includes a tutorial that describes how to create applications and attribute groups in the console and programatically with the AWS CLI using the [AppRegistry API](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_Operations_AWS_Service_Catalog_App_Registry.html).

**Topics**
+ [Tutorial: Create your first application and attribute group in AppRegistry](tutorial-appreg.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
