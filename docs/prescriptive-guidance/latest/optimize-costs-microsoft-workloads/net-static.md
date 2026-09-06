---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-static.html
---

# Support dynamic scaling for static .NET Framework apps
<a name="net-static"></a>

## Overview
<a name="net-static-overview"></a>

One of the key benefits of using the cloud for applications is elasticity, or the ability to scale compute in or out based on demand. This enables you to only pay for the compute capacity that you need, rather than provisioning for peak usage. Cyber Monday, in which online retailers can quickly get many times more traffic than normal (for example, [thousands of percent within minutes](https://aws.amazon.com/blogs/startups/how-clicktale-uses-aws-to-power-a-successful-cyber-monday/)), is a good example of elasticity.

If you're bringing legacy .NET web applications to the cloud (for example, ASP.NET Framework applications running on IIS), the ability to quickly scale load balanced server farms may be difficult or impossible due to the stateful nature of the application. User session data is stored within the memory of the application, usually with [ASP.NET session state](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178581(v=vs.100)) or static variables that hold cross-request data that must be persisted. User session affinity is usually maintained through load balancer sticky sessions.

This proves to be challenging operationally. When increased capacity is required, you must intentionally provision and add servers. This can be a slow process. Taking nodes out of service in the event of patching or for unexpected failures can be problematic for the end user experience, losing state for all users associated with affected nodes. At best, this would require users to log in again.

By centralizing session state for ASP.NET applications and applying autoscaling rules to legacy ASP.NET applications, you can take advantage of the elasticity of the cloud and potentially take advantage of cost savings when running applications. For example, you get cost reductions through compute scalability, but you also get to choose from different pricing models available, such as reducing [reserved instance usage](https://aws.amazon.com/ec2/pricing/reserved-instances/) and using [Amazon Spot Instance pricing](https://aws.amazon.com/ec2/spot/).

Two common techniques include using [Amazon DynamoDB as a session state provider](https://github.com/aws/aws-dotnet-session-provider) and using [Amazon ElastiCache (Redis OSS) as an ASP.NET session store](https://aws.amazon.com/blogs/developer/elasticache-as-an-asp-net-session-store/).

The following diagram shows an architecture that uses DynamoDB as a session state provider.

![DynamoDB as a session state provider](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/44eff032-9618-408c-97f6-37b2aa0e4c1a.png)

The following diagram shows an architecture that uses ElastiCache (Redis OSS) as a session state provider.

![ElastiCache for Redis as a session state provider](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/79040ef8-24fc-4e69-9b37-75054f536da0.png)

## Cost impact
<a name="net-static-cost"></a>

To determine the benefits of scaling for a production application, we recommend that you model your actual demand. This section makes the following assumptions to model a sample application:
+ Instances that are added and removed from rotation are identical and no instance size variation is introduced.
+ Server utilization never drops below two active servers in order to maintain high availability of the application.
+ The quantity of servers scales linearly with the traffic (that is, twice as much traffic will require twice as much compute).
+ Traffic is modeled over the course of a month in six hour increments, with intra-day variation and one abnormal peak of traffic (for example, a promotional sale) for one day of 10x traffic. Weekend traffic is modeled at base utilization.
+ Nighttime traffic is modeled at base utilization, while weekday traffic is modeled at 4x utilization.
+ Reserved Instance pricing uses one-year, no-upfront pricing. Normal daytime pricing uses on-demand pricing while burst demand uses Spot Instance pricing.

The following diagram illustrates how this model takes advantage of elasticity in a .NET application rather than provisioning for peak usage. This results in a savings of approximately 68 percent.

![Graph of Auto Scaling costs](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/e302f1ca-b323-4681-9f12-2d02f94a4b70.png)

If you use DynamoDB as a session state storage mechanism, then use the following parameters:

```
Storage: 20GB
Session Reads: 40 million
Session Writes: 20 million
Pricing Model: On demand
```

The estimated monthly cost for this service is approximately $35.00 per month.

If you use ElastiCache (Redis OSS) as a session state storage mechanism, then use the following parameters:

```
Number of Nodes: 3
Node size: cache.t4g.medium
Pricing Model: 1y reserved
```

The estimated monthly cost for this service is approximately $91.00 per month.

## Cost optimization recommendations
<a name="net-static-rec"></a>

The first step is to implement session state in a legacy .NET application. If you're using ElastiCache as your state storage mechanism, follow the guidance from [ElastiCache as an ASP.NET Session Store](https://aws.amazon.com/blogs/developer/elasticache-as-an-asp-net-session-store/) in the AWS Developer Tools Blog. If you're using DynamoDB, then follow the guidance from [What is the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/welcome.html) in the SDK for .NET documentation.

If the application uses the **InProc** session to begin with, make sure that all objects that you plan to store in the session can be serialized. To do this, use the `SerializableAttribute` attribute to decorate classes whose instances will be stored in the session. For example:

```
[Serializable()]
public class TestSimpleObject {
public string SessionProperty {get;set;}
}
```

Additionally, the .NET `MachineKey` must be the same between all the servers in use. This is normally the case when instances are created from a common Amazon Machine Image (AMI). For example:

```
<machineKey
validationKey="some long hashed value"
decryptionKey="another long hashed value"
validation="SHA1"/>
```

However, it's important to ensure that if a base image is changed, it's configured with the same .NET machine image (either configurable at the IIS or server level). For more information, see [SystemWebSectionGroup.MachineKey Property](https://learn.microsoft.com/en-us/dotnet/api/system.web.configuration.systemwebsectiongroup.machinekey?view=netframework-4.8.1) in the Microsoft documentation.

Finally, you must determine the mechanism for adding servers to an Auto Scaling group in response to a scaling event. There are several ways to accomplish this. We recommend the following methods to seamlessly deploy .NET Framework applications to an EC2 instance in an Auto Scaling group:
+ Use [EC2 Image Builder](https://aws.amazon.com/image-builder/) to configure an AMI that contains the fully configured server and application. You can then use this AMI to configure the [launch template of your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html).
+ Use [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) to deploy your application. CodeDeploy enables integration directly with [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html). This provides an alternative to creating a new AMI for each release of the application.

## Additional resources
<a name="net-static-resources"></a>
+ [Create images with EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-images.html) (EC2 Image Builder documentation)
+ [Deploying .NET Web Applications Using AWS CodeDeploy with Visual Studio Team Services](https://aws.amazon.com/blogs/developer/deploying-net-web-applications-using-aws-codedeploy-with-visual-studio-team-services/) (AWS Developer Tools Blog)
