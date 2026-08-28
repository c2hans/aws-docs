---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartTrainedModelExportJob.html
---

# StartTrainedModelExportJob
<a name="API_StartTrainedModelExportJob"></a>

Provides the information necessary to start a trained model export job.

## Request Syntax
<a name="API_StartTrainedModelExportJob_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/trained-models/{{trainedModelArn}}/export-jobs HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "outputConfiguration": {
      "members": [
         {
            "accountId": "{{string}}"
         }
      ]
   },
   "trainedModelVersionIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTrainedModelExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-uri-membershipIdentifier"></a>
The membership ID of the member that is receiving the exported trained model artifacts.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [trainedModelArn](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that you want to export.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_StartTrainedModelExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-description"></a>
The description of the trained model export job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [name](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-name"></a>
The name of the trained model export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [outputConfiguration](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-outputConfiguration"></a>
The output configuration information for the trained model export job.
Type: [TrainedModelExportOutputConfiguration](API_TrainedModelExportOutputConfiguration.md) object
Required: Yes

 ** [trainedModelVersionIdentifier](#API_StartTrainedModelExportJob_RequestSyntax) **   <a name="API-StartTrainedModelExportJob-request-trainedModelVersionIdentifier"></a>
The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## Response Syntax
<a name="API_StartTrainedModelExportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartTrainedModelExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartTrainedModelExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_StartTrainedModelExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/StartTrainedModelExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/StartTrainedModelExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
