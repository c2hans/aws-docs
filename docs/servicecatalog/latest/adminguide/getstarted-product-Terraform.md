---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted-product-Terraform.html
---

# Step 2: Create a Terraform product
<a name="getstarted-product-Terraform"></a>

After installing the Terraform provisioning engine, you are ready to create a HashiCorp Terraform product in AWS Service Catalog. In this tutorial, you create a Terraform product containing a simple Amazon S3 bucket.

**To create a Terraform product**

1. Open the AWS Service Catalog console at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/) and sign in as an admin user.

1. Navigate to the **Administration** section, and then choose **Product list**.

1. Choose **Create product**.

1. On the **Create product** page in the Product details section, choose the **External** or **Terraform Cloud** product type. Service Catalog uses the *External* product type to support Terraform Community Edition products.

1. Enter the following product details:
   + **Product name** – **Simple S3 bucket**
   + **Product description** – Terraform product containing an Amazon S3 bucket.
   + **Owner** – **IT**
   + **Distributor** – *(blank)*

1. On the **Version details** pane, choose **upload a template file** and then choose **Choose file**. Select the file you downloaded in [Step 1: Terraform configuration file download](getstarted-template-Terraform.md).

1. Enter the following:
   + **Version name** – **v1.0**
   + **Version description** – **Base Version**

1. In the **Support details** section, enter the following and then choose **Create product**.
   + **Email contact** – **ITSupport@example.com**
   + **Support link** – **https://wiki.example.com/IT/support**
   + **Support description** – **Contact the IT department for issues deploying or connecting to this product.**

1. Choose **Create product**.

After successfully creating the product, AWS Service Catalog displays a confirmation banner on the product page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
