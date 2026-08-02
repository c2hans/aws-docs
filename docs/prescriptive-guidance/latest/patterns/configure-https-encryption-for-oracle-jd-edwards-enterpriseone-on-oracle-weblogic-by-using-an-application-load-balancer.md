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
| Install and configure Oracle components. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html) | JDE CNC, WebLogic administrator |
| Enable the WebLogic plugin at the domain level. | The WebLogic plugin is required for load balancing. To enable the plugin:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html) | JDE CNC, WebLogic administrator |
| Edit the configuration file. | The `mod_wl_ohs.conf` file configures proxy requests from OHS to WebLogic.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html)<pre><VirtualHost *:8000><br /><Location /jde><br />WLSRequest On<br />SetHandler weblogic-handler<br />WebLogicHost localhost<br />WebLogicPort 8000<br />WLProxySSL On<br />WLProxySSLPassThrough On<br /></Location><br /></VirtualHost></pre> | JDE CNC, WebLogic administrator |
| Start OHS by using the Enterprise Manager. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html) | JDE CNC, WebLogic administrator |

### Configure the Application Load Balancer
<a name="configure-the-application-load-balancer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a target group. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html)For detailed instructions, see the [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html). | AWS administrator |
| Set up the load balancer. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html) | AWS administrator |
| Add a Route 53 (DNS) record. | (Optional) You can add an Amazon Route 53 DNS record for the subdomain. This record would point to your Application Load Balancer. For instructions, see the [Route 53 documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html). | AWS administrator |

## Troubleshooting
<a name="configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| HTTP server doesn’t appear. | If **HTTP Server** doesn’t appear in the **Target Navigation** list on the Enterprise Manager console, follow these steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-https-encryption-for-oracle-jd-edwards-enterpriseone-on-oracle-weblogic-by-using-an-application-load-balancer.html)<br />When the instance has been created and changes have been activated, you will be able to see the HTTP server in the **Target Navigation** panel. |

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
