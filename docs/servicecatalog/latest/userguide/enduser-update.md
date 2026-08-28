---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-update.html
---

# Updating provisioned products
<a name="enduser-update"></a>

When you want to use a new version of a product or configure a provisioned product with updated parameter values, you must update it. You can also change tags or take other actions on a provisioned product if your administrator has enabled these features.

You can only update provisioned products if they are in the **Available** or **Tainted** state.

You cannot update failed provisioned products or provisioned products that are in the process of starting, updating, or terminating. See [Viewing Provisioned Product Status](enduser-viewstack.md#enduser-viewstack-status) for more information on provisioned product status.

**Note**
 If the provisioned product you launch is a stack set, you own the stack set. Ownership of individual stacks depends whether or not you have access to the accounts where the stacks were deployed. For more information, see [Working with CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

**To update a provisioned product**

1. From the Provisioned products list, choose the provisioned product, and then choose** Actions**.

1. To update, choose **Update** and enter your parameters.

1. If your administrator allows you to update tags on this provisioned product, you see a **Tag Updates** section.

1. Choose **Update**. The provisioned product status changes to an **Under change** status.

   To see the output from the update operation, view the **Events** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
