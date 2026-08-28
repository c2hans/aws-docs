---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/odbc-driver-mac-how-to-install.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Downloading and installing the Amazon Redshift ODBC driver
<a name="odbc-driver-mac-how-to-install"></a>

Use the steps in this section to download and install the Amazon Redshift ODBC driver on a supported version of macOS. The installation process installs the driver files in the following directories:
+ `/opt/amazon/redshift/lib/universal`
+ `/opt/amazon/redshift/ErrorMessages`
+ `/opt/amazon/redshift/Setup`<a name="rs-mgmt-install-odbc-drivers-mac"></a>

**To install the Amazon Redshift ODBC driver on macOS**

1. To install the Amazon Redshift ODBC driver on macOS, download the [macOS driver version 1.6.3](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.3.1008/AmazonRedshiftODBC-64-bit.1.6.3.1008.universal.pkg).

   Then download and review the [Amazon Redshift ODBC and JDBC driver license agreement](https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf).

1. Double-click **AmazonRedshiftODBC.pkg** to run the installer.

1. Follow the steps in the installer to complete the driver installation process. To perform the installation, agree to the terms of the license agreement.

**Important**
When you have finished installing the driver, configure it for use on your system. For more information on driver configuration, see [Use an ODBC driver manager to configure the driver](odbc-driver-configure-mac.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
