---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html
---

# Amazon EC2 macOS AMIs release notes
<a name="macos-ami-overview"></a>

The following information provides details about the packages included by default in the EC2 macOS AMIs and summarizes the changes for each EC2 macOS AMI release.

For information about how to subscribe to macOS AMI notifications, see [Subscribe to macOS AMI notifications](macos-subscribe-notifications.md).

Mac instances can run one of the following operating systems:
+ macOS Mojave (version 10.14) (x86 Mac instances only)
+ macOS Catalina (version 10.15) (x86 Mac instances only)
+ macOS Big Sur (version 11) (x86 and M1 Mac instances)
+ macOS Monterey (version 12) (x86 and M1 Mac instances)
+ macOS Ventura (version 13) (all Mac instances, M2 and M2 Pro Mac instances support macOS Ventura version 13.2 or later)
+ macOS Sonoma (version 14) (all Mac instances)
+ macOS Sequoia (version 15) (all Mac instances)
**Note**
M4 and M4 Pro Mac instances support macOS Sequoia version 15.6 or later.

## Approve Local Network Privacy policies for macOS Sequoia
<a name="macos-sequoia-lnp"></a>

macOS Sequoia (version 15) has a new Local Network Privacy feature that impacts users of local IP-based services, including Amazon EC2 Instance Metadata Service (IMDS).

**Important**
To make sure that you have uninterrupted access to local IP-based services, use the following steps to approve the Local Network Privacy policies.

**To approve Local Network Privacy policies**

1. [Connect to your instance's graphical user interface (GUI)](connect-to-mac-instance.md#mac-instance-vnc).

1. Follow the prompts on the screen to approve the Local Network Privacy policies.

1. After you have approved the policies, create an AMI of your EC2 Mac instance. For more information, see [Create an Amazon EBS-backed AMI](creating-an-ami-ebs.md).

Any EC2 Mac instances that are launched from the newly created AMI will retain the Local Network Privacy permissions.

## Default packages included in Amazon EC2 macOS AMIs
<a name="macos-ami-default-packages"></a>

The following table describes packages that are included by default in the EC2 macOS AMIs.

| Packages | Release notes |
| --- | --- |
| EC2 macOS Init | [https://github.com/aws/ec2-macos-init/tags](https://github.com/aws/ec2-macos-init/tags) |
| EC2 macOS Utils | [https://github.com/aws/ec2-macos-utils/tags](https://github.com/aws/ec2-macos-utils/tags) |
| Amazon SSM Agent | [https://github.com/aws/amazon-ssm-agent/releases](https://github.com/aws/amazon-ssm-agent/releases) |
| AWS Command Line Interface (AWS CLI) version 2 | [https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) |
| Command Line Tools for Xcode | [https://developer.apple.com/documentation/xcode-release-notes](https://developer.apple.com/documentation/xcode-release-notes) |
| Homebrew | [https://github.com/Homebrew/brew/releases](https://github.com/Homebrew/brew/releases) |
| EC2 Instance Connect | [https://github.com/aws/aws-ec2-instance-connect-config/releases](https://github.com/aws/aws-ec2-instance-connect-config/releases) |
| Safari | [https://developer.apple.com/documentation/safari-release-notes](https://developer.apple.com/documentation/safari-release-notes) |

## Amazon EC2 macOS AMI updates
<a name="macos-ami-change-log"></a>

The following table describes changes included in the EC2 macOS AMI releases. Note that some changes apply to all EC2 macOS AMIs, whereas others apply to only a subset of these AMIs.

### EC2 macOS AMI updates
<a name="monthly-ami-updates"></a>

| Release | Changes |
| --- | --- |
| 2026.07.29 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2026.05.19 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2026.04.20 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2026.04.16 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2026.03.17 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2026.03.03 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.12.26 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.12.17 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.11.18 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.09.04 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.08.05 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.06.27 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.05.21 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.05.05 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.03.18 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2025.01.24 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2024.12.20 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2024.10.28 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2024.08.20 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2024.06.07 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
| 2024.04.12 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html) [See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html)  |
