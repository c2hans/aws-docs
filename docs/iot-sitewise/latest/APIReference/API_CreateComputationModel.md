---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateComputationModel.html
---

# CreateComputationModel
<a name="API_CreateComputationModel"></a>

Create a computation model with a configuration and data binding.

## Request Syntax
<a name="API_CreateComputationModel_RequestSyntax"></a>

```
POST /computation-models HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "computationModelConfiguration": {
      "anomalyDetection": {
         "inputProperties": "{{string}}",
         "resultProperty": "{{string}}"
      }
   },
   "computationModelDataBinding": {
      "{{string}}" : {
         "assetModelProperty": {
            "assetModelId": "{{string}}",
            "propertyId": "{{string}}"
         },
         "assetProperty": {
            "assetId": "{{string}}",
            "propertyId": "{{string}}"
         },
         "list": [
            "ComputationModelDataBindingValue"
         ]
      }
   },
   "computationModelDescription": "{{string}}",
   "computationModelName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateComputationModel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateComputationModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [computationModelConfiguration](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-computationModelConfiguration"></a>
The configuration for the computation model.
Type: [ComputationModelConfiguration](API_ComputationModelConfiguration.md) object
Required: Yes

 ** [computationModelDataBinding](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-computationModelDataBinding"></a>
The data binding for the computation model. Key is a variable name defined in configuration. Value is a `ComputationModelDataBindingValue` referenced by the variable.
Type: String to [ComputationModelDataBindingValue](API_ComputationModelDataBindingValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-z][a-z0-9_]*$`
Required: Yes

 ** [computationModelDescription](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-computationModelDescription"></a>
The description of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`
Required: No

 ** [computationModelName](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-computationModelName"></a>
The name of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`
Required: Yes

 ** [tags](#API_CreateComputationModel_RequestSyntax) **   <a name="iotsitewise-CreateComputationModel-request-tags"></a>
A list of key-value pairs that contain metadata for the asset. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the * AWS IoT SiteWise User Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateComputationModel_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "computationModelArn": "string",
   "computationModelId": "string",
   "computationModelStatus": {
      "error": {
         "code": "string",
         "details": [
            {
               "code": "string",
               "message": "string"
            }
         ],
         "message": "string"
      },
      "state": "string"
   }
}
```

## Response Elements
<a name="API_CreateComputationModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [computationModelArn](#API_CreateComputationModel_ResponseSyntax) **   <a name="iotsitewise-CreateComputationModel-response-computationModelArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the computation model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [computationModelId](#API_CreateComputationModel_ResponseSyntax) **   <a name="iotsitewise-CreateComputationModel-response-computationModelId"></a>
The ID of the computation model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [computationModelStatus](#API_CreateComputationModel_ResponseSyntax) **   <a name="iotsitewise-CreateComputationModel-response-computationModelStatus"></a>
The status of the computation model, containing a state (CREATING after successfully calling this operation) and any error messages.
Type: [ComputationModelStatus](API_ComputationModelStatus.md) object

## Errors
<a name="API_CreateComputationModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** resourceArn **
The ARN of the resource that already exists.
 ** resourceId **
The ID of the resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateComputationModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateComputationModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateComputationModel)
