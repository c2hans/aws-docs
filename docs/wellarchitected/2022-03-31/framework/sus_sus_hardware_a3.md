---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_hardware_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS05-BP02 Use instance types with the least impact
<a name="sus_sus_hardware_a3"></a>

 Continually monitor the release of new instance types and take advantage of energy efficiency improvements, including those instance types designed to support specific workloads such as machine learning training, inference, and video transcoding.

 **Common anti-patterns:**
+  You are only using one family of instances.
+  You are only using x86 instances.
+  You specify one instance type in your Amazon EC2 Auto Scaling configuration.
+  You use AWS instances in a manner that they were not designed for (for example, you use compute-optimized instances for a memory-intensive workload).
+  You do not evaluate new instance types regularly.
+  You do not check recommendations from AWS rightsizing tools such as [AWS Compute Optimizer.](https://aws.amazon.com/compute-optimizer/)

 **Benefits of establishing this best practice:** By using energy-efficient and right-sized instances, you are able to greatly reduce the environmental impact and cost of your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Learn and explore instance types which can lower your workload environmental impact.
  +  Subscribe to [What's New with AWS](https://aws.amazon.com/new/) to be up-to-date with the latest AWS technologies and instances.
  +  Learn about different AWS instance types.
  +  Learn about AWS Graviton-based instances which offer the best performance per watt of energy use in Amazon EC2 by watching [re:Invent 2020 - Deep dive on AWS Graviton2 processor-powered Amazon EC2 instances](https://www.youtube.com/watch?v=NLysl0QvqXU) and [Deep dive into AWS Graviton3 and Amazon EC2 C7g instances](https://www.youtube.com/watch?v=WDKwwFQKfSI&ab_channel=AWSEvents).
+  Plan and transition your workload to instance types with the least impact.
  +  Define a process to evaluate new features or instances for your workload. Take advantage of agility in the cloud to quickly test how new instance types can improve your workload environmental sustainability. Use proxy metrics to measure how many resources it takes you to complete a unit of work.
  +  If possible, modify your workload to work with different numbers of vCPUs and different amounts of memory to maximize your choice of instance type.
  +  Consider transitioning your workload to Graviton-based instances to improve the performance efficiency of your workload (see [AWS Graviton Fast Start](https://aws.amazon.com/ec2/graviton/fast-start/) and [AWS Graviton2 for ISVs](https://docs.aws.amazon.com/whitepapers/latest/aws-graviton2-for-isv/welcome.html)). Keep in mind the [considerations when transitioning workloads to AWS Graviton-based Amazon Elastic Compute Cloud instances.](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md)
  +  Consider selecting the AWS Graviton option in your usage of [AWS managed services.](https://github.com/aws/aws-graviton-getting-started/blob/main/managed_services.md)
  +  Migrate your workload to Regions that offer instances with the least sustainability impact and still meet your business requirements.
  +  For machine learning workloads, use Amazon EC2 instances which are based on custom Amazon Machine Learning chips such as [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/), and [Amazon EC2 DL1.](https://aws.amazon.com/ec2/instance-types/dl1/)
  +  Use [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to right size ML inference endpoint.
  +  For workloads with real time video transcoding, use [Amazon EC2 VT1 Instances.](https://aws.amazon.com/ec2/instance-types/vt1/)
  +  For spikey workloads (workloads with infrequent requirements for additional capacity), use [burstable performance instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
  +  For stateless and fault-tolerant workloads, use [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) to increase overall utilization of the cloud, and reduce the sustainability impact of unused resources.
+  Operate and optimize your workload instance.
  +  For ephemeral workloads, evaluate [instance Amazon CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics) such as `CPUUtilization` to identify if the instance is idle or under-utilized.
  +  For stable workloads, check AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) at regular intervals to identify opportunities to optimize and right-size the instances.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
+  [AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/)
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/)
+  [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/)
+  [Amazon EC2 Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
+  [Amazon EC2 Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)
+  [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)
+  [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
+  [Amazon EC2 VT1 Instances](https://aws.amazon.com/ec2/instance-types/vt1/)
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)

 **Related videos:**
+  [Deep dive on AWS Graviton2 processer-powered Amazon EC2 instances](https://www.youtube.com/watch?v=NLysl0QvqXU)
+  [Deep dive into AWS Graviton3 and Amazon EC2 C7g instances](https://www.youtube.com/watch?v=WDKwwFQKfSI&ab_channel=AWSEvents)

 **Related examples:**
+  [Lab: Rightsizing Recommendations](https://wellarchitectedlabs.com/cost/100_labs/100_aws_resource_optimization/)
+  [Lab: Rightsizing with Compute Optimizer](https://wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/)
+  [Lab: Optimize Hardware Patterns and Observe Sustainability KPIs](https://wellarchitectedlabs.com/sustainability/200_labs/200_optimize_hardware_patterns_observe_sustainability_kpis/)
