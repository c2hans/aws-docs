---
source_url: https://docs.aws.amazon.com/linux/al2/ug/perl.html
---

# Perl in AL2
<a name="perl"></a>

AL2 provides version 5.16 of the [https://www.perl.org/](https://www.perl.org/) programming language.

## Perl modules in AL2
<a name="perl-modules"></a>

Various Perl modules are packaged as RPMs in AL2. Although there are many Perl modules available as RPMs, Amazon Linux does not try to package every possible Perl module. Modules packaged as RPMs might be relied upon by other operating system RPM packages, so Amazon Linux will prioritize ensuring they are security patched over pure feature updates.

AL2 also includes `CPAN` so that Perl developers can use the idiomatic package manager for Perl modules.
