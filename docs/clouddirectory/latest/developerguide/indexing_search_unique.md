---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/indexing_search_unique.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Unique vs Nonunique Indexes
<a name="indexing_search_unique"></a>

Unique indexes differ from nonunique indexes in enforcing uniqueness of the indexed attribute values for objects that are attached to the index. For example, you might want to populate Person objects into two indexes, a unique one on an “email” attribute, and a nonunique one on a “lastname” attribute. The lastname index allows many Person objects with the same last name to be attached. On the other hand, the `AttachToIndex` call that targets the email index returns a `LinkNameAlreadyInUseException` error if a Person with the same email attribute is already attached. Note that the error does not remove the Person object itself. Consequently, an application might create the Person, attach it to the hierarchy, and attach it to indexes, all in a single batch request. This ensures that if uniqueness is violated on any of the indexes, the object and all of its attachments are rolled back automatically.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
