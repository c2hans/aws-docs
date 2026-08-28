---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-mpts.html
---

# MPTS
<a name="commands-mpts"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST MPTS | POST | /mpts | Create an MPTS output and optionally specify its Single-Protocol Transport Service (SPTS) programs. |
| PUT MPTS | PUT | /mpts/<ID of MPTS> | Change the attributes and/or SPTS programs of the specified MPTS output. |
| GET MPTS List | GET | /mpts | Get the list of MPTS outputs.  |
| GET MPTS  | GET | /mpts/<ID of MPTS> | Get the attributes and SPTS programs of one MPTS output. |
| DELETE MPTS | DELETE  | /mpts/<ID of MPTS> | Delete the specified MPTS output. |
| GET MPTS Status List | GET | /mpts/statuses | Get the status of all MPTS outputs. |
| GET MPTS Status | GET | /mpts/<ID of MPTS>/status | Get the status of the specified MPTS output. |
| GET MPTS Bitrate | GET | /mpts/<ID of MPTS>/stats | Get bitrate information for the specified MPTS output. |
| POST Start MPTS | POST | /mpts/<ID of mpts>/mux | Start an MPTS output. |
| DELETE Stop MPTS | GET | /mpts/<ID of mpts>/mux | Stop an MPTS output. |
| PUT Swap Allocation | PUT | /mpts/swap\_allocation\_priority | Swap the allocation values (allocation\_message\_priority element) in two related MPTS outputs. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
