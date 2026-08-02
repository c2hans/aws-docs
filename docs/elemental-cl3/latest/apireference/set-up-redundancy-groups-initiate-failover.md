---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-initiate-failover.html
---

# POST Initiate Failover
<a name="set-up-redundancy-groups-initiate-failover"></a>

Initiate failover of the specified node. The node must be part of a redundancy group, must have an “active” role, and must be running a channel. The redundancy group must also have least one backup node.

When failover is initiated, the node becomes to "idle" and all its channels are moved to a backup node. That backup node become an active node.

To make the original node active again, associate channels with the node again (using the PUT Channel command) and change that node’s status to "active."

## HTTP Request and Response
<a name="set-up-redundancy-groups-initiate-failover-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-initiate-failover-http-request-response-url"></a>

```
POST http://<Conductor IP address>/nodes/<ID of node>/backup
```

### Call Header
<a name="set-up-redundancy-groups-initiate-failover-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-redundancy-groups-initiate-failover-example"></a>

This request initiates failover the node with the ID 8.

```
POST http://198.51.100.0/nodes/8/backup
```
