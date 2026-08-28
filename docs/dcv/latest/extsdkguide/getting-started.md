---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/getting-started.html
---

# Getting started with the Amazon DCV Extension SDK
<a name="getting-started"></a>

The Amazon DCV Extension SDK uses Protocol Buffers (protobuf), an open-source data format designed to serialize structured data in a compact, binary form. By using Protocol Buffers, Amazon DCV components and extensions can communicate with one another in a way that is platform-independent and extensible, regardless of the selected programming language.

 The definitions of the messages are contained in the file `extensions.proto`.

**To get started with the Amazon DCV Extension SDK**

1. Get familiar with Protocol Buffers ([protobuf](https://protobuf.dev))

1. Review the code samples available at [https://github.com/aws-samples/dcv-extension-sdk-samples](https://github.com/aws-samples/dcv-extension-sdk-samples)

1. Download the protocol definition file `extensions.proto` from the Github repository at [https://github.com/aws-samples/dcv-extension-sdk](https://github.com/aws-samples/dcv-extension-sdk)

**Topics**
+ [Extension architecture](extension-architecture.md)
+ [Installing and registering the extension](install-register-extension.md)
+ [Permissions](permissions.md)
+ [Protocol and framing](protocol-framing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
