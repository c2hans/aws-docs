---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python.html
---

# Create AWS CloudFormation templates for AWS DMS tasks using Microsoft Excel and Python
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python"></a>

*Venkata Naveen Koppula, Amazon Web Services*

## Summary
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-summary"></a>

This pattern outlines steps for automatically creating AWS CloudFormation templates for [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) using Microsoft Excel and Python.

Migrating databases using AWS DMS often involves creation of AWS CloudFormation templates to provision AWS DMS tasks. Previously, creating AWS CloudFormation templates required knowledge of the JSON or YAML programming language. With this tool, you only need basic knowledge of Excel and how to run a Python script using a terminal or command window.

As input, the tool takes an Excel workbook that includes the names of the tables to be migrated, Amazon Resource Names (ARNs) of AWS DMS endpoints, and AWS DMS replication instances. The tool then generates AWS CloudFormation templates for the required AWS DMS tasks.

For detailed steps and background information, see the blog post [Create AWS CloudFormation templates for AWS DMS tasks using Microsoft Excel](https://aws.amazon.com/blogs/database/create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel/) in the AWS Database blog.

## Prerequisites and limitations
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Microsoft Excel version 2016 or later
+ Python version 2.7 or later
+ The **xlrd** Python module (installed at a command prompt with the command: **pip install xlrd**)
+ AWS DMS source and target endpoints and AWS DMS replication instance

**Limitations**
+ The names of schemas, tables, and associated columns are transformed into lowercase characters at the destination endpoints.
+ This tool doesn’t address the creation of AWS DMS endpoints and replication instances.
+ Currently, the tool supports only one schema for each AWS DMS task.

## Architecture
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-architecture"></a>

**Source technology stack**
+ An on-premises database
+ Microsoft Excel

**Target technology stack**
+ AWS CloudFormation templates
+ A database in the AWS Cloud

**Architecture**

![Workflow to use Excel and Python to automatically create CloudFormation templates for AWS DMS.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/778c7c1e-2647-496f-8afd-52ff1ef02489/images/8fe1550d-8966-41aa-a480-5f7bef20629f.png)

## Tools
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-tools"></a>
+ [Pycharm IDE](https://aws.amazon.com/pycharm/), or any integrated development environment (IDE) that supports Python version 3.6
+ Microsoft Office 2016 (for Microsoft Excel)

## Epics
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-epics"></a>

### Configure the network, AWS DMS replication instance, and endpoints
<a name="configure-the-network-aws-dms-replication-instance-and-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| If necessary, request a service quota increase. | Request a service quota increase for the AWS DMS tasks if needed. | General AWS |
| Configure the AWS Region, virtual private clouds (VPCs), CIDR ranges, Availability Zones, and subnets. |  | General AWS |
| Configure the AWS DMS replication instance. | The AWS DMS replication instance can connect to both on-premises and AWS databases. | General AWS |
| Configure AWS DMS endpoints. | Configure endpoints for both the source and target databases. | General AWS |

### Prepare the worksheets for AWS DMS tasks and tags
<a name="prepare-the-worksheets-for-aws-dms-tasks-and-tags"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the tables list. | List all tables involved in the migration. | Database |
| Prepare the tasks worksheet. | Prepare the Excel worksheet using the tables list you configured. | General AWS, Microsoft Excel |
| Prepare the tags worksheet. | Detail the AWS resource tags to attach to the AWS DMS tasks. | General AWS, Microsoft Excel |

### Download and run the tool
<a name="download-and-run-the-tool"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download and extract the template generation tool from the GitHub repository. | GitHub repository: https://github.com/aws-samples/dms-cloudformation-templates-generator/ |  |
| Run the tool. | Follow the detailed instructions in the blog post listed under "References and help." |  |

## Related resources
<a name="create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel-and-python-resources"></a>
+ [Create AWS CloudFormation templates for AWS DMS tasks using Microsoft Excel (blog post)](https://aws.amazon.com/blogs/database/create-aws-cloudformation-templates-for-aws-dms-tasks-using-microsoft-excel/)
+ [DMS CloudFormation Templates Generator (GitHub repository)](https://github.com/aws-samples/dms-cloudformation-templates-generator/tree/v1.0)
+ [Python documentation](https://www.python.org/)
+ [xlrd description and download](https://pypi.org/project/xlrd/)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/)
+ [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)
