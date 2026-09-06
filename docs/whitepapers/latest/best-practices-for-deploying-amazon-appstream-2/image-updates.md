---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/image-updates.html
---

# Image updates
<a name="image-updates"></a>

 Software patching is critical for the security and performance of compute resources. Frequent patching is listed as a best practice in the [*Security Pillar*](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html) of the [*Well-Architected Framework*](https://aws.amazon.com/architecture/well-architected).

 When your image is built and deployed, there are four categories of software that require patching in your WorkSpaces Applications image:
+  **Applications and dependencies** — You are responsible for patching the applications and dependencies in your images.
+  **Microsoft Windows operating system** — You are responsible for installing and maintaining updates for Windows.
+  **Software components** — These are drivers, agents, and other software that is required for WorkSpaces Applications operation (for example, the [*Amazon CloudWatch*](https://aws.amazon.com/cloudwatch/) agent). WorkSpaces Applications periodically releases new base images that contain new agents and drivers. You can rebuild your image using the latest base to bring the software components on their images to the latest baseline. The process to rebuild an image on the latest base can be time-consuming and cumbersome when there are many applications, or with complex application installs.
+  **WorkSpaces Applications agent** — You can choose **Always use the latest agent version** in Image Assistant. With this option, streaming instances that are launched from the image automatically use the latest version of the agent.

 You can keep your WorkSpaces Applications image up to date by doing either of the following:
+  [*Update an Image by Using Managed WorkSpaces Applications Image Updates*](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#keep-image-updated-managed-image-updates) – This update method provides the latest Windows operating system updates and driver updates, and the latest WorkSpaces Applications agent software. This managed method **does** update service and Microsoft operating system components, but it **does not** allow you to update your application components. It is a best practice to use this method when application installs are complex, or require manual configuration.
+  [*Update the WorkSpaces Applications Agent Software by Using Managed WorkSpaces Applications Image Versions*](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#keep-image-updated-manage-image-versions) – This update method provides the latest WorkSpaces Applications agent software. This method **does** allow you to update your application components.
