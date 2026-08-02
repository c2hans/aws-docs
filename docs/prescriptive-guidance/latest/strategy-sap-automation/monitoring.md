---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/monitoring.html
---

# Example: Monitoring SAP clusters and services
<a name="monitoring"></a>

Another example of automation for SAP on AWS is monitoring SAP application clusters, SAP HANA clusters, and SAP application service. By automating monitoring, you can effectively monitor SAP NetWeaver and database cluster environments at a low cost, without the need to deploy or manage any servers or agents. The blog post [SAP application cluster, SAP HANA cluster and SAP application service monitoring](https://aws.amazon.com/blogs/awsforsap/sap-application-cluster-sap-hana-cluster-and-sap-application-service-monitoring/) describes the technique of using CloudWatch metrics and dashboards to monitor the SAP application clusters, HANA database clusters, and HANA replication and SAP application core services. The benefits of this AWS automation capability are:
+ Effective monitoring of SAP Advanced Business Application Programming (ABAP)-based environments
+ No need to deploy and manage servers or agents
+ Single administrative dashboard for accessing SAP and AWS service metrics
+ Low costs and no additional licensing fees

The following image and process describe how you set up this automation to monitor SAP databases and allow users to access current data and metrics:

1. Using the SAP Java Connector (SAP JCo) development library, a Lambda function establishes a connection with the SAP system.

1. The Lambda function uses the SAP Remote Function Call (RFC) protocol to fetch data from the SAP database.

1. The Lambda function fetches SAP credentials that are securely stored in AWS Secrets Manager and uses them to log in to the SAP system.

1. Lambda publishes the SAP data to CloudWatch as custom metrics. Because of the rule, Lambda performs this action every 60 seconds.

1. The user can access SAP applications, data, and metrics through a custom CloudWatch dashboard.

![Architecture diagram showing the automation of monitoring SAP databases.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-automation/images/guide-img/029e7e61-9fe5-41b5-83f4-177d03384b91/images/c272e96e-e588-4196-9643-5bce440cd6b5.png)
