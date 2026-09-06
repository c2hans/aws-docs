---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/using-api-with-user-authentication-enabled.html
---

# Using the API with User Authentication Enabled
<a name="using-api-with-user-authentication-enabled"></a>

Your cluster deployment is configured for local or PAM user authentication (users must provide valid credentials to access Conductor Live). Check with the person who performed the initial configuration of the cluster, or see the [AWS Elemental Conductor Live Configuration Guide](https://docs.aws.amazon.com/elemental-cl3/latest/configguide/).

If authentication is enabled, then the header of each request must also include the following:

| Header | Description |
| --- | --- |
| X-Auth-User | The username of the user who is using the API. Note that the user’s password is not included in the header. |
| X-Auth-Expires | The date and time at which the individual REST request expires. Enter the date in Unix time (POSIX or Epoch time).<br />The recommended value is 30 seconds in the future, but, if the client clock and Conductor node clock are not completely in sync, you may want to make adjustments to accommodate the difference. |
| X-Auth-Key | An MD5 hash of the API key for the user who is using the API. <br />An administrator generates this key as follows:+  Log on via the web interface and go to Settings > User Profile. <br />+  Click the Reset API Key (key icon) for the applicable users.  <br />+  Provide the individual user with a key, for example, via email. <br />For information on hashing the key, see the next section. |

**Topics**
+ [Hashing the API Key](hashing-api-key.md)
+ [AuthCurl Scripts](authcurl-scripts.md)
+ [Authentication Error Messages](authentication-error-messages.md)
