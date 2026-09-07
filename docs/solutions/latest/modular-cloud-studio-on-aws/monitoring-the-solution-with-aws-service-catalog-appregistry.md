---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/monitoring-the-solution-with-aws-service-catalog-appregistry.html
---

# Monitoring the solution with AWS Service catalog appregistry
<a name="monitoring-the-solution-with-aws-service-catalog-appregistry"></a>

The solution includes a Service Catalog AppRegistry resource to register the CloudFormation template and underlying resources as an application in both Service Catalog AppRegistry and Application Manager.

Application Manager gives you an application-level view into this solution and its resources so that you can:
+ Monitor its resources, costs for the deployed resources across stacks and AWS accounts, and logs associated with this solution from a central location.
+ View operations data for the solution’s AWS resources (such as deployment status, Amazon CloudWatch alarms, resource configurations, and operational issues) in the context of an application.

The following figure depicts an example of the application view for this solution stack in Application Manager.

![mcs stack in application manager](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/mcs-stack-in-application-manager.png)

**Note**
You must activate CloudWatch Application Insights, AWS Cost Explorer, and cost allocation tags associated with this solution. They are not activated by default.

The following logs are captured and stored in this solution:
+ Application logs
+ Access Logs
+ Audit Logs
+ Default metrics

Most logs are stored with a 10-year retention period under these prefix patterns:
+ /aws/vendedlogs/lambda/modular-cloud-studio-on-aws/deployment-id/…​
+ /aws/vendedlogs/states/modular-cloud-studio-on-aws/deployment-id/…​
+ /modular-cloud-studio-on-aws/deployment-id/…​

Exception: The following logs could not be altered and have a "Never Expire" retention setting that cannot be modified:
+ Image Builder logs: /aws/imagebuilder…​
+ Cross-Region AWS SDK logs: /aws/lambda/StackSet-SC-AccountId-CrossRegionAwsSdk…​
+ API Gateway execution logs: API-Gateway-Execution-Logs\_…​/prod
