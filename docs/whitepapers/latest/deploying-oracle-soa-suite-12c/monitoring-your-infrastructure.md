---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/monitoring-your-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Monitoring your infrastructure
<a name="monitoring-your-infrastructure"></a>

 After you migrate your Oracle WebLogic applications to AWS, you can continue to use the monitoring tools you are familiar with to monitor your Oracle SOA Suite 12c environment.

 You can use [Oracle Enterprise Manager Fusion Middleware Control](https://docs.oracle.com/cloud/latest/soa121300/SOAAG/GUID-266118F3-8B14-4896-8081-A0A489FD0CEC.htm#SOAAG249), the Oracle WebLogic Server Administration Console, or the command line (using the WebLogic Scripting Tool (WLST) state command) to monitor your Oracle WebLogic Server infrastructure components. This includes WebLogic domains, Managed Servers, and clusters. You can also monitor the Java applications deployed and get information such as the state of your application, the number of active sessions, and response times. For more information about how to monitor Oracle WebLogic Server, refer to the [Oracle WebLogic Server documentation](https://docs.oracle.com/middleware/1212/wls/wls-monitortune.htm).

 You can also use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor AWS Cloud resources and the Oracle SOA Suite 12c components. Amazon CloudWatch enables you to monitor your AWS resources in near real-time, including Amazon EC2 instances, Amazon EBS volumes, Amazon EFS, ELB, and Amazon RDS instances. Metrics such as CPU utilization, latency, and request counts are provided automatically for these AWS resources. Amazon CloudWatch can also monitor your own logs or custom application and system metrics, such as memory usage, transaction volumes, or error rates.

 If your Oracle SOA Suite deployment uses a database deployed on Amazon RDS, you can use Amazon RDS [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) to monitor your database. Enhanced Monitoring gives you access to over 50 metrics, including CPU, memory, file system, and disk I/O. You can also view the processes running on the database instance and their related metrics, including percentage of CPU usage and memory usage. You can also set up custom metrics in Amazon CloudWatch and then set up alarms, dashboards, widgets, and more.
