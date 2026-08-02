---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_software_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP02 Remove or refactor workload components with low or no use
<a name="sus_sus_software_a3"></a>

 Monitor workload activity to identify changes in utilization of individual components over time. Remove components that are unused and no longer required, and refactor components with little utilization to limit wasted resources.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Analyze load (using indicators such as transaction flow and API calls) on functional components to identify unused and underutilized components.
+  Retire components that are no longer needed.
+  Refactor underutilized components.
+  Consolidate underutilized components with other resources to improve utilization efficiency.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Using ServiceLens to monitor the health of your applications](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)
+  [Automated Cleanup of Unused Images in Amazon ECR](https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)
