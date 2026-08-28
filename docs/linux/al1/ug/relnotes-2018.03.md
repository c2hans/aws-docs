---
source_url: https://docs.aws.amazon.com/linux/al1/ug/relnotes-2018.03.html
---

# Amazon Linux 1 (AL1) version 2018.03 release notes
<a name="relnotes-2018.03"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and Amazon Linux 2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

This topic includes Amazon Linux 1 (AL1) release notes updates for the 2018.03 release.

## Upgrading to Amazon Linux 1 (AL1) version 2018.03
<a name="upgrading-2018.03"></a>

To upgrade to Amazon Linux 1 (AL1) version 2018.03 from Amazon Linux 1 (AL1) version 2011.09 or later, run `sudo yum clean all` followed by `sudo yum update`. When the upgrade is complete, reboot your instance.

The Amazon Linux 1 (AL1) repositories provided updates that allow you to roll from one version of Amazon Linux 1 (AL1) to the next.

## Amazon Linux 2018.03.0.20230404.0
<a name="release-2018.03.0.20230404.0"></a>

Updated Packages:
+ `db4-4.7.25-22.13.amzn1.x86_64`
+ `db4-utils-4.7.25-22.13.amzn1.x86_64`
+ `kernel-4.14.311-161.529.amzn1.x86_64`
+ `kernel-devel-4.14.311-161.529.amzn1.x86_64`
+ `kernel-headers-4.14.311-161.529.amzn1.x86_64`
+ `kernel-tools-4.14.311-161.529.amzn1.x86_64`
+ `microcode_ctl-2.1-47.41.amzn1.x86_64`
+ `python27-2.7.18-2.145.amzn1.x86_64`
+ `python27-babel-0.9.4-5.1.9.amzn1.noarch`
+ `python27-devel-2.7.18-2.145.amzn1.x86_64`
+ `python27-libs-2.7.18-2.145.amzn1.x86_64`
+ `vim-common-9.0.1403-1.76.amzn1.x86_64`
+ `vim-data-9.0.1403-1.76.amzn1.noarch`
+ `vim-enhanced-9.0.1403-1.76.amzn1.x86_64`
+ `vim-filesystem-9.0.1403-1.76.amzn1.noarch`
+ `vim-minimal-9.0.1403-1.76.amzn1.x86_64`

## Amazon Linux 2018.03.0.20230322.0
<a name="release-2018.03.0.20230322.0"></a>

Updated Packages:
+ `kernel-4.14.309-159.529.amzn1.x86_64`
+ `kernel-devel-4.14.309-159.529.amzn1.x86_64`
+ `kernel-headers-4.14.309-159.529.amzn1.x86_64`
+ `kernel-tools-4.14.309-159.529.amzn1.x86_64`
+ `tar-1.26-31.23.amzn1.x86_64`
+ `vim-common-9.0.1367-1.73.amzn1.x86_64`
+ `vim-data-9.0.1367-1.73.amzn1.noarch`
+ `vim-enhanced-9.0.1367-1.73.amzn1.x86_64`
+ `vim-filesystem-9.0.1367-1.73.amzn1.noarch`
+ `vim-minimal-9.0.1367-1.73.amzn1.x86_64`
+ `xorg-x11-server-Xorg-1.17.4-18.51.amzn1.x86_64`
+ `xorg-x11-server-common-1.17.4-18.51.amzn1.x86_64`

Packages with CVEs:

`kernel-4.14.309-159.529.amzn1`, `kernel-devel-4.14.309-159.529.amzn1`, `kernel-headers-4.14.309-159.529.amzn1`, `kernel-tools-4.14.309-159.529.amzn1`
+ CVE-2023-26545

`tar-1.26-31.23.amzn1`
+ CVE-2022-48303

`vim-common-9.0.1367-1.73.amzn1`, `vim-data-9.0.1367-1.73.amzn1`, `vim-enhanced-9.0.1367-1.73.amzn1`, `vim-filesystem-9.0.1367-1.73.amzn1`
+ CVE-2023-0288
+ CVE-2023-0433
+ CVE-2023-0512
+ CVE-2023-1127

`xorg-x11-server-Xorg-1.17.4-18.51.amzn1`, `xorg-x11-server-common-1.17.4-18.51.amzn1`
+ CVE-2023-0494

## Amazon Linux 2018.03.0.20230306.1
<a name="release-2018.03.0.20230306.1"></a>

Updated Packages
+ `tzdata-2022g-1.84.amzn1.noarch`
+ `tzdata-java-2022g-1.84.amzn1.noarch`

## Amazon Linux 2018.03.0.20230221.0
<a name="release-2018.03.0.20230221.0"></a>

Updated Packages
+ `ca-certificates-2018.2.22-65.1.29.amzn1.noarch`
+ `kernel-4.14.305-155.531.amzn1.x86_64`
+ `kernel-devel-4.14.305-155.531.amzn1.x86_64`
+ `kernel-headers-4.14.305-155.531.amzn1.x86_64`
+ `kernel-tools-4.14.305-155.531.amzn1.x86_64`
+ `xorg-x11-server-Xorg-1.17.4-18.50.amzn1.x86_64`
+ `xorg-x11-server-common-1.17.4-18.50.amzn1.x86_64`

Packages with CVEs:

`ca-certificates-2018.2.22-65.1.29.amzn1`
+ CVE-2022-23491

`xorg-x11-server-1.17.4-18.50.amzn1`
+ CVE-2022-2320
+ CVE-2022-4283
+ CVE-2022-46340
+ CVE-2022-46341
+ CVE-2022-46342
+ CVE-2022-46343
+ CVE-2022-46344

## Amazon Linux 2018.03.0.20230207.0
<a name="release-2018.03.0.20230207.0"></a>

Updated Packages:
+ kernel-4.14.301-153.528.amzn1.x86\_64
+ kernel-devel-4.14.301-153.528.amzn1.x86\_64
+ kernel-headers-4.14.301-153.528.amzn1.x86\_64
+ kernel-tools-4.14.301-153.528.amzn1.x86\_64
+ krb5-libs-1.15.1-55.51.amzn1.x86\_64
+ openssl-1.0.2k-16.162.amzn1.x86\_64
+ sudo-1.8.23-10.57.amzn1.x86\_64
+ vim-common-9.0.1160-1.1.amzn1.x86\_64
+ vim-data-9.0.1160-1.1.amzn1.noarch
+ vim-enhanced-9.0.1160-1.1.amzn1.x86\_64
+ vim-filesystem-9.0.1160-1.1.amzn1.noarch
+ vim-minimal-9.0.1160-1.1.amzn1.x86\_64

Packages with CVEs:

`sudo-1.8.23-10.57.amzn1`
+ CVE-2023-22809

`vim-9.0.1160-1.1.amzn1`
+ CVE-2022-4292
+ CVE-2023-0049

`krb5-1.15.1-55.51.amzn1`
+ CVE-2022-42898

## Amazon Linux 2018.03.0.20230124.1
<a name="release-2018.03.0.20230124.1"></a>

There are no major updates in this release.

Updated Packages:
+ `ca-certificates-2018.2.22-65.1.28.amzn1.noarch`
+ `krb5-libs-1.15.1-46.49.amzn1.x86_64`
+ `vim-common-9.0.1006-1.1.amzn1.x86_64`
+ `vim-data-9.0.1006-1.1.amzn1.noarch`
+ `vim-enhanced-9.0.1006-1.1.amzn1.x86_64`
+ `vim-filesystem-9.0.1006-1.1.amzn1.noarch`
+ `vim-minimal-9.0.1006-1.1.amzn1.x86_64`

## Amazon Linux 2018.03.0.20221209.1
<a name="release-2018.03.0.20221209.1"></a>

There are no major updates in this release.

Updated Packages:
+ `curl-7.61.1-12.101.amzn1.x86_64`
+ `expat-2.1.0-15.33.amzn1.x86_64`
+ `kernel-4.14.299-152.520.amzn1.x86_64`
+ `kernel-devel-4.14.299-152.520.amzn1.x86_64`
+ `kernel-headers-4.14.299-152.520.amzn1.x86_64`
+ `kernel-tools-4.14.299-152.520.amzn1.x86_64`
+ `libcurl-7.61.1-12.101.amzn1.x86_64`
+ `nvidia-450.216.04-2018.03.118.amzn1.x86_64`
+ `nvidia-dkms-450.216.04-2018.03.118.amzn1.x86_64`
+ `rsync-3.0.6-12.14.amzn1.x86_64`
+ `tzdata-2022f-1.83.amzn1.noarch`
+ `tzdata-java-2022f-1.83.amzn1.noarch`
+ `zlib-1.2.8-7.20.amzn1.x86_64`
+ `zlib-devel-1.2.8-7.20.amzn1.x86_64`

