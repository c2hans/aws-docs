---
source_url: https://docs.aws.amazon.com/eks/latest/best-practices/windows-images.html
---

# Container image scanning
<a name="windows-images"></a>

Image Scanning is an automated vulnerability assessment feature that helps improve the security of your application’s container images by scanning them for a broad range of operating system vulnerabilities.

Currently, the Amazon Elastic Container Registry (ECR) is only able to scan Linux container image for vulnerabilities. However; there are third-party tools which can be integrated with an existing CI/CD pipeline for Windows container image scanning.
+  [Anchore](https://anchore.com/blog/scanning-windows-container-images/)
+  [PaloAlto Prisma Cloud](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/vulnerability_management/windows_image_scanning.html)
+  [Trend Micro - Deep Security Smart Check](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/smart-check-image-scanning.html)

To learn more about how to integrate these solutions with Amazon Elastic Container Repository (ECR), check:
+  [Anchore, scanning images on Amazon Elastic Container Registry (ECR)](https://anchore.com/blog/scanning-images-on-amazon-elastic-container-registry/)
+  [PaloAlto, scanning images on Amazon Elastic Container Registry (ECR)](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/vulnerability_management/registry_scanning0/scan_ecr.html)
+  [TrendMicro, scanning images on Amazon Elastic Container Registry (ECR)](https://cloudone.trendmicro.com/docs/container-security/sc-about/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
