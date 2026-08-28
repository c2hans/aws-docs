---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/route-53_example_route-53_ListHostedZonesByName_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListHostedZonesByName` with a CLI
<a name="route-53_example_route-53_ListHostedZonesByName_section"></a>

The following code examples show how to use `ListHostedZonesByName`.

------
#### [ CLI ]

**AWS CLI**
The following command lists up to 100 hosted zones ordered by domain name:

```
aws route53 list-hosted-zones-by-name
```
Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-2",
          "Config": {
              "Comment": "test2",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z119WBBTVP5WFX",
          "Name": "2.example.com."
      },
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "test20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "IsTruncated": false,
  "MaxItems": "100"
}
```
The following command lists hosted zones ordered by name, beginning with `www.example.com`:

```
aws route53 list-hosted-zones-by-name --dns-name {{www.example.com}}
```
Output:

```
{
  "HostedZones": [
      {
          "ResourceRecordSetCount": 2,
          "CallerReference": "mwunderl20150527-1",
          "Config": {
              "Comment": "test",
              "PrivateZone": false
          },
          "Id": "/hostedzone/Z3P5QSUBK4POTI",
          "Name": "www.example.com."
      }
  ],
  "DNSName": "www.example.com",
  "IsTruncated": false,
  "MaxItems": "100"
}
```
+  For API details, see [ListHostedZonesByName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns all of your public and private hosted zones in ASCII order by domain name.**

```
Get-R53HostedZonesByName
```
**Example 2: Returns your public and private hosted zones, in ASCII order by domain name, starting at the specified DNS name.**

```
Get-R53HostedZonesByName -DnsName example2.com
```
+  For API details, see [ListHostedZonesByName](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns all of your public and private hosted zones in ASCII order by domain name.**

```
Get-R53HostedZonesByName
```
**Example 2: Returns your public and private hosted zones, in ASCII order by domain name, starting at the specified DNS name.**

```
Get-R53HostedZonesByName -DnsName example2.com
```
+  For API details, see [ListHostedZonesByName](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
