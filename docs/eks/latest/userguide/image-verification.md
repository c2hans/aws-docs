---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/image-verification.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Validate container image signatures during deployment
<a name="image-verification"></a>

If you use [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) and want to verify signed container images at the time of deployment, you can use one of the following solutions:
+  [Gatekeeper and Ratify](https://ratify.dev/docs/1.0/quickstarts/ratify-on-aws) – Use Gatekeeper as the admission controller and Ratify configured with an AWS Signer plugin as a web hook for validating signatures.
+  [Kyverno](https://github.com/nirmata/kyverno-notation-aws) – A Kubernetes policy engine configured with an AWS Signer plugin for validating signatures.

**Note**
Before verifying container image signatures, configure the [Notation](https://github.com/notaryproject/notation#readme) trust store and trust policy, as required by your selected admission controller.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
