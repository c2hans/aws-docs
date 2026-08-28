---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Root.html
---

# Root
<a name="API_Root"></a>

Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. The root contains every AWS account in the organization.

## Contents
<a name="API_Root_Contents"></a>

 ** Arn **   <a name="organizations-Type-Root-Arn"></a>
The Amazon Resource Name (ARN) of the root.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:root\/o-[a-z0-9]{10,32}\/r-[0-9a-z]{4,32}`
Required: No

 ** Id **   <a name="organizations-Type-Root-Id"></a>
The unique identifier (ID) for the root. The ID is unique to the organization only.
The [regex pattern](http://wikipedia.org/wiki/regex) for a root ID string requires "r-" followed by from 4 to 32 lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^r-[0-9a-z]{4,32}$`
Required: No

 ** Name **   <a name="organizations-Type-Root-Name"></a>
The friendly name of the root.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** PolicyTypes **   <a name="organizations-Type-Root-PolicyTypes"></a>
The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.
Even if a policy type is shown as available in the organization, you can separately enable and disable them at the root level by using [EnablePolicyType](API_EnablePolicyType.md) and [DisablePolicyType](API_DisablePolicyType.md). Use [DescribeOrganization](API_DescribeOrganization.md) to see the availability of the policy types in that organization.
Type: Array of [PolicyTypeSummary](API_PolicyTypeSummary.md) objects
Required: No

## See Also
<a name="API_Root_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Root)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Root)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Root)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
