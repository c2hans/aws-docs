---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteTrainedModelOutput.html
---

# DeleteTrainedModelOutput
<a name="API_DeleteTrainedModelOutput"></a>

Deletes the model artifacts stored by the service.

## Request Syntax
<a name="API_DeleteTrainedModelOutput_RequestSyntax"></a>

```
DELETE /memberships/{{membershipIdentifier}}/trained-models/{{trainedModelArn}}?versionIdentifier={{versionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrainedModelOutput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_DeleteTrainedModelOutput_RequestSyntax) **   <a name="API-DeleteTrainedModelOutput-request-uri-membershipIdentifier"></a>
The membership ID of the member that is deleting the trained model output.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [trainedModelArn](#API_DeleteTrainedModelOutput_RequestSyntax) **   <a name="API-DeleteTrainedModelOutput-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model whose output you want to delete.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [versionIdentifier](#API_DeleteTrainedModelOutput_RequestSyntax) **   <a name="API-DeleteTrainedModelOutput-request-uri-versionIdentifier"></a>
The version identifier of the trained model to delete. If not specified, the operation will delete the base version of the trained model. When specified, only the particular version will be deleted.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_DeleteTrainedModelOutput_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrainedModelOutput_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTrainedModelOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTrainedModelOutput_Errors"></a>

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
<a name="API_DeleteTrainedModelOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/DeleteTrainedModelOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
