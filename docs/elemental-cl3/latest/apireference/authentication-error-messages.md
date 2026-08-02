---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/authentication-error-messages.html
---

# Authentication Error Messages
<a name="authentication-error-messages"></a>

The following errors describe why authentication requests can fail.

| Error Message | Reason |
| --- | --- |
| X-Auth-Login is required. | The request headers are missing “X-Auth-Login” or the values are malformed. |
| X-Auth-Key is required. | The request headers are missing “X-Auth-Key” or the values are malformed. |
| X-Auth-Expires is required. | The request headers are missing “X-Auth-Expires” or the values are malformed. |
| X-Auth-Login is invalid. | Invalid user or the user exists but the role is invalid. |
| X-Auth-Key is invalid. | The key is not valid.<br />To troubleshoot:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/apireference/authentication-error-messages.html) |
| X-Auth-Expires is invalid. | The “expires” value did not pass validation.<br />To troubleshoot:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/apireference/authentication-error-messages.html) |
