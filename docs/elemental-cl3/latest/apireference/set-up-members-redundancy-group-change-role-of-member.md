---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-redundancy-group-change-role-of-member.html
---

# PUT: Change Role of a Member of a Redundancy Group
<a name="set-up-members-redundancy-group-change-role-of-member"></a>

Modify the role of the specified node in the specified redundancy group.

## HTTP Request and Response
<a name="set-up-members-redundancy-group-change-role-of-member-http-request-response"></a>

### Request URL
<a name="set-up-members-redundancy-group-change-role-of-member-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>/members/<ID of member node>
```

**Note**
Identify the member to change by specifying the redundancy group member ID within the redundancy group, not the ID within the cluster (the node ID). See the table under [GET List: Get a List of Redundancy Group Members](set-up-redundancy-groups-get-list-of-members.md) for an explanation of how to get each kind of ID.

### Call Header
<a name="set-up-members-redundancy-group-change-role-of-member-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-members-redundancy-group-change-role-of-member-http-request-response-request-body"></a>

The request contains XML content consisting of:
+ One redundancy\_group\_member with
+ role: “active” or “backup”

## Example
<a name="set-up-members-redundancy-group-change-role-of-member-example"></a>

This request changes a property of the redundancy group member identified by the member ID 3 that is in the redundancy group with the ID 1. It changes the node’s role from “backup” to “active.”

```
PUT http://198.51.100.0/redundancy_groups/1/members/3
--------------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group_member>
<role>active</role>
</redundancy_group_member>
```
