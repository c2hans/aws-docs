---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-idt-dev-tester-prereqs.html
---

# Set up the LTS qualification prerequisites
<a name="lts-idt-dev-tester-prereqs"></a>

This section describes the prerequisites for testing microcontrollers with AWS IoT Device Tester.

## Prepare for FreeRTOS qualification
<a name="idt-preparing-qualification"></a>

**Note**
AWS IoT Device Tester for FreeRTOS strongly recommends using the latest patch release of the most recently FreeRTOS-LTS version.

IDT for FRQ 2.0 is a qualification for FreeRTOS. Before running IDT FRQ 2.0 for qualification, you must complete [Qualifying your board](https://docs.aws.amazon.com/freertos/latest/qualificationguide/freertos-qualification.html) in the *FreeRTOS Qualification Guide*. To port libraries, tests, and setup the `manifest.yml`, see [Porting the FreeRTOS libraries](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting.html) in the *FreeRTOS Porting Guide*. FRQ 2.0 contains a different process for qualification. See [Latest changes in qualification](https://docs.aws.amazon.com/freertos/latest/qualificationguide/latest-changes.html) in the *FreeRTOS qualification guide* for details.

The [FreeRTOS-Libraries-Integration-Tests](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests) repository must be present for IDT to run. See the [README.md](https://github.com/FreeRTOS/FreeRTOS-Libraries-Integration-Tests/blob/main/README.md) on how to clone and port this repository to your source project. FreeRTOS-Libraries-Integration-Tests must include the `manifest.yml` located in the root of your project, for IDT to run.

**Note**
IDT is dependent on the tests repository's implementation of `UNITY_OUTPUT_CHAR`. The test output logs and the device logs must not interleave with each other. See [ Implementing the library logging macros](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-library-logging-macros.html) section in the *FreeRTOS Porting Guide* for further details.

## Download IDT for FreeRTOS
<a name="idt-download-dev-tester-afr"></a>

Every version of FreeRTOS has a corresponding version of IDT for FreeRTOS to perform qualification tests. Download the appropriate version of IDT for FreeRTOS from [ Supported versions of AWS IoT Device Tester for FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/dev-test-versions-afr.html).

Extract IDT for FreeRTOS to a location on the file system where you have read and write permissions. Since Microsoft Windows has a character limit for the path length, extract IDT for FreeRTOS into a root directory such as `C:\` or `D:\`.

**Note**
Multiple users must not run IDT from a shared location, such as an NFS directory or a Windows network shared folder. This will result in crashes or data corruption. We recommend that you extract the IDT package to a local drive.

## Download Git
<a name="idt-download-git"></a>

IDT must have Git installed as a prerequisite to ensure source code integrity.

Follow the instructions in the [GitHub](https://github.com/git-guides/install-git) guide to install Git. To verify the current installed version of Git, enter the command `git --version` at the terminal.

**Warning**
IDT uses Git to align with a directory's status of clean or dirty. If Git is not installed, the `FreeRTOSIntegrity` test groups will either fail, or won't run as expected. If IDT returns an error such as `git executable not found` or `git command not found`, install or re-install Git and try again.

**Topics**
+ [Prepare for FreeRTOS qualification](#idt-preparing-qualification)
+ [Download IDT for FreeRTOS](#idt-download-dev-tester-afr)
+ [Download Git](#idt-download-git)
+ [Create an AWS account](#lts-config-aws-account)
+ [AWS IoT Device Tester managed policy](#managed-policy)
+ [(Optional) Install the AWS Command Line Interface](#install-cli)

## Create an AWS account
<a name="lts-config-aws-account"></a>

**Note**
The full IDT qualification suite is supported only in the following AWS Regions
US East (N. Virginia)
 US West (Oregon)
Asia Pacific (Tokyo)
Europe (Ireland)

In order to test your device, IDT for FreeRTOS creates resources like AWS IoT things, FreeRTOS groups and Lambda functions. To create those resources, IDT for FreeRTOS requires you to create and configure an AWS account, and an IAM policy that grants IDT for FreeRTOS permission to access resources on your behalf while running tests.

The following steps are to create and configure your AWS account.

1. If you already have an AWS account, skip to the next step. Else create an [AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).

1. Follow the steps in [ Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html). Do not add permissions or policies at this time.

1. To run OTA qualification tests, go to Step 4. Else go to Step 5.

1.  Attach the OTA IAM permissions inline policy to your IAM role.

   1.
**Important**
 The following policy template grants IDT permission to create roles, create policies, and attach policies to roles. IDT for FreeRTOS uses these permissions for tests that create roles. Although the policy template doesn't provide administrator privileges to the user, the permissions can be used to gain administrator access to your AWS account.

   1.  Follow the steps below to attach the necessary permissions to your IAM role:

      1. On the **Permissions** page, choose **Add permissions**.

      1. Choose **Create inline policy**.

      1. Choose the **JSON** tab and copy the following permissions in to the **JSON** text box. Use the template under **Most Regions** if you are not in the China region. If you are in the China region, use the template under **Beijing and Ningxia Regions**.

------
#### [ Most Regions ]

------
#### [ JSON ]

****

         ```
         {
             "Version":"2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": "iotdeviceadvisor:*",
                     "Resource": [
                         "arn:aws:iotdeviceadvisor:*:*:suiterun/*/*",
                         "arn:aws:iotdeviceadvisor:*:*:suitedefinition/*"
                     ]
                 },
                 {
                     "Effect": "Allow",
                     "Action": "iam:PassRole",
                     "Resource": "arn:aws:iam::*:role/idt*",
                     "Condition": {
                         "StringEquals": {
                             "iam:PassedToService": "iotdeviceadvisor.amazonaws.com"
                         }
                     }
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "execute-api:Invoke*",
                         "iam:ListRoles",
                         "iot:Connect",
                         "iot:CreateJob",
                         "iot:DeleteJob",
                         "iot:DescribeCertificate",
                         "iot:DescribeEndpoint",
                         "iot:DescribeJobExecution",
                         "iot:DescribeJob",
                         "iot:DescribeThing",
                         "iot:GetPolicy",
                         "iot:ListAttachedPolicies",
                         "iot:ListCertificates",
                         "iot:ListPrincipalPolicies",
                         "iot:ListThingPrincipals",
                         "iot:ListThings",
                         "iot:Publish",
                         "iot:UpdateThingShadow",
                         "logs:CreateLogGroup",
                         "logs:CreateLogStream",
                         "logs:DescribeLogGroups",
                         "logs:DescribeLogStreams",
                         "logs:PutLogEvents",
                         "logs:PutRetentionPolicy"
                     ],
                     "Resource": "*"
                 },
                 {
                     "Effect": "Allow",
                     "Action": "iotdeviceadvisor:*",
                     "Resource": "*"
                 },
                 {
                     "Effect": "Allow",
                     "Action": "logs:DeleteLogGroup",
                     "Resource": "arn:aws:logs:*:*:log-group:/aws/iot/deviceadvisor/*"
                 },
                 {
                     "Effect": "Allow",
                     "Action": "logs:GetLogEvents",
                     "Resource": "arn:aws:logs:*:*:log-group:/aws/iot/deviceadvisor/*:log-stream:*"
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "iam:CreatePolicy",
                         "iam:DetachRolePolicy",
                         "iam:DeleteRolePolicy",
                         "iam:DeletePolicy",
                         "iam:CreateRole",
                         "iam:DeleteRole",
                         "iam:AttachRolePolicy"
                     ],
                     "Resource": [
                         "arn:aws:iam::*:policy/idt*",
                         "arn:aws:iam::*:role/idt*"
                     ]
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "ssm:GetParameters"
                     ],
                     "Resource": [
                         "arn:aws:ssm:*::parameter/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
                     ]
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "ec2:DescribeInstances",
                         "ec2:RunInstances",
                         "ec2:CreateSecurityGroup",
                         "ec2:CreateTags",
                         "ec2:DeleteTags"
                     ],
                     "Resource": [
                         "*"
                     ]
                 },
                 {
                     "Effect": "Allow",
                     "Action": [
                         "ec2:CreateKeyPair",
                         "ec2:DeleteKeyPair"
                     ],
                     "Resource": [
                         "arn:aws:ec2:*:*:key-pair/idt-ec2-ssh-key-*"
                     ]
                 },
                 {
                     "Effect": "Allow",
                     "Condition": {
                         "StringEqualsIgnoreCase": {
                             "aws:ResourceTag/Owner": "IoTDeviceTester"
                         }
                     },
                     "Action": [
                         "ec2:TerminateInstances",
                         "ec2:DeleteSecurityGroup",
                         "ec2:AuthorizeSecurityGroupIngress",
                         "ec2:RevokeSecurityGroupIngress"
                     ],
                     "Resource": [
                         "*"
                     ]
                 }
             ]
         }
         ```

------

------
#### [ Beijing and Ningxia Regions ]

         The following policy template can be used in the Beijing and Ningxia Regions.

------

      1. When you're finished, choose **Review policy**.

      1. Enter **IDTFreeRTOSIAMPermissions** as the policy name.

      1. Choose **Create policy**.

1.  Attach **AWSIoTDeviceTesterForFreeRTOSFullAccess** to your IAM role.

   1. To attach the necessary permissions to your IAM role:

      1. On the **Permissions** page, choose **Add permissions**.

      1. Choose **Attach policies**.

      1. Search for the **AWSIoTDeviceTesterForFreeRTOSFullAccess** policy. Check the box.

   1. Choose **Add permissions**.

1. Export credentials for IDT. See [Getting IAM role credentials for CLI access](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html) for details.

## AWS IoT Device Tester managed policy
<a name="managed-policy"></a>

The `AWSIoTDeviceTesterForFreeRTOSFullAccess` managed policy contains the following AWS IoT Device Tester permissions for version checking, auto update features, and collection of metrics.
+ `iot-device-tester:SupportedVersion`

  Grants AWS IoT Device Tester permission to fetch the list of supported products, test suites and IDT versions.
+ `iot-device-tester:LatestIdt`

  Grants AWS IoT Device Tester permission to fetch the latest IDT version available for download.
+ `iot-device-tester:CheckVersion`

  Grants AWS IoT Device Tester permission to check version compatibility for IDT, test suites and products.
+ `iot-device-tester:DownloadTestSuite`

  Grants AWS IoT Device Tester permission to download test suite updates.
+ `iot-device-tester:SendMetrics`

  Grants AWS permission to collect metrics about AWS IoT Device Tester internal usage.

## (Optional) Install the AWS Command Line Interface
<a name="install-cli"></a>

You might prefer to use the AWS CLI to perform some operations. If you don't have the AWS CLI installed, follow the instructions at [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

Configure the AWS CLI for the AWS Region you want to use by running **aws configure** from a command line. For information about the AWS Regions that support IDT for FreeRTOS, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#amazon-freertos-ota-control). For more information about **aws configure** see [ Quick configuration with **aws configure**](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config).
