---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-disable.html
---

# DELETE Disable: Disable Conductor Redundancy Group
<a name="set-up-conductor-redundancy-groups-disable"></a>

Disable Conductor Redundancy mode (high availability) on the two Conductor nodes in the Conductor redundancy group.

If you are using a VM, take a snapshot before disabling high availability. See the VMware VSphere help text for more information.

## HTTP Request and Response
<a name="set-up-conductor-redundancy-groups-disable-http-request-response"></a>

### Request URL
<a name="set-up-conductor-redundancy-groups-disable-http-request-response-url"></a>

```
DELETE http://<VIP>/conductor_redundancy_groups/<ID of Conductor redundancy group>/disable
```

The process of disabling Conductor redundancy takes more than a few minutes, so you should not disable it unless you have a good reason:
+ You must disable Conductor redundancy to change any of the network settings.
+ You must disable Conductor redundancy in order to upgrade the Conductor Live software.

**Note**
You do not need to disable Conductor redundancy in order to add or remove worker nodes from the cluster\!

While the mode is being disabled, the Conductor nodes cannot take REST API requests.

Once Conductor redundancy is disabled, you must send API requests to the IP address of the Conductor node that is currently primary.

So the process is:

1. To disable Conductor redundancy, send the POST Enable request to the virtual IP address.

1. Once Conductor redundancy is successfully enabled, send all future API commands to the Conductor node that is currently primary.

**Warning**
When Conductor redundancy is disabled, do not send requests to the VIP.

### Call Header
<a name="set-up-conductor-redundancy-groups-disable-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-conductor-redundancy-groups-disable-http-request-response-response"></a>

The response is identical to the [response for GET List of Redundancy Groups](set-up-redundancy-groups-get-a-list.md#set-up-redundancy-groups-get-a-list-http-request-response-response).

## Example
<a name="set-up-conductor-redundancy-groups-disable-example"></a>

This example disables Conductor redundancy on the Conductor redundancy group (which has ID 1) by submitting a request from the VIP:

```
DELETE http://10.4.200.200/conductor_redundancy_groups/1/disable
```
