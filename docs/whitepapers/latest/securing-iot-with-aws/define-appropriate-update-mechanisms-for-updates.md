---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/define-appropriate-update-mechanisms-for-updates.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 4. Define appropriate update mechanisms for software and firmware updates.
<a name="define-appropriate-update-mechanisms-for-updates"></a>

 Whether it’s deploying patches to individual packages, updating local firmware, or wholesale replacing the software on an IoT device, patching is critical during the IoT device’s lifecycle. Although different use cases will have different tradeoffs, common things to consider include rolling out patches gradually to catch defects and ensuring all devices of the same type aren’t brought down simultaneously, being responsive to vulnerabilities, and ensuring the patch delivery mechanism can’t be used by unauthorized actors. Some additional considerations include:
+  Begin with having a mechanism to push software and firmware to devices in the field to patch security vulnerabilities and improve device functionality.
+  Apply and verify digital signatures on distributed deployment artifacts.
+  Verify the integrity of the software on the device before starting to run it ensuring that it comes from a reliable source (signed by the vendor) and that it is obtained in a secure manner.
+  Monitor status of deployments throughout your ecosystem and investigate any failed or stalled deployments.
+  Use rolling patches using asset tags or other segmentation mechanism based on the impact of a latent issue.
+  Include patch status in your inventory of the deployed devices.
+  Use version control mechanisms to prevent unauthorized actors from forcing firmware or software downgrades.
+  Maintain notification mechanisms to immediately alert the appropriate stakeholders when security updates are required or fail.
+  Create mechanisms to identify, isolate into a different network segment, or replace IoT devices that are outside of compliance.
+  Create detection and response mechanisms to handle unauthorized changes in deployed software or firmware.

## Supporting AWS resources
<a name="resources-4"></a>

 AWS provides the following capabilities and services to help you organize and maintain a continuous development and deployment pipeline:
+  [FreeRTOS over-the-air updates](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-ota-dev.html)
+  [OTA updates of AWS IoT Greengrass Core software](https://docs.aws.amazon.com/greengrass/v1/developerguide/core-ota-update.html)
+  [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) – Defines a set of remote operations that you send to and run on one or more devices connected to AWS IoT.
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) – Automates the process of patching managed instances with both security related and other types of updates, such as operating systems and applications.
+  [Security Pillar of AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html)
