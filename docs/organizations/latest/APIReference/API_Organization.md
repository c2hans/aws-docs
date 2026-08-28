---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Organization.html
---

# Organization
<a name="API_Organization"></a>

Contains details about an organization. An organization is a collection of accounts that are centrally managed together using consolidated billing, organized hierarchically with organizational units (OUs), and controlled with policies .

## Contents
<a name="API_Organization_Contents"></a>

 ** Arn **   <a name="organizations-Type-Organization-Arn"></a>
The Amazon Resource Name (ARN) of an organization.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32}`
Required: No

 ** AvailablePolicyTypes **   <a name="organizations-Type-Organization-AvailablePolicyTypes"></a>
Do not use. This field is deprecated and doesn't provide complete information about the policies in your organization.
To determine the policies that are enabled and available for use in your organization, use the [ListRoots](API_ListRoots.md) operation instead.
Type: Array of [PolicyTypeSummary](API_PolicyTypeSummary.md) objects
Required: No

 ** FeatureSet **   <a name="organizations-Type-Organization-FeatureSet"></a>
Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED\_BILLING", then only consolidated billing functionality is available. For more information, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the * AWS Organizations User Guide*.
Type: String
Valid Values: `ALL | CONSOLIDATED_BILLING`
Required: No

 ** Id **   <a name="organizations-Type-Organization-Id"></a>
The unique identifier (ID) of an organization.
The [regex pattern](http://wikipedia.org/wiki/regex) for an organization ID string requires "o-" followed by from 10 to 32 lowercase letters or digits.
Type: String
Pattern: `^o-[a-z0-9]{10,32}$`
Required: No

 ** MasterAccountArn **   <a name="organizations-Type-Organization-MasterAccountArn"></a>
The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:account\/o-[a-z0-9]{10,32}\/\d{12}`
Required: No

 ** MasterAccountEmail **   <a name="organizations-Type-Organization-MasterAccountEmail"></a>
The email address that is associated with the AWS account that is designated as the management account for the organization.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: No

 ** MasterAccountId **   <a name="organizations-Type-Organization-MasterAccountId"></a>
The unique identifier (ID) of the management account of an organization.
The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_Organization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Organization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Organization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Organization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
