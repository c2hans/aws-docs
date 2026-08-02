---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/modify-attributes-of-a-channel.html
---

# PUT: Modify the Attributes of a Channel
<a name="modify-attributes-of-a-channel"></a>

Modify the attributes of the specified channel. The channel must be in a state that allows modifications. To check the status, use GET Channel. For information on the status, see [Channel Status Elements](monitoring-manage-channels.md#monitoring-manage-channels-status).

## HTTP Request and Response
<a name="modify-attributes-of-a-channel-http-request-response"></a>

### Request URL
<a name="modify-attributes-of-a-channel-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/channels/<ID of channel>
```

### Call Header
<a name="modify-attributes-of-a-channel-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="modify-attributes-of-a-channel-http-request-response-request-body"></a>

The body contains only the elements to change; see POST above.

## Example
<a name="modify-attributes-of-a-channel-example"></a>

This request changes the name of the channel with the ID 3. It modifies it to use the node that has the ID 1.

```
PUT http://198.51.100.0/channels/3
------------------------------------------
Content-type:application/xml
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<channel>
  <node_id>1</node_id>
</channel>
```
