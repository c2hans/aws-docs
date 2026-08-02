---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-decomposition/faq-access.html
---

# FAQs about controlling database access
<a name="faq-access"></a>

Controlling database access by using the database wrapper service pattern is discussed in the [Controlling database access during decomposition](access.md) section of this guide. This FAQ section addresses common concerns and questions about introducing a database wrapper service, including its potential impact on performance, handling of existing stored procedures, managing complex transactions, and overseeing schema changes.

## Won't the wrapper service become a new bottleneck?
<a name="wont-the-wrapper-service-become-a-new-bottleneck"></a>

While the database wrapper service does add an extra network hop, the impact is usually minimal. You can scale the service horizontally, and the benefits of controlled access typically outweigh the small performance cost. Consider it a temporary trade-off between performance and maintainability.

## What happens to existing stored procedures?
<a name="what-happens-to-existing-stored-procedures"></a>

Initially, the database wrapper service can expose stored procedures as service methods. Over time, you can gradually move the logic into the application layer, which improves testing and version control. Migrate the business logic incrementally to minimize risk.

## How do I manage schema changes during the transition?
<a name="how-do-i-manage-schema-changes-during-the-transition"></a>

Centralize schema change control through the wrapper service team. This team is responsible for maintaining comprehensive visibility across all consumers. This team reviews proposed changes for system-wide impact, coordinates with affected teams, and implements modifications by using a controlled deployment process. For instance, when adding new fields, this team should maintain backward compatibility by implementing default values or initially allowing nulls.

Establish a clear change management process that includes impact assessment, testing requirements, and rollback procedures. Use database versioning tools, and maintain clear documentation of all changes. This centralized approach prevents schema modifications from disrupting dependent services and maintains system stability.
