---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert.html
---

# Create a code-signing certificate
<a name="ota-code-sign-cert"></a>

To digitally sign firmware images, you need a code-signing certificate and private key. For testing purposes, you can create a self‐signed certificate and private key. For production environments, purchase a certificate through a well‐known certificate authority (CA).

Different platforms require different types of code-signing certificates. The following sections describe how to create code-signing certificates for different FreeRTOS-qualified platforms.

**Topics**
+ [Creating a code-signing certificate for the Texas Instruments CC3220SF-LAUNCHXL](ota-code-sign-cert-ti.md)
+ [Creating a code-signing certificate for the Espressif ESP32](ota-code-sign-cert-esp.md)
+ [Creating a code-signing certificate for the Nordic nrf52840-dk](ota-code-sign-cert-nordic.md)
+ [Creating a code-signing certificate for the FreeRTOS Windows simulator](ota-code-sign-cert-win.md)
+ [Creating a code-signing certificate for custom hardware](ota-code-sign-cert-other.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
