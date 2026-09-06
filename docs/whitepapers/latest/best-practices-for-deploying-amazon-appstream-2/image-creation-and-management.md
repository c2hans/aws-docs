---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/image-creation-and-management.html
---

# Image creation and management
<a name="image-creation-and-management"></a>

 When launching a fleet or image builder in WorkSpaces Applications, you must select one of the WorkSpaces Applications base images. Administrators can then build on the base image to add their own applications and configuration settings.

 There are key considerations when building an image to ensure applications work correctly and securely. In addition, there are design considerations for how that image will be maintained.

## Building a WorkSpaces Applications image
<a name="building-an-appstream-2.0-image"></a>

 When building a new image, it is important to consider the following:
+  Operating system
+  Applications
+  User profile
+  Security
+  Performance
+  Agent version
+  Image Assistant CLI

## Building a WorkSpaces Applications image
<a name="operating-system"></a>

 In November 2021, WorkSpaces Applications launched support for Amazon Linux 2. With this announcement, WorkSpaces Applications now supports four platform types:
+  Windows Server 2012 R2
+  Windows Server 2016
+  Windows Server 2019
+  Amazon Linux 2

It’s possible that you may have to choose a particular platform based on what is required by your application (for example, if your application requires Windows, Amazon Linux 2 will not be an option). Beyond application requirements, reference the following comparison matrix to help you choose which platform type best fits your use case and environment:

*Table 1 — Platform types, when to use them, and pricing*

|  Platform type  |   **When to use**   |   **Fleet pricing\***   |
| --- | --- | --- |
| Windows Server (2012 R2, 2016 or 2019) | Your application can be run only in Windows (and it does not support Amazon Linux 2). You wish to domain join your streaming instances. You wish to use existing Group Policy on your WorkSpaces Applications streaming instances (Linux does not adhere to Group Policy, but you can use [Session Scripts](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-session-scripts.html) to automate configuration when a session starts). You will use Desktop View and your users prefer the Windows desktop experience. You prefer to use the Image Assistant application, which provides a step-by-step wizard, to create your application catalog and image. Currently, you must create your Amazon Linux 2 image using terminal commands (see [this tutorial](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-create-linux-image.html) for more info). You want to use [Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html). Enabling application settings persistence is currently not supported for Linux-based stacks. | RDS SAL (Microsoft Remote Desktop Services Subscriber Access License) fee of $4.19 per month for each unique user\*\* plus the following:1.  $0.10 per hour for Always-On, On-Demand fleets <br />2.  $0.15 per hour for Elastic fleets  |
| Amazon Linux 2 | You want to take advantage of lower cost streaming instances and avoid RDS SAL license fees.Your applications are compatible with Amazon Linux 2 | Linux instances are lower cost compared to Window instances. With Linux, you pay no RDS SAL fees and the following hourly fees:1.  $0.084 per hour for Always-On, On-Demand fleets <br />2.  $0.112 per hour for Elastic fleets  |

\* Based on stream.standard.medium in N Virginia Region

