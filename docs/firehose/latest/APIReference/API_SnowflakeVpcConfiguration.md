---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeVpcConfiguration.html
---

# SnowflakeVpcConfiguration
<a name="API_SnowflakeVpcConfiguration"></a>

Configure a Snowflake VPC

## Contents
<a name="API_SnowflakeVpcConfiguration_Contents"></a>

 ** PrivateLinkVpceId **   <a name="Firehose-Type-SnowflakeVpcConfiguration-PrivateLinkVpceId"></a>
The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
Type: String
Length Constraints: Minimum length of 47. Maximum length of 255.
Pattern: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
Required: Yes

## See Also
<a name="API_SnowflakeVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SnowflakeVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SnowflakeVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SnowflakeVpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
