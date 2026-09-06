---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRoute53HostedZoneObjectDetails.html
---

# AwsRoute53HostedZoneObjectDetails
<a name="API_AwsRoute53HostedZoneObjectDetails"></a>

 An object that contains information about an Amazon Route 53 hosted zone.

## Contents
<a name="API_AwsRoute53HostedZoneObjectDetails_Contents"></a>

 ** Config **   <a name="securityhub-Type-AwsRoute53HostedZoneObjectDetails-Config"></a>
 An object that includes the `Comment` element.
Type: [AwsRoute53HostedZoneConfigDetails](API_AwsRoute53HostedZoneConfigDetails.md) object
Required: No

 ** Id **   <a name="securityhub-Type-AwsRoute53HostedZoneObjectDetails-Id"></a>
 The ID that Route 53 assigns to the hosted zone when you create it.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsRoute53HostedZoneObjectDetails-Name"></a>
 The name of the domain. For public hosted zones, this is the name that you have registered with your DNS registrar.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRoute53HostedZoneObjectDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRoute53HostedZoneObjectDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRoute53HostedZoneObjectDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRoute53HostedZoneObjectDetails)
