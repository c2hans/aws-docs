---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ComputeConfig.html
---

# ComputeConfig
<a name="API_ComputeConfig"></a>

The compute configuration for a notebook run in Amazon SageMaker Unified Studio.

## Contents
<a name="API_ComputeConfig_Contents"></a>

 ** environmentVersion **   <a name="datazone-Type-ComputeConfig-environmentVersion"></a>
The environment version for the notebook run compute.
Type: String
Required: No

 ** instanceType **   <a name="datazone-Type-ComputeConfig-instanceType"></a>
The instance type for the notebook run compute.
Type: String
Pattern: `(ml|sc)\.[a-z][0-9]+[a-z]*\.[a-z0-9]+`
Required: No

## See Also
<a name="API_ComputeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ComputeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ComputeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ComputeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
