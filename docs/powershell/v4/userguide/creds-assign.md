---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/creds-assign.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Credential and profile resolution
<a name="creds-assign"></a>

## Credentials Search Order
<a name="cred-provider-chain-main"></a>

When you run a command, AWS Tools for PowerShell searches for credentials in the following order. It stops when it finds usable credentials.

1. Literal credentials that are embedded as parameters in the command line.

   We strongly recommend using profiles instead of putting literal credentials in your command lines.

1. A specified profile name or profile location.
   + If you specify only a profile name, the command looks for the specified profile in the AWS SDK store and, if that does not exist, the specified profile from the AWS shared credentials file in the default location.
   + If you specify only a profile location, the command looks for the `default` profile from that credentials file.
   + If you specify both a name and a location, the command looks for the specified profile in that credentials file.

   If the specified profile or location is not found, the command throws an exception. Search proceeds to the following steps only if you did not specify a profile or location.

1. Credentials specified by the `-Credential` parameter.

1. The session profile, if one exists.

1. The default profile, in the following order:

   1. The `default` profile in the AWS SDK store.

   1. The `default` profile in the AWS shared credentials file.

   1. The `AWS PS Default` profile in the AWS SDK store.

1. If the command is running on an Amazon EC2 instance that is configured to use an IAM role, the EC2 instance's temporary credentials accessed from the instance profile.

   For more information about using IAM roles for Amazon EC2 instances, see the [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/).

If this search fails to locate the specified credentials, the command throws an exception.