\*\* Eligible customers can bring their own license to eliminate AWS RDS SAL fees. See the [WorkSpaces Applications pricing page](http://aws.amazon.com/appstream2/pricing/) for more details. Education customers may also be eligible for a special. Schools, universities, and certain public institutions may qualify for a reduced Microsoft RDS SAL user fee.

## Applications
<a name="applications"></a>

 Prior to installing applications, it is important to review application requirements such as application dependencies and hardware requirements. After successfully installing applications on image builder instances, make sure to switch users and test applications under the test user context.

When planning your application deployment, be aware of the [service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aas2.html). Additionally, clean up installer and helper files to optimize total C Drive space prior to creating an image. As a reminder, the WorkSpaces Applications instances have one 200 GB fixed-size volume. Optimizing on disk space after installations is a best practice to ensure that fixed-size volume is never exceeded.

 If you would like to modify the catalog of applications your users can access in real-time, dynamic application framework provides API operations. The applications managed by the dynamic app providers can be within the image, or they can be off-instance, such as from a Windows file share or an application virtualization technology. This feature requires an WorkSpaces Applications fleet that is joined to a Microsoft Active Directory domain. For more information, refer to [*Using Active Directory with WorkSpaces Applications*](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory.html).

## App blocks
<a name="app-blocks"></a>

 App blocks represent the setup script and application files necessary to launch the applications your users will use. The virtual hard disk (VHD) can be any object from Amazon S3. It is recommended that this object be less than 1.5GB, since it has to fully downloaded before the user can access the application.

**Optimizing app blocks**

For Windows-based fleets, it is recommended you create a VHDX file to contain your application. For Linux-based fleets, it is recommended you create an image (IMG). These virtual disk should be created as small as possible, to host the application files. Virtual disks can be zipped to further decrease their size. In the setup script, you will need to unzip the disk before mounting. The [example Windows PowerShell setup script](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks.html#create-setup-script) has the unzip functionality included. There is a trade off between expanding an archive (zip) and download speed. Some testing may be necessary to find a balance that offers the fastest application launch time.

**Updating applications**

Applications can have both minor and major changes. For minor updates, use [enable versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) on the Amazon S3 bucket that hosts your app block files. This setting allows administrators to roll back to previous versions of a specific application by changing the version of the application VHD object in question without changing the app block configuration. With major updates, [create a new App block](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks.html#create-app-block) for the updated VHD. This will allow administrators to separate major application changes at the app block level opposed to the versioning level, which provides a more organized approach for administrative application management.

## User profile customization
<a name="user-profile-customization"></a>

 Amazon WorkSpaces Applications is by design a non-persistent application and desktop solution. When a user session is terminated, both system and user changes are terminated as well. Enable [*application settings persistence*](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-it-works-app-settings-persistence.html) only when required. It can add overhead to the logon process, and cost considerations for the required S3 storage.

 In situations where application settings persistence is required, AWS recommends securing that connection through custom policy and S3 VPC gateway endpoint. Evaluate the overall application settings size, and minimize the settings saved in application settings persistence to optimize cost and performance.

 User profile customization can be configured on a WorkSpaces Applications Image Builder instance. This includes adding and modifying registry keys, adding files, and other user specific configurations. From the WorkSpaces Applications Image Assistant, there is an option to create a user profile. This copies the template user profile to the default user profile. After the image is deployed to a fleet, end users who stream sessions from the fleet will have their user profile created from the default user profile. It is important to consider minimizing the user profile size, especially when Application Settings Persistence is enabled. By default, the maximum [*VHDx*](https://en.wikipedia.org/wiki/VHD_(file_format)) size for user profile is 1 GB. Each time a streaming session starts, a user profile VHDx file is downloaded from an S3 bucket. This increases the streaming session preparation time and introduces a risk of exceeding the limit, which will cause a failure of the user profile mount using the VHDx file.

 For use cases which require a user profile larger than 1 GB, AWS recommends using alternative methods to store profiles. For example, using Roaming profiles, or FSLogix Profile Containers on shared storage such as [*Amazon FSx for Windows File Server*](http://aws.amazon.com/fsx/). For more information, refer to [*Use Amazon FSx for Windows File Server and FSLogix to Optimize Application Settings Persistence on Amazon WorkSpaces Applications*](http://aws.amazon.com/blogs/desktop-and-application-streaming/use-amazon-fsx-and-fslogix-to-optimize-application-settings-persistence-on-amazon-appstream-2-0/).

## Security
<a name="security"></a>

 There are different security measurements developers need to consider. WorkSpaces Applications administrators are responsible for installing and maintaining the updates for the Windows operating system, your applications, and their dependencies. For additional guidance on keeping base images up to date, refer to [*Keep Your WorkSpaces Applications Image Up-to-Date*](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#keep-image-updated) for additional guidance on keeping base images up to date.

 By default, WorkSpaces Applications allows users or applications to start any program on the instance, beyond what is specified in the image application catalog. This is useful when your application relies on another application as part of a workflow, but you don’t want the user to be able to start that dependent application directly. For example, your application starts the browser to provide help instructions from the application vendor’s website, but you don’t want the user to start the browser directly. In some situations, you may want to control which applications can be launched on the streaming instances. Microsoft AppLocker is application control software that uses explicit control policies to enable, or disable, which applications a user can run.

 Antivirus software can adversely affect streaming sessions and image builder instances. AWS recommends that you do **not** enable automatic updates for the antivirus software. For more information on Windows Defender, refer to [*Antivirus Software*](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#windows-update-antivirus-software-av).

## Performance
<a name="performance"></a>

 Before creating a new image, it is important to test applications as a test user. Testing as a test user enables you to ensure that applications can run under a non-administrator user context. Additionally, check application performance and user experience using built-in tools such as Task Manager and Performance Monitor. It is a best practice to monitor resource utilization such as CPU, memory, and GPU memory. If there is CPU, memory, or GPU memory resource constraint, consider upgrading the instance type. To enhance performance:
+  Disable browser pop-up windows
+  Disable Enhanced IE Security

## WorkSpaces Applications agent version selection
<a name="appstream-2.0-agent-version-selection"></a>

 When creating a new image, you can opt to use the latest WorkSpaces Applications agent software, or not update. Each version of the WorkSpaces Applications agent software includes bug fixes and feature enhancements. Keep your image with the most up-to-date software. Review mechanisms for this in the [*Image updates*](image-updates.md) section of this document.

 You can choose the **Use latest agent** option. This option ensures that on start, the latest WorkSpaces Applications agent is always installed. However, unexpected changes may affect user experiences, and an agent update can increase the time to start an instance. Updating a base image requires recreation of the image. It is also important that you perform testing before rolling out the updated image to production to minimize startup time.

## Image Assistant Command Line Interface (CLI)
<a name="image-assistant-command-line-interface-cli"></a>

 For developers who want to automate or programmatically create WorkSpaces Applications images, use the Image Assistant CLI. This is available on image builders with the WorkSpaces Applications agent software released on or after July 26, 2019. The following high-level overview describes the process for programmatically creating a WorkSpaces Applications image:

1.  Use your application installation automation to install the required applications on your image builder. This installation may include applications that your users will launch, any dependencies, and background applications.

1.  Determine the files and folders to optimize.

1.  If applicable, use the Image Assistant `add-application` CLI operation to specify the application metadata and optimization manifest for the WorkSpaces Applications image.

1.  To specify additional applications for the WorkSpaces Applications image, repeat steps 1 through 3 for each application as needed.

1.  If applicable, use the Image Assistant `update-default-profile` CLI operation to overwrite the default Windows profile and create the default application and Windows settings for your users.

1.  Use the Image Assistant `create-image` CLI operation to create the image.

 For more information, refer to [*Create Your WorkSpaces Applications Image Programmatically by Using the Image Assistant CLI Operations*](https://docs.aws.amazon.com/appstream2/latest/developerguide/programmatically-create-image.html).
