---
source_url: https://docs.aws.amazon.com/iam-toolbox/latest/APIReference/API_AttachedTo.html
---

# AttachedTo
<a name="API_AttachedTo"></a>

An entity that a policy is attached to, identified by its ARN.

## Contents
<a name="API_AttachedTo_Contents"></a>

 ** arn **   <a name="iamtoolbox-Type-AttachedTo-arn"></a>
The ARN of the entity that the policy is attached to. The ARN format depends on the policy type:
+ For identity, session, and permissions boundary policies, this is the principal ARN (for example, an IAM role or user ARN).
+ For resource-based policies, this is the resource ARN.
+ For organization control policies (SCPs and RCPs), this is the AWS Organizations ARN of the account, organizational unit, or root.
Type: String
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

## See Also
<a name="API_AttachedTo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-toolbox-2018-05-10/AttachedTo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-toolbox-2018-05-10/AttachedTo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-toolbox-2018-05-10/AttachedTo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Toolbox. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iam-toolbox` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