Packages with CVEs:

`curl-7.61.1-12.101.amzn1`
+ CVE-2022-22576
+ CVE-2022-27774
+ CVE-2022-27776
+ CVE-2022-27781
+ CVE-2022-27782
+ CVE-2022-32206
+ CVE-2022-32208
+ CVE-2022-35252

`kernel-4.14.299-152.520.amzn1`
+ CVE-2022-20369
+ CVE-2022-26373
+ CVE-2022-2978
+ CVE-2022-3542
+ CVE-2022-3564
+ CVE-2022-3565
+ CVE-2022-3594
+ CVE-2022-3621
+ CVE-2022-3646
+ CVE-2022-3649
+ CVE-2022-39842
+ CVE-2022-40768
+ CVE-2022-41849
+ CVE-2022-41850
+ CVE-2022-43750

`nvidia-450.216.04-2018.03.118.amzn1`
+ CVE-2022-34670
+ CVE-2022-34674
+ CVE-2022-34675
+ CVE-2022-34677
+ CVE-2022-34679
+ CVE-2022-34680
+ CVE-2022-34682
+ CVE-2022-42254
+ CVE-2022-42255
+ CVE-2022-42256
+ CVE-2022-42257
+ CVE-2022-42258
+ CVE-2022-42259
+ CVE-2022-42260
+ CVE-2022-42261
+ CVE-2022-42262
+ CVE-2022-42263
+ CVE-2022-42264

## Amazon Linux 2018.03.0.20221018.0
<a name="release-2018.03.0.20221018.0"></a>

There are no major updates in this release.

Updated Packages:
+ `kernel-4.14.294-150.533.amzn1.x86_64`
+ `kernel-devel-4.14.294-150.533.amzn1.x86_64`
+ `kernel-headers-4.14.294-150.533.amzn1.x86_64`
+ `kernel-tools-4.14.294-150.533.amzn1.x86_64`
+ `ruby20-2.0.0.648-2.41.amzn1.x86_64`
+ `ruby20-irb-2.0.0.648-2.41.amzn1.noarch`
+ `ruby20-libs-2.0.0.648-2.41.amzn1.x86_64`
+ `rubygem20-bigdecimal-1.2.0-2.41.amzn1.x86_64`
+ `rubygem20-psych-2.0.0-2.41.amzn1.x86_64`
+ `rubygems20-2.0.14.1-2.41.amzn1.noarch`
+ `tzdata-2022e-1.81.amzn1.noarch`
+ `tzdata-java-2022e-1.81.amzn1.noarch`
+ `vim-common-9.0.475-1.1.amzn1.x86_64`
+ `vim-data-9.0.475-1.1.amzn1.noarch`
+ `vim-enhanced-9.0.475-1.1.amzn1.x86_64`
+ `vim-filesystem-9.0.475-1.1.amzn1.noarch`
+ `vim-minimal-9.0.475-1.1.amzn1.x86_64`

Packages with CVEs:

`kernel-4.14.294-150.533.amzn1`
+ CVE-2021-4159
+ CVE-2021-33655
+ CVE-2022-1462
+ CVE-2022-1679
+ CVE-2022-2153
+ CVE-2022-2588
+ CVE-2022-2663
+ CVE-2022-3028
+ CVE-2022-36123
+ CVE-2022-36879
+ CVE-2022-36946
+ CVE-2022-40307

## Amazon Linux 2018.03.0.20220907.3
<a name="release-2018.03.0.20220907.3"></a>

There are no major updates in this release.

Updated Packages:
+ `amazon-ssm-agent-3.1.1732.0-1.amzn1.x86_64`
+ `gnupg2-2.0.28-2.35.amzn1.x86_64`
+ `java-1.7.0-openjdk-1.7.0.321-2.6.28.1.86.amzn1.x86_64`
+ `tzdata-2022c-1.80.amzn1.noarch`
+ `tzdata-java-2022c-1.80.amzn1.noarch`

## Amazon Linux 2018.03.0.20220802.0
<a name="release-2018.03.0.20220802.0"></a>

There are no major updates in this release.

Updated Packages:
+ `kernel-4.14.287-148.504.amzn1.x86_64`
+ `kernel-devel-4.14.287-148.504.amzn1.x86_64`
+ `kernel-headers-4.14.287-148.504.amzn1.x86_64`
+ `kernel-tools-4.14.287-148.504.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.3-7.amzn1.noarch`
+ `openssl-1.0.2k-16.159.amzn1.x86_64`
+ `vim-common-8.2.5172-1.1.amzn1.x86_64`
+ `vim-data-8.2.5172-1.1.amzn1.noarch`
+ `vim-enhanced-8.2.5172-1.1.amzn1.x86_64`
+ `vim-filesystem-8.2.5172-1.1.amzn1.noarch`
+ `vim-minimal-8.2.5172-1.1.amzn1.x86_64`

Packages with CVEs:

`kernel-4.14.287-148.504.amzn1`
+ CVE-2022-2318
+ CVE-2022-26365
+ CVE-2022-33740
+ CVE-2022-33741
+ CVE-2022-33742
+ CVE-2022-33744

## Amazon Linux 2018.03.0.20220705.1
<a name="release-2018.03.0.20220705.1"></a>

There are no major updates in this release.

Updated Packages:
+ `ca-certificates-2018.2.22-65.1.27.amzn1.noarch`
+ `expat-2.1.0-14.31.amzn1.x86_64`
+ `kernel-4.14.285-147.501.amzn1.x86_64`
+ `kernel-devel-4.14.285-147.501.amzn1.x86_64`
+ `kernel-headers-4.14.285-147.501.amzn1.x86_64`
+ `kernel-tools-4.14.285-147.501.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.3-5.amzn1.noarch`
+ `microcode_ctl-2.1-47.40.amzn1.x86_64`
+ `openssl-1.0.2k-16.158.amzn1.x86_64`
+ `yum-3.4.3-150.73.amzn1.noarch`
+ `zlib-1.2.8-7.19.amzn1.x86_64`
+ `zlib-devel-1.2.8-7.19.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220609.0
<a name="release-2018.03.0.20220609.0"></a>

There are no major updates in this release.

Updated Packages:
+ `expat-2.1.0-12.28.amzn1.x86_64`
+ `gzip-1.5-9.20.amzn1.x86_64`
+ `kernel-4.14.281-144.502.amzn1.x86_64`
+ `kernel-devel-4.14.281-144.502.amzn1.x86_64`
+ `kernel-headers-4.14.281-144.502.amzn1.x86_64`
+ `kernel-tools-4.14.281-144.502.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.3-1.amzn1.noarch`
+ `openldap-2.4.40-16.32.amzn1.x86_64`
+ `python27-2.7.18-2.142.amzn1.x86_64`
+ `python27-devel-2.7.18-2.142.amzn1.x86_64`
+ `python27-libs-2.7.18-2.142.amzn1.x86_64`
+ `rsyslog-5.8.10-9.29.amzn1.x86_64`
+ `tzdata-2022a-1.79.amzn1.noarch`
+ `tzdata-java-2022a-1.79.amzn1.noarch`
+ `vim-common-8.2.4877-1.1.amzn1.x86_64`
+ `vim-data-8.2.4877-1.1.amzn1.noarch`
+ `vim-enhanced-8.2.4877-1.1.amzn1.x86_64`
+ `vim-filesystem-8.2.4877-1.1.amzn1.noarch`
+ `vim-minimal-8.2.4877-1.1.amzn1.x86_64`
+ `xz-5.2.2-1.14.amzn1.x86_64`
+ `xz-libs-5.2.2-1.14.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220503.0
<a name="release-2018.03.0.20220503.0"></a>

There are no major updates in this release.

