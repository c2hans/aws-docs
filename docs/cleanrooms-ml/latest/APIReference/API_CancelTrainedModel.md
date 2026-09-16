---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CancelTrainedModel.html
---

# CancelTrainedModel
<a name="API_CancelTrainedModel"></a>

Submits a request to cancel the trained model job.

## Request Syntax
<a name="API_CancelTrainedModel_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/trained-models/{{trainedModelArn}}?versionIdentifier={{versionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelTrainedModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CancelTrainedModel_RequestSyntax) **   <a name="API-CancelTrainedModel-request-uri-membershipIdentifier"></a>
The membership ID of the trained model job that you want to cancel.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [trainedModelArn](#API_CancelTrainedModel_RequestSyntax) **   <a name="API-CancelTrainedModel-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model job that you want to cancel.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [versionIdentifier](#API_CancelTrainedModel_RequestSyntax) **   <a name="API-CancelTrainedModel-request-uri-versionIdentifier"></a>
The version identifier of the trained model to cancel. This parameter allows you to specify which version of the trained model you want to cancel when multiple versions exist.
If `versionIdentifier` is not specified, the base model will be cancelled.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_CancelTrainedModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelTrainedModel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelTrainedModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelTrainedModel_Errors"></a>

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
<a name="API_CancelTrainedModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CancelTrainedModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CancelTrainedModel)
