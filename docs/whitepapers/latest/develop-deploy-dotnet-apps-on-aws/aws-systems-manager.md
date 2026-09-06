---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/aws-systems-manager.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Systems Manager
<a name="aws-systems-manager"></a>

[AWS Systems Manager](https://aws.amazon.com/systems-manager/) is a service for hybrid and cross-platform infrastructure management. Although it is designed to help system administrators maintain their infrastructure resources, some of its capabilities are also useful for developers and DevOps engineers.

One of the most basic application requirements is the need for configuration variables; for example, an external service’s URL, or a database connection string. A common practice is to store these variables in an app.config or web.config configuration file, or to store them in environment variables. However, this requires updating the configuration on all the application servers, which requires a significant effort when working with a multi-server environment. The AWS Systems Manager [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides the alternative of a centralized location for storing configuration variables, allowing configuration values to be updated in a single place and retrieved by all application instances.

Another common use case handled by Systems Manager is the ability to run a particular command or script on multiple servers. For example, you may have a simple PowerShell cmdlet to delete files from a local application cache. One way to run the command is to open a Remote Desktop Protocol (RDP) session to the target servers and manually run the command. However, if the command must run on dozens, hundreds, or even thousands of servers, this approach becomes impractical. Fortunately, you can use the AWS Systems Manager [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html) to securely run the command at any scale.

You can also use AWS Systems Manager [State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) for handling drift-management and ensuring compliance of your target server configurations. State Manager supports [PowerShell Desired State Configuration](https://docs.microsoft.com/powershell/scripting/dsc/overview/) (DSC) and enables you to use DSC [Managed Object Format](https://docs.microsoft.com/windows/win32/wmisdk/managed-object-format--mof-) (MOF) files to define your desired state using declarative language. For example, you can specify the installed state of [Windows Communication Foundation](https://docs.microsoft.com/dotnet/framework/wcf/whats-wcf) (WCF) as the desired state on a server, and DSC will ensure WCF is installed. AWS Systems Manager augments PowerShell DSC through integration with [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).

For more details, see [this entry](https://aws.amazon.com/blogs/mt/run-compliance-enforcement-and-view-compliant-and-non-compliant-instances-using-aws-systems-manager-and-powershell-dsc/) on the [AWS Management Tools Blog](https://aws.amazon.com/blogs/aws/category/management-tools/).

Finally, you can use AWS Systems Manager [Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) to simplify complex operations and define dynamic workflows that orchestrate invocation of AWS Systems Manager or any other AWS APIs in fully automated runbooks.

 For example, you can define these steps in a document to update EC2 instances:
+  Provision a new EC2 instance using an updated AMI
+  Bootstrap the new instance and deploy the application in offline mode
+  Shut down the old instance
+  Switch the new instance into online mode

By specifying these steps in a Systems Manager Automation document, the steps can be saved as a reusable runbook, ensuring updates can be carried out consistently and shared between members of the development and operations teams.
