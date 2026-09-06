---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_hardware_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS05-BP01 Use the minimum amount of hardware to meet your needs
<a name="sus_sus_hardware_a2"></a>

Use the minimum amount of hardware for your workload to efficiently meet your business needs.

 **Common anti-patterns:**
+  You do not monitor resource utilization.
+  You have resources with a low utilization level in your architecture.
+  You do not review the utilization of static hardware to determine if it should be resized.
+  You do not set hardware utilization goals for your compute infrastructure based on business KPIs.

 **Benefits of establishing this best practice:** Rightsizing your cloud resources helps to reduce a workload’s environmental impact, save money, and maintain performance benchmarks.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimally select the total number of hardware required for your workload to improve its overall efficiency. The AWS Cloud provides the flexibility to expand or reduce the number of resources dynamically through a variety of mechanisms, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/), and meet changes in demand. It also provides [APIs and SDKs](https://aws.amazon.com/developer/tools/) that allow resources to be modified with minimal effort. Use these capabilities to make frequent changes to your workload implementations. Additionally, use rightsizing guidelines from AWS tools to efficiently operate your cloud resource and meet your business needs.

 **Implementation steps**
+  Choose the instances type to best fit your needs.
  + [ How do I choose the appropriate Amazon EC2 instance type for my workload? ](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/)
  + [ Attribute-based instance type selection for Amazon EC2 Fleet. ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html)
  + [ Create an Auto Scaling group using attribute-based instance type selection. ](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html)
+  Scale using small increments for variable workloads.
+  Use multiple compute purchase options in order to balance instance flexibility, scalability, and cost savings.
  +  [On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html) are best suited for new, stateful, and spiky workloads which can’t be instance type, location, or time flexible.
  +  [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) are a great way to supplement the other options for applications that are fault tolerant and flexible.
  +  Leverage [Compute Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) for steady state workloads that allow flexibility if your needs (like AZ, Region, instance families, or instance types) change.
+  Use instance and availability zone diversity to maximize application availability and take advantage of excess capacity when possible.
+  Use the rightsizing recommendations from AWS tools to make adjustments on your workload.
  + [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
  + [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
+  Negotiate service-level agreements (SLAs) that allow for a temporary reduction in capacity while automation deploys replacement resources.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [ Optimizing your AWS Infrastructure for Sustainability, Part I: Compute ](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
+ [ Attirbute based Instance Type Selection for Auto Scaling for Amazon EC2 Fleet ](https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/)
+ [AWS Compute Optimizer Documentation ](https://docs.aws.amazon.com/compute-optimizer/index.html)
+  [Operating Lambda: Performance optimization](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/)
+  [Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/index.html)

 **Related videos:**
+ [ Build a cost-, energy-, and resource-efficient compute environment ](https://www.youtube.com/watch?v=8zsC5e1eLCg)

 **Related examples:**
+ [ Well-Architected Lab - Rightsizing with AWS Compute Optimizer and Memory Utilization Enabled (Level 200) ](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
