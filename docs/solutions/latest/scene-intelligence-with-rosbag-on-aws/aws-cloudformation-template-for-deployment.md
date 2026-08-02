---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/aws-cloudformation-template-for-deployment.html
---

# AWS CloudFormation template for deployment
<a name="aws-cloudformation-template-for-deployment"></a>

You can download the CloudFormation template for this solution before deploying it. This solution uses a separate CloudFormation template to handle the deployment workflow.

 [https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-create.template](https://solutions-reference.s3.amazonaws.com/scene-intelligence-with-rosbag-on-aws/latest/scene-intelligence-with-rosbag-on-aws-create.template) **scene-intelligence-with-rosbag-on-aws-create.template -** Use this template to launch the solution and all associated components. The default configuration deploys the core and supporting services found in the [AWS services in this solution](aws-services-in-this-solution.md) section orchestrated by an open source GitOps library called `seedfarmer`, but you can customize the template to meet your specific needs.

**Note**
CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

## Prerequisites for deployment
<a name="prerequisites-for-deployment"></a>

This AWS CloudFormation template deploys Scene Intelligence with Rosbag on AWS in the AWS Cloud. You must meet the following prerequisites before launching the stack:
+ Administrative permissions, or permissions sufficient to create and configure the AWS services used by these stacks.
