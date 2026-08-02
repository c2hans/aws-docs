---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/log4j-hotpatch.html
---

# Removal of log4j hotpatch (`log4j-cve-2021-44228-hotpatch`)
<a name="log4j-hotpatch"></a>

**Note**
AL2023 doesn't ship with the `log4j-cve-2021-44228-hotpatch` package.

 In response to [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html), Amazon Linux released an RPM packaged version of the [Hotpatch for Apache Log4j](https://aws.amazon.com/blogs/opensource/hotpatch-for-apache-log4j/) for AL1 and AL2. In the [announcement of the addition of the hotpatch to Amazon Linux](https://alas.aws.amazon.com/announcements/2021-001.html) we noted that "Installing the hotpatch is not a replacement for updating to a log4j version that mitigates CVE-2021-44228 or CVE-2021-45046.".

 The hotpatch was a mitigation to allow time to patch `log4j`. The first General Availability (GA) release of AL2023 was 15 months after [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html), thus AL2023 doesn't ship with the hotpatch (enabled or not).

 Users running their own `log4j` versions on Amazon Linux should ensure that they have updated to versions not affected by [CVE-2021-44228](https://alas.aws.amazon.com/cve/html/CVE-2021-44228.html) or [CVE-2021-45046](https://alas.aws.amazon.com/cve/html/CVE-2021-45046.html).

 AL2023 provides guidance on [Updating AL2023](updating.md) so that you can keep up to date with security patches. Security advisories are published on the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
