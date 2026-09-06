---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/github-repo-migration.html
---

# Amazon-FreeRTOS Github Repository Migration Guide
<a name="github-repo-migration"></a>

 If you have an existing FreeRTOS project based on the now deprecated amazon-freertos repository, follow these steps:

1.  Stay up to date with the latest, publicly available security fixes. Check the [FreeRTOS LTS libraries](https://www.freertos.org/lts-libraries.html) page for updates, or subscribe to the [FreeRTOS-LTS](https://github.com/FreeRTOS/FreeRTOS-LTS) GitHub repository to receive the latest LTS patches with critical and security bug fixes. You can download or clone the latest FreeRTOS LTS patches required directly from the individual GitHub repositories.

1.  Consider refactoring the network transport interface implementation to optimize your hardware platform. The abstract APIs like [secure sockets](https://docs.aws.amazon.com/freertos/latest/userguide/secure-sockets.html) and [Wifi APIs](https://docs.aws.amazon.com/freertos/latest/userguide/freertos-wifi.html) are not required by the latest [coreMQTT ](https://www.freertos.org/mqtt/index.html) library. See [Transport Interface](https://www.freertos.org/network-interface.html) for further details.

## Appendix
<a name="appendix"></a>

The following table provides recommendations for all demo projects, legacy libraries, and abstract APIs within the Amazon-FreeRTOS repository.

**Migrated libraries and demos**

| Name | Type | Recommendations |
| --- | --- | --- |
| **coreHTTP** | demos and library | Clone or download the coreHTTP library directly from the [coreHTTP](https://github.com/FreeRTOS/coreHTTP) repository (sub-module if using git) in the [FreeRTOS Github organization](https://github.com/FreeRTOS). The coreHTTP demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/coreHTTP_Windows_Simulator). For more details, refer to the [coreHTTP page](https://www.freertos.org/http/index.html). |
| coreMQTT | demos and library | Clone or download the coreMQTT library directly from the [coreMQTT](https://github.com/FreeRTOS/coreMQTT) repository (sub-module if using git) in the [FreeRTOS Github organization](https://github.com/FreeRTOS). The coreMQTT demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/coreMQTT_Windows_Simulator). For more details, refer to the [coreMQTT page](https://www.freertos.org/mqtt/index.html). |
| coreMQTT-Agent | demos and library  | Clone or download the coreMQTT-Agent library directly from the [coreMQTT-Agent](https://github.com/FreeRTOS/coreMQTT-Agent) repository (sub-module if using git) in the [FreeRTOS Github organization](https://github.com/FreeRTOS). The coreMQTT-Agent demos are in the [coreMQTT-Agent-Demos](https://github.com/FreeRTOS/coreMQTT-Agent-Demos) repository. For more details, refer to the [coreMQTT-Agent page](https://www.freertos.org/mqtt-agent/index.html). |
| device\_defender\_for\_aws | demos and library  | The AWS IoT Device Defender library is in its repository in the [AWS GitHub organisation](https://github.com/AWS). Clone or download it (sub-module if using git) directly from the [AWS IoT Device Defender](https://github.com/aws/Device-Defender-for-AWS-IoT-embedded-sdk) repository. The AWS IoT Device Defender demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/AWS/Device_Defender_Windows_Simulator/Device_Defender_Demo). For more details, refer to the [AWS IoT Device Defender page](https://www.freertos.org/iot-device-defender/index.html). |
| device\_shadow\_for\_aws | demos and library  | The AWS IoT Device Shadow library is in its repository in the [AWS GitHub organisation](https://github.com/AWS). Clone or download it (sub-module if using git) directly from the [AWS IoT Device Shadow](https://github.com/aws/Device-Shadow-for-AWS-IoT-embedded-sdk)) repository. The AWS IoT Device Shadow demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/AWS/Device_Shadow_Windows_Simulator). For more details, refer to the [AWS IoT Device Shadow page](https://www.freertos.org/iot-device-shadow/index.html). |
| jobs\_for\_aws | demos and library  | The AWS IoT Jobs library is in its repository in the [AWS GitHub organization](https://github.com/AWS). Clone or download it (sub-module if using git) directly from the [AWS IoT Jobs](https://github.com/aws/Jobs-for-AWS-IoT-embedded-sdk) repository. The AWS IoT Jobs demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/AWS/Jobs_Windows_Simulator/Jobs_Demo). For more details, refer to the [AWS IoT Jobs page](https://www.freertos.org/iot-jobs/index.html). |
| OTA | demos and library  | The AWS IoT Over-The-Air (OTA) Update library is in its repository in the [AWS GitHub organization](https://github.com/AWS). Clone or download it (sub-module if using git) directly from the [AWS IoT OTA](https://github.com/aws/ota-for-aws-iot-embedded-sdk) repository. The AWS IoT OTA demos are in the [ primary FreeRTOS distribution](https://github.com/FreeRTOS/FreeRTOS/tree/main/FreeRTOS-Plus/Demo/AWS/Ota_Windows_Simulator). For more details, refer to the [AWS IoT OTA page](https://www.freertos.org/ota/index.html). |
| CLI and FreeRTOS\_Plus\_CLI  | demos and library  | There is a CLI example running on WinSim. Refer to the [ FreeRTOS Plus Command Line Interface](https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_CLI/FreeRTOS_Plus_Command_Line_Interface.html) page for more details. The Featured FreeRTOS IoT reference integrations on the [ NXP i.MX RT1060](https://github.com/FreeRTOS/iot-reference-nxp-rt1060/tree/main/examples/common/cli) and [ STM32U5](https://github.com/FreeRTOS/iot-reference-stm32u5/tree/main/Common/cli) platforms, also provide CLI examples on actual hardware. |
| logging  | macro | There are implementations of the logging macro for specific hardware platforms used by some of the FreeRTOS libraries. Refer to the [logging page](https://www.freertos.org/logging.html) for how to implement the logging macro. Refer to [ one of the FreeRTOS featured IoT references](https://github.com/FreeRTOS/iot-reference-nxp-rt1060/tree/main/examples/common/logging) for an example running on actual hardware. |
| greengrass\_connectivity  | demo | [Migration in progress] This demo project assumed that cloud connectivity was available before connecting to an AWS IoT Greengrass device. A new project that demonstrates local authentication and discovery capability is under development. Expect the new demo project to be published shortly in the [FreeRTOS Github organization](https://github.com/FreeRTOS). |

**Deprecated libraries and demos**

| Name | Type | Recommendations |
| --- | --- | --- |
| BLE | demos and libraries | The FreeRTOS BLE library implements the proprietary MQTT protocol and supports publishing and subscribing to MQTT topics over Bluetooth Low Energy (BLE) through a proxy device such as a mobile phone. This is no longer mandated. Use either your own BLE stack or a third-party option such as [NimBLE](https://mynewt.apache.org/latest/network/) to best optimize your project. |
| dev\_mode\_key\_provisioning | demos | The Featured FreeRTOS IoT reference integrations on the [ NXP i.MX RT1060](https://github.com/FreeRTOS/iot-reference-nxp-rt1060/blob/main/examples/common/cli/cli.c), [ STM32U5](https://github.com/FreeRTOS/iot-reference-stm32u5/blob/main/Common/cli/cli_pki.c), or [ ESP32-C3](https://github.com/FreeRTOS/iot-reference-esp32c3/blob/main/GettingStartedGuide.md) platforms provide examples of crucial provisioning using a CLI. |
| posix | abstraction and demo | Not recommended for use. |
| wifi\_provisioning | example | This example demonstrated how to provision WiFi credentials on a device using the Amazon-FreeRTOS BLE library. Refer to the FreeRTOS Featured IoT reference on the [ESP32C3 platform](https://github.com/FreeRTOS/iot-reference-esp32c3) for an example of WiFi provisioning via BLE. |
| Legacy abstract APIs | code | These are APIs that were created to provide an abstract interface for various third-party software stacks, connectivity modules, and MCU platforms from a variety of vendors. For example, there are interfaces for WiFi abstraction, secure sockets, and so on. They are supported in the Amazon-FreeRTOS repository and are in the folder `/libraries/abstractions/`. These APIs are not required when using the [ FreeRTOS LTS libraries](https://www.freertos.org/lts-libraries.html). |

The libraries and demos in the table above will not get security patches or bug fixes.

**Third-party libraries**

When demos in Amazon-FreeRTOS use third-party libraries, we recommend that you sub-module them directly from their third-party repositories.
+ **CMock**: clone it (submodule if you use git) directly from the [Cmock](https://github.com/ThrowTheSwitch/CMock) repository.
+ **jsmn**: not recommended and no longer supported.
+ **lwip**: clone it (submodule if you use git) directly from the [lwip-tcpip](https://github.com/lwip-tcpip/lwip) repository.
+ **lwip\_osal**: refer to the FreeRTOS Featured Reference Integrations on [i.MX RT1060](https://github.com/FreeRTOS/iot-reference-nxp-rt1060) or [STM32U5](https://github.com/FreeRTOS/iot-reference-stm32u5) for how to implement lwip\_osal on your hardware platform/board.
+ **mbedtls**: clone it (submodule if you use git) directly from the [Mbed-TLS](https://github.com/Mbed-TLS/mbedtls) repository. The mbedtls config and utilities can be reused; make a local copy in this case.
+ **pkcs11**: clone it (submodule if you use git) directly from either the [corePKCS11](https://github.com/FreeRTOS/corePKCS11) library or the [OASIS PKCS 11](https://github.com/oasis-tcs/pkcs11) repository.
+ **tinycbor**: clone it (submodule if you use git) directly from the[tinycbor](https://github.com/intel/tinycbor) repository.
+ **tinycrypt**: we recommend that you use crypto accelerators from your MCU platform, if available. If you want to continue to use tinycrypt, clone it (submodule if you use git) directly from the [ tinycrypt](https://github.com/intel/tinycrypt) repository.
+ **tracealyzer\_recorder**: clone it (submodule if you use git) directly from Percepio's [trace recorder](https://github.com/percepio/TraceRecorderSource) repository.
+ **unity**: clone it (submodule if you use git) directly from the [ThrowTheSwitch/Unity](https://github.com/ThrowTheSwitch/Unity) repository.
+ **win\_pcap**: win\_pcap is no longer maintained. We recommend that you use libslirp, libpcap (posix), or npcap instead.

**Porting tests and integration tests**

All tests under the `/tests` folder that are required to validate integration of FreeRTOS libraries were migrated to the [ FreeRTOS-Libraries-Integration-Tests](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests) repository. These can be used to test PAL implementation and library integration. The same tests are used by AWS IoT Device Tester (IDT) for the [AWS Device Qualification Program for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/qualificationguide/afr-qualification.html).
