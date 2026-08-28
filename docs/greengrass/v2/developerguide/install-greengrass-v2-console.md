---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-v2-console.html
---

# Install the AWS IoT Greengrass Core software (console)
<a name="install-greengrass-v2-console"></a>

1. Sign in to the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass).

1. Under **Get started with Greengrass**, choose **Set up core device**.

1. Under **Step 1: Register a Greengrass core device**, for **Core device name**, enter the name of the AWS IoT thing for your Greengrass core device. If the thing doesn't exist, the installer creates it.

1. Under **Step 2: Add to a thing group to apply a continuous deployment**, for **Thing group**, choose the AWS IoT thing group to which you want to add your core device.
   + If you select **Enter a new group name**, then in **Thing group name**, enter the name of the new group to create. The installer creates the new group for you.
   + If you select **Select an existing group**, then in **Thing group name**, choose the existing group that you want to use.
   + If you select **No group**, then the installer doesn't add the core device to a thing group.

1. Under **Step 3: Install the Greengrass Core software**, complete the following steps.

------
#### [ Nucleus classic ]

   1. Choose **Nucleus classic** as your core device's software runtime.

   1. Choose your core device's operating system: **Linux** or **Windows**.

   1. <a name="installer-export-aws-credentials"></a>Provide your AWS credentials to the device so that the installer can provision the AWS IoT and IAM resources for your core device. To increase security, we recommend that you get temporary credentials for an IAM role that allows only the minimum permissions necessary to provision. For more information, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md).
