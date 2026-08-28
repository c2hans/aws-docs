---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-2/ug/create-external-resources.html
---

# Create external resources
<a name="create-external-resources"></a>

This CloudFormation stack creates networking, storage, active directory, and domain certificates (if a PortalDomainName is provided). You must have these external resources available to deploy the product.

You may [ download the recipes template](https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml) before deployment.

**Time to deploy:** Approximately 40-90 minutes

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).
**Note**
Make sure you are in your administrator account.

1. Launch [ the template](https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateURL=https%3A%2F%2Fs3.amazonaws.com%2Faws-hpc-recipes%2Fmain%2Frecipes%2Fres%2Fres_demo_env%2Fassets%2Fbi.yaml) in the console.

   If you are deploying in an AWS GovCloud Region, launch the template in your GovCloud partition account (for example, [ here](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/quickcreate?templateURL=https://s3.amazonaws.com/aws-hpc-recipes/main/recipes/res/res_demo_env/assets/bi.yaml) for the AWS GovCloud (US-West) Region).

1. Enter the template parameters:
**Important**
Use different values for `AdminPassword` and `ServiceAccountPassword` to maintain proper security boundaries between these accounts.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/res/archive/release-minus-2/ug/create-external-resources.html)

1.  Acknowledge all checkboxes in **Capabilities**, and choose **Create stack**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
