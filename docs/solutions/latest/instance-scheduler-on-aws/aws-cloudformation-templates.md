---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation templates specify the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the templates.

You can download the CloudFormation templates for this solution before deploying it.

 [![View template](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/view-template-button.png)](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws.template) **instance-scheduler-on-aws.template** - Use this template to launch the solution and all associated components. The default configuration deploys an AWS Lambda function, an Amazon DynamoDB table, an Amazon CloudWatch event, and CloudWatch custom metrics, but you can also customize the template based on your specific needs.

 [![View template](http://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/images/view-template-button.png)](https://s3.amazonaws.com/solutions-reference/instance-scheduler-on-aws/latest/instance-scheduler-on-aws-remote.template)

 **instance-scheduler-on-aws-remote.template** - Use this template to launch the cross-account role used by the solution to schedule instances in spoke accounts. For deployments using AWS Organizations, deploying the template also registers the spoke account with the hub, requiring no manual configuration.

**Note**
If you previously deployed this solution, see [Update the solution](update-the-solution.md) for update instructions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Instance Scheduler on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
