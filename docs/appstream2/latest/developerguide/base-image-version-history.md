---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html
---

# WorkSpaces Applications Base Image and Managed Image Update Release Notes
<a name="base-image-version-history"></a>

Amazon WorkSpaces Applications provides base images to help you create images that include your own applications. Base images are Amazon Machine Images (AMIs) that contain software configurations specific to the operating system. For WorkSpaces Applications, each base image includes the WorkSpaces Applications agent and the latest version of one of the following operating systems:

**Important**
Operating system versions that are no longer supported by the vendor are not guaranteed to work and are not supported by AWS Support.
+ Windows Server 2025 Base — Available on the following image types: Base, Graphics G4dn, Graphics G5, and Graphics G6
+ Windows Server 2022 Base — Available on the following image types: Base, Graphics G4dn, Graphics G5, and Graphics G6
+ Windows Server 2019 Base — Available on the following image types: Base, Graphics G4dn and Graphics G5
+ Windows Server 2016 Base — Available on the following image types: Base, Graphics G4dn and Graphics G5
+ Red Hat Enterprise Linux 8 – Available on the following image types: Base, Graphics G4dn, Graphics G5, and Graphics G6
+ Rocky Linux 8 – Available on the following image types: Base, Graphics G4dn, Graphics G5, and Graphics G6

After you create your own image that includes your own applications, you are responsible for installing and maintaining the updates for the operating system, your applications, and their dependencies. WorkSpaces Applications provides an automated way to update your image using managed WorkSpaces Applications image updates. With managed image updates, you select the image that you want to update. WorkSpaces Applications creates an image builder in the same AWS account and Region to install the updates and create the new image. After the new image is created, you can test it on a pre-production fleet before updating your production fleets or sharing the image with other AWS accounts. For more information, see "Keep Your WorkSpaces Applications Image Up-to-Date" in [Administer Your Amazon WorkSpaces Applications Images](administer-images.md).

For information about the latest WorkSpaces Applications agent, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md).

The following table lists the latest released images.

**Note**
Public base images for Graphics Pro instances are no longer available from AWS after 10/31/2025 due to End of Life of hardware supporting Graphics Pro instance types.
Public base images for Graphics Design instances are no longer available from AWS after 12/31/2025 due to End of Life of hardware supporting Graphics Design instance types.
Public base images for Amazon Linux 2 are no longer available from AWS after 04/15/2026 due End of Support for Amazon Linux 2 (AL2) for Amazon WorkSpaces Applications.

| Image type | Image name |
| --- | --- |
| Base |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| Graphics G4dn |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| Graphics G5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| Graphics G6  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| Sample apps | Amazon-AppStream2-Sample-Image-06-17-2024<br />For information about how to access this base image, see [Get Started with Amazon WorkSpaces Applications: Set Up With Sample Applications](getting-started.md). |

The following table lists the software components for the latest released base images and the components that are available if you update your image using managed image updates. If the version is marked “latest”, the current stable software component available from the vendor will be installed. If the version is marked “not included”, managed image updates is not managing the component and the version will not be changed when you update your image.

The following table lists the software components for the latest released Windows, Rocky Linux, and Red Hat Enterprise Linux base images and Managed image updates.

------
#### [ Windows ]

