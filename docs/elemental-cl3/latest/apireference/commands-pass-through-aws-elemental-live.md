---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-pass-through-aws-elemental-live.html
---

# Pass Through to AWS Elemental Live
<a name="commands-pass-through-aws-elemental-live"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Live action | POST |  http://<Conductor IP address>/channels/<ID of channel>/live\_events/<action> | Pass an AWS Elemental Live API event command to the Live node via the Conductor Live API. |
| GET System Status | GET | http://<Conductor IP address>/nodes/<ID of node>/system\_status | Get status information on an AWS Elemental Live node in the cluster. |
| GET Inputs | GET | http://<Conductor IP address> /channels/<ID of channel>/live\_events/inputs | Get the ID of an event input. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
