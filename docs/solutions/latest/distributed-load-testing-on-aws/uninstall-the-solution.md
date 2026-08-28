---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

You can uninstall the Distributed Load Testing on AWS solution from the AWS Management Console or by using the AWS Command Line Interface (AWS CLI). You must manually delete several retained resources created by this solution. AWS Solutions do not automatically delete storage and logging resources in case you have data to retain. As such, see the following information on how to delete S3 buckets, DynamoDB tables, CloudWatch log groups, and CloudWatch dashboards.

**Important**
Before uninstalling the solution, ensure that all regional stacks have been deleted first. We also recommend deleting all test scenarios through the DLT web console before deleting the main stack. This ensures that runtime-created resources such as CloudWatch dashboards are properly cleaned up.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

### AWS CloudFormation
<a name="aws-cloudformation"></a>

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home/).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose **Delete**.

### AWS Launch Wizard
<a name="aws-launch-wizard"></a>

1. Sign in to the AWS Launch Wizard console.

1. On the [Launch Wizard Deployments](https://console.aws.amazon.com/launchwizard/home#/deployment/list) page, select this solution’s deployment.

1. Choose **Actions**, then **Delete**.

1. Confirm the deletion.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name <installation-stack-name>
```

## Cleaning up ALB \+ ECS Fargate post-deployment resources
<a name="deleting-dns-records"></a>

If you chose the ALB \+ ECS Fargate deployment option, delete the CNAME or Route 53 Alias record that maps your custom domain to the ALB DNS name in your DNS provider. If the ACM certificate is no longer needed, you can also delete it from the [ACM console](https://console.aws.amazon.com/acm/). The AWS WAF web ACL deployed in front of the ALB is automatically deleted when the CloudFormation stack is deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
