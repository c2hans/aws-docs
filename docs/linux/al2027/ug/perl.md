---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/perl.html
---

# Perl in AL2027
<a name="perl"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 The default Perl version in AL2027 is 5.42, and it stays at 5.42 for the life of the release. The package name is `perl`, and we do not namespace it. For more information about the language, see [Learn Perl](https://www.perl.org/learn.html) on the Perl website.

 Perl 5.42 is the only Perl version that AL2027 retains. We do not move to a later feature release, such as 5.44. Updates cover 5.42 patch releases and security fixes only. You can therefore plan on 5.42 throughout the life of your deployment.

## Perl modules in AL2027
<a name="perl-modules"></a>

 You can install many Perl modules as RPMs from the AL2027 repositories. These package names begin with `perl-`. We do not aim to package every module available on CPAN.

 For the modules that we do package, stability and reliability take priority over the newest available version. We do not track the latest release of each module. However, module versions are not locked. A module can move to a newer version after we evaluate the compatibility impact on the packages that depend on it.

 Many packaged modules are dependencies of other operating system packages. We therefore prioritize security patches for those modules over feature updates.
