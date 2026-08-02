---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-list-of-profiles.html
---

# GET List: Get a List of Profiles
<a name="get-list-of-profiles"></a>

## HTTP Request and Response
<a name="get-list-of-profiles-http-request-response"></a>

### Request URL
<a name="get-list-of-profiles-http-request-response-url"></a>

```
GET http://<Conductor IP address>/profiles
```

### Call Header
<a name="get-list-of-profiles-http-request-response-call-header"></a>
+ Accept: Set to application/xml

### Response
<a name="get-list-of-profiles-http-request-response-response"></a>

The response contains XML content consisting of one `profiles` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `profile` elements, one for each profile found. Each element contains several elements, including these key elements. For details on other elements, see [Recommended Method for Working with Profiles](recommended-method-working-with-profiles.md).

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this profile, assigned by the system when the profile is created. |
| name | String | The name that you assigned to the profile. |
| permalink | String | The ID of the node, assigned by the system. For profiles, the ID is a string (not an integer) and is created by taking the name you assigned, converting it to lower case, and changing spaces and illegal characters to underscores. |

## Example
<a name="get-list-of-profiles-example"></a>

The response to this request specifies that there are three profiles set up in the cluster.

```
<?xml version="1.0" encoding="UTF-8"?>
<profiles href="/profiles" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
<profile href="/profiles/1">
  <id>1</id>
  <name>Profile A</name>
  <permalink>profile_a</permalink>
  <description></description>
  <input>
.
.
.
</profile>
<profile href="/profiles/4">
  <id>4</id>
  <name>Profile C</name>
  <permalink>profile_c</permalink>
  <description></description>
  <input>
.
.
.
</profile>
<profile href="/profiles/5">
  <id>5</id>
  <name>Profile D</name>
  <permalink>profile_d</permalink>
  <description></description>
  <input>
.
.
</profile>
</profile_list>
```
