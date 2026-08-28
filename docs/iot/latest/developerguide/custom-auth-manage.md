---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-manage.html
---

# Managing custom authorizers
<a name="custom-auth-manage"></a>

 You can manage your authorizers by using the following APIs.
+ [ListAuthorizers](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuthorizers.html): Show all authorizers in your account.
+  [DescribeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuthorizer.html): Displays properties of the specified authorizer. These values include creation date, last modified date, and other attributes.
+ [SetDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_SetDefaultAuthorizer.html): Specifies the default authorizer for your AWS IoT Core data endpoints. AWS IoT Core uses this authorizer if a device doesn't pass AWS IoT Core credentials and doesn't specify an authorizer. For more information about using AWS IoT Core credentials, see [Client authentication](client-authentication.md).
+ [UpdateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html):  Changes the status, token key name, or public keys for the specified authorizer.
+  [DeleteAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuthorizer.html): Deletes the specified authorizer.

**Note**
 You can't update an authorizer's signing requirement. This means that you can't disable signing in an existing authorizer that requires it. You also can't require signing in an existing authorizer that doesn't require it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
