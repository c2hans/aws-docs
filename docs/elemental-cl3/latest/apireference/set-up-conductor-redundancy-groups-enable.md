---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-enable.html
---

# POST Enable: Enable Conductor Redundancy Group
<a name="set-up-conductor-redundancy-groups-enable"></a>

Enable Conductor Redundancy mode (high availability) on the two Conductor nodes in the Conductor redundancy group in order to enable the failover mode for the Conductor nodes.

If you are using a VM, take a snapshot before enabling high availability. See the VMware VSphere help text for more information.

## HTTP Request and Response
<a name="set-up-conductor-redundancy-groups-enable-http-request-response"></a>

### Request URL
<a name="set-up-conductor-redundancy-groups-enable-http-request-response-url"></a>

```
POST http://<IP of primary Conductor node>/conductor_redundancy_groups/<ID of Conductor redundancy group>/enable
```

where:
+ <ID of primary Conductor node> is the ID of the node that you want to have the role of primary once redundancy is enabled. In other words, perform this command from the node that you want to become the primary Conductor.

The process of enabling Conductor redundancy takes more than a few minutes, so you should only enable when you are absolutely sure you have performed all the necessary cluster configuration. While the mode is being enabled, the Conductor nodes cannot take REST API requests.

Once Conductor redundancy is enabled, you must send API requests to the virtual IP address (VIP) you specified in the [POST Conductor Redundancy Group](set-up-conductor-redundancy-groups-create.md). The virtual IP redirects the request to the Conductor node that is currently primary.

So the process is:

1. To enable Conductor redundancy, send the POST Enable request to the Conductor node that is currently primary.

1. Once Conductor redundancy is successfully enabled, send all future API commands to the virtual IP address.

**Warning**
When Conductor redundancy is enabled, do not send requests to the individual primary Conductor node, even if you know which node is currently the primary.

### Call Header
<a name="set-up-conductor-redundancy-groups-enable-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-conductor-redundancy-groups-enable-http-request-response-response"></a>

The response is returned immediately (the system does not wait for Conductor redundancy to finish). The response is identical to the [response for GET List of Redundancy Groups](set-up-redundancy-groups-get-a-list.md#set-up-redundancy-groups-get-a-list-http-request-response-response).

## Example
<a name="set-up-conductor-redundancy-groups-enable-example"></a>

This example enables Conductor redundancy on the Conductor redundancy group (which has ID 1) by submitting a request from the node 198.51.100.0, which is currently the primary node.

```
POST http://198.51.100.0/conductor_redundancy_groups/1/enable
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
