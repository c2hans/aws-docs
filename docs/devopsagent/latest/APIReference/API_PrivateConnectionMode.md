---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PrivateConnectionMode.html
---

# PrivateConnectionMode
<a name="API_PrivateConnectionMode"></a>

Private Connection mode — either service-managed or self-managed.

## Contents
<a name="API_PrivateConnectionMode_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** selfManaged **   <a name="devopsagent-Type-PrivateConnectionMode-selfManaged"></a>
Caller manages their own resource configuration.
Type: [SelfManagedInput](API_SelfManagedInput.md) object
Required: No

 ** serviceManaged **   <a name="devopsagent-Type-PrivateConnectionMode-serviceManaged"></a>
Service manages the Resource Gateway lifecycle.
Type: [ServiceManagedInput](API_ServiceManagedInput.md) object
Required: No

## See Also
<a name="API_PrivateConnectionMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PrivateConnectionMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PrivateConnectionMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PrivateConnectionMode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
