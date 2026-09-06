---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-delete.html
---

# DELETE: Delete a Redundancy Group
<a name="set-up-redundancy-groups-delete"></a>

Delete the redundancy group that has the specified ID.

## HTTP Request and Response
<a name="set-up-redundancy-groups-delete-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-delete-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>
```

### Call Header
<a name="set-up-redundancy-groups-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-redundancy-groups-delete-example"></a>

This request deletes the redundancy group with the ID 2 .

```
DELETE http://198.51.100.0/redundancy_groups/2
```
