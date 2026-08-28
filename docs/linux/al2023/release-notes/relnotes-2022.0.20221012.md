---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20221012.html
---

# Amazon Linux 2023 version 2022.0.20221012 release notes
<a name="relnotes-2022.0.20221012"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20221012"></a>

Amazon Linux 2022 includes the following major updates.
+ Starting with [AL2023 version 2022.0.20220728](relnotes-2022.0.20220728.md), SELinux was switched from an enforcing to a permissive mode by default. You can change SELinux settings to enforced mode via command line by running the `setenforce` command.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.

**Known Issues**
+ Amazon Linux 2022 contains a known issue where customer defined NTP servers via DHCP are not honored.

  **Work-Around** - Configure the NTP servers using a config file in `/etc/chrony.d`
+ Enabling FIPS mode is currently unsupported, and there will be changes to how a FIPS mode enabled system works in upcoming releases.
+ There is a known issue by which enabling FIPS mode with `update-crypto-policies —set FIPS` will result in a non functional system. This will be addressed in a future release.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

**Contact us**

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2022/security/policy) rather than opening an issue.

We use GitHub issues to gather feedback about Amazon Linux 2022 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2022/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2022/issues/new/choose).

If you just have questions about Amazon Linux 2022, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2022/discussions). Feedback on Amazon Linux 2022 can also be provided through your designated AWS representative.

## Major changes since the first Tech Preview release
<a name="major-changes-20221012"></a>
+ `Kernel` updated from 5.10 to 5.15
+ `OpenSSL` updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in Amazon Linux 2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ `rsyslog` is no longer installed by default, and thus the `system-journald` is the way `syslog` works, with `journalctl` as the client that can look at logs.
+ The default `curl` is part of the `curl-minimal` package, which supports the most popular protocols. You can switch to the full-featured `curl` if needed by running `dnf install --allowerasing curl-full libcurl-full`
+ The default `gnupg` is a minimal one, which is limited in functionality, but has the minimal code needed to GPG verify RPMs, and brings a minimal number of packages into AMIs and container images. If you need full `gnupg` functionality, you can get the full `gnupg` by running `dnf install --allowerasing gnupg2-full`
+ **Curation of packages** - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.
+ The Java ecosystem is now based on Amazon Corretto 17 rather than OpenJDK 11. Java build tools have been rebuilt to newer versions and run with Amazon Corretto.

**Repository**

This update to the Amazon Linux 2022 repository and AMI includes the following new packages.
+ `amazon-ecr-credential-helper-0:0.6.0-1.amzn2022.src`
+ `container-selinux-2:2.189.0-287.amzn2022.src`
+ `dotnet6.0-0:6.0.108-1.amzn2022.0.1.src`
+ `libpeas-0:1.32.0-1.amzn2022.0.2.src`
+ `lttng-ust-0:2.13.1-2.amzn2022.0.2.src`

The repository includes the following packages that were removed since the last release.
+ `apache-commons-daemon-1.2.4-1.amzn2022`
+ `apache-commons-lang-2.6-33.amzn2022`
+ `cal10n-0.8.1-14.amzn2022`
+ `dain-snappy-0.4-12.amzn2022`
+ `findbugs-3.0.1-25.amzn2022`
+ `findbugs-bcel-6.0-0.22.20140707svn1547656.amzn2022`
+ `jakarta-persistence-2.2.3-2.amzn2022`
+ `jakarta-ws-rs-2.1.6-8.amzn2022`
+ `jakarta-xml-rpc-1.1.4-2.amzn2022`
+ `jboss-el-2.2-api-1.0.5-5.amzn2022`
+ `jboss-jsp-2.2-api-1.0.1-24.amzn2022`
+ `jboss-modules-1.5.2-13.amzn2022`
+ `maven-artifact-resolver-1.0-26.amzn2022`
+ `maven-install-plugin-2.5.2-14.amzn2022`
+ `objectweb-pom-1.5-14.amzn2022`
+ `os-maven-plugin-1.6.2-3.amzn2022`
+ `shrinkwrap-1.2.6-6.amzn2022`
+ `snappy-java-1.1.2.4-19.amzn2022`
+ `tomcat-taglibs-standard-1.2.5-13.amzn2022`
+ `univocity-output-tester-2.1-5.amzn2022`

