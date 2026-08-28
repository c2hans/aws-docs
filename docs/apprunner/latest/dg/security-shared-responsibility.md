---
source_url: https://docs.aws.amazon.com/apprunner/latest/dg/security-shared-responsibility.html
---

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Configuration and vulnerability analysis in App Runner
<a name="security-shared-responsibility"></a>

AWS and our customers share responsibility for achieving a high level of software component security and compliance. For more information, see the AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## Patch container images
<a name="security-shared-responsibility.patch-images"></a>

Patching the container image is part of the customer's responsibility in the shared security model. The image owner is responsible for updating and regularly patching the container image. We recommend establishing a routine schedule for checking and applying updates to your container images. For more information on how to scan your images for vulnerabilities, see the [AWS App Runner Documentation](security-best-practices.md#security-best-practices.preventive.scan)

For other App Runner security topics, see [Security in App Runner](security.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
