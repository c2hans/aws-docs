---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/connect-by-using-an-ssh-tunnel-in-pgadmin.html
---

# Connect by using an SSH tunnel in pgAdmin
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin"></a>

*Jeevan Shetty and Bhanu Ganesh Gudivada, Amazon Web Services*

## Summary
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-summary"></a>

For security reasons, it’s always good to place databases in a private subnet. Queries against the database can be run by connecting through an Amazon Elastic Compute Cloud (Amazon EC2) bastion host in a public subnet on the Amazon Web Services (AWS) Cloud. This requires installing software, such as pgAdmin or DBeaver, which are commonly used by developers or database administrators, on the Amazon EC2 host.

Running pgAdmin on a Linux server and accessing it through a web browser requires the installation of additional dependencies, permissions setup, and configuration.

As an alternate solution, developers or database administrators can connect to a PostgreSQL database by using pgAdmin to enable an SSH tunnel from their local system. In this approach, pgAdmin uses the Amazon EC2 host in the public subnet as an intermediary host before connecting to the database. The diagram in the *Architecture* section shows the setup.

**Note**
Ensure that the security group attached to the PostgreSQL database allows connection on port 5432 from the Amazon EC2 host.

## Prerequisites and limitations
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-prereqs"></a>

**Prerequisites **
+ An existing AWS account
+ A virtual private cloud (VPC) with a public subnet and a private subnet
+ An EC2 instance with a security group attached
+ An Amazon Aurora PostgreSQL-Compatible Edition database with a security group attached
+ A Secure Shell (SSH) key pair for setting up the tunnel

**Product versions**
+ pgAdmin version 6.2\+
+ Amazon Aurora PostgreSQL-Compatible Edition version 12.7\+

## Architecture
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-architecture"></a>

**Target technology stack**
+ Amazon EC2
+ Amazon Aurora PostgreSQL-Compatible

**Target architecture**

The following diagram shows using pgAdmin with an SSH tunnel to connect through an internet gateway to the EC2 instance, which connects to the database.

![pgAdmin with SSH tunnel connects through internet gateway to EC2 instance that connects to database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7d25d570-5685-4f1a-bef0-212e257cb589/images/4556d930-f9b3-4b65-be5d-d40dd9437d5a.png)

## Tools
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.

**Other services**
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.

## Epics
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-epics"></a>

### Create the connection
<a name="create-the-connection"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a server. | In pgAdmin, choose **Create**, and then choose **Server**. For additional help with setting up pgAdmin to register a server, configure a connection, and connect through SSH tunneling by using the Server Dialog, see the links in the *Related resources* section. | DBA |
| Provide a name for the server. | On the **General** tab, enter a name. | DBA |
| Enter the database details. | On the **Connection** tab, enter values for the following:+ **Host name/address**<br />+ **Port**<br />+ **Maintenance database**<br />+ **Username**<br />+ **Password** | DBA |
| Enter the Amazon EC2 server details. | On the **SSH Tunnel** tab, provide the details of the Amazon EC2 instance that is in the public subnet.+ Set **Use SSH tunneling** to **Yes** to specify that pgAdmin should use an SSH tunnel when connecting to the specified server.<br />+ In the **Tunnel host** field, specify the name or IP address of the SSH host (for example, 10.x.x.x).<br />+ In the **Tunnel port** field, specify the port of the SSH host (for example, 22).<br />+ In the **Username** field, specify the name of a user with login privileges for the SSH host (for example, ec2-user).<br />+ Specify the type of authentication as **Identity file** so that pgAdmin will use a private key file when connecting.Include the location of the Privacy Enhanced Mail (PEM) file in the **Identity file** field. The .pem file is the Amazon EC2 key pair. | DBA |
| Save and connect. | Choose **Save** to complete the setup and connect to the Aurora PostgreSQL-Compatible database by using the SSH tunnel. | DBA |

## Related resources
<a name="connect-by-using-an-ssh-tunnel-in-pgadmin-resources"></a>
+ [Server Dialog](https://www.pgadmin.org/docs/pgadmin4/latest/server_dialog.html)
+ [Connect to Server](https://www.pgadmin.org/docs/pgadmin4/latest/connect_to_server.html)
