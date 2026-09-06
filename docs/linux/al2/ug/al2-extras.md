---
source_url: https://docs.aws.amazon.com/linux/al2/ug/al2-extras.html
---

# AL2 Extras Library
<a name="al2-extras"></a>

**Warning**
 The `epel` Extra enables the third party EPEL7 repository. As of 2024-06-30 the third-party EPEL7 repository is *no longer being maintained*.
 This third-party repository will have *no future updates*. This means there will be *no security fixes* for packages in the *EPEL* repository.
 See the [EPEL section of the Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/epel.html) for options for some EPEL packages.

With AL2, you can use the Extras Library to install application and software updates on your instances. These software updates are known as *topics*. You can install a specific version of a topic or omit the version information to use the most recent version. Extras help alleviate having to compromise between the stability of an operating system and the freshness of available software.

The contents of Extras topics are exempt from the Amazon Linux policy on long-term support and binary compatibility. Extras topics provide access to a curated list of packages. The versions of the packages might be updated frequently or might not be supported for the same amount of time as AL2.

**Note**
Individual Extras topics might be deprecated before AL2 reaches EOL.

To list the available topics, use the following command.

```
[ec2-user ~]$ amazon-linux-extras list
```

To enable a topic and install the latest version of its package to ensure freshness, use the following command.

```
[ec2-user ~]$ sudo amazon-linux-extras install {{topic}}
```

To enable topics and install specific versions of their packages to ensure stability, use the following command.

```
[ec2-user ~]$ sudo amazon-linux-extras install {{topic}}={{version}} {{topic}}={{version}}
```

To remove a package installed from a topic, use the following command.

```
[ec2-user ~]$ sudo yum remove $(yum list installed | grep amzn2extra-{{topic}} | awk '{ print $1 }')
```

**Note**
This command does not remove packages that were installed as dependencies of the Extra.

To disable a topic and make the packages inaccessible to the yum package manager, use the following command.

```
[ec2-user ~]$ sudo amazon-linux-extras disable {{topic}}
```

**Important**
This command is intended for advanced users. Improper usage of this command could cause package compatibility conflicts.
