---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ContainerServiceRegistryLogin.html
---

# ContainerServiceRegistryLogin
<a name="API_ContainerServiceRegistryLogin"></a>

Describes the sign-in credentials for the container image registry of an Amazon Lightsail account.

## Contents
<a name="API_ContainerServiceRegistryLogin_Contents"></a>

 ** expiresAt **   <a name="Lightsail-Type-ContainerServiceRegistryLogin-expiresAt"></a>
The timestamp of when the container image registry sign-in credentials expire.
The log in credentials expire 12 hours after they are created, at which point you will need to create a new set of log in credentials using the `CreateContainerServiceRegistryLogin` action.
Type: Timestamp
Required: No

 ** password **   <a name="Lightsail-Type-ContainerServiceRegistryLogin-password"></a>
The container service registry password to use to push container images to the container image registry of a Lightsail account
Type: String
Required: No

 ** registry **   <a name="Lightsail-Type-ContainerServiceRegistryLogin-registry"></a>
The address to use to push container images to the container image registry of a Lightsail account.
Type: String
Required: No

 ** username **   <a name="Lightsail-Type-ContainerServiceRegistryLogin-username"></a>
The container service registry username to use to push container images to the container image registry of a Lightsail account.
Type: String
Required: No

## See Also
<a name="API_ContainerServiceRegistryLogin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/ContainerServiceRegistryLogin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/ContainerServiceRegistryLogin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/ContainerServiceRegistryLogin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
