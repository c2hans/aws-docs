---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html
---

# Comparing AL1 and AL2023
<a name="compare-with-al1"></a>

The following topics describe key differences between AL1 and AL2023 that aren't already covered by the [comparison with AL2](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html).

**Note**
AL1 reached its end-of-life (EOL) on December 31, 2023 and will not receive any security updates or bug fixes starting January 1, 2024. For more information about AL1 EOL and maintenance support, see the blog post [Update on Amazon Linux AMI end-of-life](https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/). We recommend that you upgrade applications to AL2023, which includes long-term support until 2028.

**Topics**
+ [Support for each release](#al1-eol-date)
+ [`systemd` replaces `upstart` as `init` system](#al1-systemd)
+ [Python 2.6 and 2.7 has been replaced with Python 3](#python2.6-no-more)
+ [OpenJDK 8 as oldest JDK](#al1-java)
+ [AL2023 kernel changes from Amazon Linux 1 (AL1)](compare-with-al1-kernel.md)
+ [Comparing packages installed on Amazon Linux 1 (AL1) and Amazon Linux 2023 AMIs](amzn1-al2023-ami.md)
+ [Comparing packages installed on Amazon Linux 1 (AL1) and Amazon Linux 2023 Minimal AMIs](amzn1-al2023-minimal-ami.md)
+ [Comparing packages installed on Amazon Linux 1 (AL1) and Amazon Linux 2023 base container images](amzn1-al2023-container.md)

## Support for each release
<a name="al1-eol-date"></a>

 For AL2023, we offer five years of support from the release date. AL1 ended standard support as of December 31, 2020 and ended maintenance support as of December 31, 2023.

 For more information, see [Release cadence](release-cadence.md).

## `systemd` replaces `upstart` as `init` system
<a name="al1-systemd"></a>

 In AL2 `upstart` was replaced by `systemd` as the `init` system. AL2023 also uses `systemd` as its `init` system, further adopting new features and functionality of `systemd`.

## Python 2.6 and 2.7 has been replaced with Python 3
<a name="python2.6-no-more"></a>

 Although AL1 marked Python 2.6 as EOL with the 2018.03 release, the packages were still available in the repositories to install. AL2 shipped with Python 2.7 as the earliest supported Python version, and AL2023 completes the transition to Python 3. No Python 2.x versions are included in the AL2023 repositories.

For more information on Python on Amazon Linux, see [Python in AL2023](python.md).

## OpenJDK 8 as oldest JDK
<a name="al1-java"></a>

 AL2023 ships with [Amazon Corretto](https://aws.amazon.com/corretto/) as the default (and only) Java Development Kit (JDK). All Java based packages in AL2023 are built with Amazon Corretto 17.

 In AL1, OpenJDK 1.6.0 (`java-1.6.0-openjdk`) went EOL with the first 2018.03 release, and OpenJDK 1.7.0 (`java-1.7.0-openjdk`) went EOL in mid-2020, although both versions were available in the AL1 repositories. The earliest OpenJDK version available in AL2023 is OpenJDK 8, provided by Amazon Corretto 8.
