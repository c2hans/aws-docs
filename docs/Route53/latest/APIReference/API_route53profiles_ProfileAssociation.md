---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileAssociation.html
---

# ProfileAssociation
<a name="API_route53profiles_ProfileAssociation"></a>

 An association between a Route 53 Profile and a VPC.

## Contents
<a name="API_route53profiles_ProfileAssociation_Contents"></a>

 ** CreationTime **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-CreationTime"></a>
 The date and time that the Profile association was created, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Id **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-Id"></a>
 ID of the Profile association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ModificationTime **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-ModificationTime"></a>
 The date and time that the Profile association was modified, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Name **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-Name"></a>
 Name of the Profile association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-OwnerId"></a>
 AWS account ID of the Profile association owner.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ProfileId **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-ProfileId"></a>
 ID of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceId **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-ResourceId"></a>
 The Amazon Resource Name (ARN) of the VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Status **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-Status"></a>
 Status of the Profile association.
Type: String
Valid Values: `COMPLETE | DELETING | UPDATING | CREATING | DELETED | FAILED`
Required: No

 ** StatusMessage **   <a name="Route53Profiles-Type-route53profiles_ProfileAssociation-StatusMessage"></a>
 Additional information about the Profile association.
Type: String
Required: No

## See Also
<a name="API_route53profiles_ProfileAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/ProfileAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/ProfileAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/ProfileAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
