---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/scaling-and-managing-pool-isolation-policies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scaling and managing pool isolation policies
<a name="scaling-and-managing-pool-isolation-policies"></a>

 While IAM policies provide powerful isolation constructs, they can also present SaaS providers with scaling challenges. If your system has a large number of tenants with a large population of policies, you may find that you will exceed the limits of the IAM service. You may also find it difficult to manage these polices as the number of tenants and the complexity of these policies grow. In these situations, some SaaS companies will attempt to alternate approach to how they generate and manage their IAM policies at run-time.

 One approach to this challenge is to shift to a model where your IAM policies are generated in at run-time. The idea here is to have your system implement a mechanism that will examine the current context of a call and generate the required IAM policy on-the-fly. This moves the policies out of IAM (since they are transient) and enables you to address potential limits on the number of policies that are needed to support all of your tenants. The diagram in Figure 15 provides an overview of this dynamic policy generation mechanism.

![Diagram showing dynamic policy generation using a token vending machine and token generator.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/dynamic-policy-generation.jpg)

 In this flow, you’ll see that we start with the same isolation manager that we used in our prior example. However, instead of going directly the IAM to retrieve the policies need to scope access, we have a series of steps that are used to generate a policy. The isolation manager first makes a request to the token vending machine to get a tenant scoped token (step 1). It’s the job of the vending machine to go to the templates that you have pre-defined for your tenant isolation model (step 2). Think of these as template files that have all of the moving parts of a traditional IAM policy. However, key elements of the file are not filled in (those that represent our tenant context). You might, for example, fill in a table name or the leading key condition of an Amazon DynamoDB table with a tenant identifier.

 Once you have the template that’s needed, you now call out to the token generator to request a token (step 3). In this step, we also provide the current tenant context. The token generator then fills the tenant details into the template, leaving us with a fully hydrated IAM policy (steps 4 and 5). Finally, the token generator uses this policy to generate a token that is scoped according to the provided policy. This token is returned back to the isolation manager (steps 6 and 7). Now, this token can be used to access resources with the tenant context applied.

 By moving these policies into templates, you take on the added responsibility of assuring that these policies enforce your tenant isolation requirements. Ideally, the details of this mechanism will be mostly outside the view of developers so the potential for something to go wrong is reduced.

 One upside here is the management profile of this model. Should you choose to change something about your isolation policies, the path to applying these changes will be much more straightforward since there won’t be a separate policy for each tenant. That, and you’ll own the content lifecycle of these policy templates (versioning and deploying them through your own pipeline).
