---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PutResourceConfiguration.html
---

# PutResourceConfiguration
<a name="API_PutResourceConfiguration"></a>

The resource configuration that is used to configure the environment blueprint.

## Contents
<a name="API_PutResourceConfiguration_Contents"></a>

 ** name **   <a name="datazone-Type-PutResourceConfiguration-name"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** parameters **   <a name="datazone-Type-PutResourceConfiguration-parameters"></a>
The parameters of the resource configuration.
Type: String to string map
Required: Yes

 ** region **   <a name="datazone-Type-PutResourceConfiguration-region"></a>
The AWS Region of the resource configuration.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: Yes

 ** description **   <a name="datazone-Type-PutResourceConfiguration-description"></a>
The description of the resource configuration.
Type: String
Required: No

## See Also
<a name="API_PutResourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PutResourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PutResourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PutResourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
