---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/listing-applicable-advisories.html
---

# Listing applicable Advisories
<a name="listing-applicable-advisories"></a>

 The `dnf` package manager has access to metadata describing what Advisories are fixed in what package versions. It can thus list what Advisories are applicable to an instance or container image.

**Note**
 Tools such as [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) can use this functionality to show what updates are relevant across a fleet rather than just a single instance.

 When listing updates, you can instruct `dnf` to look at the metadata of a particular AL2023 release, or the metadata from the latest release.

**Note**
 Once an AL2023 release is made, it is immutable. Thus, new or updated advisories on the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html) are only added to the metadata of *new* releases of AL2023

 We will now go through examples of looking at what advisories apply to some AL2023 container images. These commands all work on non-containerized environments such as EC2 instances.

------
#### [ Listing advisories in a specific version ]

 In this example we are going to look at what advisories in the [2023.1.20230628](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230628.html) release are relevant in a container image of the [2023.0.20230315](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html) release.

**Note**
 This example uses the [2023.0.20230315](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html) and [2023.1.20230628](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230628.html) releases, and these *are not* the latest release of AL2023 See the [AL2023 Release Notes](https://docs.aws.amazon.com/linux/al2023/release-notes/) for the latest releases, which contain the latest security updates.

 In this example we will be starting with a container image for the [2023.0.20230315](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.0.20230315.html) release.

 First, we fetch this container image from the container registry. The `.0` at the end indicates the version of the image for a particular release; this image version is usually zero.

```
$ docker pull public.ecr.aws/amazonlinux/amazonlinux:{{2023.0.20230315.0}}
	  2023.0.20230315.0: Pulling from amazonlinux/amazonlinux
b76f3b09316a: Pull complete
Digest: sha256:94e7183b0739140dbd5b639fb7600f0a2299cec5df8780c26d9cb409da5315a9
Status: Downloaded newer image for public.ecr.aws/amazonlinux/amazonlinux:2023.0.20230315.0
public.ecr.aws/amazonlinux/amazonlinux:2023.0.20230315.0
```

 We can now spawn a shell inside the container, from which we will ask `dnf` to list what advisories are relevant to the packages installed in the container.

```
$ docker run -it public.ecr.aws/amazonlinux/amazonlinux:{{2023.0.20230315.0}}
	  bash-5.2#
```

 The `dnf updateinfo` command is now used to display a summary of what advisories in the [2023.1.20230628](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230628.html) release are relevant to our installed packages.

```
$ dnf updateinfo --releasever={{2023.1.20230628}}
Amazon Linux 2023 repository                     42 MB/s |  15 MB     00:00
Last metadata expiration check: 0:00:02 ago on Mon Jul 22 20:24:24 2024.
Updates Information Summary: available
    8 Security notice(s)
        1 Important Security notice(s)
        5 Medium Security notice(s)
        2 Low Security notice(s)
```

 To get a list of the advisories, the `--list` option can be given to `dnf updateinfo`.

```
$ dnf updateinfo --releasever={{2023.1.20230628}} --list
Last metadata expiration check: 0:01:22 ago on Mon Jul 22 20:24:24 2024.
ALAS2023-2023-193 Medium/Sec.    curl-minimal-8.0.1-1.amzn2023.x86_64
ALAS2023-2023-225 Medium/Sec.    glib2-2.74.7-688.amzn2023.0.1.x86_64
ALAS2023-2023-195 Low/Sec.       libcap-2.48-2.amzn2023.0.3.x86_64
ALAS2023-2023-193 Medium/Sec.    libcurl-minimal-8.0.1-1.amzn2023.x86_64
ALAS2023-2023-145 Low/Sec.       libgcc-11.3.1-4.amzn2023.0.3.x86_64
ALAS2023-2023-145 Low/Sec.       libgomp-11.3.1-4.amzn2023.0.3.x86_64
ALAS2023-2023-145 Low/Sec.       libstdc++-11.3.1-4.amzn2023.0.3.x86_64
ALAS2023-2023-163 Medium/Sec.    libxml2-2.10.4-1.amzn2023.0.1.x86_64
ALAS2023-2023-220 Important/Sec. ncurses-base-6.2-4.20200222.amzn2023.0.4.noarch
ALAS2023-2023-220 Important/Sec. ncurses-libs-6.2-4.20200222.amzn2023.0.4.x86_64
ALAS2023-2023-181 Medium/Sec.    openssl-libs-1:3.0.8-1.amzn2023.0.2.x86_64
ALAS2023-2023-222 Medium/Sec.    openssl-libs-1:3.0.8-1.amzn2023.0.3.x86_64
```

------
#### [ Listing advisories in the latest version ]

 In this example we are going to look at what updates are available in the `latest` version of AL2023 if we launched a container of the [2023.4.20240319](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240319.html) release. At the time of writing, the `latest` release is [2023.5.20240708](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html), so the listed updates in this example will be as of that release.

**Note**
 This example uses the [2023.4.20240319](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240319.html) and [2023.5.20240708](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.5.20240708.html) releases, the latter being the latest release *at the time of writing*. For more information on the latest releases, see the [AL2023 Release Notes](https://docs.aws.amazon.com/linux/al2023/release-notes/).

 In this example we will be starting with a container image for the [2023.4.20240319](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.4.20240319.html) release.

 First, we fetch this container image from the container registry. The `.1` at the end indicates the version of the image for a particular release. While the image version is typically zero, this example uses a release where the image version is one.

```
$ docker pull public.ecr.aws/amazonlinux/amazonlinux:{{2023.4.20240319.1}}
	  2023.4.20240319.1: Pulling from amazonlinux/amazonlinux
6de065fda9a2: Pull complete
Digest: sha256:b4838c4cc9211d966b6ea158dacc9eda7433a16ba94436508c2d9f01f7658b4e
Status: Downloaded newer image for public.ecr.aws/amazonlinux/amazonlinux:2023.4.20240319.1
public.ecr.aws/amazonlinux/amazonlinux:2023.4.20240319.1
```

 We can now spawn a shell inside the container, from which we will check for updates.

```
$ docker run -it public.ecr.aws/amazonlinux/amazonlinux:{{2023.4.20240319.1}}
	  bash-5.2#
```

 The `dnf updateinfo` command is now used to display a summary of what advisories in the latest release are relevant to our installed packages. At the time of writing, [2023.1.20230628](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.1.20230628.html) was the latest release.

```
$ dnf --releasever=latest updateinfo
Amazon Linux 2023 repository                     76 MB/s |  25 MB     00:00
Last metadata expiration check: 0:00:04 ago on Mon Jul 22 20:59:54 2024.
Updates Information Summary: available
    9 Security notice(s)
        4 Important Security notice(s)
        4 Medium Security notice(s)
        1 Low Security notice(s)
```

 To get a list of the advisories, the `--list` option can be given to `dnf updateinfo`.

```
$ dnf updateinfo --releasever={{latest}} --list
Last metadata expiration check: 0:00:58 ago on Mon Jul 22 20:59:54 2024.
ALAS2023-2024-581 Low/Sec.       curl-minimal-8.5.0-1.amzn2023.0.3.x86_64
ALAS2023-2024-596 Medium/Sec.    curl-minimal-8.5.0-1.amzn2023.0.4.x86_64
ALAS2023-2024-576 Important/Sec. expat-2.5.0-1.amzn2023.0.4.x86_64
ALAS2023-2024-589 Important/Sec. glibc-2.34-52.amzn2023.0.10.x86_64
ALAS2023-2024-589 Important/Sec. glibc-common-2.34-52.amzn2023.0.10.x86_64
ALAS2023-2024-589 Important/Sec. glibc-minimal-langpack-2.34-52.amzn2023.0.10.x86_64
ALAS2023-2024-586 Medium/Sec.    krb5-libs-1.21-3.amzn2023.0.4.x86_64
ALAS2023-2024-581 Low/Sec.       libcurl-minimal-8.5.0-1.amzn2023.0.3.x86_64
ALAS2023-2024-596 Medium/Sec.    libcurl-minimal-8.5.0-1.amzn2023.0.4.x86_64
ALAS2023-2024-592 Important/Sec. libnghttp2-1.59.0-3.amzn2023.0.1.x86_64
ALAS2023-2024-640 Medium/Sec.    openssl-libs-1:3.0.8-1.amzn2023.0.12.x86_64
ALAS2023-2024-605 Medium/Sec.    python3-3.9.16-1.amzn2023.0.7.x86_64
ALAS2023-2024-616 Important/Sec. python3-3.9.16-1.amzn2023.0.8.x86_64
ALAS2023-2024-605 Medium/Sec.    python3-libs-3.9.16-1.amzn2023.0.7.x86_64
ALAS2023-2024-616 Important/Sec. python3-libs-3.9.16-1.amzn2023.0.8.x86_64
```

------
