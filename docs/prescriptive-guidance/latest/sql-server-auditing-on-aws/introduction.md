---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/introduction.html
---

# Auditing SQL Server instances, database objects, and logins in Amazon RDS and Amazon EC2
<a name="introduction"></a>

*Ashish Srivastava, Bhavani Akundi, and Sreenivas Nettem, Amazon Web Services*

This guide explains how to implement the SQL Server auditing process for SQL Server on Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) for SQL Server database instances.

Database auditing is an IT auditing method for certifying that organizational data is secure. It involves evaluating data and logging key critical business operations on databases.

Database auditing has become mandatory, especially when the data includes personally identifiable information (PII) and has to adhere to security and compliance guidelines. Some guidelines involve data types and recommendations issued by a country's governance policies. An auditing process requires evidence, which can be extracted from database logs. Auditing helps prevent unauthorized access to data. By tracking data usage, you can investigate false activity and take appropriate actions. Database auditing for data confidentiality, integrity, and accessibility help ensure that data is protected. To prevent data violations, the best practice is to have both database security and auditing in place.

SQL Server auditing is a requirement for complying with security, financial, and healthcare standards such as ISO/IEC 27001, the Payment Card Industry Data Security Standard (PCI DSS), BASEL III, the European Union General Data Protection Regulation (GDPR), Information Governance (IG), and the Health Insurance Portability and Accountability Act (HIPAA).

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Organizations implement database and SQL Server auditing for several reasons, including the following:
+ Auditors need meaningful and contextual data for compliance and auditing. DB audit logs are suitable for DBA teams but not for auditors.
+ The ability to generate critical alerts in case of a security breach is a basic requirement for large-scale software. You can use audit logs for this purpose, because the logging information assists in identifying and tracking control checks.
+ Database auditing provides information such as the following:
  + Who accessed the data―for example, DBAs, developers, auditors, extract, transform, and load (ETL) processes, DevOps engineers?
  + What was the earlier state of the data?
  + When was the data updated, what was modified, and why?
  + Did an authorized person approve the request?
  + Are internal users using their privileges properly?
+ Because audit trails help identify infiltrators, they help deter insiders. People who know that their actions are scrutinized are less likely to access unauthorized databases or tamper with specific data.
+ Finance, medical, energy, food service, public works, and many other industries need to analyze data access and produce detailed reports regularly for government agencies. For example, [HIPAA](https://www.hhs.gov/hipaa/index.html) regulations require healthcare providers to deliver audit trails that detail who accessed the data in their records, down to the row and record level. [GDPR](https://gdpr.eu/what-is-gdpr/) has similar requirements. The [Sarbanes Oxley Act (SOX)](https://www.sarbanes-oxley-101.com/sarbanes-oxley-audits.htm) places a wide range of accounting regulations on public corporations. These organizations need to analyze data access and produce detailed reports regularly.
