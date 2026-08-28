---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/PcaKubernetes.html
---

# Secure Kubernetes with AWS Private Certificate Authority
<a name="PcaKubernetes"></a>

You can use AWS Private Certificate Authority to provide certificates for secure authentication and encryption over TLS and mTLS. AWS Private CA provides an open source plugin, [AWS Private CA Connector for Kubernetes](https://github.com/cert-manager/aws-privateca-issuer), (`aws-privateca-issuer`) for the widely adopted [cert-manager](https://cert-manager.io/docs/) add-on to Kubernetes that requests certificates, distributes them to Kubernetes secrets, and automates certificate renewal.

The `aws-privateca-issuer` plugin allows you to issue AWS Private CA certificates through `cert-manager`. You can use the plugin with Amazon Elastic Kubernetes Service (Amazon EKS), a self-managed Kubernetes cluster on AWS, or in an on-premise Kubernetes cluster. The plugin works on both x86 and ARM architectures.

AWS Private CA has HSM backed keys that can't be exported. If you have regulatory requirements for controlling access and auditing your CA operations, you can use AWS Private CA to improve auditability and to support compliance.

**Note**
If you are running on Amazon EKS, we recommend that you use the `cert-manager` and `aws-privateca-connector-for-kubernetes` add-ons for a managed installation experience. For more information, refer to [AWS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/workloads-add-ons-available-eks.html#add-ons-aws-privateca-connector).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
