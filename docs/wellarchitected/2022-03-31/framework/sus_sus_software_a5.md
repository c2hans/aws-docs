---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_software_a5.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP04 Optimize impact on customer devices and equipment
<a name="sus_sus_software_a5"></a>

 Understand the devices and equipment your customers use to consume your services, their expected lifecycle, and the financial and sustainability impact of replacing those components. Implement software patterns and architectures to minimize the need for customers to replace devices and upgrade equipment. For example, implement new features using code that is backward compatible with older hardware and operating system versions, or manage the size of payloads so they don’t exceed the storage capacity of the target device.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Inventory the devices your customers use.
+  Test using managed device farms with representative sets of hardware to understand the impact of your changes, and iterate development to maximize the devices supported.
+  Account for network bandwidth and latency when building payloads, and implement capabilities that help your applications work well on low-bandwidth, high-latency links.
+  Pre-process data payloads to reduce local processing requirements and limit data transfer requirements.
+  Perform computationally intense activities server-side (such as image rendering), or use application streaming to improve the user experience on older devices.
+  Segment and paginate output, especially for interactive sessions, to manage payloads and limit local storage requirements.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What is AWS Device Farm?](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
+  [Amazon AppStream 2.0 Documentation](https://docs.aws.amazon.com/appstream2/)
+  [NICE DCV](https://docs.aws.amazon.com/dcv/)
+  [Amazon Elastic Transcoder Documentation](https://docs.aws.amazon.com/elastic-transcoder/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)
