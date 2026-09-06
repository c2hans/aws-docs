---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/templates.html
---

# AWS CloudFormation templates
<a name="templates"></a>

You can download the CloudFormation templates for this solution before deploying it.

## Hub account
<a name="hub-account"></a>

 [![Cost Optimizer for Amazon WorkSpaces template for hub account button](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/cost-optimizer-for-amazon-workspaces/latest/cost-optimizer-for-amazon-workspaces.template)

 **cost-optimizer-for-amazon-workspaces.template** - Use this template to launch Cost Optimizer for Amazon WorkSpaces and all associated components for your hub account (or single account if you only have one account). The default configuration deploys AWS Lambda functions, an Amazon ECS task definition, an Amazon CloudWatch event, and an Amazon S3 bucket. You can customize the template based on your specific needs.

## Spoke accounts
<a name="spoke-accounts"></a>

 [![Cost Optimizer for Amazon WorkSpaces template for spoke accounts button](http://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/cost-optimizer-for-amazon-workspaces/latest/cost-optimizer-for-amazon-workspaces-spoke.template)

 **cost-optimizer-for-amazon-workspaces-spoke.template** − Use this template to launch Cost Optimizer for Amazon WorkSpaces and all associated components for your spoke accounts. Do not deploy this template if you only have one account. The default configuration deploys AWS Lambda functions, an Amazon ECS task definition, an Amazon CloudWatch event, and an Amazon S3 bucket. You can customize the template based on your specific needs.

**Note**
If you have previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.
