---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteTrainingDataset.html
---

# DeleteTrainingDataset
<a name="API_DeleteTrainingDataset"></a>

Specifies a training dataset that you want to delete. You can't delete a training dataset if there are any audience models that depend on the training dataset. In Clean Rooms ML, the `TrainingDataset` is metadata that points to a Glue table, which is read only during `AudienceModel` creation. This action deletes the metadata.

## Request Syntax
<a name="API_DeleteTrainingDataset_RequestSyntax"></a>

```
DELETE /training-dataset/{{trainingDatasetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrainingDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trainingDatasetArn](#API_DeleteTrainingDataset_RequestSyntax) **   <a name="API-DeleteTrainingDataset-request-uri-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset that you want to delete.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_DeleteTrainingDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrainingDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTrainingDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTrainingDataset_Errors"></a>

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

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_DeleteTrainingDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/DeleteTrainingDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/DeleteTrainingDataset)
