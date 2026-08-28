---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/viewing-svms.html
---

# Monitoring storage virtual machine (SVM) configuration details
<a name="viewing-svms"></a>

You can see the FSx for ONTAP storage virtual machines that are currently on your file system using the Amazon FSx console, the AWS CLI, and the Amazon FSx API.

**To view a storage virtual machine on your file system:**
+ **Using the console** – Choose a file system to view its **File systems** detail page. To list all the storage virtual machines on the file system, choose the **Storage virtual machines** tab, and then choose the storage virtual machine that you want to view.
+ **Using the CLI or API** – Use the [describe-storage-virtual-machines](https://docs.aws.amazon.com/cli/latest/reference/fsx/describe-storage-virtual-machines.html) CLI command or the [DescribeStorageVirtualMachines](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeStorageVirtualMachines.html) API operation.

  The system response is a list of full descriptions of all the SVMs in your account in that AWS Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
