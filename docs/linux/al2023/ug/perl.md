---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/perl.html
---

# Perl in AL2023
<a name="perl"></a>

AL2023 provides version 5.32 of the [Perl](https://www.perl.org/) programming language.

Although Perl has provided a high degree of language compatibility as part of Perl 5 releases over the past decades, Amazon Linux is not expected to move from Perl 5.32 during the AL2023 release. Amazon Linux will continue to security patch Perl for the lifetime of AL2023 in accordance with our [package support statements](https://docs.aws.amazon.com/linux/al2023/release-notes/all-packages-AL2023.12.html).

## Perl modules in AL2023
<a name="perl-modules"></a>

Various Perl modules are packaged as RPMs in AL2023. Although there are many Perl modules available as RPMs, Amazon Linux does not aim to package every possible Perl module. Modules packaged as RPMs might be relied upon by other operating system RPM packages, so Amazon Linux will prioritize those security patches over pure feature updates.

AL2023 also includes `CPAN` so that Perl developers can use the idiomatic package manager for Perl modules.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
