---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_patch_mgmt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP05 Perform patch management
<a name="ops_dev_integ_patch_mgmt"></a>

 Perform patch management to gain features, address issues, and remain compliant with governance. Automate patch management to reduce errors caused by manual processes, and reduce the level of effort to patch.

 Patch and vulnerability management are part of your benefit and risk management activities. It is preferable to have immutable infrastructures and deploy workloads in verified known good states. Where that is not viable, patching in place is the remaining option.

 Updating machine images, container images, or Lambda [custom runtimes and additional libraries](https://docs.aws.amazon.com/lambda/latest/dg/security-configuration.html) to remove vulnerabilities are part of patch management. You should manage updates to [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) (AMIs) for Linux or Windows Server images using [EC2 Image Builder](https://aws.amazon.com/image-builder/). You can use [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) with your existing pipeline to [manage Amazon ECS images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html) and [manage Amazon EKS images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_EKS.html). AWS Lambda includes [version](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) management features.

 Patching should not be performed on production systems without first testing in a safe environment. Patches should only be applied if they support an operational or business outcome. On AWS, you can use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) to automate the process of patching managed systems and schedule the activity using [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html).

 **Common anti-patterns:**
+  You are given a mandate to apply all new security patches within two hours resulting in multiple outages due to application incompatibility with patches.
+  An unpatched library results in unintended consequences as unknown parties use vulnerabilities within it to access your workload.
+  You patch the developer environments automatically without notifying the developers. You receive multiple complaints from the developers that their environment cease to operate as expected.
+  You have not patched the commercial off-the-self software on a persistent instance. When you have an issue with the software and contact the vendor, they notify you that version is not supported and you will have to patch to a specific level to receive any assistance.
+  A recently released patch for the encryption software you used has significant performance improvements. Your unpatched system has performance issues that remain in place as a result of not patching.

 **Benefits of establishing this best practice:** By establishing a patch management process, including your criteria for patching and methodology for distribution across your environments, you will be able to realize their benefits and control their impact. This will enable the adoption of desired features and capabilities, the removal of issues, and sustained compliance with governance. Implement patch management systems and automation to reduce the level of effort to deploy patches and limit errors caused by manual processes.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Patch management: Patch systems to remediate issues, to gain desired features or capabilities, and to remain compliant with governance policy and vendor support requirements. In immutable systems, deploy with the appropriate patch set to achieve the desired result. Automate the patch management mechanism to reduce the elapsed time to patch, to reduce errors caused by manual processes, and reduce the level of effort to patch.
  +  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)

 **Related videos:**
+  [CI/CD for Serverless Applications on AWS](https://www.youtube.com/watch?v=tEpx5VaW4WE)
+  [Design with Ops in Mind](https://youtu.be/uh19jfW7hw4)

   **Related examples:**
+  [Well-Architected Labs – Inventory and Patch Management](https://wellarchitectedlabs.com/operational-excellence/100_labs/100_inventory_patch_management/)
