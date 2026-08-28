---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/commands-mpts-members.html
---

# Members of an MPTS
<a name="commands-mpts-members"></a>

| Nickname | Action | Signature | Description |
| --- | --- | --- | --- |
| POST MPTS Member | POST | /mpts/mpts\_id/mpts\_members | Add an SPTS to the specified MPTS output. |
| PUT MPTS Member | PUT | /mpts/mpts\_id/mpts\_members/:<mpts\_member\_id> | Change the attributes of the specified SPTS program in the specified MPTS output. |
| GET MPTS Member List | GET | /mpts/mpts\_id/mpts\_members | Get the list of all the SPTS programs in the specified MPTS output. |
| GET MPTS Member  | GET | /mpts/mpts\_id/mpts\_members/:<mpts\_member\_id> | Get the specified SPTS program from the specified MPTS output. |
| DELETE MPTS Member  | DELETE  | /mpts/mpts\_id/mpts\_members/:<mpts\_member\_id> | Delete the specified SPTS program from the specified MPTS output. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
