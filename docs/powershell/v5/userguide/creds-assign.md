---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/creds-assign.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Credential and profile resolution
<a name="creds-assign"></a>

## Credentials Search Order
<a name="cred-provider-chain-main"></a>

When you run a command, AWS Tools for PowerShell searches for credentials in the following order. It stops when it finds usable credentials.

1. Literal credentials that are embedded as parameters in the command line.

   We strongly recommend using profiles instead of putting literal credentials in your command lines.

1. Credentials specified by the `-Credential` parameter.

1. A profile name or profile location that was specified by using the [Set-AWSCredential](https://docs.aws.amazon.com/powershell/v5/reference/items/Set-AWSCredential.html) cmdlet.
   + If you specify only a profile name, the command looks for the specified profile in the AWS SDK store and, if that does not exist, the specified profile from the AWS shared credentials file in the default location.
   + If you specify only a profile location, the command looks for the `default` profile from that credentials file.
   + If you specify both a name and a location, the command looks for the specified profile in that credentials file.

   If the specified profile or location is not found, the command throws an exception. Search proceeds to the following steps only if you did not specify a profile or location.

1. Credentials that are created from the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables, if all three variables have a value.

1. The credentials profile with the name specified by the `AWS_PROFILE` environment variable.

1. The default profile, in the following order:

   1. The `default` profile in the AWS SDK store.

   1. The `default` profile in the shared AWS `credentials` file.

   1. The `AWS PS Default` profile in the AWS SDK store.

1. If the command is running on an Amazon EC2 instance that is configured to use an IAM role, the EC2 instance's temporary credentials accessed from the instance profile.

   For more information about using IAM roles for Amazon EC2 instances, see [Granting access with a role](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-hosm.html) in the [AWS SDK for .NET Developer Guide](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/).

If this search fails to locate the specified credentials, the command throws an exception.

For additional information about environment variables and credentials profiles, see the following topics in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/): [Environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html), [Environment variables list](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#EVarSettings), and [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html).
