---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs.html
---

# Setting Up Router Outputs
<a name="set-up-router-outputs"></a>

The Router Outputs entity holds information about each router output that is connected to an SDI card on an AWS Elemental Live appliance. The information is a mapping from the router output to the SDI input.

If, after the initial setup, you ever hook up another cable between a router output and an SDI input, you must set it up using POST Router Input.

**Topics**
+ [POST: Create a Router Output](set-up-router-outputs-create.md)
+ [PUT: Modify a Router Output](set-up-router-outputs-modify.md)
+ [GET List: Get Router Output List](set-up-router-outputs-get-list.md)
+ [GET: Get Attributes of a Router Output](set-up-router-outputs-get-attributes.md)
+ [DELETE: Delete a Router Output](set-up-router-outputs-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
