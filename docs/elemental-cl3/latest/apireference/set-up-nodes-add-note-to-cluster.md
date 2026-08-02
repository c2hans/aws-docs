---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-add-note-to-cluster.html
---

# POST: Add a Node to the Cluster
<a name="set-up-nodes-add-note-to-cluster"></a>

## HTTP Request and Response
<a name="set-up-nodes-add-note-to-cluster-http-request-response"></a>

### Request URL
<a name="set-up-nodes-add-note-to-cluster-http-request-response-url"></a>

Add a node to the cluster.

```
POST http://<Conductor IP address>/nodes
```

### Request Body
<a name="set-up-nodes-add-note-to-cluster-http-request-response-request-body"></a>

The request body is XML content consisting of one `hosts` element (of type “array”) that contains:
+ One or more `host` elements, one for each node found. Each element contains:
  + One IP address.
  + A range of IP addresses (for example, 10.4.136.[90-92]).

### Call Header
<a name="set-up-nodes-add-note-to-cluster-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-nodes-add-note-to-cluster-http-request-response-response"></a>

No response is supplied for a successful node addition. Operators should perform the GET Node operation to confirm that the node has been added successfully. For assistance, see [GET: Get the Attributes of a Node](set-up-nodes-get-attributes-of-node.md).

## Example
<a name="set-up-nodes-add-note-to-cluster-example"></a>

### Request
<a name="set-up-nodes-add-note-to-cluster-example-request"></a>

This request adds four nodes: 10.4.136.15, 10.4.136.90, 10.4.136.91, 10.4.136.92.

```
POST http://198.51.100.0/nodes
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<hosts type="array">
  <host>10.4.136.15</host>
  <host>10.4.136.[90-92]</host>
</hosts>
```
