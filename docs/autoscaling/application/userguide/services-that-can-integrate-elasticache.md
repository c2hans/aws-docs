---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/services-that-can-integrate-elasticache.html
---

# ElastiCache and Application Auto Scaling
<a name="services-that-can-integrate-elasticache"></a>

You can horizontally scale Amazon ElastiCache replication groups (Redis OSS and Valkey) and Memcached self-designed clusters using target tracking scaling policies and scheduled scaling.

To integrate ElastiCache with Application Auto Scaling, use the following information.

## Service-linked role created for ElastiCache
<a name="integrate-service-linked-role-elasticache"></a>

The following service-linked role is automatically created in your AWS account when registering ElastiCache resources as scalable targets with Application Auto Scaling. This role allows Application Auto Scaling to perform supported operations within your account. For more information, see [Service-linked roles for Application Auto Scaling](application-auto-scaling-service-linked-roles.md).
+ `AWSServiceRoleForApplicationAutoScaling_ElastiCacheRG`

## Service principal used by the service-linked role
<a name="integrate-service-principal-elasticache"></a>

The service-linked role in the previous section can be assumed only by the service principal authorized by the trust relationships defined for the role. The service-linked role used by Application Auto Scaling grants access to the following service principal:
+ `elasticache.application-autoscaling.amazonaws.com`

## Registering ElastiCache resources as scalable targets with Application Auto Scaling
<a name="integrate-register-elasticache"></a>

Application Auto Scaling requires a scalable target before you can create scaling policies or scheduled actions for an ElastiCache replication group, cluster, or node. A scalable target is a resource that Application Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the combination of resource ID, scalable dimension, and namespace.

If you configure auto scaling using the ElastiCache console, then ElastiCache automatically registers a scalable target for you.

If you want to configure auto scaling using the AWS CLI or one of the AWS SDKs, you can use the following options:
+ AWS CLI:

  Call the [register-scalable-target](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/register-scalable-target.html) command for an ElastiCache replication group. The following example registers the desired number of node groups for a replication group called `mycluster1`, with a minimum capacity of one and a maximum capacity of five.

  ```
  aws application-autoscaling register-scalable-target \
     --service-namespace elasticache \
     --scalable-dimension elasticache:replication-group:NodeGroups \
     --resource-id replication-group/{{mycluster1}} \
     --min-capacity {{1}} \
     --max-capacity {{5}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/1234abcd56ab78cd901ef1234567890ab123"
  }
  ```

  The following example registers the desired number of replicas per node group for a replication group called `mycluster2`, with a minimum capacity of one and a maximum capacity of five.

  ```
  aws application-autoscaling register-scalable-target \
     --service-namespace elasticache \
     --scalable-dimension elasticache:replication-group:Replicas \
     --resource-id replication-group/{{mycluster2}} \
     --min-capacity {{1}} \
     --max-capacity {{5}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/234abcd56ab78cd901ef1234567890ab1234"
  }
  ```

  The following example registers the desired number of nodes for a cluster called `mynode1`, with a minimum capacity of 20 and a maximum capacity of 50.

  ```
  aws application-autoscaling register-scalable-target \
     --service-namespace elasticache \
     --scalable-dimension elasticache:cache-cluster:Nodes \
     --resource-id cache-cluster/{{mynode1}} \
     --min-capacity {{20}} \
     --max-capacity {{50}}
  ```

  If successful, this command returns the ARN of the scalable target.

  ```
  {
      "ScalableTargetARN": "arn:aws:application-autoscaling:{{region}}:{{account-id}}:scalable-target/01234abcd56ab78cd901ef1234567890ab12"
  }
  ```
+ AWS SDK:

  Call the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) operation and provide `ResourceId`, `ScalableDimension`, `ServiceNamespace`, `MinCapacity`, and `MaxCapacity` as parameters.

## Related resources
<a name="elasticache-related-resources"></a>

For more information, see [Auto Scaling Valkey and Redis OSS clusters](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoScaling.html) and [Scaling clusters for Memcached](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling-self-designed.mem-heading.html) in the *Amazon ElastiCache User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
