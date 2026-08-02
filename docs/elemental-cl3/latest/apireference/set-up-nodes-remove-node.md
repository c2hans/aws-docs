---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-remove-node.html
---

# DELETE: Remove a Node from the Cluster
<a name="set-up-nodes-remove-node"></a>

Remove the specified node from the Conductor Live cluster. The node cannot be associated with any channels, so follow this procedure.

1. Send a GET Channel List request to see which channels use this node.

1. Send a POST Stop request to stop the channels that are running.

1. Send a PUT Channel request on each channel to modify it so that it does not use this node.

1. Delete the channel as described in [DELETE: Delete a Channel](delete-a-channel.md).

## HTTP Request and Response
<a name="set-up-nodes-remove-node-http-request-response"></a>

### Request URL
<a name="set-up-nodes-remove-node-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/nodes/<ID of node>
```

### Call Header
<a name="set-up-nodes-remove-node-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-nodes-remove-node-example"></a>

This request removes the node with the ID 8.

```
DELETE http://198.51.100.0/nodes/8
```
