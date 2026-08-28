---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_HttpPackageConfiguration.html
---

# HttpPackageConfiguration
<a name="API_HttpPackageConfiguration"></a>

The HTTP package configuration properties for the requested VOD source.

## Contents
<a name="API_HttpPackageConfiguration_Contents"></a>

 ** Path **   <a name="mediatailor-Type-HttpPackageConfiguration-Path"></a>
The relative path to the URL for this VOD source. This is combined with `SourceLocation::HttpConfiguration::BaseUrl` to form a valid URL.
Type: String
Required: Yes

 ** SourceGroup **   <a name="mediatailor-Type-HttpPackageConfiguration-SourceGroup"></a>
The name of the source group. This has to match one of the `Channel::Outputs::SourceGroup`.
Type: String
Required: Yes

 ** Type **   <a name="mediatailor-Type-HttpPackageConfiguration-Type"></a>
The streaming protocol for this package configuration. Supported values are `HLS` and `DASH`.
Type: String
Valid Values: `DASH | HLS`
Required: Yes

## See Also
<a name="API_HttpPackageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/HttpPackageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/HttpPackageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/HttpPackageConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
