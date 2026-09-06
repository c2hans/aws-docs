---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/cost_type_size_number_resources_data.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST06-BP02 Select resource type, size, and number based on data
<a name="cost_type_size_number_resources_data"></a>

Select resource size or type based on data about the workload and resource characteristics. For example, compute, memory, throughput, or write intensive. This selection is typically made using a previous (on-premises) version of the workload, using documentation, or using other sources of information about the workload.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Select resource size or type based on workload and resource characteristics, for example, compute, memory, throughput, or write intensive. This selection is typically made using cost modelling, a previous version of the workload (such as an on-premises version), using documentation, or using other sources of information about the workload (whitepapers, published solutions).

**Implementation steps**
+ **Select resources based on data:** Using your cost modeling data, select the expected workload usage level, then select the specified resource type and size.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [Amazon CloudWatch features](https://aws.amazon.com/cloudwatch/features/)
+  [Cost Optimization: EC2 Right Sizing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html)
