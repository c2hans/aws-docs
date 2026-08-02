---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/route-53_example_route-53_GetHostedZone_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetHostedZone` with a CLI
<a name="route-53_example_route-53_GetHostedZone_section"></a>

The following code examples show how to use `GetHostedZone`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a hosted zone**
The following `get-hosted-zone` command gets information about the hosted zone with an `id` of `Z1R8UBAEXAMPLE`:

```
aws route53 get-hosted-zone --id {{Z1R8UBAEXAMPLE}}
```
+  For API details, see [GetHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns details of the hosted zone with ID Z1D633PJN98FT9.**

```
Get-R53HostedZone -Id Z1D633PJN98FT9
```
+  For API details, see [GetHostedZone](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns details of the hosted zone with ID Z1D633PJN98FT9.**

```
Get-R53HostedZone -Id Z1D633PJN98FT9
```
+  For API details, see [GetHostedZone](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
