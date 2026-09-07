---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/bridge.html
---

# PostgreSQL bridge model
<a name="bridge"></a>

The PostgreSQL bridge model is a combination of the pooled and siloed approaches. Like the pooled model, you provision a single PostgreSQL instance for each tenant. To maintain tenant data isolation, you use PostgreSQL logical constructs. In the following diagram, PostgreSQL databases are used to logically separate data.

**Note**
    A PostgreSQL database doesn't refer to a separate Amazon RDS for PostgreSQL or Aurora PostgreSQL-Compatible DB instance. Instead, it refers to a logical construct of the PostgreSQL database management system to separate data.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/images/guide-img/df8a9c2c-aa88-448f-93ca-fcf7168e9781/images/65570929-2cef-4d98-a38c-ca2b71900557.png)

You can also implement the bridge model by using a single PostgreSQL database, with tenant-specific schemas in each database, as illustrated in the following diagram.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/images/guide-img/df8a9c2c-aa88-448f-93ca-fcf7168e9781/images/2d4e1ec5-eb37-4a28-8bd0-3037e467e3c9.png)

The bridge model suffers from the same noisy neighbor and tenant performance isolation concerns as the pool model. It also incurs some additional operational and provisioning overhead by requiring either separate databases or schemas to be provisioned on a per-tenant basis. It requires effective monitoring to respond quickly to tenant performance concerns. It also requires application instrumentation to monitor tenant-specific usage. Overall, the bridge model can be viewed as an alternative to RLS that slightly augments the tenant onboarding effort by requiring new PostgreSQL databases or schemas. As with the silo model, an application or a data access layer will have to maintain a mapping of tenants to their associated PostgreSQL databases or schemas.