Updated Packages:
+ `rpm-4.11.3-40.80.amzn1.x86_64`
+ `rpm-build-libs-4.11.3-40.80.amzn1.x86_64`
+ `rpm-libs-4.11.3-40.80.amzn1.x86_64`
+ `rpm-python27-4.11.3-40.80.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220419.0
<a name="release-2018.03.0.20220419.0"></a>

There are no major updates in this release.

Updated Packages:
+ `amazon-ssm-agent-3.1.1188.0-1.amzn1.x86_64`
+ `glibc-2.17-324.189.amzn1.x86_64`
+ `glibc-common-2.17-324.189.amzn1.x86_64`
+ `glibc-devel-2.17-324.189.amzn1.x86_64`
+ `glibc-headers-2.17-324.189.amzn1.x86_64`
+ `kernel-4.14.275-142.503.amzn1.x86_64`
+ `kernel-devel-4.14.275-142.503.amzn1.x86_64`
+ `kernel-headers-4.14.275-142.503.amzn1.x86_64`
+ `kernel-tools-4.14.275-142.503.amzn1.x86_64`
+ `libblkid-2.23.2-63.36.amzn1.x86_64`
+ `libcap54-2.54-1.4.amzn1.x86_64`
+ `libgcrypt-1.5.3-12.20.amzn1.x86_64`
+ `libmount-2.23.2-63.36.amzn1.x86_64`
+ `libsmartcols-2.23.2-63.36.amzn1.x86_64`
+ `libuuid-2.23.2-63.36.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.1-16.amzn1.noarch`
+ `util-linux-2.23.2-63.36.amzn1.x86_64`
+ `vim-common-8.2.4621-1.1.amzn1.x86_64`
+ `vim-data-8.2.4621-1.1.amzn1.noarch`
+ `vim-enhanced-8.2.4621-1.1.amzn1.x86_64`
+ `vim-filesystem-8.2.4621-1.1.amzn1.noarch`
+ `vim-minimal-8.2.4621-1.1.amzn1.x86_64`

## Amazon Linux 2018.03.20220315.0 Release (03/15)
<a name="release-2018.03.20220315.0"></a>

There are no major updates in this release.

Updated Packages:
+ `openssl-1.0.2k-16.156.amzn1.x86_64`

## Amazon Linux 2018.03.20220310.0 Release (03/10)
<a name="release-2018.03.20220310.0"></a>

There are no major updates in this release.

Updated Packages:
+ `cyrus-sasl-2.1.23-13.17.amzn1.x86_64`
+ `cyrus-sasl-lib-2.1.23-13.17.amzn1.x86_64`
+ `cyrus-sasl-plain-2.1.23-13.17.amzn1.x86_64`
+ `expat-2.1.0-12.27.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.1-13.amzn1.noarch`
+ `tzdata-2021e-1.78.amzn1.noarch`
+ `tzdata-java-2021e-1.78.amzn1.noarch`
+ `vim-common-8.2.4314-1.1.amzn1.x86_64`
+ `vim-data-8.2.4314-1.1.amzn1.noarch`
+ `vim-enhanced-8.2.4314-1.1.amzn1.x86_64`
+ `vim-filesystem-8.2.4314-1.1.amzn1.noarch`
+ `vim-minimal-8.2.4314-1.1.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220209.2 Update
<a name="release-2018.03.0.20220209.2"></a>

There are no major updates in this release.

Updated Packages:
+ `kernel-4.14.268-139.500.amzn1.x86_64`
+ `kernel-devel-4.14.268-139.500.amzn1.x86_64`
+ `kernel-headers-4.14.268-139.500.amzn1.x86_64`
+ `kernel-tools-4.14.268-139.500.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220209.0 Update
<a name="release-2018.03.0.20220209.0"></a>

There are no major updates in this release.

Updated Packages:
+ `ca-certificates-2018.2.22-65.1.26.amzn1.noarch`
+ `openssh-7.4p1-22.77.amzn1.x86_64`
+ `openssh-clients-7.4p1-22.77.amzn1.x86_64`
+ `openssh-server-7.4p1-22.77.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220207.0 Update
<a name="release-2018.03.0.20220207.0"></a>

There are no major updates in this release.

Kernel:

