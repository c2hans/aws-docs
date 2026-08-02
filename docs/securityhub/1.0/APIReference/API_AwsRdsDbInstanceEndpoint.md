---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbInstanceEndpoint.html
---

# AwsRdsDbInstanceEndpoint
<a name="API_AwsRdsDbInstanceEndpoint"></a>

Specifies the connection endpoint.

## Contents
<a name="API_AwsRdsDbInstanceEndpoint_Contents"></a>

 ** Address **   <a name="securityhub-Type-AwsRdsDbInstanceEndpoint-Address"></a>
Specifies the DNS address of the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostedZoneId **   <a name="securityhub-Type-AwsRdsDbInstanceEndpoint-HostedZoneId"></a>
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Port **   <a name="securityhub-Type-AwsRdsDbInstanceEndpoint-Port"></a>
Specifies the port that the database engine is listening on.
Type: Integer
Required: No

## See Also
<a name="API_AwsRdsDbInstanceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbInstanceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbInstanceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbInstanceEndpoint)
