---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_rule-packages_across_os.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic rules packages for supported operating systems
<a name="inspector_rule-packages_across_os"></a>

You can run Amazon Inspector Classic rules packages on the EC2 instances that are included in your assessment targets. The following table shows the availability of rules packages for supported operating systems.

**Important**
You can run an agentless assessment with the [Network Reachability](inspector_network-reachability.md) rules package on any EC2 instance regardless of operating system.

**Note**
For more information about supported operating systems, see [Amazon Inspector Classic supported operating systems and Regions](inspector_supported_os_regions.md).

| Supported Operating Systems | Common Vulnerabilities and Exposures | CIS Benchmarks | Network Reachability | Security Best Practices | Runtime Behavior Analysis |
| --- | --- | --- | --- | --- | --- |
| Amazon Linux 2 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2018.03 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2017.09 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2017.03 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2016.09 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2016.03 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2015.09 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2015.03 | Supported | Supported | Supported | Supported | Deprecated |
| Amazon Linux 2014.09 | Supported |   | Supported | Supported |  |
| Amazon Linux 2014.03 | Supported |   | Supported | Supported  |  |
| Amazon Linux 2013.09 | Supported |   | Supported | Supported  |  |
| Amazon Linux 2013.03 | Supported |   | Supported | Supported  |  |
| Amazon Linux 2012.09 | Supported |   | Supported | Supported  |  |
| Amazon Linux 2012.03 | Supported |   | Supported | Supported  |  |
| Ubuntu 20.04 LTS | Supported |  | Supported | Supported |  |
| Ubuntu 18.04 LTS | Supported | Supported | Supported | Supported | Deprecated |
| Ubuntu 16.04 LTS | Supported | Supported | Supported | Supported | Deprecated |
| Ubuntu 14.04 LTS | Supported | Supported | Supported | Supported | Deprecated |
| Debian 10.x, 9.0 - 9.5, 8.0 - 8.7 | Supported |  | Supported | Supported |  |
| RHEL 8.x | Supported |  | Supported | Supported |  |
| RHEL 7.6 - 7.x | Supported | Supported | Supported | Supported |  |
| RHEL 6.2 - 6.9, 7.2 - 7.5 | Supported | Supported | Supported | Supported | Deprecated |
| CentOS 7.6 - 7.X | Supported | Supported | Supported | Supported |  |
| CentOS 6.2 - 6.9, 7.2 - 7.5 | Supported | Supported | Supported | Supported | Deprecated |
| Windows Server 2019 Base | Supported |  | Supported |  |  |
| Windows Server 2016 Base | Supported | Supported | Supported |   | Deprecated |
| Windows Server 2012 R2 | Supported | Supported | Supported |   | Deprecated |
| Windows Server 2012 | Supported | Supported | Supported |   | Deprecated |
| Windows Server 2008 R2 | Supported | Supported | Supported |   | Deprecated |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
