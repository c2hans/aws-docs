---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/header-content-user.html
---

# Header Content for User Authentication
<a name="header-content-user"></a>

If your cluster deployment is configured for user authentication (users must log into Conductor Live), then the header must also include:
+ X-Auth-User header.
+ X-Auth-Expires header (optional).
+ X-Auth-Key header includes the API key of the individual user.

  For more information, see [Using the API with User Authentication Enabled](using-api-with-user-authentication-enabled.md).