**Note**
The installer doesn't save or store your credentials.

      On your device, do one of the following to retrieve credentials and make them available to the AWS IoT Greengrass Core software installer:
      + (Recommended) Use temporary credentials from AWS IAM Identity Center

        1. Provide the access key ID, secret access key, and session token from the IAM Identity Center. For more information, see **Manual credential refresh** in [ Getting and refreshing temporary credentials](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html#how-to-get-temp-credentials) in the *IAM Identity Center user guide*.

        1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

           ```
           export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           export AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
           ```

------
#### [ Windows Command Prompt (CMD) ]

           ```
           set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           set AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
           ```

------
#### [ PowerShell ]

           ```
           $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
           $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
           $env:AWS_SESSION_TOKEN="{{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}"
           ```

------
      + Use temporary security credentials from an IAM role:

        1. Provide the access key ID, secret access key, and session token from an IAM role that you assume. For more information about how to retrieve these credentials, see [Requesting temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*.

        1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

           ```
           export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           export AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
           ```

------
#### [ Windows Command Prompt (CMD) ]

           ```
           set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           set AWS_SESSION_TOKEN={{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}
           ```

------
#### [ PowerShell ]

           ```
           $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
           $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
           $env:AWS_SESSION_TOKEN="{{AQoDYXdzEJr1K...o5OytwEXAMPLE=}}"
           ```

------
      + Use long-term credentials from an IAM user:

        1. Provide the access key ID and secret access key for your IAM user. You can create an IAM user for provisioning that you later delete. For the IAM policy to give the user, see [Minimal IAM policy for installer to provision resources](provision-minimal-iam-policy.md). For more information about how to retrieve long-term credentials, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.

        1. Run the following commands to provide the credentials to the AWS IoT Greengrass Core software.

------
#### [ Linux or Unix ]

           ```
           export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           ```

------
#### [ Windows Command Prompt (CMD) ]

           ```
           set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
           set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
           ```

------
#### [ PowerShell ]

           ```
           $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
           $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
           ```

------

        1. (Optional) If you created an IAM user to provision your Greengrass device, delete the user.

        1. (Optional) If you used the access key ID and secret access key from an existing IAM user, update the keys for the user so that they are no longer valid. For more information, see [ Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *AWS Identity and Access Management user guide*.

   1. Under **Run the installer**, complete the following steps.

      1. Under **Download the installer**, choose **Copy** and run the copied command on your core device. This command downloads the latest version of the AWS IoT Greengrass Core software and unzips it on your device.

      1. Under **Run the installer**, choose **Copy**, and run the copied command on your core device. This command uses the AWS IoT thing and thing group names that you specified earlier to run the AWS IoT Greengrass Core software installer and set up AWS resources for your core device.

         This command also does the following:
         + <a name="install-argument-system-service"></a>Set up the AWS IoT Greengrass Core software as a system service that runs at boot. On Linux devices, this requires the [Systemd](https://en.wikipedia.org/wiki/Systemd) init system.
**Important**  <a name="windows-system-service-requirement-important-note"></a>
On Windows core devices, you must set up the AWS IoT Greengrass Core software as a system service.
         + <a name="install-argument-dev-tools"></a>Deploy the [AWS IoT Greengrass CLI component](gg-cli.md), which is a command-line tool that enables you to develop custom Greengrass components on the core device.
         + <a name="install-argument-component-default-user"></a>Specify to use the `ggc_user` system user to run software components on the core device. On Linux devices, this command also specifies to use the `ggc_group` system group, and the installer creates the system user and group for you.

         When you run this command, you should see the following messages to indicate that the installer succeeded.

         ```
         Successfully configured Nucleus with provisioned resource details!
         Configured Nucleus to deploy aws.greengrass.Cli component
         Successfully set up Nucleus as a system service
         ```
**Note**  <a name="installer-linux-no-systemd-message"></a>
If you have a Linux device and it doesn't have [systemd](https://en.wikipedia.org/wiki/Systemd), the installer won't set up the software as a system service, and you won't see the success message for setting up the nucleus as a system service.

------
#### [ Nucleus lite ]

   1. Choose **Nucleus lite** as your core device's software runtime.

   1. Select your device set up method to provision your device to a Greengrass core device.

   **Option 1: Set up a device with package download (approximately 1MB)**

   1. Create an AWS IoT thing and the role for Greengrass.

   1. Download the zip file that contains AWS IoT resources that your device needs to connect to AWS IoT:
      + A certificate and private key generated using AWS IoT's certificate authority.
      + A schema file to initiate Greengrass installation for your device.

   1. Download the package that will install the latest Greengrass Nucleus lite runtime to your Raspberry Pi.

   1. Provision your device to become an AWS IoT Greengrass Core device and connect it to AWS IoT:

      1. a. Transfer the Greengrass package and connection kit to your device using a USB thumb drive, SCP/FTP, or SD cards.

      1. b. Unzip the greengrass-package.zip file in the /GreengrassInstaller directory on the device.

      1. c. Unzip the connection kit zip file in the /directory on the device.

      1. d. Run the provided command on the device to install AWS IoT Greengrass

   1. Then, choose **View core devices**.

   **Option 2: Set up a device with a pre-configured whole disk sample image download (approximately 100MB)**

   1. Create an AWS IoT thing and the role for Greengrass.

   1. Download the zip file that contains AWS IoT resources that your device needs to connect to AWS IoT:
      + A certificate and private key generated using AWS IoT's certificate authority.
      + A schema file to initiate Greengrass installation for your device.

   1. Download the pre-configured whole disk sample image that contains Greengrass and the operating system.

      1. To transfer the connection kit and flash the image onto your device, follow the readme file downloaded with the image.

      1. To start Greengrass installation, turn on and boot the device from the flashed image

   1. Then, choose **View core devices**.

   **Option 3: Set up a device with your own custom build**

   1. Create an AWS IoT thing and the role for Greengrass.

   1. Download the zip file that contains AWS IoT resources that your device needs to connect to AWS IoT:
      + A certificate and private key generated using AWS IoT's certificate authority.
      + A schema file to initiate Greengrass installation for your device.

   1. To customize and build your own image using Yocto from source code, and then use the connection kit to install nucleus lite, follow the instructions on GitHub.

      1. Then, choose **View core devices**.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
