---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

**Note**
If you previously deployed Workload Discovery on AWS and would like to upgrade to the latest version, refer to [Update the solution](update-the-solution.md).

Follow the step-by-step instructions in this section to configure and deploy the solution into your account.

 **Time to deploy:** Approximately 30 minutes

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [network security](security-1.md), and other considerations discussed in this guide.

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
