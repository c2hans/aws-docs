---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_BadRequestDetails.html
---

# BadRequestDetails
<a name="API_BadRequestDetails"></a>

Detailed information about the input that failed to satisfy the constraints specified by a call.

## Contents
<a name="API_BadRequestDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** InvalidConfiguration **   <a name="appconfig-Type-BadRequestDetails-InvalidConfiguration"></a>
Detailed information about the bad request exception error when creating a hosted configuration version.
Type: Array of [InvalidConfigurationDetail](API_InvalidConfigurationDetail.md) objects
Required: No

## See Also
<a name="API_BadRequestDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/BadRequestDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/BadRequestDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/BadRequestDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
