---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/kubernetes-verification.html
---

# Verify an image during in Amazon EKS or Kubernetes clusters
<a name="kubernetes-verification"></a>

For AWS Signer customers wishing to verify signed container images at the time of deployment, there are various open-source solutions such as the following.
+ [Deis Labs Gatekeeper and Ratify](https://ratify.dev/docs/quickstarts/ratify-on-aws) – Use Gatekeeper as the admission controller and Ratify configured with an AWS Signer plug-in as a web hook for validating signatures.
+ [Kyverno](https://github.com/nirmata/kyverno-notation-aws) – A Kubernetes policy engine configured with a AWS Signer plugin for validating signatures.

**Note**
Before verifying container-image signatures, customers must configure the Notation trust store and trust policy as required by their selected admission controller.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
