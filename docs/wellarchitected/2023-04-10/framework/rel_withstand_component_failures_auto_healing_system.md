---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_withstand_component_failures_auto_healing_system.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL11-BP03 Automate healing on all layers
<a name="rel_withstand_component_failures_auto_healing_system"></a>

 Upon detection of a failure, use automated capabilities to perform actions to remediate.

 *Ability to restart* is an important tool to remediate failures. As discussed previously for distributed systems, a best practice is to make services stateless where possible. This prevents loss of data or availability on restart. In the cloud, you can (and generally should) replace the entire resource (for example, EC2 instance, or Lambda function) as part of the restart. The restart itself is a simple and reliable way to recover from failure. Many different types of failures occur in workloads. Failures can occur in hardware, software, communications, and operations. Rather than constructing novel mechanisms to trap, identify, and correct each of the different types of failures, map many different categories of failures to the same recovery strategy. An instance might fail due to hardware failure, an operating system bug, memory leak, or other causes. Rather than building custom remediation for each situation, treat any of them as an instance failure. Terminate the instance, and allow AWS Auto Scaling to replace it. Later, carry out the analysis on the failed resource out of band.

 Another example is the ability to restart a network request. Apply the same recovery approach to both a network timeout and a dependency failure where the dependency returns an error. Both events have a similar effect on the system, so rather than attempting to make either event a “special case”, apply a similar strategy of limited retry with exponential backoff and jitter.

 *Ability to restart* is a recovery mechanism featured in Recovery Oriented Computing and high availability cluster architectures.

 Amazon EventBridge can be used to monitor and filter for events such as CloudWatch Alarms or changes in state in other AWS services. Based on event information, it can then invoke AWS Lambda, AWS Systems Manager Automation, or other targets to run custom remediation logic on your workload.

 Amazon EC2 Auto Scaling can be configured to check for EC2 instance health. If the instance is in any state other than running, or if the system status is impaired, Amazon EC2 Auto Scaling considers the instance to be unhealthy and launches a replacement instance. If using AWS OpsWorks, you can configure Auto Healing of EC2 instances at the OpsWorks layer level.

 For large-scale replacements (such as the loss of an entire Availability Zone), static stability is preferred for high availability instead of trying to obtain multiple new resources at once.

 **Common anti-patterns:**
+  Deploying applications in instances or containers individually.
+  Deploying applications that cannot be deployed into multiple locations without using automatic recovery.
+  Manually healing applications that automatic scaling and automatic recovery fail to heal.

 **Benefits of establishing this best practice:** Automated healing, even if the workload can only deployed into one location at a time will reduce your mean time to recovery, and ensure availability of the workload.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use Auto Scaling groups to deploy tiers in an workload. Auto scaling can perform self-healing on stateless applications, and add and remove capacity.
  +  [How AWS Auto Scaling Works](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html)
+  Implement automatic recovery on EC2 instances that have applications deployed that cannot be deployed in multiple locations, and can tolerate rebooting upon failures. Automatic recovery can be used to replace failed hardware and restart the instance when the application is not capable of being deployed in multiple locations. The instance metadata and associated IP addresses are kept, as well as the Amazon EBS volumes and mount points to Elastic File Systems or File Systems for Lustre and Windows.
  +  [Amazon EC2 Automatic Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
  +  [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
  +  [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html)
  +  [What is Amazon FSx for Lustre?](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)
  +  [What is Amazon FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
    +  Using AWS OpsWorks, you can configure Auto Healing of EC2 instances at the layer level
      +  [AWS OpsWorks: Using Auto Healing to Replace Failed Instances](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autohealing.html)
+  Implement automated recovery using AWS Step Functions and AWS Lambda when you cannot use automatic scaling or automatic recovery, or when automatic recovery fails. When you cannot use automatic scaling, and either cannot use automatic recovery or automatic recovery fails, you can automate the healing using AWS Step Functions and AWS Lambda.
  +  [What is AWS Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
  +  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
    +  Amazon EventBridge can be used to monitor and filter for events such as CloudWatch Alarms or changes in state in other AWS services. Based on event information, it can then invoke AWS Lambda (or other targets) to run custom remediation logic on your workload.
      +  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
      +  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with automation of your fault tolerance](https://aws.amazon.com/partners/find/results/?keyword=automation)
+  [AWS Marketplace: products that can be used for fault tolerance](https://aws.amazon.com/marketplace/search/results?searchTerms=fault+tolerance)
+  [AWS OpsWorks: Using Auto Healing to Replace Failed Instances](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autohealing.html)
+  [Amazon EC2 Automatic Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
+  [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
+  [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html)
+  [How AWS Auto Scaling Works](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html)
+  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
+  [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  [What is AWS Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
+  [What is Amazon FSx for Lustre?](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)
+  [What is Amazon FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

 **Related videos:**
+  [Static stability in AWS: AWS re:Invent 2019: Introducing The Amazon Builders’ Library (DOP328)](https://youtu.be/sKRdemSirDM?t=704)

 **Related examples:**
+  [Well-Architected lab: Level 300: Implementing Health Checks and Managing Dependencies to Improve Reliability](https://wellarchitectedlabs.com/Reliability/300_Health_Checks_and_Dependencies/README.html)
