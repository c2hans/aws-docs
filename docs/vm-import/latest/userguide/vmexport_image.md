---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport_image.html
---

# Export a VM from an Amazon Machine Image (AMI) using VM Import/Export
<a name="vmexport_image"></a>

Exporting a VM file based on an Amazon Machine Image (AMI) is useful when you want to deploy a new, standardized instance in your virtualization environment. You can export most AMIs to Citrix Xen, Microsoft Hyper-V, or VMware vSphere.

When you export an image, you are charged the standard Amazon S3 rates for the bucket where the exported VM is stored. In addition, there might be a small charge for the temporary use of an Amazon EBS snapshot. For more information about Amazon S3 pricing, see [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/).

**Topics**
+ [Prerequisites for exporting an image from Amazon EC2](prerequisites-image-export.md)
+ [Considerations for image export](limits-image-export.md)
+ [Start an export image task](start-image-export.md)
+ [Monitor an export image task](monitor-image-export.md)
+ [Cancel an export image task](cancel-image-export.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
