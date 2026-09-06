---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/operational-excellence.html
---

# Operational excellence pillar
<a name="operational-excellence"></a>

The operational excellence pillar of the AWS Well-Architected Framework focuses on running and monitoring systems, and continually improving processes and procedures. The following recommendations can help you meet the operational excellence design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Automating changes
+ Responding to events
+ Defining standards to manage daily operations

## Perform operations as code
<a name="perform-operations-as-code"></a>
+ Apply infrastructure as a code (IaC) to deploy FSx for Windows File Server. You can use the [Amazon FSx for Windows File Server Quick Start](https://github.com/aws-quickstart/quickstart-fsx-windows-file-server) to implement your file system on AWS.
+ Automate FSx for Windows File Server operational procedures whenever possible. For example, it's a best practice to automate tasks such as [turning on user storage quotas in Track mode and data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/admin-best-practices-fsxw.html), and upgrading from a single Availability Zone to multiple Availability Zones.

## Make frequent, small, reversible changes
<a name="make-frequent-small-reversible-changes"></a>
+ Store IaC templates and scripts in a source control service, such as GitHub or GitLab.
+ Require IaC deployments to use a continuous integration and continuous delivery (CI/CD) service, such as [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html). These services compile, test, and deploy code in a test environment, before infrastructure is deployed on AWS and within FSx for Windows File Server.
+ Mount file shares for the correct set of users by using group policies.

## Refine operational procedures frequently
<a name="refine-operational-procedures-frequently"></a>
+ Test your infrastructure changes in a test environment that has the same configuration as your production environment (same Active Directory, network configurations, file system size and configuration, and Windows features such as data deduplication and shadow copies) before you deploy any changes to production.

## Anticipate failure
<a name="anticipate-failure"></a>
+ Create a monitoring plan where you can use file system metrics to monitor your storage and performance usage, and understand your usage patterns.
+ Set notifications to monitor the health of FSx for Windows File Server file systems. For more information, see the blog post [Monitoring the health of Amazon FSx file systems using Amazon EventBridge and AWS Lambda](https://aws.amazon.com/blogs/storage/monitoring-the-health-of-amazon-fsx-file-systems-using-amazon-eventbridge-and-aws-lambda/).
+ Validate your Active Directory configuration regularly―the availability of your file systems depend on it. For more information, see [Validating your Active Directory configuration](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/validate-ad-config.html) in the Amazon FSx documentation.
+ Validate connectivity to your Active Directory domain controllers on a regular basis and set up an alarm in case the validation fails. For more information, see [Validating connectivity to your Active Directory domain controllers](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/validate-ad-domain-controllers.html) in the Amazon FSx documentation.
+ Automatically scale storage and throughput capacity for your FSx for Windows File Server file systems based on utilization metrics. For more information, see:
  + [Increasing the storage capacity of an FSx for Windows File Server file system dynamically ](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html#automate-storage-capacity-increase)in the Amazon FSx documentation.
  + [How to modify throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html#increase-throughput-capacity) in the Amazon FSx documentation.
  + [Amazon FSx for Windows File Server - Automatic Storage and Throughput Capacity Scaling](https://www.youtube.com/watch?v=1p0tnll1l14) on the AWS YouTube channel.
