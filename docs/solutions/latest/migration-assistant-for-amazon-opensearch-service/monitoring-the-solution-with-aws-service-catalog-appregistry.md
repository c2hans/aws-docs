---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/monitoring-the-solution-with-aws-service-catalog-appregistry.html
---

# Monitor the solution with Service Catalog AppRegistry
<a name="monitoring-the-solution-with-aws-service-catalog-appregistry"></a>

The solution includes a Service Catalog AppRegistry resource to register the CloudFormation template and underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html).

AWS Systems Manager Application Manager gives you an application-level view into this solution and its resources so that you can:
+ Monitor its resources, costs for the deployed resources across stacks and AWS accounts, and logs associated with this solution from a central location.
+ View operations data for the solution’s AWS resources (such as deployment status, Amazon CloudWatch alarms, resource configurations, and operational issues).

 **Depicts Migration Assistant Traffic Replayer stack in Application Manager**

![image8](http://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/images/image8.png)
