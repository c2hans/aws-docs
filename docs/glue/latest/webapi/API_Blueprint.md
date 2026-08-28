---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Blueprint.html
---

# Blueprint
<a name="API_Blueprint"></a>

The details of a blueprint.

## Contents
<a name="API_Blueprint_Contents"></a>

 ** BlueprintLocation **   <a name="Glue-Type-Blueprint-BlueprintLocation"></a>
Specifies the path in Amazon S3 where the blueprint is published.
Type: String
Required: No

 ** BlueprintServiceLocation **   <a name="Glue-Type-Blueprint-BlueprintServiceLocation"></a>
Specifies a path in Amazon S3 where the blueprint is copied when you call `CreateBlueprint/UpdateBlueprint` to register the blueprint in AWS Glue.
Type: String
Required: No

 ** CreatedOn **   <a name="Glue-Type-Blueprint-CreatedOn"></a>
The date and time the blueprint was registered.
Type: Timestamp
Required: No

 ** Description **   <a name="Glue-Type-Blueprint-Description"></a>
The description of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** ErrorMessage **   <a name="Glue-Type-Blueprint-ErrorMessage"></a>
An error message.
Type: String
Required: No

 ** LastActiveDefinition **   <a name="Glue-Type-Blueprint-LastActiveDefinition"></a>
When there are multiple versions of a blueprint and the latest version has some errors, this attribute indicates the last successful blueprint definition that is available with the service.
Type: [LastActiveDefinition](API_LastActiveDefinition.md) object
Required: No

 ** LastModifiedOn **   <a name="Glue-Type-Blueprint-LastModifiedOn"></a>
The date and time the blueprint was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="Glue-Type-Blueprint-Name"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** ParameterSpec **   <a name="Glue-Type-Blueprint-ParameterSpec"></a>
A JSON string that indicates the list of parameter specifications for the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: No

 ** Status **   <a name="Glue-Type-Blueprint-Status"></a>
The status of the blueprint registration.
+ Creating — The blueprint registration is in progress.
+ Active — The blueprint has been successfully registered.
+ Updating — An update to the blueprint registration is in progress.
+ Failed — The blueprint registration failed.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | FAILED`
Required: No

## See Also
<a name="API_Blueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Blueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Blueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Blueprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
