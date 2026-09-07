---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/run-time-policy-based-isolation-with-iam.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Run-time, policy-based isolation with IAM
<a name="run-time-policy-based-isolation-with-iam"></a>

 In the pooled environment, SaaS providers will typically turn to IAM to find a strategy to isolate their resources. However, as noted above, you’ll need to be creative with how you apply IAM to achieve isolation in a pooled model. Instead of inheriting the IAM scoping of your compute node, you’ll need to introduce your own code that will provide run-time enforcement of your pooled isolation model. The diagram in Figure 13 provides a conceptual view of this model.

![Diagram showing runtime acquired scoping.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/runtime-acquired-scoping.png)

In this diagram, you’ll see that we have a microservice that needs to access some downstream resources (databases, S3 buckets, etc.). This microservice was deployed in a pooled model, which means that it will be processing requests from multiple tenants. The job of this microservice is to ensure that, as it processes these requests, it will apply constraints that will prevent tenants from crossing a boundary to another tenant’s resources. In the diagram, you’ll see that our microservice reaches out to the isolation manager to acquire a scoping context that is used to control interactions with and resources that are accessed by the code running in this microservice.

 This conceptual model provides some view of the moving parts. However, to see this in action, we need to look at a more concrete strategy that explain how this context is express and applied. The diagram in Figure 14 provides a more in-depth look at how IAM can be used as part of this run-time scoping of access to tenant resources.

 Here you’ll see the full lifecycle of configuring and applying policies in a run-time model. In the first step of this process, the tenant onboards to your system. During this process, they setup the user for our tenant as well as the IAM policies for that tenant (steps 2 and 3). Once the tenant has onboarded, we then hit the microservice of our application (step 4). Because this microservice is running in a pooled model, it has been deployed with a broad IAM scope that enables it to access resources for all tenants. Our job, then, is to look at each request that is sent to this service and narrow the scope of that request based to a single tenant. We do that by asking the isolation manager for a set of credentials that are specific to the current tenant (step 5). This isolation manager will look-up the IAM policies for the tenant (step 6) and generate a tenant scoped set of credentials that are returned back to the calling microservice. Finally, this microservice uses these credentials to access a database (step 7). With these new tenant-scoped credential, the code of the microservice will be prevented from accessing the resources of another tenant.

![Diagram showing scoping with IAM policies.](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/scoping-with-iam-policies.png)

 In this model, we’re essentially saying that our microservice will have this tenant context applied each time it attempts to access another resource. This scoping is applied as a matter of an agreed upon convention where the microservice is expected to always acquire new credentials before accessing a tenant resource.
