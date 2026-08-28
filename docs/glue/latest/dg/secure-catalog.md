---
source_url: https://docs.aws.amazon.com/glue/latest/dg/secure-catalog.html
---

# Securing your Data Catalog using Lake Formation
<a name="secure-catalog"></a>

 AWS Lake Formation is a service that makes it easier to set up a secure data lake in AWS. It provides a central place to create and securely manage your data lakes by defining fine-granied access control permissions. Lake Formation uses the Data Catalog to store and retrieve metadata about your data lake, such as table definitions, schema information, and data access control settings.

You can register your Amazon S3 data location of the metadata table or database with Lake Formation and use it to define metadata-level permissions on the Data Catalog resources. You can also use Lake Formation to manage storage access permissions on the underlying data stored in Amazon S3 on behalf of integrated analytical engines.

For more information see [What is AWS Lake Formation?](lake-formation/latest/dg/what-is-lake-formation.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
