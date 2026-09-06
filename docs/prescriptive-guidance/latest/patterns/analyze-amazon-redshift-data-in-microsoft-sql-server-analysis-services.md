---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services.html
---

# Analyze Amazon Redshift data in Microsoft SQL Server Analysis Services
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services"></a>

*Sunil Vora, Amazon Web Services*

## Summary
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-summary"></a>

This pattern describes how to connect and analyze Amazon Redshift data in Microsoft SQL Server Analysis Services, by using the Intellisoft OLE DB Provider or CData ADO.NET Provider for database access.

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. SQL Server Analysis Services is an online analytical processing (OLAP) tool that you can use to analyze data from data marts and data warehouses such as Amazon Redshift. You can use SQL Server Analysis Services to create OLAP cubes from your data for rapid, advanced data analysis.

## Prerequisites and limitations
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-prereqs"></a>

**Assumptions**
+ This pattern describes how to set up SQL Server Analysis Services and Intellisoft OLE DB Provider or CData ADO.NET Provider for Amazon Redshift on an Amazon Elastic Compute Cloud (Amazon EC2) instance. Alternatively, you can install both on a host in your corporate data center.

**Prerequisites**
+ An active AWS account
+ An Amazon Redshift cluster with credentials

## Architecture
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-architecture"></a>

**Source technology stack**
+ An Amazon Redshift cluster

**Target technology stack**
+ Microsoft SQL Server Analysis Services

**Source and target architecture**

![Analyzing Amazon Redshift data in Microsoft SQL Server Analysis Services](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e444fec0-e00f-4cc6-acc6-4ffc61b654a0/images/6f29dab5-1ea7-452f-9b07-d1d23ae469a2.png)

## Tools
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-tools"></a>
+ [Microsoft Visual Studio 2019 (Community Edition)](https://visualstudio.microsoft.com/vs/)
+ [Intellisoft OLE DB Provider for Amazon Redshift (Trial)](https://www.pgoledb.com/index.php?option=com_filecabinet&view=files&id=1&Itemid=68) or[ CData ADO.NET Provider for Amazon Redshift (Trial)](https://www.cdata.com/kb/tech/redshift-ado-ssas.rst)

## Epics
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-epics"></a>

### Analyze tables
<a name="analyze-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Analyze the tables and data to be imported. | Identify the Amazon Redshift tables to be imported and their sizes. | DBA |

### Set up EC2 instance and install tools
<a name="set-up-ec2-instance-and-install-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up an EC2 instance. | In your AWS account, create an EC2 instance in a private or public subnet. | Systems administrator |
| Install tools for database access. | Download and install the [Intellisoft OLE DB Provider for Amazon Redshift](https://www.pgoledb.com/index.php?option=com_filecabinet&view=files&id=1&Itemid=68) (or [CData ADO.NET Provider for Amazon Redshift](https://www.cdata.com/kb/tech/redshift-ado-ssas.rst)).  | Systems administrator |
| Install Visual Studio. | Download and install [Visual Studio 2019 (Community Edition)](https://visualstudio.microsoft.com/vs/).  | Systems administrator |
| Install extensions. | Install the **Microsoft Analysis Services Projects** extension in Visual Studio. | Systems administrator |
| Create a project. | Create a new tabular model project in Visual Studio to store your Amazon Redshift data. In Visual Studio, choose the **Analysis Services Tabular Project** option when creating your project. | DBA |

### Create data source and import tables
<a name="create-data-source-and-import-tables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon Redshift data source. | Create an Amazon Redshift data source by using the Intellisoft OLE DB Provider for Amazon Redshift (or CData ADO.NET Provider for Amazon Redshift) and your Amazon Redshift credentials. | Amazon Redshift, DBA |
| Import tables. | Select and import tables and views from Amazon Redshift into your SQL Server Analysis Services project. | Amazon Redshift, DBA |

### Clean up after migration
<a name="clean-up-after-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the EC2 instance. | Delete the EC2 instance you launched previously. | Systems administrator |

## Related resources
<a name="analyze-amazon-redshift-data-in-microsoft-sql-server-analysis-services-resources"></a>
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/) (AWS documentation)
+ [Install SQL Server Analysis Services](https://docs.microsoft.com/en-us/analysis-services/instances/install-windows/install-analysis-services?view=asallproducts-allversions) (Microsoft documentation)
+ [Tabular Model Designer](https://docs.microsoft.com/en-us/analysis-services/tabular-models/tabular-model-designer-ssas?view=asallproducts-allversions) (Microsoft documentation)
+ [Overview of OLAP cubes for advanced analytics](https://docs.microsoft.com/en-us/system-center/scsm/olap-cubes-overview?view=sc-sm-2019) (Microsoft documentation)
+ [Microsoft Visual Studio 2019 (Community Edition)](https://visualstudio.microsoft.com/vs/)
+ [Intellisoft OLE DB Provider for Amazon Redshift (Trial)](https://www.pgoledb.com/index.php?option=com_filecabinet&view=files&id=1&Itemid=68)
+ [CData ADO.NET Provider for Amazon Redshift (Trial)](https://www.cdata.com/kb/tech/redshift-ado-ssas.rst)