The repository includes the following packages that were updated since the last release.
+ `ant-1.10.12-5.amzn2022.0.`
+ `apache-commons-beanutils-1.9.4-10.amzn2022.0.2`
+ `apache-commons-cli-1.5.0-3.amzn2022.0.2`
+ `apache-commons-codec-1.15-6.amzn2022.0.2`
+ `apache-commons-collections-3.2.2-27.amzn2022.0.2`
+ `apache-commons-compress-1.21-3.amzn2022.0.2`
+ `apache-commons-io-2.8.0-7.amzn2022.0.3`
+ `apache-commons-jxpath-1.3-43.amzn2022.0.2`
+ `apache-commons-lang3-3.12.0-5.amzn2022.0.2`
+ `apache-commons-logging-1.2-30.amzn2022.0.2`
+ `apache-commons-parent-52-6.amzn2022.0.2`
+ `apache-parent-23-8.amzn2022.0.2`
+ `apache-resource-bundles-30-5.amzn2022.0.2`
+ `apiguardian-1.1.2-3.amzn2022.0.2`
+ `atinject-1.0.5-3.amzn2022.0.2`
+ `beust-jcommander-1.78-9.amzn2022.0.2`
+ `byte-buddy-1.12.0-3.amzn2022.0.2`
+ `cdi-api-2.0.2-5.amzn2022.0.2`
+ `cglib-3.3.0-7.amzn2022.0.2`
+ `curl-7.85.0-1.amzn2022.0.1`
+ `dnf-plugin-release-notification-1.2-1.amzn2022.0.1`
+ `dracut-config-ec2-3.0-4.amzn2022.0.1`
+ `easymock-4.2-7.amzn2022.0.2`
+ `felix-parent-7-8.amzn2022.0.2`
+ `felix-utils-1.11.6-5.amzn2022.0.2`
+ `flatpak-builder-1.2.2-1.amzn2022.0.1`
+ `fusesource-pom-1.12-10.amzn2022.0.2`
+ `guava-31.0.1-3.amzn2022.0.3`
+ `httpcomponents-client-4.5.13-4.amzn2022.0.3`
+ `httpcomponents-core-4.4.13-6.amzn2022.0.2`
+ `httpcomponents-project-12-6.amzn2022.0.2`
+ `jakarta-annotations-1.3.5-13.amzn2022.0.2`
+ `jakarta-servlet-5.0.0-10.amzn2022.0.2`
+ `jansi-2.4.0-3.amzn2022.0.2`
+ `java_cup-0.11b-21.amzn2022.0.2`
+ `jdom-1.1.3-30.amzn2022.0.2`
+ `jdom2-2.0.6-27.amzn2022.0.2`
+ `jflex-1.7.0-10.amzn2022.0.2`
+ `jsoup-1.13.1-9.amzn2022.0.3`
+ `jsr-305-3.0.2-5.amzn2022.0.3`
+ `junit-4.13.1-7.amzn2022.0.2`
+ `junit5-5.7.1-5.amzn2022.0.2`
+ `libesmtp-1.0.6-25.amzn2022.0.1`
+ `libtool-2.4.7-1.amzn2022.0.2`
+ `lua-5.4.4-3.amzn2022.0.1`
+ `maven-antrun-plugin-3.0.0-5.amzn2022.0.2`
+ `maven-artifact-transfer-0.13.1-6.amzn2022.0.2`
+ `maven-assembly-plugin-3.3.0-8.amzn2022.0.2`
+ `maven-common-artifact-filters-3.2.0-3.amzn2022.0.2`
+ `maven-compiler-plugin-3.8.1-12.amzn2022.0.2`
+ `maven-dependency-analyzer-1.11.3-6.amzn2022.0.2`
+ `maven-dependency-plugin-3.1.2-9.amzn2022.0.2`
+ `maven-dependency-tree-3.0.1-10.amzn2022.0.2`
+ `maven-file-management-3.0.0-17.amzn2022.0.2`
+ `maven-filtering-3.2.0-5.amzn2022.0.2`
+ `maven-jar-plugin-3.2.0-9.amzn2022.0.2`
+ `maven-parent-34-10.amzn2022.0.2`
+ `maven-plugin-build-helper-3.2.0-7.amzn2022.0.2`
+ `maven-plugin-testing-3.3.0-25.amzn2022.0.2`
+ `maven-plugin-tools-3.6.0-12.amzn2022.0.3`
+ `maven-resources-plugin-3.2.0-6.amzn2022.0.2`
+ `maven-shared-incremental-1.1-25.amzn2022.0.2`
+ `maven-shared-io-3.0.0-17.amzn2022.0.2`
+ `maven-source-plugin-3.2.1-8.amzn2022.0.2`
+ `maven-wagon-3.4.2-6.amzn2022.0.3`
+ `mockito-3.12.4-3.amzn2022.0.2`
+ `modello-1.11-8.amzn2022.0.2`
+ `mojo-parent-60-5.amzn2022.0.2`
+ `munge-maven-plugin-1.0-24.amzn2022.0.2`
+ `openssl-3.0.5-1.amzn2022.0.2`
+ `opentest4j-1.2.0-10.amzn2022.0.2`
+ `osgi-compendium-7.0.0-12.amzn2022.0.2`
+ `p11-kit-0.24.1-2.amzn2022.0.1`
+ `plexus-archiver-4.2.4-5.amzn2022.0.2`
+ `plexus-build-api-0.0.7-36.amzn2022.0.2`
+ `plexus-classworlds-2.6.0-10.amzn2022.0.3`
+ `plexus-compiler-2.8.8-5.amzn2022.0.2`
+ `plexus-components-pom-6.5-6.amzn2022.0.2`
+ `plexus-containers-2.1.0-9.amzn2022.0.3`
+ `plexus-interpolation-1.26-10.amzn2022.0.3`
+ `plexus-io-3.2.0-9.amzn2022.0.2`
+ `plexus-languages-1.0.6-6.amzn2022.0.2`
+ `plexus-pom-7-5.amzn2022.0.2`
+ `plexus-resources-1.1.0-9.amzn2022.0.2`
+ `plexus-utils-3.3.0-9.amzn2022.0.3`
+ `postfix-3.7.2-4.amzn2022.0.2`
+ `qdox-2.0.0-9.amzn2022.0.2`
+ `rsync-3.2.6-1.amzn2022.0.2`
+ `sisu-mojos-0.3.4-11.amzn2022.0.2`
+ `slf4j-1.7.32-3.amzn2022.0.3`
+ `subversion-1.14.2-5.amzn2022.0.1`
+ `system-release-2022.0.20221012-0.amzn2022`
+ `tzdata-2022d-1.amzn2022.0.1`
+ `xbean-4.18-7.amzn2022.0.2`
+ `xz-java-1.9-3.amzn2022.0.2`

