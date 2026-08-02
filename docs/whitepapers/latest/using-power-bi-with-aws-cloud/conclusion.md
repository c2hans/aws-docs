---
source_url: https://docs.aws.amazon.com/whitepapers/latest/using-power-bi-with-aws-cloud/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

If you’re looking to use Microsoft Power BI Desktop, we generally find that customers start experimenting with the software on premises, connecting to data sources over the internet. While private connectivity options exist for using Site-to-Site VPN and Direct Connect, many customers have concluded that running Microsoft Power BI Desktop in Amazon WorkSpaces provides a better performing experience.

If you want to connect data sources in AWS to Microsoft Power BI Service, you should feel comfortable knowing that this is an established architectural pattern. You can install the Microsoft on-premises data gateway within an Amazon VPC and connect data sources such as Amazon RDS, Amazon Redshift, Amazon Athena, Amazon OpenSearch Service, and AWS Lake Formation seamlessly to the service.

If you want a solution that provides the same business outcomes, without the added complexity of installing, configuring, patching, and scaling self-managed BI solutions, we recommend Amazon Quick. This fully managed service combines all the required functionality in a simple web browser experience with pay-per-user pricing. There is nothing to install and no additional components are required.

Hopefully, this is just the start of your business intelligence journey with AWS. For additional resources to help you get started, see the [Appendix: Microsoft Power BI supported AWS data sources](appendix-microsoft-power-bi-supported-aws-data-sources.md).