| Software component | Latest base images (December 18, 2025) | Managed image updates (June 29, 2026) |
| --- | --- | --- |
| Amazon AWS (AvsCamera) Driver | 1.0.23.0 | 1.0.23.0 |
| Amazon CloudWatch Agent | 1.4.37917 | 1.300063 |
| SSM Agent | 3.3.3050.0 | 3.3.3598.0 |
| NICE DCV Virtual Display | 2024.0-19143 | 2025.0-20850 |
| AMD Driver for Graphics Design instances | 24.20.13028.7002  | 24.20.13028.7002 |
| AppStream 2.0 Agent | LATEST (06-29-2026) | -- |
| AWS Command Line Interface (AWS CLI) | 1.40.24 (Windows Server 2016/2019)<br />2.31.30.0 (Windows Server 2022/2025) | Not included |
| Firefox | 144 (Windows Server 2016/2019) | Not included |
| Microsoft Message Queuing (MSMQ) | Installed with Windows Server | Installed with Windows Server |
| NVIDIA Graphics Driver for G4dn, G5 and G6 instances | 581.42 (Windows Server 2022/2025)<br />539.19 (Windows Server 2019)<br />512.78 (Windows Server 2016) | 581.42 (Windows Server 2022/2025)<br />539.19 (Windows Server 2019)<br />512.78 (Windows Server 2016) |
| Process monitor | 4.01 | [Latest](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) |
| Quality Windows Audio/Video Experience (qWAVE) | Installed with Windows Server | Installed with Windows Server |
| Visual C\+\+ redistributable packages | Microsoft Visual C\+\+ 2013 Redistributable (x64) - 12.0.40664.0Microsoft Visual C\+\+ 2015-2022 Redistributable (x64) - 14.42.34438 | Microsoft Visual C\+\+ 2013 Redistributable (x64) - 12.0.30501Microsoft Visual C\+\+ 2015-2022 Redistributable (x64) - 14.44.35211  |
| Windows Server updates | Base image updates as of November 2025 | [Latest](https://www.catalog.update.microsoft.com/home.aspx) |
| WinSCard Filter Driver | 1.0.19.0 | 1.0.19.0 |
| Paravirtual (PV) driver | 8.6.0 | 8.6.0 |
| ENA driver | 2.11.0 | 2.11.0 |
| AWS NVMe driver | 1.7.0 | 1.7.0 |

------
#### [ Rocky Linux ]

| Software component | Latest base images (February 18, 2026) | Managed image updates (February 18, 2026) |
| --- | --- | --- |
| AWS Command Line Interface (AWS CLI) | 2.33.24 | 2.33.24 |
| Amazon CloudWatch Agent | 1.300064.0b1337-1 | 1.300064.0b1337-1 |
| SSM Agent | 3.3.3598.0-1 | 3.3.3598.0-1 |
| NICE DCV Server AppStream | 2024.0.17598-18 | 2024.0.17598-18 |
| Cloud-init | 23.4-78\_10.11.0.2 | 23.4-78\_10.11.0.2 |
| Kernel | 4.18.0-553.104.1 | 4.18.0-553.104.1 |
| NVIDIA Graphics Driver for G4dn, G5 and G6 instances | 580.95.05 | 580.95.05 |
| Cuda Version | 13.0 | 13.0 |

------
#### [ Red Hat Enterprise Linux ]

| Software component | Latest base images (February 18, 2026) | Managed image updates (February 18, 2026) |
| --- | --- | --- |
| AWS Command Line Interface (AWS CLI) | 2.33.24 | 2.33.24 |
| Amazon CloudWatch Agent | 1.300064.0b1337-1 | 1.300064.0b1337-1 |
| SSM Agent | 3.3.3598.0-1 | 3.3.3598.0-1 |
| NICE DCV Server AppStream | 2024.0.17598-18 | 2024.0.17598-18 |
| Cloud-init | 23.4-78\_10.11 | 23.4-78\_10.11 |
| Kernel | 4.18.0-553.105.1 | 4.18.0-553.105.1 |
| NVIDIA Graphics Driver for G4dn, G5 and G6 instances | 580.95.05 | 580.95.05 |
| Cuda Version | 13.0 | 13.0 |

------

**Important**
The following public images are deprecated and therefore no longer available from AWS:
2016/2019/2022 Windows images released before May 30, 2025
Images for the Graphics Desktop, Graphics Design, and Graphics Pro instance families
 If you want to use an image for a multi-session fleet, the image must meet the following conditions:
The image must be created from a base image released on or after June 12, 2023. Or, the image must be updated by using managed WorkSpaces Applications image updates released on or after September 6, 2023. For more information, see [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md).
The WorkSpaces Applications agent release version must be 09-06-2023 or later. For more information, see [Manage WorkSpaces Applications Agent Versions](base-images-agent.md).
If you have updated your image using Managed WorkSpaces Applications Image updates, then the WorkSpaces Applications agent release version is not applicable. Your image must be updated using a Managed Image Update released on or after September 6, 2023. For more information, see [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md).
Multi-session fleets are supported only for Microsoft Server 2019, 2022, and 2025.

The following table describes all released base images.

| Release | Platform | Image  | Changes |
| --- | --- | --- | --- |
| 02/18/2026 | Red Hat Enterprise Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 02/18/2026 | Rocky Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12/18/2025 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11/10/2025 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11/10/2025 | Red Hat Enterprise Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11/10/2025 | Rocky Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-05-2025 | Red Hat Enterprise Linux  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-05-2025 | Rocky Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-30-2025 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-30-2025 | Red Hat Enterprise Linux  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-30-2025 | Rocky Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 02-11-2025 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12-19-2024 | Rocky Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 10-22-2024 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-30-2024 | Red Hat Enterprise Linux  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-17-2024 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-08-2024 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-08-2024 | Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-24-2024 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-24-2024 | Linux |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 01-26-2024 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12-11-2023 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11-13-2023 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11-13-2023 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-12-2023 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-11-2023 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-29-2023 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-15-2023 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 10-05-2022 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-21-2022 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-14-2022 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-01-2022 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-12-2022 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-20-2022 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-03-2022 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 02-18-2022 | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11-19-2021  | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11-15-2021  | Amazon<br />Linux 2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 10-08-2021 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-19-2021 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-01-2021 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12-28-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-16-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 04-22-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-18-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-16-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-05-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 01-13-2020 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12-12-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-18-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-05-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-24-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-28-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 04-29-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 01-22-2019 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-12-2018 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-02-2018 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 03-19-2018 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 01-24-2018 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 01-01-2018 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 12-07-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 11-13-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 09-05-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-25-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 07-24-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 06-20-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
| 05-18-2017 | Windows |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html)  |
