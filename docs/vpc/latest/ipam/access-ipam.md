---
source_url: https://docs.aws.amazon.com/vpc/latest/ipam/access-ipam.html
---

# Access IPAM
<a name="access-ipam"></a>

As with other AWS services, you can create, access, and manage your IPAM using the following methods:
+ **AWS Management Console**: Provides a web interface that you can use to create and manage your IPAM. See [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/).
+ **AWS Command Line Interface (AWS CLI)**: Provides commands for a broad set of AWS services, including Amazon VPC. The AWS CLI is supported on Windows, macOS, and Linux. To get the AWS CLI, see [AWS Command Line Interface](https://aws.amazon.com/cli/).
+ **AWS SDKs**: Provide language-specific APIs. The AWS SDKs take care of many of the connection details, such as calculating signatures, handling request retries, and handling errors. For more information, see [AWS SDKs](http://aws.amazon.com/tools/#SDKs).
+ **Query API**: Provides low-level API actions that you call using HTTPS requests. Using the Query API is the most direct way to access IPAM. However, it requires your application to handle low-level details such as generating the hash to sign the request, and handling errors. For more information, see Amazon IPAM actions in the [Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/).

This guide primarily focuses on using the AWS Management Console to create, access, and manage your IPAM. In each description of how to complete a process in the console, we include links to the *AWS CLI Command Reference* so that you can do the same tasks by using the AWS CLI.

If you are a first-time user of IPAM, review [How IPAM works](how-it-works-ipam.md) to learn about the role of IPAM in Amazon VPC and then continue with the instructions in [Configure integration options for your IPAM](choose-single-user-or-orgs-ipam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
