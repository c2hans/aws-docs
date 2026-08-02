---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-attributes-of-profiles.html
---

# GET: Get the Attributes of a Profile
<a name="get-attributes-of-profiles"></a>

Get the attributes of the specified profile.

## HTTP Request and Response
<a name="get-attributes-of-profiles-http-request-response"></a>

### Request URL
<a name="get-attributes-of-profiles-http-request-response-url"></a>

```
GET http://<Conductor IP address>/profiles/<ID of profile>
```

### Call Header
<a name="get-attributes-of-profiles-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="get-attributes-of-profiles-http-request-response-response"></a>

The response contains XML content consisting of one profile, with the same elements as the response for GET Profile List, above. For a sketch of XML structure, see [Recommended Method for Working with Profiles](recommended-method-working-with-profiles.md).

## Example
<a name="get-attributes-of-profiles-example"></a>

This example shows the contents of a profile with the name Profile A, with the permalink “profile\_a” (the name in lowercase with spaces replaced by underscores).

```
<?xml version="1.0" encoding="UTF-8"?>
<profile href="/profiles/2" product="AWS Elemental Conductor Live" version="3.0.nnnnn">
  <name>Profile A</name>
  <permalink>profile_a</permalink>
  <description></description>
.
.
.
</profile>
```
