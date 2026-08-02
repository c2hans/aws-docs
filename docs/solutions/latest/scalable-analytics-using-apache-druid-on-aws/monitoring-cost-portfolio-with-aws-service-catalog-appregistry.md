---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/monitoring-cost-portfolio-with-aws-service-catalog-appregistry.html
---

# Monitoring cost and portfolio with Service Catalog AppRegistry
<a name="monitoring-cost-portfolio-with-aws-service-catalog-appregistry"></a>

This guidance includes a Service Catalog AppRegistry resource to register the CloudFormation template and underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html).

AWS Systems Manager Application Manager gives you an application-level view into this guidance and its resources so that you can:
+ Monitor its resources, costs for the deployed resources across stacks and AWS accounts, and logs associated with this guidance from a central location.
+ View operations data for the resources of this guidance (such as deployment status, CloudWatch alarms, resource configurations, and operational issues) in the context of an application.

  The following figure depicts an example of the application view for the guidance stack in Application Manager.

 **Depicts an AWS guidance stack in Application Manager**

![appregistry1](http://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/appregistry1.png)
