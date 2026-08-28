---
source_url: https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-limitations.html
---

# Limitations for zero-ETL integration in Oracle Database@AWS
<a name="zero-etl-limitations"></a>

Note the following general limitations:

**Single PDB per integration**
Each zero-ETL integration can only replicate data from one pluggable database (PDB). Data filters like `include: pdb1.*.*, include: pdb2.*.*` aren't supported.

**Single integration per Autonomous Database or Exadata Infrastructure**
Each zero-ETL integration can only replicate data from one Autonomous Database on Dedicated Infrastructure.

**Fixed SSL port**
SSL connections must use port 2484.

**Same Region requirement**
The source Oracle Database@AWS VM cluster and target Amazon Amazon Redshift cluster must be in the same AWS Region. Cross-region replication isn't supported.

**No mTLS support**
Mutual TLS (mTLS) isn't supported. If your OCI database has mTLS enabled, you must disable it to use zero-ETL integration.

**Immutable integration settings**
After you create the secret ARN or KMS key associated with an integration, you can't modify it. You must delete and re-create the integration to change these settings.

**TDE column-level encryption**
Column-level Transparent Data Encryption (TDE) isn't supported for Oracle Exadata databases. Only tablespace-level TDE is supported.

**Data type support**
Some Oracle-specific data types might not be fully supported or might require transformation during replication. Test your specific data types thoroughly before you deploy your database to production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database at AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
