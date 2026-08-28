---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_ScopeDetails.html
---

# ScopeDetails
<a name="API_ScopeDetails"></a>

Details about the scope of the notifications such as the affected resources.

## Contents
<a name="API_ScopeDetails_Contents"></a>

 ** LakeFormationTagPolicies **   <a name="dataexchange-Type-ScopeDetails-LakeFormationTagPolicies"></a>
Underlying LF resources that will be affected by this notification.
Type: Array of [LakeFormationTagPolicyDetails](API_LakeFormationTagPolicyDetails.md) objects
Required: No

 ** RedshiftDataShares **   <a name="dataexchange-Type-ScopeDetails-RedshiftDataShares"></a>
Underlying Redshift resources that will be affected by this notification.
Type: Array of [RedshiftDataShareDetails](API_RedshiftDataShareDetails.md) objects
Required: No

 ** S3DataAccesses **   <a name="dataexchange-Type-ScopeDetails-S3DataAccesses"></a>
Underlying S3 resources that will be affected by this notification.
Type: Array of [S3DataAccessDetails](API_S3DataAccessDetails.md) objects
Required: No

## See Also
<a name="API_ScopeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/ScopeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/ScopeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/ScopeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
