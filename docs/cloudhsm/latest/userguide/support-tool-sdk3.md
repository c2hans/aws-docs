---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/support-tool-sdk3.html
---

# AWS CloudHSM Client SDK 3 support tool
<a name="support-tool-sdk3"></a>

The script for the AWS CloudHSM Client SDK 3 extracts the following information:
+ Operating system and its current version
+ Client configuration information from `cloudhsm_client.cfg`, `cloudhsm_mgmt_util.cfg`, and `application.cfg` files
+ Client logs from the location specific to the platform
+ Cluster and HSM information by using cloudhsm\_mgmt\_util
+ OpenSSL information
+ Current client and build version
+ Installer version

## Running the info tool for Client SDK 3
<a name="running-script"></a>

The script creates an output file with all the gathered information. The script creates the output file inside the `/tmp` directory.

**Linux**: `/opt/cloudhsm/bin/client_info`

**Windows**: `C:\Program Files\Amazon\CloudHSM\client_info`

**Warning**
This script has a known issue for Client SDK 3 versions 3.1.0 through 3.3.1. We strongly recommend you upgrade to version 3.3.2 which includes a fix for this issue. Please refer to the [Known Issues](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-all.html#ki-all-9) page for more information before using this tool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
