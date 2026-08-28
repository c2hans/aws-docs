---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_FailedConfiguration.html
---

# FailedConfiguration
<a name="API_FailedConfiguration"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 A configuration ID paired with an error message.

## Contents
<a name="API_FailedConfiguration_Contents"></a>

 ** configurationId **   <a name="DiscServ-Type-FailedConfiguration-configurationId"></a>
 The unique identifier of the configuration the failed to delete.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: No

 ** errorMessage **   <a name="DiscServ-Type-FailedConfiguration-errorMessage"></a>
 A descriptive message indicating why the associated configuration failed to delete.
Type: String
Required: No

 ** errorStatusCode **   <a name="DiscServ-Type-FailedConfiguration-errorStatusCode"></a>
 The integer error code associated with the error message.
Type: Integer
Required: No

## See Also
<a name="API_FailedConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/FailedConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/FailedConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/FailedConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
