---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-router-inputs.html
---

# Router Inputs
<a name="commands-router-inputs"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Router Input | POST | /routers/<ID of router>/inputs | Create a new input for the specified router. |
| PUT Router Input | PUT | /routers/<ID of router>/inputs/<ID of input> | Modify the attributes of the specified input on the specified router. |
| GET Router Input List | GET | /routers/<ID of router>/inputs | Get the list of inputs for the specified router. |
| GET Router Input | GET | /routers/<ID of router>/inputs/<ID of input> | Get the attributes of the specified input on the specified router. |
| DELETE Router Input | DELETE  | /routers/<ID of router>/inputs/<ID of input> | Delete the specified input on the specified router |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
