---
source_url: https://docs.aws.amazon.com/linux/al2/ug/amazon-linux-source-packages.html
---

# AL2 Source Packages
<a name="amazon-linux-source-packages"></a>

You can view the source of packages you have installed on your instance for reference purposes by using tools provided in Amazon Linux. Source packages are available for all of the packages included in Amazon Linux and the online package repository. Determine the package name for the source package you want to install and use the **yumdownloader --source** command to view source within your running instance. For example:

```
[ec2-user ~]$ yumdownloader --source bash
```

The source RPM can be unpacked and, for reference, you can view the source tree using standard RPM tools. After you finish debugging, the package is available for use.
