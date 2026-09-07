---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/oracle-e-business-suite-components.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle E-Business Suite components
<a name="oracle-e-business-suite-components"></a>

 Oracle E-Business Suite has a three-tier architecture consisting of client, application, and database (DB) tiers.

 Database tier for Oracle E-Business Suite can be deployed either on Amazon RDS Custom for Oracle managed service or self-managed Oracle Database on Amazon EC2.

![Diagram showing Oracle E-Business Suite three-tier architecture with database tier on RDS Custom for Oracle](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/images/e-business-suite-three-tier-architecture.png)

![Diagram showing Oracle E-Business Suite three-tier architecture with database tier on Amazon EC2](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/images/e-business-suite-arch-with-ec2.png)

 The client tier contains the client user interface, which is provided through HTML or Java applets in a web browser for forms-based applications.

 The application tier consists of Oracle Fusion Middleware (Oracle HTTP Server and Oracle WebLogic Server) and the concurrent processing server. The Fusion Middleware server has HTTP, Java, and Forms services that process the business logic and talk to the database tier. The Oracle HTTP Server (OHS) accepts incoming HTTP requests from clients, and routes the requests to the Oracle Web Logic Server (WLS), which hosts the business logic and other server-side components. The HTTP services, forms services, and concurrent processing server can be installed on multiple application tier nodes and load balanced.

 The database tier consists of an Oracle database that stores the data for Oracle E-Business Suite. This tier has the Oracle database run items and the Oracle database files that physically store the tables, indexes, and other database objects in the system.

 See the [Oracle E-Business Suite Concepts](https://docs.oracle.com/cd/E51111_01/current/acrobat/122oacg.pdf) guide for a deeper dive on the Oracle E-Business Suite architecture components.
