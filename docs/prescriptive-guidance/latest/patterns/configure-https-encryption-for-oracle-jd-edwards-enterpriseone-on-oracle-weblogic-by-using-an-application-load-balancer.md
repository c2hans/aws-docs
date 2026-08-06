---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html
---

# Configure HTTPS encryption for Oracle JD Edwards EnterpriseOne on Oracle WebLogic by using an Application Load Balancer
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer"></a>

*Thanigaivel Thirumalai, Amazon Web Services*

## Summary
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-summary"></a>

This pattern explains how to configure HTTPS encryption for SSL offloading in Oracle JD Edwards EnterpriseOne on Oracle WebLogic workloads. This approach encrypts traffic between the user’s browser and a load balancer to remove the encryption burden from the EnterpriseOne servers.

Many users scale the EnterpriseOne JAVA virtual machine (JVM) tier horizontally by using an [AWS Application Load Balancer. ](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)The load balancer serves as the single point of contact for clients, and distributes incoming traffic across multiple JVMs. Optionally, the load balancer can distribute the traffic across multiple Availability Zones and increase the availability of EnterpriseOne.

The process  described in this pattern configures encryption between the browser and the load balancer instead of encrypting the traffic between the load balancer and the EnterpriseOne JVMs. This approach is referred to as *SSL offloading*. Offloading the SSL decryption process from the EnterpriseOne web or application server to the Application Load Balancer reduces the burden on the application side. After SSL termination at the load balancer, the unencrypted traffic is routed to the application on AWS.

[Oracle JD Edwards EnterpriseOne](https://www.oracle.com/applications/jd-edwards-enterpriseone/) is an enterprise resource planning (ERP) solution for organizations that manufacture, construct, distribute, service, or manage products or physical assets. JD Edwards EnterpriseOne supports various hardware, operating systems, and database platforms.

## Prerequisites and limitations
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS Identity and Access Management (IAM) role that has permissions to make AWS service calls and manage AWS resources
+ An SSL certificate

**Product versions**
+ This pattern was tested with Oracle WebLogic 12c, but you can also use other versions.

## Architecture
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-architecture"></a>

There are multiple approaches to perform SSL offloading. This pattern uses an Application Load Balancer and Oracle HTTP Server (OHS), as illustrated in the following diagram.

![SSL offloading with a load balancer and OHS](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c62b976b-31e4-42ca-b7e8-13f7c9d9a187/images/2ae2d0eb-b9f3-41f8-ad86-9af3aade7072.png)

The following diagram shows the JD Edwards EnterpriseOne, Application Load Balancer, and Java Application Server (JAS) JVM layout.

![EnterpriseOne, load balancer, and JAS JVM layout](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c62b976b-31e4-42ca-b7e8-13f7c9d9a187/images/72ea35b0-2907-48b3-aeb7-0c5d9a3b831b.png)

## Tools
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-tools"></a>

**AWS services**
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) distribute incoming application traffic across multiple targets, such as Amazon Elastic Compute Cloud (Amazon EC2 instances), in multiple Availability Zones.
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

## Best practices
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-best-practices"></a>
+ For ACM best practices, see the [ACM documentation.](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html)

## Epics
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-epics"></a>

