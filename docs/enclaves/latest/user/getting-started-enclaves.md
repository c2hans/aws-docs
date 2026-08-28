---
source_url: https://docs.aws.amazon.com/enclaves/latest/user/getting-started-enclaves.html
---

# Getting started with Nitro Enclaves
<a name="getting-started-enclaves"></a>

These tutorials help you get started with AWS Nitro Enclaves. An enclave has no external network connectivity, no persistent storage, and no interactive access. An enclave communicates only with its associated parent instance over a local channel called a *vsock*. Understanding how to launch, validate, and communicate with an enclave helps you design secure, isolated workloads that protect sensitive data.

The following sections walk you through three foundational topics:
+ **Hello Enclaves sample application** – Launch an enclave-enabled parent instance, build an enclave image file, validate that the enclave is running, and terminate it when you are finished.
+ **Vsock communication** – Establish a virtio-vsock channel between the parent instance and the enclave to pass data securely over the local socket.
+ **AWS KMS integration with cryptographic attestation** – Use AWS KMS and cryptographic attestation to decrypt secrets from inside a validated enclave, ensuring that only an enclave launched from a specific enclave image file can access sensitive data.

**Topics**
+ [Getting started: Hello Enclaves](getting-started.md)
+ [Getting started: Using the virtio-vsock](enclave-networking.md)
+ [Getting started: Integrating with AWS KMS](connect-enclave-kms.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query enclaves` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
