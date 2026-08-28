---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/afc-setup-steps.html
---

# Set up for customization
<a name="afc-setup-steps"></a>

The next sections give steps to set up Account Factory for the customization process. We recommend that you set up [delegated admin](https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-delegated-admin.html) for the hub account, before you begin these steps.

**Summary**
+ **Step 1. Create the required role.** Create an IAM role that grants permission for AWS Control Tower to have access to the (hub) account, where the Service Catalog products, also called blueprints, are stored.
+ **Step 2. Create the AWS Service Catalog product.** Create the AWS Service Catalog product (also called a “blueprint product”) that you'll need for baselining the custom account.
+ **Step 3. Review your custom blueprint.** Inspect the AWS Service Catalog product (blueprint) that you created.
+ **Step 4. Call your blueprint to create a customized account.** Enter the blueprint product information and the role information into the proper fields in Account Factory, in the AWS Control Tower console, while creating the account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
