---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_S3AccessPoint.html
---

# S3AccessPoint
<a name="API_S3AccessPoint"></a>

Describes the S3 access point configuration of the S3 access point attachment.

## Contents
<a name="API_S3AccessPoint_Contents"></a>

 ** Alias **   <a name="FSx-Type-S3AccessPoint-Alias"></a>
The S3 access point's alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[0-9a-z\\-]{1,63}`
Required: No

 ** ResourceARN **   <a name="FSx-Type-S3AccessPoint-ResourceARN"></a>
he S3 access point's ARN.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`
Required: No

 ** VpcConfiguration **   <a name="FSx-Type-S3AccessPoint-VpcConfiguration"></a>
The S3 access point's virtual private cloud (VPC) configuration.
Type: [S3AccessPointVpcConfiguration](API_S3AccessPointVpcConfiguration.md) object
Required: No

## See Also
<a name="API_S3AccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
