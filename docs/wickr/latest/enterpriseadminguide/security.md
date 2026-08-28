---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/security.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Security
<a name="security"></a>

The **Security** section has the following available options for administration:
+ **Always Re-authenticate:** Forces mobile users to enter their password or biometric auth when bringing the app to focus. Disabled by default.
+ **User Password Permission:** If disabled users will be unable to change their password during registration and after activation. Enabled by default.
+ **Password Complexity Requirements:** Forces users to follow specified criteria when creating a password during registration and when changing their password.
+ **Device Reset:** The number of bad login attempts before the device is reset.
+ **User Account Suspension** If a user continues to enter the wrong password, it will suspend the account after this amount of tries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
