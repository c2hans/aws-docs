---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/aws-cloudformation-template.html
---

# AWS CloudFormation template
<a name="aws-cloudformation-template"></a>

You can download the CloudFormation templates for this solution before deploying it. This solution uses AWS CloudFormation to automate the deployment of Distributed Load Testing on AWS. It includes the following AWS CloudFormation templates, which you can download before deployment:

 [https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template) **distributed-load-testing-on-aws.template** - Use this template to launch the solution with the default CloudFront \+ S3 web console hosting. The default configuration deploys the core and supporting services found in the [AWS services in this solution](architecture-details.md#aws-services-in-this-solution) section, but you can customize the template to meet your specific needs.

 [https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-alb-ecs.template) **distributed-load-testing-on-aws-alb-ecs.template** - Use this template to launch the solution with the web console hosted on ECS Fargate behind an ALB. For deployment instructions, refer to [Deploy using ALB \+ ECS Fargate](deploy-alb-ecs-fargate.md).

 [https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws-headless.template) **distributed-load-testing-on-aws-headless.template** - Use this template to launch the solution backend only, with the web console assets available for download. For deployment instructions, refer to [Deploy using headless template (bring your own web server)](deploy-self-hosted.md).

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs. If you have previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.
