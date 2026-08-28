---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/uninstall-the-solution.html
---

# Uninstall the solution
<a name="uninstall-the-solution"></a>

 You can uninstall the Dynamic Object and Rule Extensions for AWS Network solution from the AWS Management Console or by using the AWS Command Line Interface. You must manually delete S3, Lambda, and other resources created by this solution. AWS Solutions Implementations do not automatically delete DynamoDB tables in case you have stored data to retain.

## Using the AWS Management Console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [CloudFormation console;](https://console.aws.amazon.com/cloudformation/home).

1.  On the **Stacks** page, select this solution’s installation stack.

1.  Choose **Delete**.

## Using the AWS Command Line Interface (CLI)
<a name="using-the-aws-command-line-interface-cli"></a>

 To uninstall the solution
+  Run `cdk destroy` from the `sources` folder, or
+  Delete the stack from the CloudFormation console. Note that the cross-account access stacks also need to be deleted for this method.

**Note**
 For data retention and audit purpose the following resources will not be removed.
 OPA policy bucket and its encryption key in KMS.
 All four domain data DynamoDB tables (including the table for rule bundle, rule, object and audit) and their encryption keys in KMS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
