---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/well-architected-best-practices-fsx-windows/performance-efficiency.html
---

# Performance efficiency pillar
<a name="performance-efficiency"></a>

The performance efficiency pillar of the AWS Well-Architected Framework focuses on structured and streamlined allocation of IT and computing resources. The following recommendations can help you meet the** **performance efficiency design principles and architectural best practices for Amazon FSx for Windows File Server.

**Key focus areas**
+ Selecting resource types and sizes optimized for workload requirements
+ Monitoring performance
+ Maintaining efficiency as business needs evolve

## Democratize advanced technologies and make their implementation easier for your team
<a name="democratize-advanced-technologies-and-make-their-implementation-easier-for-your-team"></a>
+ Use AWS services to tackle the complex tasks that would take more time and effort to do it yourself. For example, use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) to migrate your data, and [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) runbooks and [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates to automate manual tasks.

## Scale globally if needed
<a name="scale-globally-if-needed"></a>
+ Replicate the FSx for Windows File Server file system across multiple AWS Regions. For more information, see the AWS blog post [How to replicate Amazon FSx for Windows File Server data across AWS Regions](https://aws.amazon.com/blogs/storage/how-to-replicate-amazon-fsx-file-server-data-across-aws-regions/).

## Use serverless architectures
<a name="use-serverless-architectures"></a>
+ Use serverless services, such as AWS Lambda and AWS Step Functions, to extend the functionality of Amazon FSx for Windows File Server. For example, serverless products can help you configure more efficient enforcement of security controls. For more information, see the blog post [Automating Amazon FSx for Windows File Server configuration for more efficient enforcement of security controls](https://aws.amazon.com/blogs/modernizing-with-aws/automating-amazon-fsx-for-windows-file-server-configuration/).

## Test and experiment often
<a name="test-and-experiment-often"></a>
+ Test your infrastructure changes in a test environment that has the same configuration as your production environment (same Active Directory, network configurations, file system size and configuration, and Windows features, such as data deduplication and shadow copies) before you deploy any changes to production.
+ Stay up to date on new services and features, and regularly test them in your test environment.

## Consider mechanical sympathy
<a name="consider-mechanical-sympathy"></a>

[Mechanical sympathy](https://aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.mechanical-sympathy.en.html) refers to using a tool with an understanding of how it operates best.
+ Back up your file systems regularly, especially before making a change to an FSx for Windows File Server file system that is running. For more information, see [Working with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html) in the Amazon FSx documentation.
+ Use Amazon CloudWatch metrics to generate alarm-based notifications for FSx for Windows File Server. For more information, see [Creating CloudWatch alarms to monitor Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/creating_alarms.html) in the Amazon FSx documentation.

## Improve performance
<a name="improve-performance"></a>
+ Automatically scale storage and throughput capacity for your FSx for Windows File Server file systems based on utilization metrics. For more information, see:
  + [Increasing the storage capacity of an FSx for Windows File Server file system dynamically ](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-storage-capacity.html#automate-storage-capacity-increase)in the Amazon FSx documentation.
  + [How to modify throughput capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html#increase-throughput-capacity) in the Amazon FSx documentation.
  + [Amazon FSx for Windows File Server - Automatic Storage and Throughput Capacity Scaling](https://www.youtube.com/watch?v=1p0tnll1l14) on the AWS YouTube channel.
+ Use Microsoft Distributed File System (DFS) Namespaces to scale out performance across multiple file systems in the same namespace up to tens of gigabits per second (Gbps) and millions of IOPS. For more information, see [Walkthrough 6: Scaling out performance with shards](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/scale-out-performance.html) in the Amazon FSx documentation.
+ Use enhanced performance metrics to optimize the performance of your FSx for Windows File Server file systems. For more information, see the blog post [Optimizing Amazon FSx for Windows File Server performance with new metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/).
