---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HostedZoneOwner.html
---

# HostedZoneOwner
<a name="API_HostedZoneOwner"></a>

A complex type that identifies a hosted zone that a specified Amazon VPC is associated with and the owner of the hosted zone. If there is a value for `OwningAccount`, there is no value for `OwningService`, and vice versa.

## Contents
<a name="API_HostedZoneOwner_Contents"></a>

 ** OwningAccount **   <a name="Route53-Type-HostedZoneOwner-OwningAccount"></a>
If the hosted zone was created by an AWS account, or was created by an AWS service that creates hosted zones using the current account, `OwningAccount` contains the account ID of that account. For example, when you use AWS Cloud Map to create a hosted zone, Cloud Map creates the hosted zone using the current AWS account.
Type: String
Required: No

 ** OwningService **   <a name="Route53-Type-HostedZoneOwner-OwningService"></a>
If an AWS service uses its own account to create a hosted zone and associate the specified VPC with that hosted zone, `OwningService` contains an abbreviation that identifies the service. For example, if Amazon Elastic File System (Amazon EFS) created a hosted zone and associated a VPC with the hosted zone, the value of `OwningService` is `efs.amazonaws.com`.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_HostedZoneOwner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HostedZoneOwner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HostedZoneOwner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HostedZoneOwner)
