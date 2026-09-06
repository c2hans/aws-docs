---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CrossAccountRole.html
---

# CrossAccountRole
<a name="API_CrossAccountRole"></a>

Specifies a cross-account IAM role ARN and optional external ID.

## Contents
<a name="API_CrossAccountRole_Contents"></a>

 ** crossAccountRoleArn **   <a name="ngresiliencehub-Type-CrossAccountRole-crossAccountRoleArn"></a>
ARN of the IAM Role for the profile. Null if the permission profile is the 'Admin' profile.
Type: String
Length Constraints: Minimum length of 32.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):iam::[0-9]{12}:role/(([^/][!-~]+/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}`
Required: Yes

 ** externalId **   <a name="ngresiliencehub-Type-CrossAccountRole-externalId"></a>
The external ID used for assuming the cross-account role.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 1224.
Required: No

## See Also
<a name="API_CrossAccountRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CrossAccountRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CrossAccountRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CrossAccountRole)
