---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-create.html
---

# POST: Create a Conductor Redundancy Group
<a name="set-up-conductor-redundancy-groups-create"></a>

Create a new Conductor redundancy group with the specified attributes. You can create only one Conductor redundancy group.

## HTTP Request and Response
<a name="set-up-conductor-redundancy-groups-create-http-request-response"></a>

### Request URL
<a name="set-up-conductor-redundancy-groups-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/conductor_redundancy_groups
```

### Call Header
<a name="set-up-conductor-redundancy-groups-create-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-conductor-redundancy-groups-create-http-request-response-request-body"></a>

The response contains XML content consisting of one `conductor_redundancy_group` element with the following elements.

| Element | Value | Description |
| --- | --- | --- |
| vip | String | A valid ipv4 address. This address is the “cluster ID” for the two Conductor nodes.<br />This address must be an address on your network that is never allocated to any other host.  |
| vrid | Integer | The virtual router ID, a number from 1-254.<br />This ID must not conflict with any other instance of keepalived (or another (Virtual Router Redundancy Protocol)VRRP-based service) that is running on your network. <br />To check for conflicting **VRRP** services, use:<br />**sudo tcpdump vrrp**<br />If you see VRRP advertisement packets, do not use the listed VRIDs. |
| name | String | Choose a name.  |

### Response
<a name="set-up-conductor-redundancy-groups-create-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of the following.
+ id: The newly assigned ID for the Conductor redundancy group.
+ enabled: This setting is always "false" on a newly created group to indicate that Conductor redundancy is not yet enabled.
+ product\_name: This setting is always “conductor\_live.”

The response is identical to the response to a GET Conductor Redundancy Group. For an example, see [GET: Get the Attributes of the Conductor Redundancy Group](set-up-conductor-redundancy-groups-get-attributes.md).

## Example
<a name="set-up-conductor-redundancy-groups-create-example"></a>

### Request
<a name="set-up-conductor-redundancy-groups-create-example-request"></a>

This request creates one Conductor redundancy group that has the VIP 10.4.200.200 and the VRID 2.

```
POST http://198.51.100.0/conductor_redundancy_groups
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_group>
  <vip>10.4.200.200</vip>
  <vrid>2</vrid>
  <name>Conductor</name>
</conductor_redundancy_group>
```

### Response
<a name="set-up-conductor-redundancy-groups-create-example-response"></a>

```
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_groups href="/conductor_redundancy_groups" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <conductor_redundancy_group>
    <id type="integer">1</id>
    <vip>10.4.200.200</vip>
    <vrid type="integer">2</vrid>
    <name>Conductor</name>
    <product_name>conductor_live</conductor_live>
  </conductor_redundancy_group>
</conductor_redundancy_groups>
```
