---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/best-practices-for-managing-data-synchronization-and-schema-changes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Best Practices for Managing Data Synchronization and Schema Changes
<a name="best-practices-for-managing-data-synchronization-and-schema-changes"></a>

 The complexity of managing data synchronization across two distinct environments depends on the number of data stores in use, the intricacy of the data model, and the data consistency requirements.

 Both the blue and green environments need up-to-date data:
+  The green environment needs up-to-date data access because it’s becoming the new production environment.
+  The blue environment needs up-to-date data in the event of a rollback, when production is either shifts back or remains on the blue environment.

 Broadly, you accomplish this by having both the green and blue environments share the same data stores. Unstructured data stores, such as Amazon Simple Storage Service (Amazon S3) object storage, NoSQL databases, and shared file systems are often easier to share between the two environments. Structured data stores, such as relational database management systems (RDBMS), where the data schema can diverge between the environments, typically require additional considerations.

## Decoupling Schema Changes from Code Changes
<a name="decoupling-schema-changes-from-code-changes"></a>

 A general recommendation is to decouple schema changes from the code changes. This way, the relational database is outside of the environment boundary defined for the blue/green deployment and shared between the blue and green environments. The two approaches for performing the schema changes are often used in tandem:
+  The schema is changed first, before the blue/green code deployment. Database updates must be backward compatible, so the old version of the application can still interact with the data.
+  The schema is changed last, after the blue/green code deployment. Code changes in the new version of the application must be backward compatible with the old schema.

 Schema modifications in the first approach are often additive. You can add fields to tables, new entities, and relationships. If needed, you can use triggers or asynchronous processes to populate these new constructs with data based on data changes performed by the old application version.

 It's important to follow coding best practices when developing applications to ensure your application can tolerate the presence of additional fields in existing tables, even if they are not used. When table row values are read and mapped into source code structures (for example objects, and array hashes), your code should ignore fields it can’t map instead to avoid causing application runtime errors.

 Schema modifications in the second approach are often deletive. You can remove unneeded fields, entities, and relationships, or merge and consolidate them. After this removal, the earlier application version is no longer operational.

![Workflow showing schema additions before code deployment, then schema deletions after.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/code-deployment.png)

* Decoupled schema and code changes *

 There’s an increased risk involved when managing schema with a deletive approach: failures in the schema modification process can impact your production environment. Your additive changes can bring down the earlier application because of an undocumented issue where best practices weren’t followed or where the new application version still has a dependency on a deleted field somewhere in the code.

 To mitigate risk appropriately, this pattern places a heavy emphasis on your pre-deployment software lifecycle steps. Be sure to have a strong testing phase and framework and a strong QA phase. Performing the deployment in a test environment can help identify these sorts of issues early, before the push to production.
