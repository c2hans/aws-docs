---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-asp-net-web-forms/ha-scaling.html
---

# HA and automatic scaling for ASP.NET Web Forms applications on AWS
<a name="ha-scaling"></a>

When you migrate your legacy ASP.NET Web Forms applications to AWS, achieving high availability is a critical consideration. You can use Amazon EC2 Auto Scaling groups and load balancers to distribute traffic across multiple EC2 instances. However, many ASP.NET Web Forms applications rely heavily on session state, which makes them inherently stateful. By default, the server stores the generated session IDs in memory and sends the ID back to the client through a cookie. This approach becomes problematic when you try to run the same application across multiple EC2 instances, because each instance maintains its own session state, leading to inconsistent user experiences and potential data loss.

To address this challenge and ensure that your migrated ASP.NET Web Forms application can scale seamlessly across multiple instances while maintaining session state, you have two main options: enabling sticky sessions or using shared backing storage.

## Enable sticky sessions for the Application Load Balancer
<a name="sticky-sessions"></a>

On AWS, you can configure Application Load Balancers to use [sticky sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#sticky-sessions), also known as *session affinity*. When you enable sticky sessions, the Application Load Balancer routes subsequent requests from the same client to the same EC2 instance. This ensures that the user's session state is preserved throughout their interactions with the application.

This approach provides a straightforward solution but has limitations in terms of scalability and fault tolerance. If an EC2 instance fails or becomes unavailable, the sticky session is broken, and the user's session state is lost. Additionally, sticky sessions might lead to uneven load distribution across instances and potentially cause resource contention or under-utilization, which limits the application's ability to scale effectively. For these reasons, we recommend that you use a shared backing store for session storage instead.

## Use a shared backing store for session storage
<a name="backing-store"></a>

The recommended approach for migrating stateful ASP.NET Web Forms applications to AWS is to use a shared backing store for session storage. Instead of relying on in-memory session state on individual EC2 instances, the application can store session data in a highly available and scalable storage solution, such as [Amazon DynamoDB](https://github.com/aws/aws-dotnet-session-provider/), [Amazon Relational Database Service (Amazon RDS) for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html), or [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/blogs/developer/elasticache-as-an-asp-net-session-store/).

When you use a shared backing store, you decouple session state from individual EC2 instances so the application can seamlessly scale across multiple instances without losing session data. This approach also improves fault tolerance, because session data persists independently from the application instances, which ensures that user sessions aren't lost even if the instance fails or during scaling events.

To configure your ASP.NET Web Forms application to use Redis as a shared backing store for session storage:

1. Create a new security group for the cluster. The security group must allow inbound requests to Redis, which uses TCP port 6379.

1. Launch a new Redis cluster. Make sure that you specify the security group you created in the first step.

1. Get the endpoint address of the instance you just created. You must wait a few minutes for the cluster to launch before the address becomes available.

1. Modify the `web.config` file and add the following configuration:

   ```
   <sessionState mode="Custom" customProvider="RedisStateStore">
    <providers>
       <add name="RedisStateStore" type="Microsoft.Web.Redis.RedisSessionStateProvider"
            host="[YourRedisClusterEndpoint]"
            accessKey=""
            ssl="true" />
    </providers>
   </sessionState>
   ```

   Replace `[YourRedisClusterEndpoint]` with the appropriate value for your ElastiCache (Redis OSS) cluster.

By implementing a shared backing store for session storage, you can provide your migrated ASP.NET Web Forms application with high availability, scalability, and fault tolerance on AWS. This approach aligns with cloud-native best practices and ensures a seamless user experience, even when your application scales across multiple EC2 instances or Availability Zones. Additionally, it provides a more robust and reliable solution than sticky sessions, and enables your application to take full advantage of the scalability and resilience offered by AWS infrastructure.
