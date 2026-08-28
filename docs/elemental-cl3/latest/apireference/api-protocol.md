---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/api-protocol.html
---

# The API Protocol
<a name="api-protocol"></a>

The Conductor Live API can be accessed using HTTP or HTTPS. The API follows the REST architectural framework. In accordance with REST guidelines, the API exposes four types of operations based on the requesting HTTP(S) method:
+ POST
+ GET
+ PUT
+ DELETE

## Entities, Attributes, Elements, Properties, Parameters
<a name="entities-attributes-elements-properties-parameters"></a>

The entities that the Conductor Live API works with are:
+ Redundancy groups
+ Channels
+ Nodes
+ Profiles
+ Schedules
+ MPTS outputs
+ MPTS members (SPTS programs)
+ Routers

These entities have attributes in Conductor Live . In the API, these attributes are passed in the XML body of the request or response. They are passed as either:
+ XML elements (if they are read-write), or
+ Properties of an XML element (if they are read-only).

API requests may have parameters, which are presented in angle brackets. For example, <ID of redundancy group> is a parameter in this POST request:

`/redundancy_groups/<ID of redundancy group>/members`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
