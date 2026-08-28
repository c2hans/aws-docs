---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/fleet-provisioning-changelog.html
---

# AWS IoT fleet provisioning plugin changelog
<a name="fleet-provisioning-changelog"></a>

The following table describes the changes in each version of the AWS IoT fleet provisioning by claim plugin (`aws.greengrass.FleetProvisioningByClaim`).

|  Version  |  Changes  |
| --- | --- |
| 1.2.2 |  **Bug fixes and improvements**<br />   Adds support for custom core device certificate (`certificatePath`) and private key (`privateKeyPath`) paths.     |
| 1.2.1 |  **Bug fixes and improvements**<br />   Fixes an issue where the fleet provisioning plugin is offline during a Greengrass nucleus startup. The fleet provisioning plugin now indefinitely retries MQTT connect calls.     |
| 1.2.0 |  **Bug fixes and improvements**<br />   Adds support for device provisioning via certificate signing request with configurable private key path.   Minor fixes and improvements.     |
| 1.1.0 |  **Bug fixes and improvements**<br />   Adds support for additional file path formats when you configure the plugin on Windows devices.   Adds support for HTTPS network proxy configurations. For more information, see [Connect on port 443 or through a network proxy](configure-greengrass-core-v2.md#configure-alpn-network-proxy) and [Enable the core device to trust an HTTPS proxy](configure-greengrass-core-v2.md#https-proxy-certificate-trust).     |
| 1.0.0 | Initial version. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
