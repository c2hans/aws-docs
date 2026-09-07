---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/aws-cloudformation.html
---

# AWS CloudFormation
<a name="aws-cloudformation"></a>

 [AWS CloudFormation](https://aws.amazon.com/cloudformation/) is a service that enables customers to provision and manage almost any AWS resource using a custom template language expressed in YAML or JSON. An CloudFormation template creates infrastructure resources in a group called a *stack*, and allows you to define and customize all components needed to operate your application while retaining full control of these resources. Using templates introduces the ability to implement version control on your infrastructure, and the ability to quickly and reliably replicate your infrastructure.

 CloudFormation offers granular control over the provisioning and management of all application infrastructure components, from low-level components such as route tables or subnet configurations, to high-level components such as CloudFront distributions. CloudFormation is commonly used with other AWS deployment services or third-party tools, combining CloudFormation with more specialized deployment services to manage deployments of application code onto infrastructure components.

 AWS offers extensions to the CloudFormation service in addition to its base features:
+  [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) is an open source software development kit (SDK) to programmatically model AWS infrastructure with TypeScript, JavaScript, Python, Java, or C\#/.NET.
+  [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) (AWS SAM) is an open source framework to simplify building serverless applications on AWS. It provides shorthand syntax to express functions, APIs, databases, and event source mappings.

* Table 1: AWS CloudFormation deployment features *

|  Capability  |  Description  |
| --- | --- |
|  Provision  |  CloudFormation will automatically create and update infrastructure components that are defined in a template. <br /> Refer to [AWS CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) for more details on creating infrastructure using CloudFormation templates.  |
|  Configure  |  CloudFormation templates offer extensive flexibility to customize and update all infrastructure components. <br /> Refer to [CloudFormation Template Anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html) for more details on customizing templates.  |
|  Deploy  |  Update your CloudFormation templates to alter the resources in a stack. Depending on your application architecture, you might need an additional deployment service to update the application version running on your infrastructure. <br /> Refer to [Deploying Applications on Amazon EC2 with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/deploying.applications.html) for more details on how CloudFormation can be used as a deployment solution.  |
|  Scale  |  CloudFormation will not automatically handle infrastructure scaling on your behalf; however, you can configure auto scaling policies for your resources in a CloudFormation template.  |
|  Monitor  |  CloudFormation provides native monitoring of the success or failure of updates to infrastructure defined in a template, as well as *drift detection* to monitor when resources defined in a template do not meet specifications. Additional monitoring solutions will need to be in place for application-level monitoring and metrics. <br /> Refer to [Monitoring the Progress of a Stack Update](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-monitor-stack.html) for more details on how CloudFormation monitors infrastructure updates.  |

 The following diagram shows a common use case for CloudFormation. Here, CloudFormation templates are created to define all infrastructure components necessary to create a simple three-tier web application. In this example, we are using bootstrap scripts defined in CloudFormation to deploy the latest version of our application onto Amazon EC2 instances; however, it is also a common practice to combine additional deployment services with CloudFormation (using CloudFormation only for its infrastructure management and provisioning capabilities). Note that more than one CloudFormation template is used to create the infrastructure. In the diagram, CloudFormation is used to create all infrastructure components including IAM roles, VPCs, subnets, route tables, security groups, and Amazon S3 bucket policies. Separate CloudFormation templates are used to build each domain of the application architecture.

![AWS CloudFormation use case](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/images/image2.png)

*AWS CloudFormation use case *
