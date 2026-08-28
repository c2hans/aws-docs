---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-architecture.html
---

# FreeRTOS architecture
<a name="freertos-architecture"></a>

FreeRTOS contains two types of repositories, single library repositories and package repositories. Each single library repository contains the source code for one library without any build projects or examples. Package repositories contain multiple libraries, and can contain preconfigured projects that demonstrate the library’s use.

While package repositories contain multiple libraries, they don't contain copies of those libraries. Instead, package repositories reference the libraries they contain as git submodules. Using submodules ensures that there is a single source of truth for each individual library.

The individual library git repositories are split between two GitHub organizations. Repositories containing FreeRTOS specific libraries (such as FreeRTOS\+TCP) or generic libraries (such as coreMQTT, which is cloud agnostic because it works with any MQTT broker) are in the FreeRTOS GitHub organization. Repositories containing AWS IoT specific libraries (such as the AWS IoT over-the-air update client) are in the AWS GitHub organization. The following diagram explains the structure.

![Diagram depicting FreeRTOS package repositories on GitHub for FreeRTOS kernel, HTTP, MQTT demos, composable libraries; and RTOS agnostic package repositories for Shadow client, Fleet provisioning, OTA client demos, composable libraries.](http://docs.aws.amazon.com/freertos/latest/userguide/images/freertos-github.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
