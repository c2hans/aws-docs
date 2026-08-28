---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/uninstall-the-guidance.html
---

# Uninstall the guidance
<a name="uninstall-the-guidance"></a>

 You can uninstall the guidance from the AWS Management Console or by using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI). You must manually delete [several resources](#manually-uninstalling-resources) created by this guidance. This guidance doesn't automatically delete these resources in case you have stored data to retain.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1.  On the **Stacks** page, select this guidance's installation stack.

1.  Choose **Delete**.

## Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

 Determine whether the AWS CLI is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name {{<installation-stack-name>}}
```

## Manually uninstalling resources
<a name="manually-uninstalling-resources"></a>

 The following resources will be retained even after the guidance is deleted. Refer to the following links to manually delete the resources:
+  [AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-repository.html)
+  [Amazon CloudWatch log groups](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)
+  [Amazon S3 CodePipeline artifact bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)
+  [Amazon S3 CodeBuild source code bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)
+  [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-deleting.html)
+  [AWS Network Firewall firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-deleting.html)
+  [AWS Network Firewall rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-deleting.html)
+  [Inspection VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#VPC_Deleting)
+  [AWS Transit Gateway attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#delete-vpc-attachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Network Inspection on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
