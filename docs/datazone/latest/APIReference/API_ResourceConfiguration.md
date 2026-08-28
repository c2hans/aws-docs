---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ResourceConfiguration.html
---

# ResourceConfiguration
<a name="API_ResourceConfiguration"></a>

The details of the resource configuration.

## Contents
<a name="API_ResourceConfiguration_Contents"></a>

 ** identifier **   <a name="datazone-Type-ResourceConfiguration-identifier"></a>
The identifier of the resource configuration.
Type: String
Required: Yes

 ** name **   <a name="datazone-Type-ResourceConfiguration-name"></a>
The name of the resource configuration.
Type: String
Required: Yes

 ** parameters **   <a name="datazone-Type-ResourceConfiguration-parameters"></a>
The parameters of the resource configuration.
Type: String to string map
Required: Yes

 ** region **   <a name="datazone-Type-ResourceConfiguration-region"></a>
The AWS Region of the resource configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: Yes

 ** description **   <a name="datazone-Type-ResourceConfiguration-description"></a>
The description of the resource configuration.
Type: String
Required: No

## See Also
<a name="API_ResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ResourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
