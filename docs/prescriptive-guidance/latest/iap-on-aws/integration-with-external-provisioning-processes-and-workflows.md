---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/integration-with-external-provisioning-processes-and-workflows.html
---

# Integration with external provisioning processes and workflows
<a name="integration-with-external-provisioning-processes-and-workflows"></a>

You can interact with Service Catalog components by using AWS SDK APIs or the AWS CLI. You can use the [AWS SDK Service Catalog API](https://docs.aws.amazon.com/servicecatalog/latest/dg/service-catalog-api-overview.html) to manage Service Catalog products from any tool that can integrate Service Catalog API calls. The API covers all aspects of Service Catalog creation and management. For example, Terraform supports the launching (provisioning) of Service Catalog products by calling the AWS SDK Service Catalog API in its Launch Wizard. For more information, see [Launch AWS Service Catalog products with Terraform](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog-terraform.html) in the AWS documentation.

You can also call the AWS CLI Service Catalog commands to perform actions on Service Catalog. For more information about supported commands, see [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html) in the AWS CLI Command Reference.
