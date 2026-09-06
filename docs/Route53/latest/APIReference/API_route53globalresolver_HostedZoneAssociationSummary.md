---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_HostedZoneAssociationSummary.html
---

# HostedZoneAssociationSummary
<a name="API_route53globalresolver_HostedZoneAssociationSummary"></a>

Summary information about a hosted zone association.

## Contents
<a name="API_route53globalresolver_HostedZoneAssociationSummary_Contents"></a>

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-createdAt"></a>
The date and time when the hosted zone association was created.
Type: Timestamp
Required: Yes

 ** hostedZoneId **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-hostedZoneId"></a>
The ID of the hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** hostedZoneName **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-hostedZoneName"></a>
The name of the hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-id"></a>
The unique identifier of the hosted zone association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-name"></a>
The name of the hosted zone association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** resourceArn **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource associated with the hosted zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-status"></a>
The current status of the hosted zone association.
Type: String
Valid Values: `CREATING | OPERATIONAL | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_HostedZoneAssociationSummary-updatedAt"></a>
The date and time when the hosted zone association was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_route53globalresolver_HostedZoneAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/HostedZoneAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/HostedZoneAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/HostedZoneAssociationSummary)
