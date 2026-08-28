---
source_url: https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-dfeg.html
---

# Troubleshoot DataflowEndpointGroups not in a HEALTHY state
<a name="troubleshooting-dfeg"></a>

 Listed below are the reasons your dataflow endpoint groups may not be in a `HEALTHY` state as well as the appropriate corrective action to take.
+ `NO_REGISTERED_AGENT` - Start your EC2 instance, which will register the agent. Note that you must have a valid controller config file for this call to be successful. Refer to the [Use AWS Ground Station Agent](how-it-works.gs-agent.md) for details on configuring that file.
+ `INVALID_IP_OWNERSHIP` - Use the DeleteDataflowEndpointGroup API to delete the Dataflow Endpoint Group, then use the CreateDataflowEndpointGroup API to recreate the Dataflow Endpoint Group using IP addresses and ports that are associated with the EC2 instance.
+ `UNVERIFIED_IP_OWNERSHIP` - IP address has not been validated yet. Validation occurs periodically so this should resolve itself.
+ `NOT_AUTHORIZED_TO_CREATE_SLR` - Account is not authorized to create the necessary Service-Linked Role. Check the troubleshooting steps in [Use service-linked roles for Ground Station](using-service-linked-roles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
