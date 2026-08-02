---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-v2-cli.html
---

# Install the AWS IoT Greengrass Core software (CLI)
<a name="install-greengrass-v2-cli"></a>

**Note**
These steps do not apply to nucleus lite.

**To install and configure the AWS IoT Greengrass Core software**

1. On your Greengrass core device, run the following command to switch to the home directory.

------
#### [ Linux or Unix ]

   ```
   cd ~
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   cd %USERPROFILE%
   ```

------
#### [ PowerShell ]

   ```
   cd ~
   ```

------

1. <a name="installation-download-ggc-software-step"></a>On your core device, download the AWS IoT Greengrass Core software to a file named `greengrass-nucleus-latest.zip`.

------
#### [ Linux or Unix ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip -OutFile greengrass-nucleus-latest.zip
   ```

------

   <a name="core-software-license"></a>By downloading this software, you agree to the [Greengrass Core Software License Agreement](https://greengrass-release-license.s3.us-west-2.amazonaws.com/greengrass-license-v1.pdf).

1. <a name="installation-unzip-ggc-software-step"></a>Unzip the AWS IoT Greengrass Core software to a folder on your device. Replace {{GreengrassInstaller}} with the folder that you want to use.

------
#### [ Linux or Unix ]

   ```
   unzip greengrass-nucleus-latest.zip -d {{GreengrassInstaller}} && rm greengrass-nucleus-latest.zip
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   mkdir {{GreengrassInstaller}} && tar -xf greengrass-nucleus-latest.zip -C {{GreengrassInstaller}} && del greengrass-nucleus-latest.zip
   ```

------
#### [ PowerShell ]

   ```
   Expand-Archive -Path greengrass-nucleus-latest.zip -DestinationPath .\\{{GreengrassInstaller}}
   rm greengrass-nucleus-latest.zip
   ```

------

1. Run the following command to launch the AWS IoT Greengrass Core software installer. This command does the following:
   + <a name="install-argument-aws-resources"></a>Create the AWS resources that the core device requires to operate.
   + <a name="install-argument-system-service"></a>Set up the AWS IoT Greengrass Core software as a system service that runs at boot. On Linux devices, this requires the [Systemd](https://en.wikipedia.org/wiki/Systemd) init system.
**Important**  <a name="windows-system-service-requirement-important-note"></a>
On Windows core devices, you must set up the AWS IoT Greengrass Core software as a system service.
   + <a name="install-argument-dev-tools"></a>Deploy the [AWS IoT Greengrass CLI component](gg-cli.md), which is a command-line tool that enables you to develop custom Greengrass components on the core device.
   + <a name="install-argument-component-default-user"></a>Specify to use the `ggc_user` system user to run software components on the core device. On Linux devices, this command also specifies to use the `ggc_group` system group, and the installer creates the system user and group for you.

   Replace argument values in your command as follows.<a name="installer-replace-arguments"></a>

   1. `{{/greengrass/v2}}` or {{C:\\greengrass\\v2}}: The path to the root folder to use to install the AWS IoT Greengrass Core software.

   1. {{GreengrassInstaller}}. The path to the folder where you unpacked the AWS IoT Greengrass Core software installer.

   1. {{region}}. The AWS Region in which to find or create resources.

   1. {{MyGreengrassCore}}. The name of the AWS IoT thing for your Greengrass core device. If the thing doesn't exist, the installer creates it. The installer downloads the certificates to authenticate as the AWS IoT thing. For more information, see [Device authentication and authorization for AWS IoT Greengrass](device-auth.md).
**Note**  <a name="install-argument-thing-name-constraint"></a>
The thing name can't contain colon (`:`) characters.

   1. {{MyGreengrassCoreGroup}}. The name of AWS IoT thing group for your Greengrass core device. If the thing group doesn't exist, the installer creates it and adds the thing to it. If the thing group exists and has an active deployment, the core device downloads and runs the software that the deployment specifies.
**Note**  <a name="install-argument-thing-group-name-constraint"></a>
The thing group name can't contain colon (`:`) characters.

   1. {{GreengrassV2IoTThingPolicy}}. The name of the AWS IoT policy that allows the Greengrass core devices to communicate with AWS IoT and AWS IoT Greengrass. If the AWS IoT policy doesn't exist, the installer creates a permissive AWS IoT policy with this name. You can restrict this policy's permissions for you use case. For more information, see [Minimal AWS IoT policy for AWS IoT Greengrass V2 core devices](device-auth.md#greengrass-core-minimal-iot-policy).

   1. {{GreengrassV2TokenExchangeRole}}. The name of the IAM role that allows the Greengrass core device to get temporary AWS credentials. If the role doesn't exist, the installer creates it and creates and attaches a policy named `{{GreengrassV2TokenExchangeRole}}Access`. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).

   1. {{GreengrassCoreTokenExchangeRoleAlias}}. The alias to the IAM role that allows the Greengrass core device to get temporary credentials later. If the role alias doesn't exist, the installer creates it and points it to the IAM role that you specify. For more information, see [Authorize core devices to interact with AWS services](device-service-role.md).

------
#### [ Linux or Unix ]

   ```
   sudo -E java -Droot="{{/greengrass/v2}}" -Dlog.store=FILE \
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar \
     --aws-region {{region}} \
     --thing-name {{MyGreengrassCore}} \
     --thing-group-name {{MyGreengrassCoreGroup}} \
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} \
     --tes-role-name {{GreengrassV2TokenExchangeRole}} \
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} \
     --component-default-user ggc_user:ggc_group \
     --provision true \
     --setup-system-service true \
     --deploy-dev-tools true
   ```

------
#### [ Windows Command Prompt (CMD) ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" ^
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar ^
     --aws-region {{region}} ^
     --thing-name {{MyGreengrassCore}} ^
     --thing-group-name {{MyGreengrassCoreGroup}} ^
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} ^
     --tes-role-name {{GreengrassV2TokenExchangeRole}} ^
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} ^
     --component-default-user ggc_user ^
     --provision true ^
     --setup-system-service true ^
     --deploy-dev-tools true
   ```

