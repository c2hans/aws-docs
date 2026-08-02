---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/rls.html
---

# Row-level security recommendations
<a name="rls"></a>

Row-level security (RLS) is required to maintain tenant data isolation in a pooled model with PostgreSQL. RLS centralizes the enforcement of isolation policies at the database level and removes the burden of maintaining this isolation from software developers. The most common way to implement RLS is to enable this feature in the PostgreSQL DBMS. RLS involves filtering access to rows of data based on a value in a specified column. You can use two methods to filter access to data:
+ A specified column of data in a table is compared to the value of the current PostgreSQL user. Values in the column that are equivalent to the logged-in PostgreSQL user are accessible to that user.
+ A specified column of data in a table is compared to the value of a runtime variable set by the application. Values in the column that are equivalent to the runtime variable are accessible during that session.

The second option is preferred*, *because the first option requires the creation of a new PostgreSQL user for each tenant. Instead, a SaaS application that uses PostgreSQL should be responsible for setting a tenant-specific context at runtime when it queries PostgreSQL. This will have the effect of enforcing RLS. You can also enable RLS on a table-by-table basis. As a best practice, you should enable RLS on all tables that contain tenant data.

The following example creates two tables and enables RLS. This example compares a column of data to the value of the runtime variable app.current\_tenant.

```
-- Create a table for our tenants with indexes on the primary key and the tenant's name
CREATE TABLE tenant (
    tenant_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    status VARCHAR(64) CHECK (status IN ('active', 'suspended', 'disabled')),
    tier VARCHAR(64) CHECK (tier IN ('gold', 'silver', 'bronze'))
);

-- Create a table for users of a tenant
CREATE TABLE tenant_user (
    user_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenant (tenant_id) ON DELETE RESTRICT,
    email VARCHAR(255) NOT NULL UNIQUE,
    given_name VARCHAR(255) NOT NULL CHECK (given_name <> ''),
    family_name VARCHAR(255) NOT NULL CHECK (family_name <> '')
);

-- Turn on RLS
ALTER TABLE tenant ENABLE ROW LEVEL SECURITY;

-- Restrict read and write actions so tenants can only see their rows
-- Cast the UUID value in tenant_id to match the type current_setting
-- This policy implies a WITH CHECK that matches the USING clause
CREATE POLICY tenant_isolation_policy ON tenant
USING (tenant_id = current_setting('app.current_tenant')::UUID);

-- And do the same for the tenant users
ALTER TABLE tenant_user ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_user_isolation_policy ON tenant_user
USING (tenant_id = current_setting('app.current_tenant')::UUID);
```

For more information, see the blog post [Multi-tenant data isolation with PostgreSQL Row Level Security](https://aws.amazon.com/blogs/database/multi-tenant-data-isolation-with-postgresql-row-level-security/). The AWS SaaS Factory team also [has some examples in GitHub](https://github.com/aws-samples/aws-saas-factory-postgresql-rls) to assist in implementing RLS.
