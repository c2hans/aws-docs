---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ExportingConfig.html
---

# ExportingConfig
<a name="API_connect-customer-profiles_ExportingConfig"></a>

Configuration information about the S3 bucket where Identity Resolution Jobs writes result files.

**Note**
You need to give Customer Profiles service principal write permission to your S3 bucket. Otherwise, you'll get an exception in the API response. For an example policy, see [Amazon Connect Customer Profiles cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html#customer-profiles-cross-service).

## Contents
<a name="API_connect-customer-profiles_ExportingConfig_Contents"></a>

 ** S3Exporting **   <a name="connect-Type-connect-customer-profiles_ExportingConfig-S3Exporting"></a>
The S3 location where Identity Resolution Jobs write result files.
Type: [S3ExportingConfig](API_connect-customer-profiles_S3ExportingConfig.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_ExportingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ExportingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ExportingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ExportingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
