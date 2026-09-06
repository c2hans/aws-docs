---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PayerResponsibilityEntry.html
---

# PayerResponsibilityEntry
<a name="API_PayerResponsibilityEntry"></a>

Describes a payer responsibility setting for a VPC endpoint.

## Contents
<a name="API_PayerResponsibilityEntry_Contents"></a>

 ** payerResponsibilityType **
The AWS account to which the usage is charged.
Type: String
Valid Values: `vpc-endpoint-account | vpc-endpoint-service-account`
Required: No

 ** scope **
The scope of usage/charges.
Type: String
Valid Values: `vpc-endpoint-charges`
Required: No

## See Also
<a name="API_PayerResponsibilityEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PayerResponsibilityEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PayerResponsibilityEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PayerResponsibilityEntry)
