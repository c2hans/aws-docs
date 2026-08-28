---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2022.0.20220810.html
---

# Amazon Linux 2023 version 2022.0.20220810 release notes
<a name="relnotes-2022.0.20220810"></a>

**Note**
These release notes are for a version of the Tech Preview of Amazon Linux 2023. This is an old Tech Preview and should no longer be used.
The Generally Available Amazon Linux 2023 is the successor to the Amazon Linux 2022 Tech Preview releases. For information about AL2023 and keeping up to date with Amazon Linux releases, see the [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/).

## Major updates
<a name="major-updates-20220810"></a>

Amazon Linux 2022 includes the following major updates.
+ In this release, we have removed the remaining `openjdk` packages, as we have shifted Amazon Linux 2022 to use Amazon Corretto as the JVM in the distribution.

Upcoming Changes in future releases.
+ The legacy `pcre` package is deprecated and will be removed in a future Amazon Linux release. The `pcre2` package is the successor, and the few remaining packages in Amazon Linux 2022 that depend on the deprecated `pcre` library will be migrated to `pcre2` in future updates.
+ The kernel package will see changes to improve aspects of security and performance, and, while core functionality will be maintained, some unused or deprecated features may be removed in future Release Candidates.

**Java Ecosystem**
+ The `maven`, `xmvn`, and `javapackages-tools` should function as expected, but the versions present in this release have not yet been rebuilt after a bootstrap phase. These packages will be re-built without the use of `javapackages-bootstrap` before General Availability.

**Known Issues**
+ All known issues are resolved.

**Security Updates**
+ For information on the CVEs addressed in this release, refer to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2022.html).

## Major changes from the first Tech Preview release to this release
<a name="major-changes-20220810"></a>
+ Kernel updated from 5.10 to 5.15
+ OpenSSL updated from 1.1 to 3.0
+ AWS CLI updated to AWS CLI v2
+ AWS Tools found in Amazon Linux 2 have been added to the repositories like `ecs-agent`, `aws-cfn-bootstrap`, `aws-kinesis-agent`, `ec2-instance-connect`, and other tools.
+ Curation of packages - As part of the development cycle, we have curated the list of packages available in the repositories. This involved removing a number of packages that were no longer needed due to dependencies. Some package may be re-added to the repository as we work through customer requests.
+ Language run-times were updated and some runtimes like Ruby were name-spaced allowing newer versions to be added in the future without removing the current ones from the repositories.

This update Amazon Linux 2022 repository and AMI includes the following new packages.

**Repository**

| New Packages |
| --- |
| `dkms-3.0.3-2.amzn2022` |
| `oci-add-hooks-0-0.1.20200504git268e3bb.amzn2022` |
| `postgresql14-14.3-2.amzn2022.0.1` |
| `postgresql14-contrib-14.3-2.amzn2022.0.1` |
| `postgresql14-docs-14.3-2.amzn2022.0.1` |
| `postgresql14-llvmjit-14.3-2.amzn2022.0.1` |
| `postgresql14-plperl-14.3-2.amzn2022.0.1` |
| `postgresql14-plpython3-14.3-2.amzn2022.0.1` |
| `postgresql14-pltcl-14.3-2.amzn2022.0.1` |
| `postgresql14-private-devel-14.3-2.amzn2022.0.1` |
| `postgresql14-private-libs-14.3-2.amzn2022.0.1` |
| `postgresql14-server-14.3-2.amzn2022.0.1` |
| `postgresql14-server-devel-14.3-2.amzn2022.0.1` |
| `postgresql14-static-14.3-2.amzn2022.0.1` |
| `postgresql14-test-14.3-2.amzn2022.0.1` |
| `postgresql14-test-rpm-macros-14.3-2.amzn2022.0.1` |
| `postgresql14-upgrade-14.3-2.amzn2022.0.1` |
| `postgresql14-upgrade-devel-14.3-2.amzn2022.0.1` |
| `python3-bcrypt-3.1.7-7.amzn2022` |
| `python3-coverage+toml-5.5-1.amzn2022.0.1` |
| `python3-h2-4.0.0-2.amzn2022.0.1` |
| `python3-hamcrest-1.9.0-16.amzn2022` |
| `python3-hpack-4.0.0-2.amzn2022` |
| `python3-hyperframe-6.0.1-1.amzn2022` |
| `python3-priority-1.3.0-12.amzn2022` |
| `python3-psutil-tests-5.8.0-16.amzn2022` |

The repository includes the following packages that were removed since the last release.

