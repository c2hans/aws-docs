---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListMembershipItem.html
---

# ListMembershipItem
<a name="API_ListMembershipItem"></a>

## Contents
<a name="API_ListMembershipItem_Contents"></a>

 ** membershipId **   <a name="securityir-Type-ListMembershipItem-membershipId"></a>

Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`
Required: Yes

 ** accountId **   <a name="securityir-Type-ListMembershipItem-accountId"></a>

Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** membershipArn **   <a name="securityir-Type-ListMembershipItem-membershipArn"></a>

Type: String
Length Constraints: Minimum length of 12. Maximum length of 80.
Pattern: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:membership/m-[a-z0-9]{10,32}`
Required: No

 ** membershipStatus **   <a name="securityir-Type-ListMembershipItem-membershipStatus"></a>

Type: String
Valid Values: `Active | Cancelled | Terminated`
Required: No

 ** region **   <a name="securityir-Type-ListMembershipItem-region"></a>

Type: String
Valid Values: `af-south-1 | ap-east-1 | ap-east-2 | ap-northeast-1 | ap-northeast-2 | ap-northeast-3 | ap-south-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-3 | ap-southeast-4 | ap-southeast-5 | ap-southeast-6 | ap-southeast-7 | ca-central-1 | ca-west-1 | cn-north-1 | cn-northwest-1 | eu-central-1 | eu-central-2 | eu-north-1 | eu-south-1 | eu-south-2 | eu-west-1 | eu-west-2 | eu-west-3 | il-central-1 | me-central-1 | me-south-1 | mx-central-1 | sa-east-1 | us-east-1 | us-east-2 | us-west-1 | us-west-2`
Required: No

## See Also
<a name="API_ListMembershipItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/ListMembershipItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/ListMembershipItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/ListMembershipItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
