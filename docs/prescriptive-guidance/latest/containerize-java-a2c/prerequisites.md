---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/prerequisites.html
---

# Prerequisites and setup
<a name="prerequisites"></a>

There are [prerequisites](https://docs.aws.amazon.com/app2container/latest/UserGuide/a2c-setup.html) for setting up and using AWS App2Container (A2C). In most cases, applications are running in a private network. It might not be possible for the application server to meet the requirements to containerize your application and deploy to AWS or to install the Docker engine on the application server. In such cases, a consolidated virtual machine (VM) can be provisioned and used as a platform to containerize the applications running on the application servers. Choose a worker machine that can be used for modernizing multiple applications and application servers. The worker machine should meet the following requirements:
+ Must have internet connectivity or alternate connection with access to necessary AWS services.
+ Have connectivity to the application servers to copy the tar package from the application server by using Secure Copy Protocol (SCP) or Secure Shell (SSH). For the connection, allow access to port 22 from the worker machine.
+ Docker must be installed only on the worker machine.

For scenarios where the application server can only be accessed remotely, a worker machine can use the remote option to run all the App2Container tasks. Running remotely requires the following configuration:
+ SSH connectivity from the worker machine to the application server
+ SSH credentials of the application server stored in AWS Secrets Manager and configured on the worker machine

For scenarios where there is no direct connection between the application server and the worker machine, you must use a bridge machine. The bridge machine can connect to the application server and the worker machine. The bridge machine transfers artifacts from the application server to the worker machine.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
