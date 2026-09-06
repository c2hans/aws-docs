---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/administration.html
---

# Privileged access
<a name="administration"></a>

Amazon RDS for Oracle is fully managed. To deliver a managed service experience, it does not allow access to the underlying host, and it restricts access to some procedures and objects that require high-level privileges.

Amazon RDS Custom for Oracle grants access to the database administrator privilege and underlying operating system. You can perform operations as root user at the operating system level, and as `SYS` or `SYSTEM` user at the database level. For legacy, custom, and packaged applications, you can customize the operating system and Amazon RDS Custom for Oracle database environment by doing the following:
+ Install a custom database, and operating system patches, and packages.
+ Configure specific database settings.
+ Configure file systems to share files directly with their applications.

|  |  |  |
| --- |--- |--- |
| Access | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| Access to operating system | No | Yes |
| Access to built-in Oracle users (for example, `SYS`, `SYSTEM`) | No | Yes |
