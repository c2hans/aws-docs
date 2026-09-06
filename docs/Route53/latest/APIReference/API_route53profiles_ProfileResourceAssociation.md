---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileResourceAssociation.html
---

# ProfileResourceAssociation
<a name="API_route53profiles_ProfileResourceAssociation"></a>

 The association between a Route 53 Profile and resources.

## Contents
<a name="API_route53profiles_ProfileResourceAssociation_Contents"></a>

 ** CreationTime **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-CreationTime"></a>
 The date and time that the Profile resource association was created, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Id **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-Id"></a>
 ID of the Profile resource association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ModificationTime **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-ModificationTime"></a>
 The date and time that the Profile resource association was modified, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Name **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-Name"></a>
 Name of the Profile resource association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-OwnerId"></a>
 AWS account ID of the Profile resource association owner.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ProfileId **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-ProfileId"></a>
 Profile ID of the Profile that the resources are associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceArn **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-ResourceArn"></a>
 The Amazon Resource Name (ARN) of the resource association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ResourceProperties **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-ResourceProperties"></a>
 If the DNS resource is a DNS Firewall rule group, this indicates the priority.
Type: String
Required: No

 ** ResourceType **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-ResourceType"></a>
 Resource type, such as a private hosted zone, interface VPC endpoint, Resolver query log configuration, or DNS Firewall rule group.
Type: String
Required: No

 ** Status **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-Status"></a>
 Status of the Profile resource association.
Type: String
Valid Values: `COMPLETE | DELETING | UPDATING | CREATING | DELETED | FAILED`
Required: No

 ** StatusMessage **   <a name="Route53Profiles-Type-route53profiles_ProfileResourceAssociation-StatusMessage"></a>
 Additional information about the Profile resource association.
Type: String
Required: No

## See Also
<a name="API_route53profiles_ProfileResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/ProfileResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/ProfileResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/ProfileResourceAssociation)