### Set up WebLogic and OHS
<a name="set-up-weblogic-and-ohs"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install and configure Oracle components. | 1. Install Fusion Middleware Infrastructure by following the standard installation process. This program helps you install and configure a WebLogic domain. For instructions, see the [Oracle documentation](https://docs.oracle.com/middleware/1212/core/INFIN/install_gui.htm#INFIN125).<br />2. Install OHS by following the standard installation process. For instructions, see the [Oracle documentation](https://docs.oracle.com/middleware/1221/core/install-ohs/toc.htm).<br />3. When installation is complete, start the configuration wizard (`config.sh` file) to configure OHS.You can update an existing domain or create a new domain. This pattern assumes that you’re updating an existing domain.For **Available Templates**, choose **Oracle Enterprise Manager-Restricted JRF** and **Oracle HTTP Server (Restricted JRF)**. Selecting these Java Required Files (JRF) options eliminates the connection to an external database.For **Managed Servers**, **Clusters**, **Server Templates**, **Coherence Clusters**, **Machines**, **Assign Servers to Machines**, **Virtual targets**, and **Partitions**, accept the default configuration values and choose **Next** to move to the next category.Complete the configuration details (for example, administrator host and port, listen address and port, server name) for the OHS instance (for example, `ohs1`). | JDE CNC, WebLogic administrator |
| Enable the WebLogic plugin at the domain level. | The WebLogic plugin is required for load balancing. To enable the plugin:1. Log in to the WebLogic administration console by using the link:<br />`http://<WeblogicServer>:<Adminport>/console`<br />2. Choose **Lock & Edit**, and then choose **Configuration**, **Web Applications**.<br />3. Choose the **WebLogic Plugin Enabled** (check box or dropdown option).<br />4. Choose **Save and Activate Changes**. | JDE CNC, WebLogic administrator |
| Edit the configuration file. | The `mod_wl_ohs.conf` file configures proxy requests from OHS to WebLogic.1. Edit this file. It’s located at:<br />`$ORACLE_HOME/user_projects/domains/`<br />For example:<br />`/home/oracle/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/config/fmwconfig/components/OHS/instances/ohs1`<br />2. Add the WebLogic host (`WebLogicHost`) and port (`WebLogicPort`) values (This pattern assumes localhost and port 8000.)<br />3. Add `WLProxySSL` and `WLProxySSLPassThrough` values as follows:<pre><VirtualHost *:8000><br /><Location /jde><br />WLSRequest On<br />SetHandler weblogic-handler<br />WebLogicHost localhost<br />WebLogicPort 8000<br />WLProxySSL On<br />WLProxySSLPassThrough On<br /></Location><br /></VirtualHost></pre> | JDE CNC, WebLogic administrator |
| Start OHS by using the Enterprise Manager. | 1. Log in to Enterprise Manager Fusion Middleware by using the link:<br />`http://<WeblogicServer>:<Adminport>/em/`<br />2. In **Target Navigation**, under **HTTP Server**, select the OHS instance (for example, `ohs1`).<br />3. Choose **Shut Down** and **Start Up** to restart the OHS instance.<br />4. When OHS setup is complete, you can connect to the EnterpriseOne HTML client by using your HTTP server host name with port 8000 instead of the EnterpriseOne server host name.Old link: `http://<Webserver>:80/jde/owhtml`New link: `http:// <HTTP server or web server>:8000/jde/owhtml`<br />If you use a port other than the default Oracle HTTP port, edit the `httpd.conf` file to add a listener for that port in two places:<pre>#[Listen] OHS_LISTEN_PORT<br />Listen 8000</pre><br />and:<pre>#<br />ServerName <WeblogicServer1>:8000</pre> | JDE CNC, WebLogic administrator |

### Configure the Application Load Balancer
<a name="configure-the-application-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a target group. | 1. Create a target group for the HTTP server port 8000.<br />2. Register the targets under the target group with the same port.<br />3. Check the status of the targets to confirm that they are healthy.<br />4. Configure the health check settings as necessary.For detailed instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html). | AWS administrator |
| Set up the load balancer. | 1. Create an Application Load Balancer with default attributes and the required virtual private cloud (VPC), security groups, and subnets. For instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html).<br />2. Add a listener entry for HTTPS 443 and forward it to the target group that you created in the previous step. (For instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-listener.html).) An HTTPS listener requires an SSL certificate. You can choose a certificate from ACM or upload one.<br />3. For both listeners, enable stickiness by following the instructions in the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#sticky-sessions). | AWS administrator |
| Add a Route 53 (DNS) record. | (Optional) You can add an Amazon Route 53 DNS record for the subdomain. This record would point to your Application Load Balancer. For instructions, see the [Route 53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html). | AWS administrator |

## Troubleshooting
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| HTTP server doesn’t appear. | If **HTTP Server** doesn’t appear in the **Target Navigation** list on the Enterprise Manager console, follow these steps:1. Under **WebLogic Domain**, **Administration**, choose **OHS Instances**.<br />2. Choose **Create** to create a new OHS instance.<br />3. Provide an instance name, and then choose **OK** to create the instance.<br />When the instance has been created and changes have been activated, you will be able to see the HTTP server in the **Target Navigation** panel. |

## Related resources
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-resources"></a>

**AWS documentation**
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+ [Working with public hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html)
+ [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html)

**Oracle documentation:**
+ [Overview of Oracle WebLogic Server Proxy Plug-In](https://docs.oracle.com/middleware/1221/webtier/develop-plugin/overview.htm#PLGWL391)
+ [Installing WebLogic Server using the Infrastructure Installer](https://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/wls/12c/12_2_1/02-01-004-InstallWLSInfrastructure/installweblogicinfrastructure.html)
+ [Installing and Configuring Oracle HTTP Server ](https://docs.oracle.com/middleware/1221/core/install-ohs/toc.htm)
