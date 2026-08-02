---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/delete-a-profile.html
---

# DELETE: Delete a Profile
<a name="delete-a-profile"></a>

Delete the specified profile.

You must first verify that the profile is not being used: do a GET Channel List and make sure this profile is not associated with any channel. If it is, do a PUT Channel on that channel so that the channel uses a different profile before you delete this profile.

## Request URL
<a name="delete-a-profile-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/profiles/<ID of profile>
```

## Call Header
<a name="delete-a-profile-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="delete-a-profile-example"></a>

This request deletes the profile with the ID 14.

```
DELETE http://198.51.100.0/profiles/14
```
