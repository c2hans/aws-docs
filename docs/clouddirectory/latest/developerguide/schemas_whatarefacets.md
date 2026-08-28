---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/schemas_whatarefacets.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Facets
<a name="schemas_whatarefacets"></a>

Facets are the most basic abstraction within a schema. They represent a set of attributes that can be associated with an object in the directory and are similar in concept to LDAP object classes. Each directory object may have up to a certain number of facets associated with it. For more information, see [Amazon Cloud Directory Limits](limits.md).

Each facet maintains its own independent set of attributes. Each facet consists of fundamental metadata, such as the facet name, version information, and behaviors. The combination of schema ARNs, facets, and attributes define uniqueness on the object.

The set of object facets, their constraints, and the relationships between them constitute an abstract schema definition. Schema facets are used to define constraints over the following things:

1. Attributes allowed in an object

1. Policy types allowed to apply to an object

Once you have added the necessary facets to your schema, you can apply the schema to your directory and create the applicable objects. For example, you can define a device schema by adding facets such as computers, phones, and tablets. You can then use these facets to create computer objects, phone objects, and tablet objects in the directory to which the schema applies.

Cloud Directory’s schema support makes it easy to add or modify facets and attributes without worrying about breaking applications. For more information, see [In-Place Schema Upgrade](schemas_inplaceschemaupgrade.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
