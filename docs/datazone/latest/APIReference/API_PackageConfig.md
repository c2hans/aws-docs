---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PackageConfig.html
---

# PackageConfig
<a name="API_PackageConfig"></a>

The package configuration for a notebook run environment in Amazon SageMaker Unified Studio.

## Contents
<a name="API_PackageConfig_Contents"></a>

 ** packageManager **   <a name="datazone-Type-PackageConfig-packageManager"></a>
The package manager for the notebook run environment. The default value is `UV`.
Type: String
Valid Values: `UV`
Required: Yes

 ** packageSpecification **   <a name="datazone-Type-PackageConfig-packageSpecification"></a>
The package specification content for the notebook run environment. The maximum length is 10240 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

## See Also
<a name="API_PackageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PackageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PackageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PackageConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
