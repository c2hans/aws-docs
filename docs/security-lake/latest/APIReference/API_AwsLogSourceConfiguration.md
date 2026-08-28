---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsLogSourceConfiguration.html
---

# AwsLogSourceConfiguration
<a name="API_AwsLogSourceConfiguration"></a>

To add a natively-supported AWS service as a log source, use these parameters to specify the configuration settings for the log source.

## Contents
<a name="API_AwsLogSourceConfiguration_Contents"></a>

 ** regions **   <a name="securitylake-Type-AwsLogSourceConfiguration-regions"></a>
Specify the Regions where you want to enable Security Lake.
Type: Array of strings
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: Yes

 ** sourceName **   <a name="securitylake-Type-AwsLogSourceConfiguration-sourceName"></a>
The name for a AWS source.
Type: String
Valid Values: `ROUTE53 | VPC_FLOW | SH_FINDINGS | CLOUD_TRAIL_MGMT | LAMBDA_EXECUTION | S3_DATA | EKS_AUDIT | WAF`
Required: Yes

 ** accounts **   <a name="securitylake-Type-AwsLogSourceConfiguration-accounts"></a>
Specify the AWS account information where you want to enable Security Lake.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** sourceVersion **   <a name="securitylake-Type-AwsLogSourceConfiguration-sourceVersion"></a>
The version for a AWS source.
Type: String
Pattern: `(latest|[0-9]\.[0-9])`
Required: No

## See Also
<a name="API_AwsLogSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/AwsLogSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/AwsLogSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/AwsLogSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