| Removed Packages |
| --- |
| `java-latest-openjdk-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-demo-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-demo-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-demo-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-devel-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-devel-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-devel-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-headless-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-headless-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-headless-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-javadoc-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-javadoc-zip-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-jmods-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-jmods-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-jmods-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-src-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-src-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-src-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-static-libs-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-static-libs-fastdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `java-latest-openjdk-static-libs-slowdebug-17.0.2.0.8-2.rolling.amzn2022` |
| `python3-jsonschema+format-3.2.0-9.amzn2022` |
| `rubygem-ronn-ng-0.9.1-2.amzn2022` |
| `rubygem-ronn-ng-doc-0.9.1-2.amzn2022` |

The repository includes the following packages that were updated since the last release.

| Updated Packages |
| --- |
| `compat-libpthread-nonshared-2.34-40.amzn2022.0.1` |
| `aqute-bnd-javadoc-5.2.0-9.amzn2022` |
| `aqute-bndlib-5.2.0-9.amzn2022` |
| `binutils-2.38-20.amzn2022.0.1` |
| `binutils-devel-2.38-20.amzn2022.0.1` |
| `bnd-maven-plugin-5.2.0-9.amzn2022` |
| `bpftool-5.15.57-28.127.amzn2022` |
| `compat-libpthread-nonshared-2.34-40.amzn2022.0.1` |
| `git-2.37.1-1.amzn2022.0.2` |
| `git-all-2.37.1-1.amzn2022.0.2` |
| `git-core-2.37.1-1.amzn2022.0.2` |
| `git-core-doc-2.37.1-1.amzn2022.0.2` |
| `git-credential-libsecret-2.37.1-1.amzn2022.0.2` |
| `git-cvs-2.37.1-1.amzn2022.0.2` |
| `git-daemon-2.37.1-1.amzn2022.0.2` |
| `git-email-2.37.1-1.amzn2022.0.2` |
| `git-gui-2.37.1-1.amzn2022.0.2` |
| `git-instaweb-2.37.1-1.amzn2022.0.2` |
| `gitk-2.37.1-1.amzn2022.0.2` |
| `git-p4-2.37.1-1.amzn2022.0.2` |
| `git-subtree-2.37.1-1.amzn2022.0.2` |
| `git-svn-2.37.1-1.amzn2022.0.2` |
| `gitweb-2.37.1-1.amzn2022.0.2` |
| `glibc-2.34-40.amzn2022.0.1` |
| `glibc-all-langpacks-2.34-40.amzn2022.0.1` |
| `glibc-benchtests-2.34-40.amzn2022.0.1` |
| `glibc-common-2.34-40.amzn2022.0.1` |
| `glibc-devel-2.34-40.amzn2022.0.1` |
| `glibc-doc-2.34-40.amzn2022.0.1` |
| `glibc-gconv-extra-2.34-40.amzn2022.0.1` |
| `glibc-headers-x86-2.34-40.amzn2022.0.1` |
| `glibc-langpack-aa-2.34-40.amzn2022.0.1` |
| `glibc-langpack-af-2.34-40.amzn2022.0.1` |
| `glibc-langpack-agr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ak-2.34-40.amzn2022.0.1` |
| `glibc-langpack-am-2.34-40.amzn2022.0.1` |
| `glibc-langpack-an-2.34-40.amzn2022.0.1` |
| `glibc-langpack-anp-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ar-2.34-40.amzn2022.0.1` |
| `glibc-langpack-as-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ast-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ayc-2.34-40.amzn2022.0.1` |
| `glibc-langpack-az-2.34-40.amzn2022.0.1` |
| `glibc-langpack-be-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bem-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ber-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bg-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bhb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bho-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-br-2.34-40.amzn2022.0.1` |
| `glibc-langpack-brx-2.34-40.amzn2022.0.1` |
| `glibc-langpack-bs-2.34-40.amzn2022.0.1` |
| `glibc-langpack-byn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ca-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ce-2.34-40.amzn2022.0.1` |
| `glibc-langpack-chr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ckb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-cmn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-crh-2.34-40.amzn2022.0.1` |
| `glibc-langpack-cs-2.34-40.amzn2022.0.1` |
| `glibc-langpack-csb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-cv-2.34-40.amzn2022.0.1` |
| `glibc-langpack-cy-2.34-40.amzn2022.0.1` |
| `glibc-langpack-da-2.34-40.amzn2022.0.1` |
| `glibc-langpack-de-2.34-40.amzn2022.0.1` |
| `glibc-langpack-doi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-dsb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-dv-2.34-40.amzn2022.0.1` |
| `glibc-langpack-dz-2.34-40.amzn2022.0.1` |
| `glibc-langpack-el-2.34-40.amzn2022.0.1` |
| `glibc-langpack-en-2.34-40.amzn2022.0.1` |
| `glibc-langpack-eo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-es-2.34-40.amzn2022.0.1` |
| `glibc-langpack-et-2.34-40.amzn2022.0.1` |
| `glibc-langpack-eu-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fa-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ff-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fil-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fur-2.34-40.amzn2022.0.1` |
| `glibc-langpack-fy-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ga-2.34-40.amzn2022.0.1` |
| `glibc-langpack-gd-2.34-40.amzn2022.0.1` |
| `glibc-langpack-gez-2.34-40.amzn2022.0.1` |
| `glibc-langpack-gl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-gu-2.34-40.amzn2022.0.1` |
| `glibc-langpack-gv-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ha-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hak-2.34-40.amzn2022.0.1` |
| `glibc-langpack-he-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hif-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hne-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hsb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ht-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hu-2.34-40.amzn2022.0.1` |
| `glibc-langpack-hy-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ia-2.34-40.amzn2022.0.1` |
| `glibc-langpack-id-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ig-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ik-2.34-40.amzn2022.0.1` |
| `glibc-langpack-is-2.34-40.amzn2022.0.1` |
| `glibc-langpack-it-2.34-40.amzn2022.0.1` |
| `glibc-langpack-iu-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ja-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ka-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kab-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kk-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-km-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ko-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kok-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ks-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ku-2.34-40.amzn2022.0.1` |
| `glibc-langpack-kw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ky-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lg-2.34-40.amzn2022.0.1` |
| `glibc-langpack-li-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lij-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ln-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lt-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lv-2.34-40.amzn2022.0.1` |
| `glibc-langpack-lzh-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mag-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mai-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mfe-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mg-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mhr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-miq-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mjw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mk-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ml-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mni-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mnw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ms-2.34-40.amzn2022.0.1` |
| `glibc-langpack-mt-2.34-40.amzn2022.0.1` |
| `glibc-langpack-my-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nan-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nb-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nds-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ne-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nhn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-niu-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-nso-2.34-40.amzn2022.0.1` |
| `glibc-langpack-oc-2.34-40.amzn2022.0.1` |
| `glibc-langpack-om-2.34-40.amzn2022.0.1` |
| `glibc-langpack-or-2.34-40.amzn2022.0.1` |
| `glibc-langpack-os-2.34-40.amzn2022.0.1` |
| `glibc-langpack-pa-2.34-40.amzn2022.0.1` |
| `glibc-langpack-pap-2.34-40.amzn2022.0.1` |
| `glibc-langpack-pl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ps-2.34-40.amzn2022.0.1` |
| `glibc-langpack-pt-2.34-40.amzn2022.0.1` |
| `glibc-langpack-quz-2.34-40.amzn2022.0.1` |
| `glibc-langpack-raj-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ro-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ru-2.34-40.amzn2022.0.1` |
| `glibc-langpack-rw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sa-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sah-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sat-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sc-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sd-2.34-40.amzn2022.0.1` |
| `glibc-langpack-se-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sgs-2.34-40.amzn2022.0.1` |
| `glibc-langpack-shn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-shs-2.34-40.amzn2022.0.1` |
| `glibc-langpack-si-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sid-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sk-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sm-2.34-40.amzn2022.0.1` |
| `glibc-langpack-so-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sq-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ss-2.34-40.amzn2022.0.1` |
| `glibc-langpack-st-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sv-2.34-40.amzn2022.0.1` |
| `glibc-langpack-sw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-szl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ta-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tcy-2.34-40.amzn2022.0.1` |
| `glibc-langpack-te-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tg-2.34-40.amzn2022.0.1` |
| `glibc-langpack-th-2.34-40.amzn2022.0.1` |
| `glibc-langpack-the-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ti-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tig-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tk-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tl-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tn-2.34-40.amzn2022.0.1` |
| `glibc-langpack-to-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tpi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tr-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ts-2.34-40.amzn2022.0.1` |
| `glibc-langpack-tt-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ug-2.34-40.amzn2022.0.1` |
| `glibc-langpack-uk-2.34-40.amzn2022.0.1` |
| `glibc-langpack-unm-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ur-2.34-40.amzn2022.0.1` |
| `glibc-langpack-uz-2.34-40.amzn2022.0.1` |
| `glibc-langpack-ve-2.34-40.amzn2022.0.1` |
| `glibc-langpack-vi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-wa-2.34-40.amzn2022.0.1` |
| `glibc-langpack-wae-2.34-40.amzn2022.0.1` |
| `glibc-langpack-wal-2.34-40.amzn2022.0.1` |
| `glibc-langpack-wo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-xh-2.34-40.amzn2022.0.1` |
| `glibc-langpack-yi-2.34-40.amzn2022.0.1` |
| `glibc-langpack-yo-2.34-40.amzn2022.0.1` |
| `glibc-langpack-yue-2.34-40.amzn2022.0.1` |
| `glibc-langpack-yuw-2.34-40.amzn2022.0.1` |
| `glibc-langpack-zh-2.34-40.amzn2022.0.1` |
| `glibc-langpack-zu-2.34-40.amzn2022.0.1` |
| `glibc-locale-source-2.34-40.amzn2022.0.1` |
| `glibc-minimal-langpack-2.34-40.amzn2022.0.1` |
| `glibc-nss-devel-2.34-40.amzn2022.0.1` |
| `glibc-static-2.34-40.amzn2022.0.1` |
| `glibc-utils-2.34-40.amzn2022.0.1` |
| `google-guice-4.2.3-8.amzn2022.0.1` |
| `google-guice-javadoc-4.2.3-8.amzn2022.0.1` |
| `guice-assistedinject-4.2.3-8.amzn2022.0.1` |
| `guice-bom-4.2.3-8.amzn2022.0.1` |
| `guice-extensions-4.2.3-8.amzn2022.0.1` |
| `guice-grapher-4.2.3-8.amzn2022.0.1` |
| `guice-jmx-4.2.3-8.amzn2022.0.1` |
| `guice-jndi-4.2.3-8.amzn2022.0.1` |
| `guice-multibindings-4.2.3-8.amzn2022.0.1` |
| `guice-parent-4.2.3-8.amzn2022.0.1` |
| `guice-servlet-4.2.3-8.amzn2022.0.1` |
| `guice-throwingproviders-4.2.3-8.amzn2022.0.1` |
| `ipcalc-1.0.1-1.amzn2022.0.2` |
| `kernel-5.15.57-28.127.amzn2022` |
| `kernel-devel-5.15.57-28.127.amzn2022` |
| `kernel-headers-5.15.57-28.127.amzn2022` |
| `kernel-tools-5.15.57-28.127.amzn2022` |
| `kernel-tools-devel-5.15.57-28.127.amzn2022` |
| `libblkid-2.37.4-1.amzn2022.0.1` |
| `libblkid-devel-2.37.4-1.amzn2022.0.1` |
| `libfdisk-2.37.4-1.amzn2022.0.1` |
| `libfdisk-devel-2.37.4-1.amzn2022.0.1` |
| `libmount-2.37.4-1.amzn2022.0.1` |
| `libmount-devel-2.37.4-1.amzn2022.0.1` |
| `libnsl-2.34-40.amzn2022.0.1` |
| `libsmartcols-2.37.4-1.amzn2022.0.1` |
| `libsmartcols-devel-2.37.4-1.amzn2022.0.1` |
| `libuuid-2.37.4-1.amzn2022.0.1` |
| `libuuid-devel-2.37.4-1.amzn2022.0.1` |
| `nscd-2.34-40.amzn2022.0.1` |
| `nss_db-2.34-40.amzn2022.0.1` |
| `nss_hesiod-2.34-40.amzn2022.0.1` |
| `objectweb-asm-9.2-3.amzn2022` |
| `objectweb-asm-javadoc-9.2-3.amzn2022` |
| `perf-5.15.57-28.127.amzn2022` |
| `perl-Git-2.37.1-1.amzn2022.0.2` |
| `perl-Git-SVN-2.37.1-1.amzn2022.0.2` |
| `python3-coverage-5.5-1.amzn2022.0.1` |
| `python3-jsonschema-3.2.0-9.amzn2022.0.1` |
| `python3-libmount-2.37.4-1.amzn2022.0.1` |
| `python3-perf-5.15.57-28.127.amzn2022` |
| `python3-psutil-5.8.0-16.amzn2022` |
| `python3-rpm-generators-12-15.amzn2022.0.2` |
| `systemd-250.7-1.amzn2022.0.4` |
| `systemd-container-250.7-1.amzn2022.0.4` |
| `systemd-devel-250.7-1.amzn2022.0.4` |
| `systemd-journal-remote-250.7-1.amzn2022.0.4` |
| `systemd-libs-250.7-1.amzn2022.0.4` |
| `systemd-networkd-250.7-1.amzn2022.0.4` |
| `systemd-oomd-defaults-250.7-1.amzn2022.0.4` |
| `systemd-pam-250.7-1.amzn2022.0.4` |
| `systemd-resolved-250.7-1.amzn2022.0.4` |
| `systemd-rpm-macros-250.7-1.amzn2022.0.4` |
| `systemd-standalone-sysusers-250.7-1.amzn2022.0.4` |
| `systemd-standalone-tmpfiles-250.7-1.amzn2022.0.4` |
| `systemd-tests-250.7-1.amzn2022.0.4` |
| `systemd-udev-250.7-1.amzn2022.0.4` |
| `system-release-2022.0.20220810-0.amzn2022` |
| `util-linux-2.37.4-1.amzn2022.0.1` |
| `util-linux-core-2.37.4-1.amzn2022.0.1` |
| `util-linux-user-2.37.4-1.amzn2022.0.1` |
| `uuidd-2.37.4-1.amzn2022.0.1` |

## AMIs
<a name="amis-2022020220810"></a>

Docker Container image
+ `glibc-2.34-40.amzn2022.0.1`
+ `glibc-common-2.34-40.amzn2022.0.1`
+ `glibc-minimal-langpack-2.34-40.amzn2022.0.1`
+ `libblkid-2.37.4-1.amzn2022.0.1`
+ `libmount-2.37.4-1.amzn2022.0.1`
+ `libsmartcols-2.37.4-1.amzn2022.0.1`
+ `libuuid-2.37.4-1.amzn2022.0.1`
+ `system-release-2022.0.20220810-0.amzn2022`

Default AMI

|  |
| --- |
| `binutils-2.38-20.amzn2022.0.1` |
| `glibc-2.34-40.amzn2022.0.1` |
| `glibc-all-langpacks-2.34-40.amzn2022.0.1` |
| `glibc-common-2.34-40.amzn2022.0.1` |
| `glibc-locale-source-2.34-40.amzn2022.0.1` |
| `kernel-5.15.57-28.127.amzn2022` |
| `kernel-tools-5.15.57-28.127.amzn2022` |
| `libblkid-2.37.4-1.amzn2022.0.1` |
| `libfdisk-2.37.4-1.amzn2022.0.1` |
| `libmount-2.37.4-1.amzn2022.0.1` |
| `libsmartcols-2.37.4-1.amzn2022.0.1` |
| `libuuid-2.37.4-1.amzn2022.0.1` |
| `python3-jsonschema-3.2.0-9.amzn2022.0.1` |
| `systemd-250.7-1.amzn2022.0.4` |
| `systemd-libs-250.7-1.amzn2022.0.4` |
| `systemd-networkd-250.7-1.amzn2022.0.4` |
| `systemd-pam-250.7-1.amzn2022.0.4` |
| `systemd-resolved-250.7-1.amzn2022.0.4` |
| `systemd-udev-250.7-1.amzn2022.0.4` |
| `system-release-2022.0.20220810-0.amzn2022` |
| `util-linux-2.37.4-1.amzn2022.0.1` |
| `util-linux-core-2.37.4-1.amzn2022.0.1` |

Minimal AMI

|  |
| --- |
| `glibc-2.34-40.amzn2022.0.1` |
| `glibc-all-langpacks-2.34-40.amzn2022.0.1` |
| `glibc-common-2.34-40.amzn2022.0.1` |
| `glibc-locale-source-2.34-40.amzn2022.0.1` |
| `kernel-5.15.57-28.127.amzn2022` |
| `libblkid-2.37.4-1.amzn2022.0.1` |
| `libfdisk-2.37.4-1.amzn2022.0.1` |
| `libmount-2.37.4-1.amzn2022.0.1` |
| `libsmartcols-2.37.4-1.amzn2022.0.1` |
| `libuuid-2.37.4-1.amzn2022.0.1` |
| `python3-jsonschema-3.2.0-9.amzn2022.0.1` |
| `systemd-250.7-1.amzn2022.0.4` |
| `systemd-libs-250.7-1.amzn2022.0.4` |
| `systemd-networkd-250.7-1.amzn2022.0.4` |
| `systemd-pam-250.7-1.amzn2022.0.4` |
| `systemd-resolved-250.7-1.amzn2022.0.4` |
| `systemd-udev-250.7-1.amzn2022.0.4` |
| `system-release-2022.0.20220810-0.amzn2022` |
| `util-linux-2.37.4-1.amzn2022.0.1` |
| `util-linux-core-2.37.4-1.amzn2022.0.1` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
