---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_LastActiveDefinition.html
---

# LastActiveDefinition
<a name="API_LastActiveDefinition"></a>

When there are multiple versions of a blueprint and the latest version has some errors, this attribute indicates the last successful blueprint definition that is available with the service.

## Contents
<a name="API_LastActiveDefinition_Contents"></a>

 ** BlueprintLocation **   <a name="Glue-Type-LastActiveDefinition-BlueprintLocation"></a>
Specifies a path in Amazon S3 where the blueprint is published by the AWS Glue developer.
Type: String
Required: No

 ** BlueprintServiceLocation **   <a name="Glue-Type-LastActiveDefinition-BlueprintServiceLocation"></a>
Specifies a path in Amazon S3 where the blueprint is copied when you create or update the blueprint.
Type: String
Required: No

 ** Description **   <a name="Glue-Type-LastActiveDefinition-Description"></a>
The description of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-LastActiveDefinition-LastModifiedOn"></a>
The date and time the blueprint was last modified.
Type: Timestamp
Required: No

 ** ParameterSpec **   <a name="Glue-Type-LastActiveDefinition-ParameterSpec"></a>
A JSON string specifying the parameters for the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: No

## See Also
<a name="API_LastActiveDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/LastActiveDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/LastActiveDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/LastActiveDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
