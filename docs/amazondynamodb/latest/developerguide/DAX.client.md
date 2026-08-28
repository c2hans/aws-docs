---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.html
---

# Developing with the DynamoDB Accelerator (DAX) client
<a name="DAX.client"></a>

To use DAX from an application, you use the DAX client for your programming language. The DAX client is designed for minimal disruption to your existing Amazon DynamoDB applications—with only a few simple code modifications needed.

**Note**
DAX clients for various programming languages are available on the following site:
[http://dax-sdk.s3-website-us-west-2.amazonaws.com](http://dax-sdk.s3-website-us-west-2.amazonaws.com)

This section demonstrates how to launch an Amazon EC2 instance in your default Amazon VPC, connect to the instance, and run a sample application. It also provides information about how to modify your existing application so that it can use your DAX cluster.

**Topics**
+ [Tutorial: Running a sample application using DynamoDB Accelerator (DAX)](DAX.client.sample-app.md)
+ [Modifying an existing application to use DAX](DAX.client.modify-your-app.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
