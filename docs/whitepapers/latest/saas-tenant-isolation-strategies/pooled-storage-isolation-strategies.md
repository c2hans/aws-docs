---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/pooled-storage-isolation-strategies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Pooled storage isolation strategies
<a name="pooled-storage-isolation-strategies"></a>

 Isolating data in a pooled model is an area that gets lots of attention from SaaS providers. As data is co-mingled, SaaS developers become hyper-focused on identifying ways to ensure that each tenant’s data is protected. In fact, while many SaaS providers are intrigued by the cost, management, and agility profiles of the pool model, they will often default to a silo model purely to address expected pushback they may get from customers that will may be hesitant to accept pooling of their data.

 The general notion of pool storage isolation (for any storage service) is that the data for all tenants is represented in a shared storage construct. The diagram in Figure 16 provides an illustration of pooled storage.

![Diagram showing pooled storage.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/pooled-storage.jpg)

Here you’ll see that we have a product microservice that is storing its data in a pooled model. The table has an index in the first column that represents the key for each tenant. All of the tenant product data resides in this one table.

 With this model, the challenge of isolating the data becomes much more complex. How do you create some virtual view of this table that is constrained to just those rows that belong to a given tenant? Also, how will this isolation be realized spanning each of the AWS storage services? The reality is, each service may require its own unique approach to implement isolation in the pooled model.

 To get a better sense of this variation, let’s start by looking at one example of how you might use IAM to implement pooled isolation with DynamoDB. As a fully managed storage service, DynamoDB offers you a rich collection of IAM mechanisms to control access to resources. This includes the ability to define a *leading key* condition in your IAM policy that can restrict access to the items in a DynamoDB table. The IAM policy shown in Figure 17 provides an example policy that demonstrates this approach to isolation.

 The key area to focus on in this policy is the condition. This condition indicates that, when this policy is applied, all attempts to access the DynamoDB table will be limited to items that have key that matches the value of this leading key. So, in this case, the tenant identifier would be in the leading key, constraining access to data for a given tenant.

![Screen capture showing an example IAM policy for DynamoDB isolation with leading keys.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/dynamodb-isolation-with-leading-keys.jpg)

 Now, if we look at employing this same isolation model to Amazon Aurora PostgreSQL, you’ll see that the mechanism is quite different. With Aurora PostgreSQL, you cannot use IAM to scope access to data at the row level. Instead, you’ll need to use the row level security (RLS) feature of PostgreSQL to isolate your tenant data. The diagram in Figure 18 provides a simple example of how you’d setup RLS for a product table in your system.

![Screen capture showing creating pooled isolation with PostgreSQL RLS.](http://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/images/pooled-isolation-with-postgresql-rls.jpg)

 The first step in configuring RLS is to alter your table to enable row level security for that table. Then, you’ll create an isolation policy for that that requires the tenant\_id column to match the value of the current user (which is supplied contextually). Now, with these changes in place, all interactions with this table will be restricted to the rows that are valid for the current tenant.

 In contrasting the DynamoDB and Aurora PostgreSQL approaches, you can see that you’ll need to do some exploration with each storage service that you are using to find a model that will let you achieve isolation. There are also cases where services may not offer a more granular isolation model. In these cases, you’ll have to introduce your own mechanisms to enforce your pool isolation policies.
