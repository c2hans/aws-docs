---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_cis.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Center for Internet Security (CIS) Benchmarks
<a name="inspector_cis"></a>

The CIS Security Benchmarks program provides well-defined, unbiased, consensus-based industry best practices to help organizations assess and improve their security. AWS is a CIS Security Benchmarks Member company. For a list of Amazon Inspector Classic certifications, see the [Amazon Web Services page on the CIS website](https://benchmarks.cisecurity.org/membership/certified/amazon/).

Amazon Inspector Classic currently provides the following CIS Certified rules packages to help establish secure configuration postures for the following operating systems:

**Amazon Linux**
+ `CIS Benchmark for Amazon Linux 2 Benchmark v1.0.0 Level 1`
+ `CIS Benchmark for Amazon Linux 2 Benchmark v1.0.0 Level 2`
+ `CIS Benchmark for Amazon Linux Benchmark v2.1.0 Level 1`
+ `CIS Benchmark for Amazon Linux Benchmark v2.1.0 Level 2`
+ `CIS Benchmark for Amazon Linux 2014.09-2015.03 v1.1.0 Level 1`

**CentOS Linux**
+ `CIS Benchmark for CentOS Linux 7 Benchmark v2.2.0 Level 1 Server`
+ `CIS Benchmark for CentOS Linux 7 Benchmark v2.2.0 Level 2 Server`
+ `CIS Benchmark for CentOS Linux 7 Benchmark v2.2.0 Level 1 Workstation`
+ `CIS Benchmark for CentOS Linux 7 Benchmark v2.2.0 Level 2 Workstation`
+ `CIS Benchmark for CentOS Linux 6 Benchmark v2.0.2 Level 1 Server`
+ `CIS Benchmark for CentOS Linux 6 Benchmark v2.0.2 Level 2 Server`
+ `CIS Benchmark for CentOS Linux 6 Benchmark v2.0.2 Level 1 Workstation`
+ `CIS Benchmark for CentOS Linux 6 Benchmark v2.0.2 Level 2 Workstation`

**Red Hat Enterprise Linux**
+ `CIS Benchmark for Red Hat Enterprise Linux 7 Benchmark v2.1.1 Level 1 Server`
+ `CIS Benchmark for Red Hat Enterprise Linux 7 Benchmark v2.1.1 Level 2 Server`
+ `CIS Benchmark for Red Hat Enterprise Linux 7 Benchmark v2.1.1 Level 1 Workstation`
+ `CIS Benchmark for Red Hat Enterprise Linux 7 Benchmark v2.1.1 Level 2 Workstation`
+ `CIS Benchmark for Red Hat Enterprise Linux 6 Benchmark v2.0.2 Level 1 Server`
+ `CIS Benchmark for Red Hat Enterprise Linux 6 Benchmark v2.0.2 Level 2 Server`
+ `CIS Benchmark for Red Hat Enterprise Linux 6 Benchmark v2.0.2. Level 1 Workstation`
+ `CIS Benchmark for Red Hat Enterprise Linux 6 Benchmark v2.0.2 Level 2 Workstation`

**Ubuntu**
+ `CIS Benchmark for Ubuntu Linux 18.04 LTS Benchmark v1.0.0 Level 1 Server`
+ `CIS Benchmark for Ubuntu Linux 18.04 LTS Benchmark v1.0.0 Level 2 Server`
+ `CIS Benchmark for Ubuntu Linux 18.04 LTS Benchmark v1.0.0 Level 1 Workstation`
+ `CIS Benchmark for Ubuntu Linux 18.04 LTS Benchmark v1.0.0 Level 2 Workstation`
+ `CIS Benchmark for Ubuntu Linux 16.04 LTS Benchmark v1.1.0 Level 1 Server`
+ `CIS Benchmark for Ubuntu Linux 16.04 LTS Benchmark v1.1.0 Level 2 Server`
+ `CIS Benchmark for Ubuntu Linux 16.04 LTS Benchmark v1.1.0 Level 1 Workstation`
+ `CIS Benchmark for Ubuntu Linux 16.04 LTS Benchmark v1.1.0 Level 2 Workstation`
+ `CIS Benchmark for Ubuntu Linux 14.04 LTS Benchmark v2.0.0 Level 1 Server`
+ `CIS Benchmark for Ubuntu Linux 14.04 LTS Benchmark v2.0.0 Level 2 Server`
+ `CIS Benchmark for Ubuntu Linux 14.04 LTS Benchmark v2.0.0 Level 1 Workstation`
+ `CIS Benchmark for Ubuntu Linux 14.04 LTS Benchmark v2.0.0 Level 2 Workstation`

**Windows**
+ `Windows Server 2016 (CIS Benchmark for Microsoft Windows 2016 RTM (Release 1607), v1.1.0, Level 1 Member Server Profile)`
+ `Windows Server 2016 (CIS Benchmark for Microsoft Windows 2016 RTM (Release 1607), v1.1.0, Level 2 Member Server Profile)`
+ `Windows Server 2016 (CIS Benchmark for Microsoft Windows 2016 RTM (Release 1607), v1.1.0, Level 1 Domain Controller Profile)`
+ `Windows Server 2016 (CIS Benchmark for Microsoft Windows 2016 RTM (Release 1607), v1.1.0, Level 2 Domain Controller Profile)`
+ `Windows Server 2016 (CIS Benchmark for Microsoft Windows 2016 RTM (Release 1607), v1.1.0, Next Generation Windows Security Profile)`
+ `Windows Server 2012 R2 (CIS Benchmark for Microsoft Windows 2012 R2, v2.2.0, Level 1 Domain Controller Profile)`
+ `Windows Server 2012 R2 (CIS Benchmark for Microsoft Windows 2012 R2, v2.2.0, Level 2 Domain Controller Profile)`
+ `Windows Server 2012 R2 (CIS Benchmark for Microsoft Windows 2012 R2, v2.2.0, Level 1 Member Server Profile)`
+ `Windows Server 2012 R2 (CIS Benchmark for Microsoft Windows 2012 R2, v2.2.0, Level 2 Member Server Profile)`
+ `Windows Server 2012 (CIS Benchmark for Microsoft Windows 2012 non-R2, v2.0.0, Level 1 Member Server Profile)`
+ `Windows Server 2012 (CIS Benchmark for Microsoft Windows 2012 non-R2, v2.0.0, Level 2 Member Server Profile)`
+ `Windows Server 2012 (CIS Benchmark for Microsoft Windows 2012 non-R2, v2.0.0, Level 1 Domain Controller Profile)`
+ `Windows Server 2012 (CIS Benchmark for Microsoft Windows 2012 non-R2, v2.0.0, Level 2 Domain Controller Profile)`
+ `Windows Server 2008 R2 (CIS Benchmark for Microsoft Windows 2008 R2, v3.0.0, Level 1 Domain Controller Profile)`
+ `Windows Server 2008 R2 (CIS Benchmark for Microsoft Windows 2008 R2, v3.0.0, Level 1 Member Server Profile)`

If a specific CIS benchmark appears in a finding that is produced by an Amazon Inspector Classic assessment run, you can download a detailed PDF description of the benchmark from [https://benchmarks.cisecurity.org/](https://benchmarks.cisecurity.org/) (free registration required). The benchmark document provides detailed information about this CIS benchmark, its severity, and how to mitigate it.

For more information, see [Amazon Inspector Classic rules packages for supported operating systems](inspector_rule-packages_across_os.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
