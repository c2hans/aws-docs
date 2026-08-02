---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BlueprintRun.html
---

# BlueprintRun
<a name="API_BlueprintRun"></a>

The details of a blueprint run.

## Contents
<a name="API_BlueprintRun_Contents"></a>

 ** BlueprintName **   <a name="Glue-Type-BlueprintRun-BlueprintName"></a>
The name of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** CompletedOn **   <a name="Glue-Type-BlueprintRun-CompletedOn"></a>
The date and time that the blueprint run completed.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-BlueprintRun-ErrorMessage"></a>
Indicates any errors that are seen while running the blueprint.
Type: String
Required: No

 ** Parameters **   <a name="Glue-Type-BlueprintRun-Parameters"></a>
The blueprint parameters as a string. You will have to provide a value for each key that is required from the parameter spec that is defined in the `Blueprint$ParameterSpec`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: No

 ** RoleArn **   <a name="Glue-Type-BlueprintRun-RoleArn"></a>
The role ARN. This role will be assumed by the AWS Glue service and will be used to create the workflow and other entities of a workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws[^:]*:iam::[0-9]*:role/.+`
Required: No

 ** RollbackErrorMessage **   <a name="Glue-Type-BlueprintRun-RollbackErrorMessage"></a>
If there are any errors while creating the entities of a workflow, we try to roll back the created entities until that point and delete them. This attribute indicates the errors seen while trying to delete the entities that are created.
Type: String
Required: No

 ** RunId **   <a name="Glue-Type-BlueprintRun-RunId"></a>
The run ID for this blueprint run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** StartedOn **   <a name="Glue-Type-BlueprintRun-StartedOn"></a>
The date and time that the blueprint run started.
Type: Timestamp
Required: No

 ** State **   <a name="Glue-Type-BlueprintRun-State"></a>
The state of the blueprint run. Possible values are:
+ Running — The blueprint run is in progress.
+ Succeeded — The blueprint run completed successfully.
+ Failed — The blueprint run failed and rollback is complete.
+ Rolling Back — The blueprint run failed and rollback is in progress.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED | ROLLING_BACK`
Required: No

 ** WorkflowName **   <a name="Glue-Type-BlueprintRun-WorkflowName"></a>
The name of a workflow that is created as a result of a successful blueprint run. If a blueprint run has an error, there will not be a workflow created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_BlueprintRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BlueprintRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BlueprintRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BlueprintRun)
