---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_software_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP03 Optimize areas of code that consume the most time or resources
<a name="sus_sus_software_a4"></a>

 Monitor workload activity to identify application components that consume the most resources. Optimize the code that runs within these components to minimize resource usage while maximizing performance.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor performance as a function of resource usage to identify components with high resource requirements per unit of work as targets for optimization.
+  Use a code profiler to identify the areas of code that use the most time or resources as targets for optimization.
+  Replace algorithms with more efficient versions that produce the same result.
+  Use hardware acceleration to improve the efficiency of blocks of code with long execution times.
+  Use the most efficient operating system and programming language for the workload.
+  Remove unnecessary sorting and formatting.
+  Use data transfer patterns that minimize the resources used based on how frequently the data changes and how it is consumed. For example, push state change information to a client instead of having it consume resources to poll and receive valueless ‘no change’ messages.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [What is Amazon CodeGuru Profiler?](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
+  [FPGA instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fpga-getting-started.html)
+  [The AWS SDKs on Tools to Build on AWS](https://aws.amazon.com/tools/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)
