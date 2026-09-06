---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_dev_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS06-BP02 Keep your workload up-to-date
<a name="sus_sus_dev_a3"></a>

Keep your workload up-to-date to adopt efficient features, remove issues, and improve the overall efficiency of your workload.

 **Common anti-patterns:**
+ You assume your current architecture is static and will not be updated over time.
+  You do not have any systems or a regular cadence to evaluate if updated software and packages are compatible with your workload.

 **Benefits of establishing this best practice:** By establishing a process to keep your workload up to date, you can adopt new features and capabilities, resolve issues, and improve workload efficiency.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Up to date operating systems, runtimes, middlewares, libraries, and applications can improve workload efficiency and make it easier to adopt more efficient technologies. Up to date software might also include features to measure the sustainability impact of your workload more accurately, as vendors deliver features to meet their own sustainability goals. Adopt a regular cadence to keep your workload up to date with the latest features and releases.

 **Implementation steps**
+  Define a process and a schedule to evaluate new features or instances for your workload. Take advantage of agility in the cloud to quickly test how new features can improve your workload to:
  +  Reduce sustainability impacts.
  +  Gain performance efficiencies.
  +  Remove barriers for a planned improvement.
  +  Improve your ability to measure and manage sustainability impacts.
+  Inventory your workload software and architecture and identify components that need to be updated.
  +  You can use [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to collect operating system (OS), application, and instance metadata from your Amazon EC2 instances and quickly understand which instances are running the software and configurations required by your software policy and which instances need to be updated.
+  Understand how to update the components of your workload.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_dev_a3.html)
+  Use automation for the update process to reduce the level of effort to deploy new features and limit errors caused by manual processes.
  +  You can use [CI/CD](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/) to automatically update AMIs, container images, and other artifacts related to your cloud application.
  +  You can use tools such as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) to automate the process of system updates, and schedule the activity using [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [What's New with AWS](https://aws.amazon.com/new/?ref=wellarchitected&ref=wellarchitected)
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)

 **Related examples:**
+  [Well-Architected Labs - Inventory and Patch Management](https://wellarchitectedlabs.com/operational-excellence/100_labs/100_inventory_patch_management/)
+  [Lab: AWS Systems Manager](https://mng.workshop.aws/ssm.html)
