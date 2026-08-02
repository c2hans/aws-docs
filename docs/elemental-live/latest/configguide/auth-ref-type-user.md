---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-user.html
---

# Authentication user types
<a name="auth-ref-type-user"></a>

This table describes the types of users available with authentication.

****

| User type | How created | Log-in username | Log-in password | Use |
| --- | --- | --- | --- | --- |
| Default, remote terminal user | Built-in | Customer-created at install. | Default, or as changed by an administrator. | Users manually enter this information at these times: [See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-user.html) |
| Admin REST API user | An administrator enables local authentication on the node when they create the administrator user in the command line. | Customer-created. The username must not be the name of a real person. | Customer-created. | The administrator API user is used at these times: [See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-user.html)  |
| People and third-party clients | An administrator user creates these users either through the node's web interface (for local authentication) or through an LDAP server (for PAM authentication). | Customer-created. | Customer-created. | Users manually enter their log-in credentials when accessing the node through the web interface or REST API.<br />With local authentication. If a person has access to multiple nodes, you must create a user for them in each node. |
