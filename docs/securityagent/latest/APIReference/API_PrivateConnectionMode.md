---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_PrivateConnectionMode.html
---

# PrivateConnectionMode
<a name="API_PrivateConnectionMode"></a>

The configuration for a private connection. Specify either a service-managed or a self-managed mode.

## Contents
<a name="API_PrivateConnectionMode_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** selfManaged **   <a name="securityagent-Type-PrivateConnectionMode-selfManaged"></a>
The configuration for a self-managed private connection, where you manage your own resource configuration.
Type: [SelfManagedInput](API_SelfManagedInput.md) object
Required: No

 ** serviceManaged **   <a name="securityagent-Type-PrivateConnectionMode-serviceManaged"></a>
The configuration for a service-managed private connection, where the service manages the resource gateway lifecycle.
Type: [ServiceManagedInput](API_ServiceManagedInput.md) object
Required: No

## See Also
<a name="API_PrivateConnectionMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/PrivateConnectionMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/PrivateConnectionMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/PrivateConnectionMode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
