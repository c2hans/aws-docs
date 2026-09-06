---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you launch the solution, review the [cost](cost.md), [architecture](cost.md), [network security](security-1.md), and other considerations discussed earlier in this guide.

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, download the template, modify the AWS CloudFormation mapping section, and then use the AWS CloudFormation console to upload your updated template and deploy the solution. For more information, see the [Anonymized data collection](reference.md#anonymized-data-collection) section of this guide.
