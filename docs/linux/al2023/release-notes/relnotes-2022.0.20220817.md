---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20220817.html
---

# Amazon Linux 2023 version 2022.0.20220817 release notes
<a name="relnotes-2022.0.20220817"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20220817"></a>

Amazon Linux 2022 includes the following major update.

Upcoming Changes in future releases.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.
+ The kernel package will see changes to improve aspects of security and performance, and, while core functionality will be maintained, some unused or deprecated features may be removed in future Release Candidates.

**Java Ecosystem**
+ The `maven`, `xmvn`, and `javapackages-tools` should function as expected, but the versions present in this release have not yet been rebuilt after a bootstrap phase. These packages will be re-built without the use of `javapackages-bootstrap` before General Availability.

**Known Issues**
+ All known issues are resolved.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

## Major changes since the first Tech Preview
<a name="major-changes-20220817"></a>
+ Kernel updated from 5.10 to 5.15
+ OpenSSL updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in AL2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ Curation of packages - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.

This update Amazon Linux 2022 repository and AMI includes the following new packages.

**Repository**
+ `cereal-devel-1.3.2-1.amzn2022`
+ `ec2-hibinit-agent-1.0.4-0.amzn2022`

The repository includes the following packages that were removed since the last release.

The repository includes the following packages that were updated since the last release.
+ `cloud-init-22.2.2-1.amzn2022.1.1`
+ `ecs-init-1.62.1-1.amzn2022`
+ `meson-0.62.2-203.amzn2022`
+ `system-release-2022.0.20220817-0.amzn2022`

## AMIs
<a name="amis-2022020220817"></a>

Default AMI
+ `acpid-2.0.32-4.amzn2022.x86_64`
+ `cloud-init-22.2.2-1.amzn2022.1.1.noarch`
+ `ec2-hibinit-agent-1.0.4-0.amzn2022.noarch`
+ `python3-netifaces-0.10.6-13.amzn2022.aarch64`
+ `python3-netifaces-0.10.6-13.amzn2022.x86_64`
+ `system-release-2022.0.20220817-0.amzn2022.noarch`

Minimal AMI
+ `cloud-init-22.2.2-1.amzn2022.1.1.noarch`
+ `python3-netifaces-0.10.6-13.amzn2022.aarch64`
+ `python3-netifaces-0.10.6-13.amzn2022.x86_64`
+ `system-release-2022.0.20220817-0.amzn2022.noarch`