## AMIs
<a name="amis-2022020221012"></a>

**Docker Container image**
+ `curl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `curl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.aarch64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.x86_64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.aarch64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.x86_64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.x86_64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.x86_64`
+ `system-release-2022.0.20221012-0.amzn2022.noarch`
+ `tzdata-2022d-1.amzn2022.0.1.noarch`

**Default AMI**
+ `curl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `curl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `dnf-plugin-release-notification-1.2-1.amzn2022.0.1.noarch`
+ `dracut-config-ec2-3.0-4.amzn2022.0.1.noarch`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.aarch64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.x86_64`
+ `openssl-3.0.5-1.amzn2022.0.2.aarch64`
+ `openssl-3.0.5-1.amzn2022.0.2.x86_64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.aarch64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.x86_64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.x86_64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.x86_64`
+ `rsync-3.2.6-1.amzn2022.0.2.aarch64`
+ `rsync-3.2.6-1.amzn2022.0.2.x86_64`
+ `system-release-2022.0.20221012-0.amzn2022.noarch`
+ `tzdata-2022d-1.amzn2022.0.1.noarch`
+ `xxhash-libs-0.8.0-3.amzn2022.0.1.aarch64`
+ `xxhash-libs-0.8.0-3.amzn2022.0.1.x86_64`

**Minimal AMI**
+ `curl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `curl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `dnf-plugin-release-notification-1.2-1.amzn2022.0.1.noarch`
+ `dracut-config-ec2-3.0-4.amzn2022.0.1.noarch`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.aarch64`
+ `libcurl-minimal-7.85.0-1.amzn2022.0.1.x86_64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.aarch64`
+ `lua-libs-5.4.4-3.amzn2022.0.1.x86_64`
+ `openssl-3.0.5-1.amzn2022.0.2.aarch64`
+ `openssl-3.0.5-1.amzn2022.0.2.x86_64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.aarch64`
+ `openssl-libs-3.0.5-1.amzn2022.0.2.x86_64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-0.24.1-2.amzn2022.0.1.x86_64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.aarch64`
+ `p11-kit-trust-0.24.1-2.amzn2022.0.1.x86_64`
+ `system-release-2022.0.20221012-0.amzn2022.noarch`
+ `tzdata-2022d-1.amzn2022.0.1.noarch`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
