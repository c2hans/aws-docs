---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-delete.html
---

# DELETE: Delete a Conductor Redundancy Group
<a name="set-up-conductor-redundancy-groups-delete"></a>

Delete the Conductor redundancy group that has the specified ID. The group must first be [disabled](set-up-conductor-redundancy-groups-disable.md).

## HTTP Request and Response
<a name="set-up-conductor-redundancy-groups-delete-http-request-response"></a>

### Request URL
<a name="set-up-conductor-redundancy-groups-delete-http-request-response-url"></a>

```
GET http://<Conductor IP address>/conductor_redundancy_groups/<ID of Conductor redundancy group>
```

### Call Header
<a name="set-up-conductor-redundancy-groups-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-conductor-redundancy-groups-delete-example"></a>

This request deletes the Conductor redundancy group with the ID 1.

```
DELETE http://198.51.100.0/conductor_redundancy_groups/1
```
