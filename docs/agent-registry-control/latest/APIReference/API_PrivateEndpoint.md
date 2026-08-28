---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_PrivateEndpoint.html
---

# PrivateEndpoint
<a name="API_PrivateEndpoint"></a>

A private network endpoint used to reach a resource over a private path. Exactly one member is set.

## Contents
<a name="API_PrivateEndpoint_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** managedVpcResource **   <a name="agentregistrycontrol-Type-PrivateEndpoint-managedVpcResource"></a>
A private endpoint backed by a service-managed VPC resource.
Type: [ManagedVpcResource](API_ManagedVpcResource.md) object
Required: No

 ** selfManagedLatticeResource **   <a name="agentregistrycontrol-Type-PrivateEndpoint-selfManagedLatticeResource"></a>
A private endpoint backed by a self-managed VPC Lattice resource configuration.
Type: [SelfManagedLatticeResource](API_SelfManagedLatticeResource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_PrivateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PrivateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PrivateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PrivateEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
