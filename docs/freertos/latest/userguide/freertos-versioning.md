---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-versioning.html
---

# FreeRTOS versions
<a name="freertos-versioning"></a>

Individual libraries use x.y.z style version numbers, similar to semantic versioning. x is the major version number, y the minor version number, and starting from 2022, z is a patch number. Before 2022, z was a point release number, which required the first LTS libraries to have a patch number of the form *"x.y.z LTS Patch 2"*.

Library packages use yyyymm.x style date stamp version numbers. yyyy is the year, mm the month, and x an optional sequence number showing the release order within the month. In the case of the LTS package, x is a sequential patch number for that LTS release. The individual libraries contained in a package are whatever the latest version of that library was on that date. For the LTS package, it's the latest patch version of the LTS libraries originally released as an LTS version on that date.

## FreeRTOS Long Term Support
<a name="freertos-longterm-support"></a>

FreeRTOS Long Term Support (LTS) releases receive security and critical bug fixes (should any be necessary) for at least two years following their release. With this ongoing maintenance, you can incorporate bug fixes throughout a development and deployment cycle without the expensive disruption of updating to new major versions of FreeRTOS libraries.

With FreeRTOS LTS, you get the complete set of libraries needed to build secure connected IoT and embedded products. LTS helps reduce maintenance and testing costs associated with updating libraries on your devices already in production.

FreeRTOS LTS includes the FreeRTOS kernel and IoT libraries: FreeRTOS\+TCP, coreMQTT, coreHTTP, corePKCS11, coreJSON, AWS IoT OTA, AWS IoT Jobs, AWS IoT Device Defender, and AWS IoT Device Shadow. For more information, see the FreeRTOS [LTS libraries](https://freertos.org/Documentation/03-Libraries/01-Library-overview/03-LTS-libraries/01-LTS-libraries).

## FreeRTOS Extended Maintenance Plan
<a name="freetos-EMP"></a>

AWS also offers FreeRTOS Extended Maintenance Plan (EMP), which provides security patches and critical bug fixes on your chosen FreeRTOS Long Term Support (LTS) version for up to ten additional years. With FreeRTOS EMP, your FreeRTOS based long-lived devices can rely on a version that has feature stability and receives security updates for years. You receive timely notifications of upcoming patches on FreeRTOS libraries, so you can plan the deployment of security patches on your Internet of Things (IoT) devices.

To learn more about FreeRTOS EMP, see the [Features](https://aws.amazon.com/freertos/features/#FreeRTOS_Extended_Maintenance_Plan) page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
