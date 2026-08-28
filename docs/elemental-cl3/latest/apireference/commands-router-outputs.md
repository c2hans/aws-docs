---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-router-outputs.html
---

# Router Outputs
<a name="commands-router-outputs"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST Router Output | POST | /routers/<ID of router>/outputs | Create a new output for the specified router. |
| PUT Router Output | PUT | /routers/<ID of router>/outputs/<ID of output> | Modify the attributes of the specified output on the specified router. |
| GET Router Output List | GET | /routers/<ID of router>/outputs | Get the list of outputs for the specified router. |
| GET Router Output | GET | /routers/<ID of router>/outputs/<ID of output> | Get the attributes of the specified output on the specified router. |
| DELETE Router Output | DELETE | /routers/<ID of router>/outputs/<ID of output> | Delete the specified output on the specified router |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