Rebase kernel to upstream stable 4.14.262
+ CVEs Fixed:
  + CVE-2021-4083 [fget: check that the fd still exists after getting a ref to it]
  + CVE-2021-39685 [USB: gadget: detect too-big endpoint 0 requests]
  + CVE-2021-28711 [xen/blkfront: harden blkfront against event channel storms]
  + CVE-2021-28712 [xen/netfront: harden netfront against event channel storms]
  + CVE-2021-28713 [xen/console: harden hvc\_xen against event channel storms]
  + CVE-2021-28714 [xen/netback: fix rx queue stall detection]
  + CVE-2021-28715 [xen/netback: don't queue unlimited number of packages]
  + CVE-2021-44733 [tee: handle lookup of shm with reference count 0]
  + CVE-2021-4155 [xfs: map unwritten blocks in XFS\_IOC\_{ALLOC,FREE}SP just like fallocate]
  + CVE-2022-0492 [kernel: cgroups v1 release\_agent feature may allow privilege escalation]
+ Amazon Features and Backports:
  + ena: Update to 2.6.0
  + fuse: fix bad inode
  + fuse: fix live lock in fuse\_iget()
  + lustre: update to AmazonFSxLustreClient v2.10.8-10
  + cgroup-v1: require capabilities to set release\_agent
  + audit: improve audit queue handling when "audit=1" on cmdline
  + ENA: Update to v2.6.1
+ Other Fixes:
  + tracing: Fix pid filtering when triggers are attached
  + NFSv42: Don't fail clone() unless the OP\_CLONE operation failed
  + ARM: socfpga: Fix crash with CONFIG\_FORTIRY\_SOURCE
  + ipv6: fix typos in ip6\_finish\_output()
  + tracing: Check pid filtering when creating events
  + PCI: aardvark: Train link immediately after enabling training
  + PCI: aardvark: Update comment about disabling link training

Updated Packages:
+ `kernel-4.14.262-135.489.amzn1.x86_64`
+ `kernel-devel-4.14.262-135.489.amzn1.x86_64`
+ `kernel-headers-4.14.262-135.489.amzn1.x86_64 `
+ `kernel-tools-4.14.262-135.489.amzn1.x86_64`

## Amazon Linux 2018.03.0.20220128.0 Update
<a name="release-2018.03.0.20220128.0"></a>

There are no major updates in this release.

Updated Packages:
+ `vim-common-8.2.4006-1.2.amzn1.x86_64`
+ `vim-data-8.2.4006-1.2.amzn1.noarch`
+ `vim-enhanced-8.2.4006-1.2.amzn1.x86_64`
+ `vim-filesystem-8.2.4006-1.2.amzn1.noarch`
+ `vim-minimal-8.2.4006-1.2.amzn1.x86_64`

## Amazon Linux 2018.03.0.20211222.0
<a name="release-2018.03.0.20211222.0"></a>

**Note**
 The deprecated `aws-apitools-*` packages are now no longer shipped by default in the AL1 AMI (see [this forum post](https://forums.aws.amazon.com/thread.jspa?threadID=323611) for more details). As per [our previous announcement](https://alas.aws.amazon.com/announcements/2021-001.html) the `log4j-cve-2021-44228-hotpatch` is enabled by default, and is now part of the AMI rather than an update applied on launch.

Updated Packages:
+ `aws-apitools-as-1.0.61.6-1.0.amzn1.noarch`
+ `aws-apitools-elb-1.0.35.0-1.0.amzn1.noarch`
+ `apitools-mon-1.0.20.0-1.0.amzn1.noarch`
+ `java-1.7.0-openjdk-1.7.0.261-2.6.22.1.83.amzn1.x86_64`
+ `java-1.7.0-openjdk-1.7.0.261-2.6.22.1.84.amzn1.x86_64`
+ `log4j-cve-2021-44228-hotpatch-1.1-12.amzn1.noarch`

## Amazon Linux 2018.03.0.20211201.0
<a name="release-2018.03.0.20211201.0"></a>

Major Updates:
+ Updated `nss` to fix CVE-2021-43527. NSS (Network Security Services) up to and including 3.73 is vulnerable to a heap overflow when handling DER-encoded DSA or RSA-PSS signatures. Applications using NSS for handling signatures encoded within CMS, S/MIME, PKCS \#7, or PKCS \#12 are likely to be impacted. Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how they configure NSS. When verifying a DER-encoded signature, NSS decodes the signature into a fixed-size buffer and passes the buffer to the underlying PKCS \#11 module. The length of the signature is not correctly checked when processing DSA and RSA-PSS signatures. DSA and RSA-PSS signatures larger than 16384 bits will overflow the buffer in `VFYContextStr`. The vulnerable code is located within `secvfy.c:vfy_CreateContext`. (CVE-2021-43527)

Updated Packages:
+ `nss-3.53.1-7.87.amzn1.x86_64`
+ `nss-sysinit-3.53.1-7.87.amzn1.x86_64`
+ `nss-tools-3.53.1-7.87.amzn1.x86_64`

## Amazon Linux 2018.03.0.20211111.0
<a name="release-2018.03.0.20211111.0"></a>

Updated Packages:
+ `curl-7.61.1-12.100.amzn1.x86_64`
+ `kernel-4.14.252-131.483.amzn1.x86_64`
+ `kernel-devel-4.14.252-131.483.amzn1.x86_64`
+ `kernel-headers-4.14.252-131.483.amzn1.x86_64`
+ `kernel-tools-4.14.252-131.483.amzn1.x86_64`
+ `libcurl-7.61.1-12.100.amzn1.x86_64`
+ `openssl-1.0.2k-16.155.amzn1.x86_64`

Kernel Updates:

Rebase kernel to upstream stable 4.14.252
+ CVEs Fixed:
  + CVE-2021-37159 [usb: hso: fix error handling code of hso\_create\_net\_device]
  + CVE-2021-3744 [crypto: ccp - fix resource leaks in ccp\_run\_aes\_gcm\_cmd()]
  + CVE-2021-3764 [crypto: ccp - fix resource leaks in ccp\_run\_aes\_gcm\_cmd()]
  + CVE-2021-20317 [lib/timerqueue: Rely on rbtree semantics for next timer]
  + CVE-2021-20321 [ovl: fix missing negative dentry check in ovl\_rename()]
  + CVE-2021-41864 [bpf: Fix integer overflow in prealloc\_elems\_and\_freelist()]
+ Amazon Features and Backports:
  + Enable nitro-enclaves driver for arm64
+ Other Fixes:
  + md: fix a lock order reversal in md\_alloc
  + arm64: Mark stack\_chk\_guard as ro\_after\_init
  + cpufreq: schedutil: Use kobject release() method to free sugov\_tunables
  + cpufreq: schedutil: Destroy mutex before kobject\_put() frees the memory
  + ext4: fix potential infinite loop in ext4\_dx\_readdir()
  + nfsd4: Handle the NFSv4 READDIR 'dircount' hint being zero
  + net\_sched: fix NULL deref in fifo\_set\_limit()
  + perf/x86: Reset destroy callback on event init failure
  + virtio: write back F\_VERSION\_1 before validate

## Amazon Linux 2018.03.0.20211015.1
<a name="release-2018.03.0.20211015.1"></a>

Updated Packages:
+ `kernel-4.14.248-129.473.amzn1.x86_64`
+ `kernel-devel-4.14.248-129.473.amzn1.x86_64`
+ `kernel-headers-4.14.248-129.473.amzn1.x86_64`
+ `kernel-tools-4.14.248-129.473.amzn1.x86_64`
+ `openssl-1.0.2k-16.154.amzn1.x86_64`

Kernel Updates:
+ Rebase kernel to upstream stable 4.14.248
+ CVEs Fixed:
  + CVE-2020-16119 [dccp: don't duplicate ccid when cloning dccp sock]
  + CVE-2021-40490 [ext4: fix race writing to an inline\_data file while its xattrs are changing]
  + CVE-2021-42252 [soc: aspeed: lpc-ctrl: Fix boundary check for mmap]
+ Other Fixes:
  + mm/kmemleak.c: make cond\_resched() rate-limiting more efficient
  + mm/page\_alloc: speed up the iteration of max\_order
  + tcp: seq\_file: Avoid skipping sk during tcp\_seek\_last\_pos
  + KVM: x86: Update vCPU's hv\_clock before back to guest when tsc\_offset is adjusted
  + cifs: fix wrong release in sess\_alloc\_buffer() failed path
  + rcu: Fix missed wakeup of exp\_wq waiters

## Amazon Linux 2018.03.0.20211001.0
<a name="release-2018.03.0.20211001.0"></a>

Major Updates:
+ Update of `ca-certificates` to version `2018.2.22-65.1.24.amzn1`, which addresses the expiring IdentTrust DST Root CA X3, which affected some Let's Encrypt TLS certificates. The effect of the expiring certificate would be an inability of OpenSSL to validate impacted certificates issued by Let's Encrypt. Impacted customers may have experienced connection or certificate errors when attempting to connect to certain websites or APIs that use Let's Encrypt certificates.

Updated Packages:
+ `ca-certificates-2018.2.22-65.1.24.amzn1.noarch`
+ `curl-7.61.1-12.99.amzn1.x86_64`
+ `glib2-2.36.3-5.22.amzn1.x86_64`
+ `glibc-2.17-324.188.amzn1.x86_64`
+ `glibc-common-2.17-324.188.amzn1.x86_64`
+ `libcurl-7.61.1-12.99.amzn1.x86_64`

## Amazon Linux 2018.03.0.20210721.0
<a name="release-2018.03.0.20210721.0"></a>

Updated Packages:
+ `amazon-ssm-agent-3.0.1124.0-1.amzn1.x86_64`
+ `bind-libs-9.8.2-0.68.rc1.87.amzn1.x86_64`
+ `bind-utils-9.8.2-0.68.rc1.87.amzn1.x86_64`
+ `curl-7.61.1-12.98.amzn1.x86_64`
+ `dhclient-4.1.1-53.P1.29.amzn1.x86_64`
+ `dhcp-common-4.1.1-53.P1.29.amzn1.x86_64`
+ `glibc-2.17-322.181.amzn1.x86_64`
+ `glibc-common-2.17-322.181.amzn1.x86_64`
+ `glibc-devel-2.17-322.181.amzn1.x86_64`
+ `glibc-headers-2.17-322.181.amzn1.x86_64`
+ `kernel-4.14.238-125.422.amzn1.x86_64`
+ `kernel-devel-4.14.238-125.422.amzn1.x86_64`
+ `kernel-headers-4.14.238-125.422.amzn1.x86_64`
+ `kernel-tools-4.14.238-125.422.amzn1.x86_64`
+ `libX11-1.6.0-2.2.14.amzn1.x86_64`
+ `libX11-common-1.6.0-2.2.14.amzn1.x86_64`
+ `libcurl-7.61.1-12.98.amzn1.x86_64`
+ `nspr-4.25.0-2.45.amzn1.x86_64`
+ `nss-3.53.1-7.85.amzn1.x86_64`
+ `nss-softokn-3.53.1-6.46.amzn1.x86_64`
+ `nss-softokn-freebl-3.53.1-6.46.amzn1.x86_64`
+ `nss-sysinit-3.53.1-7.85.amzn1.x86_64`
+ `nss-tools-3.53.1-7.85.amzn1.x86_64`
+ `nss-util-3.53.1-1.58.amzn1.x86_64`
+ `rpm-4.11.3-40.79.amzn1.x86_64`
+ `rpm-build-libs-4.11.3-40.79.amzn1.x86_64`
+ `rpm-libs-4.11.3-40.79.amzn1.x86_64`
+ `rpm-python27-4.11.3-40.79.amzn1.x86_64`
+ `tzdata-2021a-1.79.amzn1.noarch`
+ `tzdata-java-2021a-1.79.amzn1.noarch`
+ `update-motd-1.0.1-3.1.amzn1.noarch`

Kernel Updates:
+ Rebase kernel to upstream stable 4.14.238
+ Amazon EFA Driver: update to version v1.12.1
+ CVEs Fixed:
  + CVE-2021-32399 [bluetooth: eliminate the potential race condition when removing the HCI controller]
  + CVE-2021-33034 [Bluetooth: verify AMP hci\_chan before amp\_destroy]
  + CVE-2020-26558 [Bluetooth: SMP: Fail if remote and local public keys are identical]
  + CVE-2021-0129 [Bluetooth: SMP: Fail if remote and local public keys are identical]
  + CVE-2020-24586 [mac80211: prevent mixed key and fragment cache attacks]
  + CVE-2020-24587 [mac80211: prevent mixed key and fragment cache attacks]
  + CVE-2020-24588 [cfg80211: mitigate A-MSDU aggregation attacks]
  + CVE-2020-26139 [mac80211: do not accept/forward invalid EAPOL frames]
  + CVE-2020-26147 [mac80211: assure all fragments are encrypted]
  + CVE-2021-29650 [netfilter: x\_tables: Use correct memory barriers.]
  + CVE-2021-3564 [Bluetooth: fix the erroneous flush\_work() order]\\
  + CVE-2021-3573 [Bluetooth: use correct lock to prevent UAF of hdev object]
  + CVE-2021-3587 [nfc: fix NULL ptr dereference in llcp\_sock\_getname() after failed connect]
  + CVE-2021-34693 [can: bcm: fix infoleak in struct bcm\_msg\_head]
  + CVE-2021-33624 [bpf: Inherit expanded/patched seen count from old aux data]
  + CVE-2021-33909 [seq\_file: disallow extremely large seq buffer allocations]
+ Amazon Features and Backports:
  + arm64/kernel: don't ban ADRP to work around Cortex-A53 erratum \#843419
  + arm64/errata: add REVIDR handling to framework
  + arm64/kernel: enable A53 erratum \#8434319 handling at runtime
  + arm64: fix undefined reference to 'printk'
  + arm64/kernel: rename module\_emit\_adrp\_veneer→module\_emit\_veneer\_for\_adrp
  + arm64/kernel: kaslr: reduce module randomization range to 4 GB
  + Revert "arm64: acpi/pci: invoke \_DSM whether to preserve firmware PCI setup"
  + PCI/ACPI: Evaluate PCI Boot Configuration \_DSM
  + PCI: Don't auto-realloc if we're preserving firmware config
  + arm64: PCI: Allow resource reallocation if necessary
  + arm64: PCI: Preserve firmware configuration when desired
  + bpf: fix subprog verifier bypass by div/mod by 0 exception
  + bpf, x86\_64: remove obsolete exception handling from div/mod
  + bpf, arm64: remove obsolete exception handling from div/mod
  + bpf, s390x: remove obsolete exception handling from div/mod
  + bpf, ppc64: remove obsolete exception handling from div/mod
  + bpf, sparc64: remove obsolete exception handling from div/mod
  + bpf, mips64: remove obsolete exception handling from div/mod
  + bpf, mips64: remove unneeded zero check from div/mod with k
  + bpf, arm: remove obsolete exception handling from div/mod
  + bpf: Fix 32 bit src register truncation on div/mod
  + bpf: Inherit expanded/patched seen count from old aux data
  + bpf: Do not mark insn as seen under speculative path verification
  + bpf: Fix leakage under speculation on mispredicted branches
  + seq\_file: disallow extremely large seq buffer allocations

## Amazon Linux 2018.03.0.20210521.1
<a name="release-2018.03.0.20210521.1"></a>

Updated Packages:
+ `kernel-4.14.232-123.381.amzn1.x86_64`
+ `kernel-devel-4.14.232-123.381.amzn1.x86_64`
+ `kernel-headers-4.14.232-123.381.amzn1.x86_64`
+ `kernel-tools-4.14.232-123.381.amzn1.x86_64`
+ `nvidia-418.197.02-2018.03.117.amzn1.x86_64`
+ `nvidia-dkms-418.197.02-2018.03.117.amzn1.x86_64`
+ `ruby20-2.0.0.648-2.40.amzn1.x86_64`
+ `ruby20-irb-2.0.0.648-2.40.amzn1.noarch`
+ `ruby20-libs-2.0.0.648-2.40.amzn1.x86_64`
+ `rubygem20-bigdecimal-1.2.0-2.40.amzn1.x86_64`
+ `rubygem20-psych-2.0.0-2.40.amzn1.x86_64`
+ `rubygems20-2.0.14.1-2.40.amzn1.noarch`
+ `xorg-x11-server-Xorg-1.17.4-18.44.amzn1.x86_64`
+ `xorg-x11-server-common-1.17.4-18.44.amzn1.x86_64`

Kernel Update:
+ Rebase kernel to upstream stable 4.14.232
+ lustre: update to AmazonFSxLustreClient v2.10.8-7
+ CVEs Fixed:
  + CVE-2020-29374 [gup: document and work around "COW can break either way" issue]
  + CVE-2021-23133 [net/sctp: fix race condition in sctp\_destroy\_sock]
+ Amazon Features and Backports:
  + bpf: fix up selftests after backports were fixed
  + bpf, selftests: Fix up some test\_verifier cases for unprivileged
  + bpf: Move off\_reg into sanitize\_ptr\_alu
  + bpf: Ensure off\_reg has no mixed signed bounds for all types
  + bpf: Rework ptr\_limit into alu\_limit and add common error path
  + bpf: Improve verifier error messages for users
  + bpf: Refactor and streamline bounds check into helper
  + bpf: Move sanitize\_val\_alu out of op switch
  + bpf: Tighten speculative pointer arithmetic mask
  + bpf: Update selftests to reflect new error states
  + bpf: do not allow root to mangle valid pointers
  + bpf/verifier: disallow pointer subtraction
  + selftests/bpf: fix test\_align
  + selftests/bpf: make 'dubious pointer arithmetic' test useful
  + bpf: Fix masking negation logic upon negative dst register
  + bpf: Fix leakage of uninitialized bpf stack under speculation
  + Revert "net/sctp: fix race condition in sctp\_destroy\_sock"
  + sctp: delay auto\_asconf init until binding the first addr
  + cifs: fix panic in smb2\_reconnect
+ Other Fixes:
  + arm64: fix inline asm in load\_unaligned\_zeropad()
  + ext4: correct error label in ext4\_rename()
  + x86/crash: Fix crash\_setup\_memmap\_entries() out-of-bounds access

## Amazon Linux 2018.03.0.20210408.0
<a name="release-2018.03.0.20210408.0"></a>

Major Updates:
+ iptables has been updated form 1.4.18 to 1.4.21

Updated Packages:
+ `amazon-ssm-agent-3.0.529.0-1.amzn1.x86_64`
+ `iptables-1.4.21-34.33.amzn1.x86_64`
+ `kernel-4.14.225-121.362.amzn1.x86_64`
+ `kernel-devel-4.14.225-121.362.amzn1.x86_64`
+ `kernel-headers-4.14.225-121.362.amzn1.x86_64`
+ `kernel-tools-4.14.225-121.362.amzn1.x86_64`
+ `libmnl-1.0.3-4.2.amzn1.x86_64`
+ `libnetfilter_conntrack-1.0.4-1.7.amzn1.x86_64`
+ `libnfnetlink-1.0.1-1.3.amzn1.x86_64`
+ `openssh-7.4p1-21.75.amzn1.x86_64`
+ `openssh-clients-7.4p1-21.75.amzn1.x86_64`
+ `openssh-server-7.4p1-21.75.amzn1.x86_64`
+ `python27-setuptools-36.2.7-1.35.amzn1.noarch`
+ `screen-4.0.3-19.7.amzn1.x86_64`

## Amazon Linux 2018.03.0.20210319.0
<a name="release-2018.03.0.20210319.0"></a>

No major updates. Reminder that AL1 is in Maintenance Support.

Updated Packages:
+ `bind-libs-9.8.2-0.68.rc1.86.amzn1.x86_64`
+ `bind-utils-9.8.2-0.68.rc1.86.amzn1.x86_64`
+ `cloud-init-0.7.6-43.23.amzn1.noarch`
+ `ec2-net-utils-0.7-43.5.amzn1.noarch`
+ `ec2-utils-0.7-43.5.amzn1.noarch`
+ `grub-0.97-94.32.amzn1.x86_64`
+ `kernel-4.14.225-121.357.amzn1.x86_64`
+ `kernel-devel-4.14.225-121.357.amzn1.x86_64`
+ `kernel-headers-4.14.225-121.357.amzn1.x86_64`
+ `kernel-tools-4.14.225-121.357.amzn1.x86_64`
+ `python27-pyliblzma-0.5.3-11.7.amzn1.x86_64`
+ `yum-3.4.3-150.72.amzn1.noarch`

Kernel Update:
+ Rebase kernel to upstream stable 4.14.225
+ CVEs Fixed:
  + CVE-2021-26930 [xen-blkback: fix error handling in xen\_blkbk\_map()]
  + CVE-2021-26931 [xen-blkback: don't "handle" error by BUG()]
  + CVE-2021-26932 [Xen/x86: don't bail early from clear\_foreign\_p2m\_mapping()]
  + CVE-2021-27363 [scsi: iscsi: Restrict sessions and handles to admin capabilities]
  + CVE-2021-27364 [scsi: iscsi: Restrict sessions and handles to admin capabilities]
  + CVE-2021-27365 [scsi: iscsi: Ensure sysfs attributes are limited to PAGE\_SIZE]
  + CVE-2021-28038 [Xen/gnttab: handle p2m update errors on a per-slot basis]
+ Amazon Features and Backports:
  + arm64: kaslr: Refactor early init command line parsing
  + arm64: Extend the kernel command line from the bootloader
  + arm64: Export acpi\_psci\_use\_hvc() symbol
  + hwrng: Add Gravition RNG driver
  + iommu/vt-d: Skip TE disabling on quirky gfx dedicated iommu
  + x86/x2apic: Mark set\_x2apic\_phys\_mode() as init
  + x86/apic: Deinline x2apic functions
  + x86/apic: Fix x2apic enablement without interrupt remapping
  + x86/msi: Only use high bits of MSI address for DMAR unit
  + x86/io\_apic: Reevaluate vector configuration on activate()
  + x86/ioapic: Handle Extended Destination ID field in RTE
  + x86/apic: Support 15 bits of APIC ID in MSI where availabl
  + x86/kvm: Reserve KVM\_FEATURE\_MSI\_EXT\_DEST\_ID
  + x86/kvm: Enable 15-bit extension when KVM\_FEATURE\_MSI\_EXT\_DEST\_ID detected
  + arm64: HWCAP: add support for AT\_HWCAP2
  + arm64: HWCAP: encapsulate elf\_hwcap
  + arm64: Implement archrandom.h for ARMv8.5-RNG
  + mm: memcontrol: fix NR\_WRITEBACK leak in memcg and system stats
  + mm: memcg: make sure memory.events is uptodate when waking pollers
  + mem\_cgroup: make sure moving\_account, move\_lock\_task and stat\_cpu in the same cacheline
  + mm: fix oom\_kill event handling
  + mm: writeback: use exact memcg dirty counts
+ Other Fixes:
  + net\_sched: reject silly cell\_log in qdisc\_get\_rtab()
  + x86: always\_inline {rd,wr}msr()
  + net: lapb: Copy the skb before sending a packet
  + ipv4: fix race condition between route lookup and invalidation
  + mm: hugetlb: fix a race between isolating and freeing page
  + mm: hugetlb: remove VM\_BUG\_ON\_PAGE from page\_huge\_active
  + mm: thp: fix MADV\_REMOVE deadlock on shmem THP
  + x86/apic: Add extra serialization for non-serializing MSRs
  + iommu/vt-d: Do not use flush-queue when caching-mode is on
  + fgraph: Initialize tracing\_graph\_pause at task creation
  + ARM: ensure the signal page contains defined contents
  + kvm: check tlbs\_dirty directly
  + ext4: fix potential htree index checksum corruption
  + mm/memory.c: fix potential pte\_unmap\_unlock pte error
  + mm/hugetlb: fix potential double free in hugetlb\_register\_node() error path
  + arm64: Add missing ISB after invalidating TLB in primary\_switch
  + mm/rmap: fix potential pte\_unmap on an not mapped pte
  + x86/reboot: Force all cpus to exit VMX root if VMX is supported
  + mm: hugetlb: fix a race between freeing and dissolving the page
  + arm64 module: set plt\* section addresses to 0x0
  + xfs: Fix assert failure in xfs\_setattr\_size()

## Amazon Linux 2018.03.0.20210224.0
<a name="release-2018.03.0.20210224.0"></a>

Updated Packages:
+ `kernel-4.14.219-119.340.amzn1.x86_64`
+ `kernel-devel-4.14.219-119.340.amzn1.x86_64`
+ `kernel-headers-4.14.219-119.340.amzn1.x86_64`
+ `kernel-tools-4.14.219-119.340.amzn1.x86_64`
+ `openssl-1.0.2k-16.153.amzn1.x86_64`
+ `python27-2.7.18-2.141.amzn1.x86_64`
+ `python27-devel-2.7.18-2.141.amzn1.x86_64`
+ `python27-libs-2.7.18-2.141.amzn1.x86_64`

Kernel Update:
+ Rebase kernel to upstream stable 4.14.219
+ CVEs Fixed:
  + CVE-2020-28374 [scsi: target: Fix XCOPY NAA identifier lookup]
  + CVE-2021-3178 [nfsd4: readdirplus shouldn't return parent of export]
  + CVE-2020-27825 [tracing: Fix race in trace\_open and buffer resize call]
  + CVE-2021-3347 [futex: Ensure the correct return value from futex\_lock\_pi()]
  + CVE-2021-3348 [nbd: freeze the queue while we're adding connections]
+ Backported Fixes:
  + NFS: Do uncached readdir when we're seeking a cookie in an empty page cache
+ Other Fixes:
  + virtio\_net: Fix recursive call to cpus\_read\_lock()
  + net-sysfs: take the rtnl lock when storing xps\_cpus
  + net: ethernet: ti: cpts: fix ethtool output when no ptp\_clock registered
  + vhost\_net: fix ubuf refcount incorrectly when sendmsg fails
  + net-sysfs: take the rtnl lock when accessing xps\_cpus\_map and num\_tc
  + crypto: ecdh - avoid buffer overflow in ecdh\_set\_secret()
  + x86/mm: Fix leak of pmd ptlock
  + KVM: x86: fix shift out of bounds reported by UBSAN
  + net: ip: always refragment ip defragmented packets
  + x86/resctrl: Use an IPI instead of task\_work\_add() to update PQR\_ASSOC MSR
  + x86/resctrl: Don't move a task to the same resource group
  + cpufreq: powernow-k8: pass policy rather than use cpufreq\_cpu\_get()
  + iommu/intel: Fix memleak in intel\_irq\_remapping\_alloc
  + KVM: arm64: Don't access PMCR\_EL0 when no PMU is available
  + mm/hugetlb: fix potential missing huge page size info
  + dm snapshot: flush merged data before committing metadata
  + ext4: fix bug for rename with RENAME\_WHITEOUT
  + NFS4: Fix use-after-free in trace\_event\_raw\_event\_nfs4\_set\_lock
  + ext4: fix superblock checksum failure when setting password salt
  + mm, slub: consider rest of partial list if acquire\_slab() fails
  + rxrpc: Fix handling of an unsupported token type in rxrpc\_read()
  + tipc: fix NULL deref in tipc\_link\_xmit()
  + net: use skb\_list\_del\_init() to remove from RX sublists
  + net: introduce skb\_list\_walk\_safe for skb segment walking
  + dm: avoid filesystem lookup in dm\_get\_dev\_t()
  + skbuff: back tiny skbs with kmalloc() in \_\_netdev\_alloc\_skb() too
  + tracing: Fix race in trace\_open and buffer resize call
  + x86/boot/compressed: Disable relocation relaxation
  + nbd: freeze the queue while we're adding connections
  + KVM: x86: get smi pending status correctly
  + x86/entry/64/compat: Preserve r8-r11 in int $0x80
  + x86/entry/64/compat: Fix x86/entry/64/compat: Preserve r8-r11 in int $0x80

## Amazon Linux 2018.03.0.20210126.0
<a name="release-2018.03.0.20210126.0"></a>

Updated Packages:
+ `bind-libs-9.8.2-0.68.rc1.85.amzn1.x86_64`
+ `bind-utils-9.8.2-0.68.rc1.85.amzn1.x86_64`
+ `ca-certificates-2018.2.22-65.1.23.amzn1.noarch`
+ `e2fsprogs-1.43.5-2.44.amzn1.x86_64`
+ `e2fsprogs-libs-1.43.5-2.44.amzn1.x86_64`
+ `ec2-net-utils-0.7-2.4.amzn1.noarch`
+ `ec2-utils-0.7-2.4.amzn1.noarch`
+ `expat-2.1.0-12.24.amzn1.x86_64`
+ `gnupg2-2.0.28-2.34.amzn1.x86_64`
+ `kernel-4.14.214-118.339.amzn1.x86_64`
+ `kernel-devel-4.14.214-118.339.amzn1.x86_64`
+ `kernel-headers-4.14.214-118.339.amzn1.x86_64`
+ `kernel-tools-4.14.214-118.339.amzn1.x86_64`
+ `libblkid-2.23.2-63.33.amzn1.x86_64`
+ `libcom_err-1.43.5-2.44.amzn1.x86_64`
+ `libepoxy-1.2-3.3.amzn1.x86_64`
+ `libevdev-1.4.5-2.4.amzn1.x86_64`
+ `libmount-2.23.2-63.33.amzn1.x86_64`
+ `libsmartcols-2.23.2-63.33.amzn1.x86_64`
+ `libss-1.43.5-2.44.amzn1.x86_64`
+ `libuuid-2.23.2-63.33.amzn1.x86_64`
+ `libX11-1.6.0-2.2.13.amzn1.x86_64`
+ `libX11-common-1.6.0-2.2.13.amzn1.x86_64`
+ `libxslt-1.1.28-6.15.amzn1.x86_64`
+ `mtdev-1.1.2-5.4.amzn1.x86_64`
+ `python27-pip-9.0.3-1.28.amzn1.noarch`
+ `python27-setuptools-36.2.7-1.34.amzn1.noarch`
+ `ruby20-2.0.0.648-2.39.amzn1.x86_64`
+ `ruby20-irb-2.0.0.648-2.39.amzn1.noarch`
+ `ruby20-libs-2.0.0.648-2.39.amzn1.x86_64`
+ `rubygem20-bigdecimal-1.2.0-2.39.amzn1.x86_64`
+ `rubygem20-psych-2.0.0-2.39.amzn1.x86_64`
+ `rubygems20-2.0.14.1-2.39.amzn1.noarch`
+ `sudo-1.8.23-9.56.amzn1.x86_64`
+ `system-release-2018.03-0.2.noarch`
+ `tzdata-2020d-2.76.amzn1.noarch`
+ `tzdata-java-2020d-2.76.amzn1.noarch`
+ `util-linux-2.23.2-63.33.amzn1.x86_64`
+ `vim-common-8.0.0503-1.47.amzn1.x86_64`
+ `vim-enhanced-8.0.0503-1.47.amzn1.x86_64`
+ `vim-filesystem-8.0.0503-1.47.amzn1.x86_64`
+ `vim-minimal-8.0.0503-1.47.amzn1.x86_64`
+ `xorg-x11-drv-evdev-2.9.2-1.7.amzn1.x86_64`
+ `xorg-x11-drv-vesa-2.3.4-1.8.amzn1.x86_64`
+ `xorg-x11-drv-void-1.4.1-1.8.amzn1.x86_64`
+ `xorg-x11-server-common-1.17.4-18.43.amzn1.x86_64`
+ `xorg-x11-server-Xorg-1.17.4-18.43.amzn1.x86_64`

Kernel Updates:
+ Rebase kernel to upstream stable 4.14.214
+ CVEs Fixed:
  + CVE-2019-19813 [btrfs: inode: Verify inode mode to avoid NULL pointer dereference]
  + CVE-2019-19816 [btrfs: inode: Verify inode mode to avoid NULL pointer dereference]
  + CVE-2020-29661 [tty: Fix ->pgrp locking in tiocspgrp()]
  + CVE-2020-29660 [tty: Fix ->session locking]
  + CVE-2020-27830 [speakup: Reject setting the speakup line discipline outside of speakup]
  + CVE-2020-27815 [jfs: Fix array index bounds check in dbAdjTree]
  + CVE-2020-29568 [xen/xenbus: Allow watches discard events before queueing]
  + CVE-2020-29569 [xen-blkback: set ring->xenblkd to NULL after kthread\_stop()]
+ Backported Fixes:
  + SMB3: Add support for getting and setting SACLs
  + Add SMB 2 support for getting and setting SACLs
+  Other Fixes:
  + mm: memcontrol: fix excessive complexity in memory.stat reporting
  + PCI: Fix pci\_slot\_release() NULL pointer dereference
  + ext4: fix deadlock with fs freezing and EA inodes
  + ext4: fix a memory leak of ext4\_free\_data
  + sched/deadline: Fix sched\_dl\_global\_validate()
  + cifs: fix potential use-after-free in cifs\_echo\_request()
  + btrfs: fix return value mixup in btrfs\_get\_extent
  + btrfs: fix lockdep splat when reading qgroup config on mount

## Amazon Linux 2018.03.0.20201209.1
<a name="release-2018.03.0.20201209.1"></a>

Major Updates: Security updates to `curl`, `openssl`, and `python27`.

Updated packages:
+ `curl-7.61.1-12.95.amzn1.x86_64`
+ `kernel-4.14.203-116.332.amzn1.x86_64`
+ `kernel-tools-4.14.203-116.332.amzn1.x86_64`
+ `libcurl-7.61.1-12.95.amzn1.x86_64`
+ `openssl-1.0.2k-16.152.amzn1.x86_64`
+ `python27-2.7.18-2.140.amzn1.x86_64`
+ `python27-devel-2.7.18-2.140.amzn1.x86_64`
+ `python27-libs-2.7.18-2.140.amzn1.x86_64`

Kernel update:
+ Rebase kernel to upstream stable 4.14.203
+ CVEs Fixed:
  + CVE-2020-12352 [Bluetooth: A2MP: Fix not initializing all members]
  + CVE-2020-12351 [Bluetooth: L2CAP: Fix calling sk\_filter on non-socket based channel]
  + CVE-2020-24490 [Bluetooth: fix kernel oops in store\_pending\_adv\_report]
  + CVE-2020-25211 [netfilter: ctnetlink: add a range check for l3/l4 protonum]
  + CVE-2020-0423 [binder: fix UAF when releasing todo list]
  + CVE-2020-14386 [net/packet: fix overflow in tpacket\_rcv]
+ Other fixes:
  + Soft lockup Issue during writeback in presence of memory reclaim
  + Fix CIFS trailing characters

## Amazon Linux 2018.03.0.20201028.0
<a name="release-2018.03.0.20201028.0"></a>

Updated packages:
+ `amazon-ssm-agent`: `2.3.1319.0-1` to `3.0.161.0-1.`
+ `aws-cfn-bootstrap`: `1.4-32.23` to `1.4-34.24.`
+ `kernel`: `4.14.193-113.317` to `4.14.200-116.320.`
+ `kernel-devel`: `4.14.193-113.317` to `4.14.200-116.320.`
+ `kernel-headers`: `4.14.193-113.317` to `4.14.200-116.320.`
+ `kernel-tools`: `4.14.193-113.317` to `4.14.200-116.320.`
+ `libxml2`: `2.9.1-6.4.40` to `2.9.1-6.4.41.`
+ `libxml2-python27`: `2.9.1-6.4.40` to `2.9.1-6.4.41.`
+ `ntp`: `4.2.8p12-1.41` to `4.2.8p15-1.44.`
+ `ntpdate`: `4.2.8p12-1.41` to `4.2.8p15-1.44.`
+ `rpm`: `4.11.3-40.77` to `4.11.3-40.78.`
+ `rpm-build-libs`: `4.11.3-40.77` to `4.11.3-40.78.`
+ `rpm-libs`: `4.11.3-40.77` to `4.11.3-40.78.`
+ `rpm-python27`: `4.11.3-40.77` to `4.11.3-40.78.`
+ `tzdata`: `2019c-1.73` to `2020a-1.75.`
+ `tzdata-java`: `2019c-1.73` to `2020a-1.75.tzdata-2019c.173.amzn1.noarch` to `tzdata-2020a-1.75.amzn1.noarch`

Kernel update:
+ Rebase kernel to upstream stable 4.14.200
+ CVEs Fixed:
  + CVE-2019-19448 [btrfs: only search for left\_info if there is no right\_info in try\_merge\_free\_space]
  + CVE-2020-25212 [nfs: Fix getxattr kernel panic and memory overflow]
  + CVE-2020-14331 [vgacon: Fix for missing check in scrollback handling]
  + CVE-2020-14314 [ext4: fix potential negative array index in do\_split()]
  + CVE-2020-25285 [mm/hugetlb: fix a race between hugetlb sysctl handlers]
  + CVE-2020-25641 [block: allow for\_each\_bvec to support zero len bvec]
  + CVE-2020-25211 [netfilter: ctnetlink: add a range check for l3/l4 protonum]
  + CVE-2020-12888 [vfio-pci: Invalidate mmaps and block MMIO access on disabled memory]
  + CVE-2020-25284 [rbd: require global CAP\_SYS\_ADMIN for mapping and unmapping]
  + CVE-2020-14390 [fbcon: remove soft scrollback code]
  + CVE-2020-25645 [geneve: add transport ports in route lookup for geneve]
+ Other fixes:
  + nfs: optimise readdir cache page invalidation
  + nfs: Fix security label length not being reset

## Amazon Linux 2018.03.0.20200918.0
<a name="release-2018.03.0.20200918.0"></a>

**Note**
Major Updates:
removed `aws-api-tools-ec2-1.7.3.0-2.1.amzn1.noarch`

Updated packages:
+ `tzdata-2019c.173.amzn1.noarch` to `tzdata-2020a-1.75.amzn1.noarch`
+ `tzdata-java-2019c-1.73.amzn1.noarch` to `tzdata-java-2020a-1.75.amzn1.noarch`

## Amazon Linux 2018.03.0.20200904.0
<a name="release-2018.03.0.20200904.0"></a>

Major Updates: Update to AWS CLI, as well as CVE fixes for kernel, ruby, and python. Also contains a fix for rpm usage on systems which ulimit for file descriptors is greater than 1024.

Updated packages:
+ `aws-cli-1.18.107-1.55.amzn1.noarch`
+ `kernel-4.14.193-113.317.amzn1.x86_64`
+ `kernel-devel-4.14.193-113.317.amzn1.x86_64`
+ `kernel-headers-4.14.193-113.317.amzn1.x86_64`
+ `kernel-tools-4.14.193-113.317.amzn1.x86_64`
+ `libxml2-2.9.1-6.4.40.amzn1.x86_64`
+ `libxml2-python27-2.9.1-6.4.40.amzn1.x86_64`
+ `python27-2.7.18-2.139.amzn1.x86_64`
+ `python27-botocore-1.17.31-1.72.amzn1.noarch`
+ `python27-devel-2.7.18-2.139.amzn1.x86_64`
+ `python27-libs-2.7.18-2.139.amzn1.x86_64`
+ `python27-rsa-3.4.1-1.9.amzn1.noarch`
+ `rpm-4.11.3-40.77.amzn1.x86_64`
+ `rpm-build-libs-4.11.3-40.77.amzn1.x86_64`
+ `rpm-libs-4.11.3-40.77.amzn1.x86_64`
+ `rpm-python27-4.11.3-40.77.amzn1.x86_64`
+ `ruby20-2.0.0.648-1.33.amzn1.x86_64`
+ `ruby20-irb-2.0.0.648-1.33.amzn1.noarch`
+ `ruby20-libs-2.0.0.648-1.33.amzn1.x86_64`
+ `rubygem20-bigdecimal-1.2.0-1.33.amzn1.x86_64`
+ `rubygem20-json-1.8.3-1.53.amzn1.x86_64`
+ `rubygem20-psych-2.0.0-1.33.amzn1.x86_64`
+ `rubygems20-2.0.14.1-1.33.amzn1.noarch`

Kernel update:
+ Rebase Kernel to upstream stable 4.14.193
+ Updated EFA to ver 1.9.0g
+ CVEs fixed
  + CVE-2020-16166 [random32: update the net random state on interrupt and activity]
  + CVE-2020-14386 [net/packet: fix overflow in tpacket\_rcv]

## Amazon Linux 2018.03.0.20200716.0
<a name="release-2018.03.0.20200716.0"></a>

**Note**
Major Updates:
This AMI release comes with an updated `aws-apitools-ec2` package which displays a warning as per the deprecation plan published at [here](https://forums.aws.amazon.com/ann.jspa?annID=7804)

Updated Packages:
+ `amazon-ssm-agent-2.3.1319.0-1.amzn1.x86_64`
+ `aws-apitools-ec2-1.7.3.0-2.1.amzn1.noarch`
+ `bash-4.2.46-34.43.amzn1.x86_64`
+ `initscripts-9.03.58-1.40.amzn1.x86_64`
+ `kernel-4.14.186-110.268.amzn1.x86_64`
+ `kernel-tools-4.14.186-110.268.amzn1.x86_64`
+ `ibcgroup-0.40.rc1-5.15.amzn1.x86_64`
+ `microcode_ctl-2.1-47.39.amzn1.x86_64`

Kernel update:
+ Rebase kernel to upstream stable 4.14.186
+ Update ENA module to version 2.2.10
+ CVEs fixed
  + CVE-2018-20669 [make 'user\_access\_begin()' do 'access\_ok()']
  + CVE-2019-19462 [kernel/relay.c: handle alloc\_percpu returning NULL in relay\_open]
  + CVE-2020-0543 [addressed in microcode]
  + CVE-2020-10732 [fs/binfmt\_elf.c: allocate initialized memory in fill\_thread\_core\_info()]
  + CVE-2020-10757 [mm: Fix mremap not considering huge pmd devmap]
  + CVE-2020-10766 [x86/speculation: Prepare for per task indirect branch speculation control]
  + CVE-2020-10767 [x86/speculation: Avoid force-disabling IBPB based on STIBP and enhanced IBRS]
  + CVE-2020-10768 [x86/speculation: PR\_SPEC\_FORCE\_DISABLE enforcement for indirect branches]
  + CVE-2020-12771 [bcache: fix potential deadlock problem in btree\_gc\_coalesce]
  + CVE-2020-12888 [vfio-pci: Invalidate mmaps and block MMIO access on disabled memory]
+ Fix disallowing holes in swap files [iomap: don't allow holes in swapfiles]
+ Fix populating cache information [ACPI/PPTT: Handle architecturally unknown cache types]
+ Fix memory leaks in vfio/pci [vfio/pci: fix memory leaks in alloc\_perm\_bits()]
+ Fix error handling in btrfs [btrfs: fix error handling when submitting direct I/O bio]
+ Fix race leading to null pointer dereference in ext4 [ext4: fix race between ext4\_sync\_parent() and rename()]
+ Fix null pointer dereference in ext4 [ext4: fix error pointer dereference]
+ Fix memory leak in slub allocator [mm/slub: fix a memory leak in sysfs\_slab\_add()]

## Amazon Linux 2018.03.0.20200602.1
<a name="release-2018.03.0.20200602.1"></a>

Major Updates:
+ Python 2.7 updated to most recent upstream version - 2.7.18.
+ Amazon Linux will continue to provide security fixes to Python 2.7 according to our Amazon Linux 1 (AL1) support timeline. See AL1 FAQs.
+ ca-certificates fix for Sectigo intermediate CA expiration
+ See [this](https://forums.aws.amazon.com/thread.jspa?threadID=322837&tstart=0) forum thread for more details.
+ New Kernel with fixes for five CVEs (see below)

Updated packages:
+ `aws-cfn-bootstrap-1.4-32.23.amzn1`
+ `bind-libs-9.8.2-0.68.rc1.64.amzn1`
+ `bind-utils-9.8.2-0.68.rc1.64.amzn1`
+ `ca-certificates-2018.2.22-65.1.22.amzn1`
+ `kernel-4.14.181-108.257.amzn1`
+ `kernel-devel-4.14.181-108.257.amzn1`
+ `kernel-headers-4.14.181-108.257.amzn1`
+ `kernel-tools-4.14.181-108.257.amzn1`
+ `krb5-libs-1.15.1-46.48.amzn1`
+ `python27-2.7.18-1.137.amzn1`
+ `python27-devel-2.7.18-1.137.amzn1`
+ `python27-libs-2.7.18-1.137.amzn1`

Kernel update:
+ Re-based kernel to upstream stable 4.14.181
+ Updated ENA module to version 2.2.8
+ CVEs fixed:
  + CVE-2019-19319 [ext4: protect journal inode's blocks using block\_validity]
  + CVE-2020-10751 [selinux: properly handle multiple messages in selinux\_netlink\_send()]
  + CVE-2020-1749 [net: ipv6\_stub: use ip6\_dst\_lookup\_flow instead of ip6\_dst\_lookup]
  + CVE-2019-19768 [blktrace: Protect q->blk\_trace with RCU]
  + CVE-2020-12770 [scsi: sg: add sg\_remove\_request in sg\_write]
+ Fix for a deadlock condition in xen-blkfront [xen-blkfront: Delay flush till queue lock dropped]
+ Fix for ORC unwinding [x86/unwind/orc: Fix unwind\_get\_return\_address\_ptr() for inactive tasks]

## 2018.03.0.20200514 Update
<a name="release-2018.03.0.20200514"></a>

Major updates:
+ cloud-init now supports IMDSv2
+ Kernel includes fix for Important ALAS: https://alas.aws.amazon.com/ALAS-2020-1366.html
+ Java ALAS: https://alas.aws.amazon.com/ALAS-2020-1365.html
+ AWS CLI was upgraded to 1.18.13-1.54

Updated packages:
+ `aws-cli-1.18.13-1.54.amzn1`
+ `cloud-init-0.7.6-2.20.amzn1`
+ `ec2-net-utils-0.7-1.3.amzn1`
+ `ec2-utils-0.7-1.3.amzn1`
+ `expat-2.1.0-11.22.amzn1`
+ `java-1.7.0-openjdk-1.7.0.261-2.6.22.1.83.amzn1`
+ `kernel-4.14.177-107.254`
+ `libicu-50.2-4.0`
+ `libtirpc-0.2.4-0.16.15`
+ `python27-botocore-1.15.13-1.71`
+ `python27-colorama-0.4.1-4.8`
+ `yum-3.4.3-150.71`

Kernel update:
+ Re-based Kernel to upstream stable 4.14.177
+ CVE-2020-10711 [netlabel: cope with NULL catmap]
+ CVE-2020-12826 [Extend exec\_id to 64bits]
+ CVE-2020-12657 [block, bfq: fix use-after-free in bfq\_idle\_slice\_timer\_body]
+ CVE-2020-11565 [mm: mempolicy: require at least one nodeid for MPOL\_PREFERRED]
+ CVE-2020-8648 [vt: selection, close sel\_buffer race]
+ CVE-2020-1094 [vhost: Check docket sk\_family instead of call getname]
+ CVE-2020-8649 [vgacon: Fix a UAF in vgacon\_invert\_region]
+ CVE-2020-8647 [vgacon: Fix a UAF in vgacon\_invert\_region]
+ CVE-2020-8648 [vt: selection, close sel\_buffer race]
+ Divide by zero scheduler fix

## Updated Kernel
<a name="kernel-2018.03"></a>

The primary differences in between Amazon Linux 1 (AL1) version 2017.09 and Amazon Linux 1 (AL1) version 2018.03 is the inclusion of a newer kernel - Linux Kernel 4.14.

11/19/2018 Update: ENA driver updates: An ENA driver update that introduces Low Latency Queues (LLQ) for improved average and tail latencies. The update also adds support for receive checksum offload that improves CPU utilization.

## Automation of security patching at scale with Amazon EC2 Systems Manager Patch Manager
<a name="ssm-2018.03"></a>

Amazon EC2 Systems Manager Patch Manager supports Amazon Linux 1 (AL1). This enables automated patching of fleets of Amazon Linux 1 (AL1) Amazon EC2 instances. It can scan instances for missing patches and automatically install all missing patches.

## Deprecated packages
<a name="deprecated-2018.03"></a>
+ `gcc44`
+ `java-1.6.0-openjdk`
+ `mysql51`
+ `openssl097a`
+ `php53`
+ `php54`
+ `php55`
+ `php70 `
+ `postgresql8`
+ `python26`
+ `ruby18`
+ `ruby19`
+ `ruby21`
+ `ruby22`
+ `tomcat6`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
