---
source_url: https://docs.aws.amazon.com/freertos/latest/qualificationguide/latest-changes.html
---

# Latest changes
<a name="latest-changes"></a>

The following table describes the important changes to the AWS Device Qualification Program for FreeRTOS since the last release.

**Test cases**

| Changes | Description |
| --- | --- |
| Updated source code requirements |  + FreeRTOS integration tests are now in a separate repository: [FreeRTOS-Libraries-Integration-Tests](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests). These tests must be added to the qualification project.<br />+ The [amazon-freertos](https://github.com/aws/amazon-freertos) repository is neither used nor required for qualification.<br />+ Any source code directory structure can be used for qualification by adding an additional field **path** in the `manifest.yml` file.<br />+  MQTT pub/sub demo supporting OTA capability is now required for qualification. This demo must be verified using Device Advisor tests.  |
| Updated qualification artifacts |  + Both AWS IoT Device Tester and AWS IoT Device Advisor test reports are required for qualification.<br />+ A threat modeling document for secure boot is required, and must be uploaded as a Supporting Asset when submitting your device in [APN Partner Central](https://partnercentral.awspartner.com).  |
| Updated integration tests |  + OTA tests (OTACore, OTADataplaneMQTT) are now required for qualification.<br />+ Added new Transport Interface tests: `FullTransportInterfacePlainText` and `FullTransportInterfaceTLS`. `FullTransportInterfaceTLS` is required for qualification, but `FullTransportInterfacePlainText` is not required if the TLS stack is offloaded to an external connectivity module.<br />+ FullMQTT, FullBLE, CmakeBuildSystem, FullSecureSockets, FullTLS, and FullWiFi tests have been removed.<br />+ FreeRTOSIntegrity check is still performed, but it verifies that the libraries used in the source code use the correct git commit for that version of FreeRTOS.<br />+ FreeRTOSVersion check is still performed, but it verifies that the FreeRTOS version used is compatible with FreeRTOS LTS, FreeRTOS mainline, and AWS IoT Device Tester (IDT) versions. The version of FreeRTOS used for qualification should be marked in IDT's `userdata.json` file.<br />+ `FullPKCS11` tests are not required if TLS stack is offloaded to an external connectivity module. `FullPKCS11_ECC` and `FullPKCS11_RSA` tests are replaced with the corresponding `FullPKCS11_Import`, `FullPKCS11_Onboard`, `FullPKCS11_PreProvisioned` tests.<br />+ FullMQTT tests are replaced by Device Advisor tests. See Step 4 of section [Verify the FreeRTOS libraries ported using AWS IoT Device Tester (IDT)](freertos-qualification.md#qualifying-your-device-idt).  |

For previous changes, see [FreeRTOS version history](https://docs.aws.amazon.com/freertos/latest/portingguide/doc-history.html) in the *FreeRTOS Porting Guide*.
