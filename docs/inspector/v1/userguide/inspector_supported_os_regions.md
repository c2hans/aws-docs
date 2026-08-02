---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_supported_os_regions.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic supported operating systems and Regions
<a name="inspector_supported_os_regions"></a>

This chapter provides information about the operating systems and AWS Regions that Amazon Inspector Classic supports.

**Important**
Currently, Amazon Inspector Classic assessment targets can consist only of EC2 instances. You can run an agentless assessment with the [Network Reachability](inspector_network-reachability.md) rules package on any EC2 instances regardless of operating system.

For information about the Amazon Inspector Classic rules packages that are available across supported operating systems, see [Amazon Inspector Classic rules packages for supported operating systems](inspector_rule-packages_across_os.md).

**Topics**
+ [Supported Linux-based operating systems for the Amazon Inspector Classic agent](#inspector_supported-linux-os)
+ [Supported Windows-based operating systems for the Amazon Inspector Classic agent](#inspector_supported-win-os)
+ [Supported AWS Regions](#inspector_supported-regions)

## Supported Linux-based operating systems for the Amazon Inspector Classic agent
<a name="inspector_supported-linux-os"></a>

You can use the Amazon Inspector Classic agent on 64-bit x86 and [Arm](https://aws.amazon.com/ec2/instance-types/a1/) EC2 instances. The agent is compatible with the following versions of Linux-based operating systems:
+ **64-bit x86 instances**
  + Amazon Linux 2
  + Amazon Linux (2018.03, 2017.09, 2017.03, 2016.09, 2016.03, 2015.09, 2015.03, 2014.09, 2014.03, 2013.09, 2013.03, 2012.09, 2012.03)
  + Ubuntu (20.04 LTS, 18.04 LTS, 16.04 LTS, 14.04 LTS)
  + Debian (10.x, 9.0 - 9.5, 8.0 - 8.7)
  + Red Hat Enterprise Linux (8.x, 7.2, 6.2 - 6.9)
  + CentOS (7.2 - 7.x, 6.2 - 6.9)
+ **Arm instances**
  + Amazon Linux 2
  + Red Hat Enterprise Linux (7.6 - 7.x)
  + Ubuntu (18.04 LTS, 16.04 LTS)

## Supported Windows-based operating systems for the Amazon Inspector Classic agent
<a name="inspector_supported-win-os"></a>

You can use the Amazon Inspector Classic agent only on EC2 instances that run the 64-bit version of the following Windows-based operating systems:
+ Windows Server 2019 Base
+ Windows Server 2016 Base
+ Windows Server 2012 R2
+ Windows Server 2012
+ Windows Server 2008 R2

## Supported AWS Regions
<a name="inspector_supported-regions"></a>

Amazon Inspector Classic is supported in the following AWS Regions:
+ US East (Ohio) us-east-2
+ US East (N. Virginia) us-east-1
+ US West (N. California) us-west-1
+ US West (Oregon) us-west-2
+ Asia Pacific (Mumbai) ap-south-1
+ Asia Pacific (Seoul) ap-northeast-2
+ Asia Pacific (Sydney) ap-southeast-2
+ Asia Pacific (Tokyo) ap-northeast-1
+ Europe (Frankfurt) eu-central-1
+ Europe (Ireland) eu-west-1
+ Europe (London) eu-west-2
+ Europe (Stockholm) eu-north-1
+ AWS GovCloud (US-East) gov-us-east-1
+ AWS GovCloud (US-West) gov-us-west-1

**Note**
The [Network Reachability](inspector_network-reachability.md) rules package is not available in the AWS GovCloud (US) Regions.
