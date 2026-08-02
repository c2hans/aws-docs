---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_adapt_to_changes_proactive_adapt_auto.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL07-BP03 Obtain resources upon detection that more resources are needed for a workload
<a name="rel_adapt_to_changes_proactive_adapt_auto"></a>

 Scale resources proactively to meet demand and avoid availability impact.

 Many AWS services automatically scale to meet demand. If using Amazon EC2 instances or Amazon ECS clusters, you can configure automatic scaling of these to occur based on usage metrics that correspond to demand for your workload. For Amazon EC2, average CPU utilization, load balancer request count, or network bandwidth can be used to scale out (or scale in) EC2 instances. For Amazon ECS, average CPU utilization, load balancer request count, and memory utilization can be used to scale out (or scale in) ECS tasks. Using Target Auto Scaling on AWS, the autoscaler acts like a household thermostat, adding or removing resources to maintain the target value (for example, 70% CPU utilization) that you specify.

 AWS Auto Scaling can also do [Predictive Auto Scaling](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/), which uses machine learning to analyze each resource's historical workload and regularly forecasts the future load for the next two days.

 Little’s Law helps calculate how many instances of compute (EC2 instances, concurrent Lambda functions, etc.) that you need.

 *L* = *λW*

 L = number of instances (or mean concurrency in the system)

 λ = mean rate at which requests arrive (req/sec)

 W = mean time that each request spends in the system (sec)

 For example, at 100 rps, if each request takes 0.5 seconds to process, you will need 50 instances to keep up with demand.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Obtain resources upon detection that more resources are needed for a workload. Scale resources proactively to meet demand and avoid availability impact.
  +  Calculate how many compute resources you will need (compute concurrency) to handle a given request rate.
    +  [Telling Stories About Little's Law](https://brooker.co.za/blog/2018/06/20/littles-law.html)
  +  When you have a historical pattern for usage, set up scheduled scaling for Amazon EC2 auto scaling.
    +  [Scheduled Scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
  +  Use AWS predictive scaling.
    +  [Predictive Scaling for EC2, Powered by Machine Learning](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling: How Scaling Plans Work](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html)
+  [AWS Marketplace: products that can be used with auto scaling](https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling)
+  [Managing Throughput Capacity Automatically with DynamoDB Auto Scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)
+  [Predictive Scaling for EC2, Powered by Machine Learning](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/)
+  [Scheduled Scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
+  [Telling Stories About Little's Law](https://brooker.co.za/blog/2018/06/20/littles-law.html)
+  [What Is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
