---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_user_a2.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP01 Scale infrastructure with user load
<a name="sus_sus_user_a2"></a>

 Identify periods of low or no utilization and scale down resources to eliminate excess capacity and improve efficiency.

**Common anti-patterns:**
+ You do not scale your infrastructure with user load.
+ You manually scale your infrastructure all the time.
+ You leave increased capacity after a scaling event instead of scaling back down.

 **Benefits of establishing this best practice:** Configuring and testing workload elasticity will help reduce workload environmental impact, save money, and maintain performance benchmarks. You can take advantage of elasticity in the cloud to automatically scale capacity during and after user load spikes to make sure you are only using the exact number of resources needed to meet the needs of your customers.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Elasticity matches the supply of resources you have against the demand for those resources. Instances, containers, and functions provide mechanisms for elasticity, either in combination with automatic scaling or as a feature of the service. Use elasticity in your architecture to ensure that workload can scale down quickly and easily during the period of low user load:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_user_a2.html)
+  Verify that the metrics for scaling up or down are validated against the type of workload being deployed. If you are deploying a video transcoding application, 100% CPU utilization is expected and should not be your primary metric. You can use a [customized metric](https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/) (such as memory utilization) for your scaling policy if required. To choose the right metrics, consider the following guidance for Amazon EC2:
  +  The metric should be a valid utilization metric and describe how busy an instance is.
  +  The metric value must increase or decrease proportionally to the number of instances in the Auto Scaling group.
+  Use [dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) instead of [manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html) for your Auto Scaling group. We also recommend that you use [target tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) in your dynamic scaling.
+  Verify that workload deployments can handle both scale-up and scale-down events. Create test scenarios for scale-down events to ensure that the workload behaves as expected. You can use [Activity history](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html) to test and verify a scaling activity for an Auto Scaling group.
+  Evaluate your workload for predictable patterns and proactively scale as you anticipate predicted and planned changes in demand. Use [Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/) to eliminate the need to overprove capacity.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html)
+  [Predictive Scaling for EC2, Powered by Machine Learning](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/)
+  [Analyze user behavior using Amazon OpenSearch Service, Amazon Data Firehose and Kibana](https://aws.amazon.com/blogs/database/analyze-user-behavior-using-amazon-elasticsearch-service-amazon-kinesis-data-firehose-and-kibana/)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [Monitoring DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
+  [Introducing Native Support for Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/)
+  [How to create an Amazon EC2 Auto Scaling policy based on a memory utilization metric (Linux)](https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/)
+  [Introducing Karpenter - An Open-Source, High-Performance Kubernetes Cluster Autoscaler](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/)

 **Related videos:**
+  [Better, faster, cheaper compute: Cost-optimizing Amazon EC2 (CMP202-R1)](https://www.youtube.com/watch?v=_dvh4P2FVbw)

 **Related examples:**
+  [Lab: Amazon EC2 Auto Scaling Group Examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples)
+  [Lab: Implement Autoscaling with Karpenter](https://www.eksworkshop.com/beginner/085_scaling_karpenter/)