------
#### [ PowerShell ]

   ```
   java -Droot="{{C:\greengrass\v2}}" "-Dlog.store=FILE" `
     -jar ./{{GreengrassInstaller}}/lib/Greengrass.jar `
     --aws-region {{region}} `
     --thing-name {{MyGreengrassCore}} `
     --thing-group-name {{MyGreengrassCoreGroup}} `
     --thing-policy-name {{GreengrassV2IoTThingPolicy}} `
     --tes-role-name {{GreengrassV2TokenExchangeRole}} `
     --tes-role-alias-name {{GreengrassCoreTokenExchangeRoleAlias}} `
     --component-default-user ggc_user `
     --provision true `
     --setup-system-service true `
     --deploy-dev-tools true
   ```

------
**Note**
<a name="jvm-tuning-note"></a>If you are running AWS IoT Greengrass on a device with limited memory, you can control the amount of memory that AWS IoT Greengrass Core software uses. To control memory allocation, you can set JVM heap size options in the `jvmOptions` configuration parameter in your nucleus component. For more information, see [Control memory allocation with JVM options](configure-greengrass-core-v2.md#jvm-tuning).

   When you run this command, you should see the following messages to indicate that the installer succeeded.

   ```
   Successfully configured Nucleus with provisioned resource details!
   Configured Nucleus to deploy aws.greengrass.Cli component
   Successfully set up Nucleus as a system service
   ```
**Note**  <a name="installer-linux-no-systemd-message"></a>
If you have a Linux device and it doesn't have [systemd](https://en.wikipedia.org/wiki/Systemd), the installer won't set up the software as a system service, and you won't see the success message for setting up the nucleus as a system service.
