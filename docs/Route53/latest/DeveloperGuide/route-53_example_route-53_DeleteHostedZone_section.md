---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53_example_route-53_DeleteHostedZone_section.html
---

# Use `DeleteHostedZone` with a CLI
<a name="route-53_example_route-53_DeleteHostedZone_section"></a>

The following code examples show how to use `DeleteHostedZone`.

------
#### [ CLI ]

**AWS CLI**
**To delete a hosted zone**
The following `delete-hosted-zone` command deletes the hosted zone with an `id` of `Z36KTIQEXAMPLE`:

```
aws route53 delete-hosted-zone --id {{Z36KTIQEXAMPLE}}
```
+  For API details, see [DeleteHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the hosted zone with the specified ID. You will be prompted for confirmation before the command proceeds unless you add the -Force switch parameter.**

```
Remove-R53HostedZone -Id Z1PA6795UKMFR9
```
+  For API details, see [DeleteHostedZone](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the hosted zone with the specified ID. You will be prompted for confirmation before the command proceeds unless you add the -Force switch parameter.**

```
Remove-R53HostedZone -Id Z1PA6795UKMFR9
```
+  For API details, see [DeleteHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using Route 53 with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
