---
source_url: https://docs.aws.amazon.com/sap/latest/general/dp4.3.html
---

# DataProvider 4.3
<a name="dp4.3"></a>

If you are new to AWS Data Provider for SAP, see [Installing DataProvider 4.3](data-provider-installation.md).

If you need to update or uninstall DataProvider 4.3, see [Updating to DataProvider 4.3](data-provider-update.md).

If you have an older version on your system, see [Uninstalling older versions](uninstall-older-dp.md).

**Important**
All the previous versions (v1, v2, v3) of the DataProvider have been deprecated and will no longer receive updates. For new DataProvider installations, you must install DataProvider 4.3 using an SSM distributor.

 **Run the following command to check the current version of DataProvider on your system.**

```
rpm -qa | grep aws-sap
```

To check the current version of DataProvider on **Windows**, go to **Services(Local)**, select ** AWS Data Provider for SAP**, and open **Properties**. You can see the current version in the Description field.

![Data sources for Data Provider for SAP](http://docs.aws.amazon.com/sap/latest/general/images/check-data-provider-on-windows.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for SAP on AWS Technical Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
