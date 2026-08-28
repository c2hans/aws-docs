---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Creating Parameter Store parameters in Systems Manager
<a name="sysman-paramstore-su-create"></a>

A *parameter* is any piece of data stored in Parameter Store, such as a block of text, a list of names, an AMI ID, a license key, and so on. You can centrally and securely reference this data in your scripts, commands, and SSM documents.

Parameter Store provides support for the following parameter types:
+ `String`
+ `StringList`
+ `SecureString`

For more information about the preceding types, see [Parameter Store reference](what-is-a-parameter.md).

In the following sections, you learn how to create Parameter Store parameters using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell (Tools for Windows PowerShell).

**Topics**
+ [Creating a Parameter Store parameter using the console](parameter-create-console.md)
+ [Creating a Parameter Store parameter using the AWS CLI](param-create-cli.md)
+ [Creating a Parameter Store parameter using Tools for Windows PowerShell](param-create-ps.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
