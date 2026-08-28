---
source_url: https://docs.aws.amazon.com/sap/latest/general/uninstall-older-dp.html
---

# Uninstalling older versions
<a name="uninstall-older-dp"></a>

Uninstalling the AWS Data Provider for SAP does not require SAP downtime and can be done online. The only impact will be a gap in metric monitoring information for the time that the DataProvider was installed on your system.

## Uninstall DataProvider 3.0
<a name="uninstall-dp3.0"></a>

 **Linux**

1. Log in to Linux as a superuser, like root.

1. Stop and remove the DataProvider using the following command.

 **SLES**

```
zypper remove -y aws-sap-dataprovider
```

 **RHEL/OEL**

```
yum -y erase aws-sap-dataprovider
```

 **Windows**

```
“C:\Program Files\Amazon\DataProvider\uninstall.exe“
```

## Uninstall DataProvider 2.0
<a name="uninstall-dp2.0"></a>

 **Linux**

1. Log in to Linux as a superuser, like root.

1. Stop and remove the DataProvider using the following command.

```
/usr/local/ec2/aws-agent/bin/aws-agent_uninstall
```

 **Windows**

```
“C:\Program Files\Amazon\DataProvider\uninstall.exe“
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
