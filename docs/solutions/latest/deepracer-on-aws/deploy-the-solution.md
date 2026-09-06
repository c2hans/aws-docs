---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

 [AWS Launch Wizard](deploy-using-aws-launch-wizard.md) is the recommended deployment method for this solution. It provides:
+ A guided configuration experience with detailed help panels at each step
+ A centralized page to monitor the health of all your deployments
+ Indication when there is a more recent version of the solution available for deployment or upgrade

Alternatively, you can deploy the solution directly using an [AWS CloudFormation template](deploy-using-aws-cloudformation.md).

## Overview
<a name="deployment-process-overview"></a>

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security-1.md), and other considerations discussed earlier in this guide.

 **Time to deploy:** Approximately 30 minutes

**Note**
This solution includes data collection metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

**Note**
You are responsible for the cost of the AWS services used while running this solution. For more details, visit the [Cost](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/cost.html) section in this guide and refer to the pricing webpage for each AWS service used in this solution.

## Deploy using AWS CDK commands
<a name="aws-cdk"></a>

You can use the AWS Cloud Development Kit (CDK) and its CLI commands to deploy the solution into your account. To do this, follow the instructions in the [README.md](https://github.com/aws-solutions/deepracer-on-aws/blob/main/README.md) in our GitHub repository.
