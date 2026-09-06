---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteAudienceModel.html
---

# DeleteAudienceModel
<a name="API_DeleteAudienceModel"></a>

Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.

## Request Syntax
<a name="API_DeleteAudienceModel_RequestSyntax"></a>

```
DELETE /audience-model/{{audienceModelArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAudienceModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [audienceModelArn](#API_DeleteAudienceModel_RequestSyntax) **   <a name="API-DeleteAudienceModel-request-uri-audienceModelArn"></a>
The Amazon Resource Name (ARN) of the audience model that you want to delete.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_DeleteAudienceModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAudienceModel_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAudienceModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAudienceModel_Errors"></a>

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
<a name="API_DeleteAudienceModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/DeleteAudienceModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/DeleteAudienceModel)
