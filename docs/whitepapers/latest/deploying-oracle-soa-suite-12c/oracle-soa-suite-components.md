---
source_url: https://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/oracle-soa-suite-components.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle SOA Suite components
<a name="oracle-soa-suite-components"></a>

 Oracle SOA Suite 12c is deployed on [Oracle WebLogic Server](https://www.oracle.com/java/weblogic/) and includes the following major components:
+  [Oracle SOA](https://docs.oracle.com/cd/E28280_01/doc.1111/e10223/index.htm)
+  [Oracle Service Bus](https://www.oracle.com/middleware/technologies/service-bus.html) (OSB)
+  [Oracle Business Process Management](https://www.oracle.com/middleware/technologies/bpm.html) (Oracle BPM)
+  [Oracle Business Activity Monitoring](https://www.oracle.com/middleware/technologies/business-activity-monitoring.html) (Oracle BAM)
+  [Oracle Application Development Framework](https://www.oracle.com/database/technologies/developer-tools/adf/) (Oracle ADF)

 The following diagram shows these components of Oracle SOA Suite when deployed on an Oracle WebLogic Server.

![A diagram depicting Oracle SOA Suite components deployed on Oracle WebLogic Server.](http://docs.aws.amazon.com/whitepapers/latest/deploying-oracle-soa-suite-12c/images/soa-components.jpeg)

 Each WebLogic Server deployment has a WebLogic domain, which typically contains multiple WebLogic Server instances (Managed Servers). A WebLogic domain is the basic unit of administration for WebLogic Server instances: it is a group of logically- related WebLogic Server resources. For example, you can have one WebLogic domain for each component of Oracle SOA Suite.

 WebLogic Server instances can run on physical or virtual servers (such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) or in containers. You can create a group of multiple WebLogic Managed Servers, known as a WebLogic Server Cluster. WebLogic Server Clusters support load balancing and failover and are required for high availability and scalability of your production deployments. You should deploy your WebLogic Server Cluster across multiple WebLogic Server Machines (Amazon EC2 instances) so that the loss of a single WebLogic Server Machine does not affect the availability of your application.

 There are two types of WebLogic Server instances in a domain: a single Administration Server, and one or more Managed Servers. Each WebLogic Server instance runs its own Java Virtual Machine (JVM) and can be configured individually. You deploy and run the components of Oracle SOA Suite on the Managed Server instances in a WebLogic Server Cluster. The Administration Server is used to configure, manage, and monitor the resources in the domain, including the Managed Server instances.
