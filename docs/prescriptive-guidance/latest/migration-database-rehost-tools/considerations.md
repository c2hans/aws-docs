---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/considerations.html
---

# Migration waves, servers, and databases
<a name="considerations"></a>

Migration projects start with the following list of open questions, which are common across the three scenarios described in the previous section:
+ How can we build migration waves?
+ How can we group servers inside each wave?
+ Should database servers be migrated before application servers or with them?
+ Which tool should we use for database migrations?

However, to address these questions, we need to clarify some definitions first. This section of the guide focuses on the term *database* and what it means in the context of migration waves. This definition is important, because the understanding of that term could change the overall migration approach for particular migration waves or even change migration waves by shifting servers between different waves.

Does the term *database* describe a server that runs the DBMS software or the logical database entry point? Does it refer to one database out of several on the same server or a cluster of servers? Depending on the context, a database could refer to either option. Database administrators (DBAs) usually consider logical databases, not physical servers. However, in the context of migration, especially large-scale, lift-and-shift migrations, a database usually corresponds to a physical server or a cluster of servers.

The migration of a database must be aligned and associated with the application it works with, because the logical database is always a part of the application and its dependencies. However, the physical location of that logical database could vary. For example, it could be located on:
+ A standalone physical server, without any other databases present.
+ A standalone physical server colocated with other logical databases.
+ A cluster of physical servers, either as a single logical database or as part of a larger set of databases that serve other applications.

Forming the dependency mapping for migration waves is complicated if there's no clear one-to-one dependency between the application and the database servers, especially when multiple logical databases from different applications are colocated on the same physical server. Such database systems require a [replatforming](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html#replatform) approach that involves a decomposition or consolidation of databases, which complicates large-scale lift-and-shift migration efforts.

This is where database migration tools (such as native tools from the database engine's vendors or third parties) can help. These tools work on a logical database level instead of the block-level replication approach of AWS Transform MGN, and can move the data or databases on a logical level between physical servers and locations. These native database migration tools can help you consolidate logical databases on a single physical server. They can also do the opposite: They can decompose logical databases between various physical database servers, to align them with different applications and spread them across different migration waves.
