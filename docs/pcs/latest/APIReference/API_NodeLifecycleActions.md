---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_NodeLifecycleActions.html
---

# NodeLifecycleActions
<a name="API_NodeLifecycleActions"></a>

The lifecycle actions configured on a compute node group. Lifecycle actions define scripts that AWS PCS runs on compute nodes at specific stages of their lifecycle.

## Contents
<a name="API_NodeLifecycleActions_Contents"></a>

 ** stages **   <a name="PCS-Type-NodeLifecycleActions-stages"></a>
The lifecycle stages where you configure scripts to run.
Type: [NodeLifecycleStages](API_NodeLifecycleStages.md) object
Required: Yes

 ** scriptCachingPolicy **   <a name="PCS-Type-NodeLifecycleActions-scriptCachingPolicy"></a>
The caching policy for node lifecycle scripts. The default value is `CACHE_ONCE`. Valid values:
+  `CACHE_ONCE` – Downloads each script once and reuses it on subsequent boots.
+  `REFRESH_ON_REBOOT` – Downloads each script on every boot.
Type: String
Valid Values: `CACHE_ONCE | REFRESH_ON_REBOOT`
Required: No

## See Also
<a name="API_NodeLifecycleActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/NodeLifecycleActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/NodeLifecycleActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/NodeLifecycleActions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
