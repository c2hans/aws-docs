---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_PolicyInfo.html
---

# PolicyInfo

Contains details about a policy evaluated during authorization. Details include the policy type, whether it is inline or managed, a URI that identifies it, the entities it is attached to, and its source, if present.

## Contents
<a name="API_PolicyInfo_Contents"></a>

 ** attachedTo **   <a name="iamtoolbox-Type-PolicyInfo-attachedTo"></a>
The entities that the policy is attached to. For identity, session, and resource-based policies, this is typically a single entity. For organization control policies (SCPs and RCPs), it can be multiple entities at different levels of the organization hierarchy.
Type: Array of [AttachedTo](API_AttachedTo.md) objects
Required: No

 ** inline **   <a name="iamtoolbox-Type-PolicyInfo-inline"></a>
Specifies whether this is an inline policy (`true`) or a managed policy (`false`).
Type: Boolean
Required: No

 ** policySource **   <a name="iamtoolbox-Type-PolicyInfo-policySource"></a>
What the policy was built from, such as a KMS key policy or grant. Absent for other policies.
The `type` and `typeName` keys are always present. `type` identifies the policy-source kind. `typeName` is its readable name. Compare `type`, not `typeName`.
A policy source can include additional keys that depend on its type. For example, a KMS grant includes a `grantId` key that identifies the grant. A grant has no ARN. Use the grant ID with the KMS key ARN in `attachedTo` to find the grant with the AWS KMS `ListGrants` operation.
New types and keys can be added, so clients should ignore types and keys they don't recognize.
Type: String to string map
Required: No

 ** type **   <a name="iamtoolbox-Type-PolicyInfo-type"></a>
The type of policy. Valid values:
+  `IDENTITY_BASED_POLICY` - An identity-based policy attached to an IAM user, group, or role.
+  `PERMISSIONS_BOUNDARY` - A permissions boundary for an IAM entity.
+  `RESOURCE_BASED_POLICY` - A resource-based policy attached to a resource. An AWS service can evaluate and report a policy kind it defines, such as a KMS grant, as `RESOURCE_BASED_POLICY`. `policySource` identifies the kind.
+  `RESOURCE_CONTROL_POLICY` - A resource control policy (RCP) in AWS Organizations.
+  `SERVICE_CONTROL_POLICY` - A service control policy (SCP) in AWS Organizations.
+  `SESSION_POLICY` - A session policy passed during role assumption or federation.
+  `VPC_ENDPOINT_POLICY` - A VPC endpoint policy.
Type: String
Valid Values: `IDENTITY_BASED_POLICY | RESOURCE_BASED_POLICY | PERMISSIONS_BOUNDARY | SESSION_POLICY | SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY | VPC_ENDPOINT_POLICY`
Required: No

 ** uri **   <a name="iamtoolbox-Type-PolicyInfo-uri"></a>
A URI that identifies the policy. Use this URI to cross-reference the policy with the matching policies in each evaluation. To retrieve the policy document, pass this URI as the `policyUri` parameter of `GetRequestAuthorizationPolicy`, together with the same authorization ID. The value depends on the policy type:
+ For managed policies, this is the policy ARN.
+ For inline policies, which have no ARN, this is an opaque identifier.
Type: String
Required: No

## See Also
<a name="API_PolicyInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/PolicyInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/PolicyInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/PolicyInfo)
