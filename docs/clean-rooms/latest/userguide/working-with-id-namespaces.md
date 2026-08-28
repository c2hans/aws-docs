---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/working-with-id-namespaces.html
---

# ID namespaces in AWS Clean Rooms
<a name="working-with-id-namespaces"></a>

An *ID namespace* is a wrapper around your identity table that enables you to provide metadata explaining your dataset and how to use it in an ID mapping workflow. An *ID mapping workflow* is a data processing job that maps data from an input data source to an input data target based on the specified ID mapping method. It produces an ID mapping table.

There are two types of ID namespaces: **Source** and **Target**. The **Source** contains configurations for the source data that will be processed in an ID mapping workflow. The **Target** contains a configuration of the target data which all sources will resolve to. To deﬁne the input data that you want to resolve across two AWS accounts, create an ID namespace source and an ID namespace target to translate your data from one set (**Source**) to another (**Target**).

You can either create a new ID namespace or you can associate an existing one. For more information about how to create an ID namespace in AWS Entity Resolution, see [Define input data using an ID namespace](https://docs.aws.amazon.com/entityresolution/latest/userguide/id-namespace.html) in the *AWS Entity Resolution User Guide*.

**Topics**
+ [Creating and associating a new ID namespace](create-new-id-namespace.md)
+ [Associating an existing ID namespace](associate-existing-id-namespace.md)
+ [Editing ID namespace associations](edit-id-namespace-association.md)
+ [Disassociating ID namespace associations](disassociate-id-namespace-association.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
