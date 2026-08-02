---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsLogSourceResource.html
---

# AwsLogSourceResource
<a name="API_AwsLogSourceResource"></a>

Amazon Security Lake can collect logs and events from natively-supported AWS services.

## Contents
<a name="API_AwsLogSourceResource_Contents"></a>

 ** sourceName **   <a name="securitylake-Type-AwsLogSourceResource-sourceName"></a>
The name for a AWS source. This must be a Regionally unique value.
Type: String
Valid Values: `ROUTE53 | VPC_FLOW | SH_FINDINGS | CLOUD_TRAIL_MGMT | LAMBDA_EXECUTION | S3_DATA | EKS_AUDIT | WAF`
Required: No

 ** sourceVersion **   <a name="securitylake-Type-AwsLogSourceResource-sourceVersion"></a>
The version for a AWS source. This must be a Regionally unique value.
Type: String
Pattern: `(latest|[0-9]\.[0-9])`
Required: No

## See Also
<a name="API_AwsLogSourceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/AwsLogSourceResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/AwsLogSourceResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/AwsLogSourceResource)
