---
source_url: https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-storage-2.html
---

# Storage
<a name="net-win-storage-2"></a>

The storage services we use across this guide are:
+ Amazon EBS
  + Provides persistent storage for SAP application and database. The EBS volumes can be resized and even the EBS volume type can be changed without disrupting the applications. For more information, see [Requesting Modifications to Your EBS Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html). You will need to [extend the filesystem](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/recognize-expanded-volume-windows.html) to match the extended volume size using the Windows operating system tools.
+ Amazon FSx for Windows File Server
  + Does not need you to explicitly provision storage at all – you simply pay for what you use.
  + Does need regular maintenance, but you can define your own maintenance window as per [Amazon FSx Maintenance Windows](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/maintenance-windows.html).
  + The Amazon FSx Service Level Agreement provides for a service credit if your monthly uptime percentage is below our service commitment in any billing cycle.
+ Amazon S3
  + Does not need you to explicitly provision storage at all – you simply pay for what you use.
  + You can use [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) to set rules that define when objects are transitioned or archived to colder storage, such as S3 Standard-IA, S3 Glacier, or S3 Glacier Deep Archive, and when they expire. These actions happen automatically after being set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
