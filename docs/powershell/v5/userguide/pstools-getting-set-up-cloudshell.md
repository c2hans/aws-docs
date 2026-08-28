---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/pstools-getting-set-up-cloudshell.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Installed AWS Tools for PowerShell on AWS CloudShell
<a name="pstools-getting-set-up-cloudshell"></a>

`AWS.Tools` is pre-installed on AWS CloudShell as described in [Pre-installed software](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#pre-installed-software) in the [AWS CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/). Since console credentials are automatically passed to CloudShell, a user with permissions to open CloudShell can immediately run Tools for PowerShell cmdlets without additional installation or configuration.

To use the AWS Tools for PowerShell on CloudShell, perform steps similar to the following:

1. Open the [CloudShell Console](https://console.aws.amazon.com/cloudshell/home).

1. Run `pwsh`.

1. Run any `AWS.Tools` PowerShell commands you need such as `Get-S3Bucket`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
