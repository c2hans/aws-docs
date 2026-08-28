---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/entity-ids.html
---

# IDs of Entities
<a name="entity-ids"></a>

When an entity is created, it is automatically assigned an ID that is stored in the <id></id> element.

These unique IDs are typically shown on the Conductor Live web interface under the “ID” column.

## Obtaining an ID
<a name="obtain-an-id"></a>

The ID is shown in the POST response and can be obtained using GET List. To obtain an ID:
+ Obtain a list of IDs for an entity using a GET request.
+ Parse the response for the desired ID by looking for the ID that corresponds to a piece of data that you specified, such as the entity name.

The ID must be passed in any PUT, GET, and DELETE. In general, you cannot identify an entity using the name element.

## Multiple Identities
<a name="multiple-identities"></a>

Conductor systems and worker nodes within a cluster are assigned a node ID. Redundancy group membership assigns a redundancy member ID. It is important that you not conflate the node ID with the redundancy member ID; they are different IDs.

Any element that is a grouping of attributes is usually assigned a unique ID. The presence of this ID does not mean you can query this grouping by passing in this ID. You can only query the entities listed in [Entities, Attributes, Elements, Properties, Parameters](api-protocol.md#entities-attributes-elements-properties-parameters).

## Uniqueness of IDs
<a name="uniqueness-of-ids"></a>

Each type of entity has its own numbering scheme. For example, redundancy groups are numbered from 1 and channels are numbered separately, starting from 1.

Numbering increments indefinitely. If an entity is deleted, its number is *not *recycled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
