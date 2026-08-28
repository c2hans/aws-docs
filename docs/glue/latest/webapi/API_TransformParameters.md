---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TransformParameters.html
---

# TransformParameters
<a name="API_TransformParameters"></a>

The algorithm-specific parameters that are associated with the machine learning transform.

## Contents
<a name="API_TransformParameters_Contents"></a>

 ** TransformType **   <a name="Glue-Type-TransformParameters-TransformType"></a>
The type of machine learning transform.
For information about the types of machine learning transforms, see [Creating Machine Learning Transforms](https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html).
Type: String
Valid Values: `FIND_MATCHES`
Required: Yes

 ** FindMatchesParameters **   <a name="Glue-Type-TransformParameters-FindMatchesParameters"></a>
The parameters for the find matches algorithm.
Type: [FindMatchesParameters](API_FindMatchesParameters.md) object
Required: No

## See Also
<a name="API_TransformParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TransformParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TransformParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TransformParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
