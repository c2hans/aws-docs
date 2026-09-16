---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeComputationModel.html
---

# DescribeComputationModel
<a name="API_DescribeComputationModel"></a>

Retrieves information about a computation model.

## Request Syntax
<a name="API_DescribeComputationModel_RequestSyntax"></a>

```
GET /computation-models/{{computationModelId}}?computationModelVersion={{computationModelVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeComputationModel_RequestParameters"></a>

The request uses the following URI parameters.

 ** [computationModelId](#API_DescribeComputationModel_RequestSyntax) **   <a name="iotsitewise-DescribeComputationModel-request-uri-computationModelId"></a>
The ID of the computation model.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [computationModelVersion](#API_DescribeComputationModel_RequestSyntax) **   <a name="iotsitewise-DescribeComputationModel-request-uri-computationModelVersion"></a>
The version of the computation model.
Pattern: `^(LATEST|ACTIVE|[1-9]{1}\d{0,9})$`

## Request Body
<a name="API_DescribeComputationModel_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeComputationModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionDefinitions": [
      {
         "actionDefinitionId": "string",
         "actionName": "string",
         "actionType": "string"
      }
   ],
   "computationModelArn": "string",
   "computationModelConfiguration": {
      "anomalyDetection": {
         "inputProperties": "string",
         "resultProperty": "string"
      }
   },
   "computationModelCreationDate": number,
   "computationModelDataBinding": {
      "string" : {
         "assetModelProperty": {
            "assetModelId": "string",
            "propertyId": "string"
         },
         "assetProperty": {
            "assetId": "string",
            "propertyId": "string"
         },
         "list": [
            "ComputationModelDataBindingValue"
         ]
      }
   },
   "computationModelDescription": "string",
   "computationModelId": "string",
   "computationModelLastUpdateDate": number,
   "computationModelName": "string",
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
   },
   "computationModelVersion": "string"
}
```

## Response Elements
<a name="API_DescribeComputationModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionDefinitions](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-actionDefinitions"></a>
The available actions for this computation model.
Type: Array of [ActionDefinition](API_ActionDefinition.md) objects

 ** [computationModelArn](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the computation model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [computationModelConfiguration](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelConfiguration"></a>
The configuration for the computation model.
Type: [ComputationModelConfiguration](API_ComputationModelConfiguration.md) object

 ** [computationModelCreationDate](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelCreationDate"></a>
The model creation date, in Unix epoch time.
Type: Timestamp

 ** [computationModelDataBinding](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelDataBinding"></a>
The data binding for the computation model. Key is a variable name defined in configuration. Value is a `ComputationModelDataBindingValue` referenced by the variable.
Type: String to [ComputationModelDataBindingValue](API_ComputationModelDataBindingValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-z][a-z0-9_]*$`

 ** [computationModelDescription](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelDescription"></a>
The description of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9 _\-#$*!@]+$`

 ** [computationModelId](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelId"></a>
The ID of the computation model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [computationModelLastUpdateDate](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelLastUpdateDate"></a>
The date the model was last updated, in Unix epoch time.
Type: Timestamp

 ** [computationModelName](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelName"></a>
The name of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`

 ** [computationModelStatus](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelStatus"></a>
The current status of the asset model, which contains a state and an error message if any.
Type: [ComputationModelStatus](API_ComputationModelStatus.md) object

 ** [computationModelVersion](#API_DescribeComputationModel_ResponseSyntax) **   <a name="iotsitewise-DescribeComputationModel-response-computationModelVersion"></a>
The version of the computation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

## Errors
<a name="API_DescribeComputationModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeComputationModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeComputationModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeComputationModel)
