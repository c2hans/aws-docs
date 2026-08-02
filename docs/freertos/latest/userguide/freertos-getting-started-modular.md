---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-getting-started-modular.html
---

# Get started with FreeRTOS
<a name="freertos-getting-started-modular"></a>

**Topics**
+ [Get started with Quick Connect](#freertos-getting-started-quick-connect)
+ [Explore FreeRTOS libraries](#explore-freertos-libraries)
+ [Build a secure and robust AWS IoT product](#secure-robust-iot)
+ [Develop your AWS IoT application](#develop-application)

## Get started with Quick Connect
<a name="freertos-getting-started-quick-connect"></a>

 To quickly explore AWS IoT, start with [AWS Quick Connect Demos](https://www.freertos.org/Why-FreeRTOS/Quick-connect). Quick Connect demos are simple to setup and connect a partner provided, FreeRTOS qualified board to [AWS IoT](https://aws.amazon.com/iot/).

 Follow the [AWS IoT Getting Started](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) tutorial for a better understanding of AWS IoT and the AWS IoT console. You can modify the demo source code provided with the Quick Connect demos using the chosen board’s build system and tools to connect to your AWS account. The data flow from the AWS IoT console on your account is visible now.

## Explore FreeRTOS libraries
<a name="explore-freertos-libraries"></a>

 Once you have an understanding of how an IoT device and AWS IoT work together, you can start exploring [FreeRTOS libraries](https://www.freertos.org/Documentation/03-Libraries/01-Library-overview/01-All-libraries), and the [Long-Term Support (LTS) libraries](https://www.freertos.org/lts-libraries.html).

 Some commonly used libraries for FreeRTOS based AWS IoT devices are:
+ [FreeRTOS Kernel](https://www.freertos.org/RTOS.html)
+ [coreMQTT](https://www.freertos.org/mqtt/index.html)
+ [AWS IoT Over-the-Air (OTA)](https://www.freertos.org/ota/index.html)

Visit [freertos.org](https://freertos.org/) for library-specific technical documentation and demos.

## Build a secure and robust AWS IoT product
<a name="secure-robust-iot"></a>

 Refer to [ Featured FreeRTOS AWS IoT Integrations](https://www.freertos.org/featured-freertos-iot-integrations.html) to learn about best practices in making IoT device software more secure and robust. These FreeRTOS IoT integrations are designed for improved security using a combination of FreeRTOS software, and a partner-provided board with hardware security features. Use them in production as is, or use them as a model for your own designs.

## Develop your AWS IoT application
<a name="develop-application"></a>

 Follow these steps to create an application project for your AWS IoT product:

1.  Download the latest FreeRTOS or Long Term Support (LTS) version from [freertos.org](https://www.freertos.org/a00104.html), or clone from the [FreeRTOS-LTS](https://github.com/FreeRTOS/FreeRTOS-LTS) GitHub repository. You can also integrate the required FreeRTOS libraries into your project from the [MCU vendor’s toolchain](https://freertos.org/2021/10/freertos-lts-libraries-are-now-part-of-our-partner-toolchains.html) if available.

1.  Follow the [FreeRTOS Porting guide](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-guide.html) to create a project, set up the development environment, and integrate FreeRTOS libraries into your project. Use the [FreeRTOS-Libraries-Integration-Tests](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests) GitHub repository to validate the porting.
