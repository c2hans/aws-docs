---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/the-microsoft-power-bi-suite.html
---

# The Microsoft Power BI suite
<a name="the-microsoft-power-bi-suite"></a>

To reduce confusion due to product naming similarities, this whitepaper presents what each Microsoft Power BI product and service is.

## Power BI Desktop
<a name="power-bi-desktop"></a>

Power BI Desktop is a free application you install on your local computer. It lets you connect to, transform, and visualize your data. With Power BI Desktop, you can connect to multiple different sources of data and combine them (often called *modeling*) into a data model. This data model lets you build visuals and collections of visuals you can share as reports with other people inside your organization.

Power BI Desktop can connect to any supported data source that is available locally or over the network. For supported data sources, see the [Appendix: Microsoft Power BI supported AWS data sources](appendix-microsoft-power-bi-supported-aws-data-sources.md).

Most users who work on business intelligence projects use Power BI Desktop to create reports. Then they push content to either Power BI Report Server or the Power BI service in order to share their reports with others. The act of pushing content from Power BI Desktop to the Power BI Report Server or the Power BI service is known as *publishing*. For more information, see [What is Power BI Desktop?](https://docs.microsoft.com/en-us/power-bi/fundamentals/desktop-what-is-desktop)

**Note**
 Power BI Desktop is a Windows-only application. It is not available for Linux, macOS, or other operating systems.

## Power BI Service
<a name="power-bi-service"></a>

Power BI is a collection of software services, apps, and connectors that work together to help you create, share, and consume business insights in a way that serves you and your business most effectively. The Power BI service, sometimes referred to as Power BI online, is the *software as a service* (SaaS) part of Power BI. For more information, see [What is the Power BI service?](https://docs.microsoft.com/en-us/power-bi/fundamentals/power-bi-service-overview)

The Power BI service is a cloud-based service. It supports light report editing and collaboration for teams and organizations. You can connect to data sources in the Power BI service too, but modeling is limited.

Most report designers who work on business intelligence projects use Power BI Desktop to create reports, and then use the Power BI service to distribute their reports with others. For additional information on this crucial component, refer to [Connecting the Microsoft Power BI service to AWS data sources](https://docs.aws.amazon.com/en_us/whitepapers/latest/using-power-bi-with-aws-cloud/connecting-the-microsoft-power-bi-service-to-aws-data-sources).

## Power BI Report Server
<a name="power-bi-report-server"></a>

Power BI Report Server (PBIRS) is a private report server with a web portal in which you display and manage reports and KPIs. You can use Power BI Report Server when you don't want your reports published to the Power BI service.

With the release of SQL Server 2025, PBIRS has become the default reporting solution for SQL Server and no new versions of SQL Server Reporting Services (SSRS) will be released. This means that for deployments of SQL Server 2025, you can deploy Power BI Report Server on AWS. This applies to SQL Server Enterprise and Standard editions, for both License Included and BYOL deployments. For SQL Server versions prior to 2025, PBIRS is not permitted on AWS. Instead, use SSRS or the Power BI Service (SaaS).

On License Included instances, retrieve the product key from `C:\SQLServerSetup\x64\DefaultSetup.ini` or by running the SQL Server setup program. For BYOL licensing details, including core-count requirements and failover instance rules, see the [Microsoft SQL Server 2025 Product Terms](https://www.microsoft.com/licensing/terms/productoffering/SQLServer/EAEAS).

**Note**
A Power BI Pro User Subscription License is required to publish shared reports.

For hardware requirements, see [System requirements for Power BI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/system-requirements).

For installation instructions, see [Install Power BI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/install-report-server).

## On-premises data gateway
<a name="on-premises-data-gateway"></a>

The Microsoft on-premises data gateway is a commonly-deployed component that can increase the security and performance of Power BI deployments. It allows the Power BI service to access privatized data sources, which are located in another facility and accessible by internal network connectivity between the data source and the data gateway. Although it is typically installed as a server component, you can also install a personal mode on your local computer as an application. This whitepaper focuses only on the standard (server) mode. For additional information, refer to [Connecting the Microsoft Power BI service to AWS data sources](https://docs.aws.amazon.com/en_us/whitepapers/latest/using-power-bi-with-aws-cloud/connecting-the-microsoft-power-bi-service-to-aws-data-sources.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
