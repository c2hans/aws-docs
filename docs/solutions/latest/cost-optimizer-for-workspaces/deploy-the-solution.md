---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

**Important**
Don’t set the parameters **Simulate End of Month Cleanup** and **Terminate workspaces not used for a month** to `Yes` at the same time. Doing this will unexpectedly terminate WorkSpaces.
The **Simulate End of Month Cleanup** parameter will run the solution as if it’s the last day of the month and then terminate WorkSpaces unexpectedly. To use the **Terminate unused WorkSpaces** feature, set **Simulate End of Month Cleanup** to `No`.

This solution uses AWS CloudFormation to automate the deployment of Cost Optimizer for Amazon WorkSpaces on the AWS Cloud. It includes the following AWS CloudFormation templates, which you can download before deployment.

This solution uses [CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates describe the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

## Deployment process overview
<a name="deployment-overview"></a>

Before you launch the automated deployment, please review the [cost](cost.md), [architecture](architecture.md), [network security](security.md), and other considerations discussed in this guide. Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

**Note**
Deploy the hub template first. If you have a single-account environment, you do not need to deploy the spoke template. If you have a multi-account environment, install the spoke template for each WorkSpaces account you wish to monitor.

 **Time to deploy:** Approximately five minutes

 [Step 1: Launch the hub stack](launch-the-stack-hub-template.md)
+ Launch the AWS CloudFormation template in your hub account
+ Enter values for the required parameters
+ Review the other template parameters and adjust, if necessary

 [Step 2: Launch the spoke stack](launch-the-spoke-stack.md)
+ Launch the CloudFormation template in your spoke account
+ Enter values for the required parameters
+ Review the other template parameters and adjust, if necessary

**Note**
This solution includes data collection. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Policy](http://aws.amazon.com/privacy/).
