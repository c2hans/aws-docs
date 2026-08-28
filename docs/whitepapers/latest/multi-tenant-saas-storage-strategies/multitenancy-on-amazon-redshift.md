---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multitenancy-on-amazon-redshift.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Multitenancy on Amazon Redshift
<a name="multitenancy-on-amazon-redshift"></a>

 Amazon Redshift introduces additional twists to factor into your multitenant thinking. Amazon Redshift focuses on building high-performance clusters to house large-scale data warehouses. Amazon Redshift also places some [limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) on the constructs that you can create within each cluster.

 You can imagine how these limits influence the scale and performance that is delivered to Amazon Redshift. You can also see how these limits can impact your approach to multitenancy with Amazon Redshift. If you are targeting a modest tenant count, these limits might have little influence on your solution. However, if you’re targeting a large number of tenants, you’d need to factor these limits into your overall strategy.

 The following sections highlight the strategies that are commonly used to realize each multitenant storage model on Amazon Redshift.

## Silo model
<a name="silo-model-3"></a>

 Achieving a true, silo model isolation of tenants on Amazon Redshift requires you to provision separate clusters for each tenant. Via clusters, you can create the well-defined boundary between tenants that is commonly required to assure customers that their data is successfully isolated from cross-tenant access. This approach best leverages the natural security mechanisms in Amazon RedShift, so you can control and restrict tenant access to a cluster using a combination of IAM policies and database privileges. IAM controls overall cluster management, and the database privileges are used to control access to data within the cluster.

 The silo model gives you the opportunity to create a tuned experience for each tenant. With Amazon Redshift, you can configure the number and type of nodes in your cluster, so that you can create environments that target the load profile of each individual tenant. You can also use this as a strategy for optimizing costs.

 The challenge of this model, as we’ve seen with other silo models, is that each tenant’s cluster must be provisioned as part of the onboarding process. Automating this process and absorbing the extra time and overhead associated with the provisioning process adds a layer of complexity to your deployment footprint. It also has some impact on the speed with which a new tenant can be allocated.

## Bridge model
<a name="bridge-model-3"></a>

 The bridge model does not have a natural mapping on Amazon Redshift. Technically, you could create separate schemas for each tenant. However, you would likely run into issues with the Amazon Redshift limit of 256 schemas. In environments with any significant number of tenants, this simply doesn’t scale. Security is also a challenge for Amazon Redshift in the bridge model. When you are authorized as a user of an Amazon Redshift cluster, you are granted access to all the databases within that cluster. This pushes the responsibility for enforcing finer-grained access controls to your SaaS application.

 Given the motives for the bridge model and these technical considerations, it seems impractical for most SaaS providers to consider using this approach on Amazon Redshift. Even if the limits are manageable for your solution, the isolation profile is likely unacceptable to your customers. Ultimately, the best answer is to simply use the silo model for any tenant that requires isolation.

## Pool model
<a name="pool-model-3"></a>

 Building the pool model on Amazon Redshift looks very much like the other storage models we’ve discussed. The basic idea is to store data for all tenants in a single Amazon Redshift cluster with shared databases and tables. In this approach, the data for tenants is partitioned via the introduction of a column that represents a unique tenant identifier.

 This approach gives most of the goodness that we saw with the other pool models. Certainly the overall management, monitoring, and agility are improved by housing all of the tenant data in a single Amazon Redshift cluster.

 The limit on concurrent connections is the area that adds a degree of difficulty to implementing the pool model on Amazon Redshift. With an upper limit of 500 concurrent connections, many multitenant SaaS environments can quickly exceed this limit. This doesn’t eliminate the pool model from contention. Instead, it pushes more responsibility to the SaaS developer to put an effective strategy in place to manage how and when these connections are consumed and released.

 There are some common ways to address connection management. Developers often leverage client-based caching to limit their need for actual connections to Amazon Redshift. Connection pooling can also be applied in this model. Developers need to select a strategy that ensures that the data access patterns of their application can be met effectively without exceeding the Amazon Redshift connection limit.

 Adopting the pool model also means keeping your eye on the typical issues that come up any time you’re operating in a shared infrastructure. The security of your data, for example, requires some application-level policies to limit cross-tenant access. Also, you likely need to continually tune and refine the performance of your environment to prevent any one tenant from degrading the experience of others.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
