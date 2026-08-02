---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_hardware_a5.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS05-BP04 Optimize your use of GPUs
<a name="sus_sus_hardware_a5"></a>

 Graphics Processing Units (GPUs) can be a source of high-power consumption, and many GPU workloads are highly variable, such as rendering, transcoding, and machine learning training and modeling. Only run GPU instances for the time needed, and decommission them with automation when not required to minimize resources consumed.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use GPUs only for tasks where they’re more efficient than CPU-based alternatives.
+  Use automation to release GPU instances when not in use.
+  Use flexible graphics acceleration rather than dedicated GPU instances.
+  Take advantage of custom-purpose hardware that is specific to your workload.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/)
+  [Accelerated Computing for EC2 Instances](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
+  [Amazon EC2 VT1 Instances](https://aws.amazon.com/ec2/instance-types/vt1/)
+  [Amazon Elastic Graphics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-graphics.html)
