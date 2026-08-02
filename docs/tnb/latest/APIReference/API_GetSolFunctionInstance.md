---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionInstance.html
---

# GetSolFunctionInstance
<a name="API_GetSolFunctionInstance"></a>

Gets the details of a network function instance, including the instantiation state and metadata from the function package descriptor in the network function package.

A network function instance is a function in a function package .

## Request Syntax
<a name="API_GetSolFunctionInstance_RequestSyntax"></a>

```
GET /sol/vnflcm/v1/vnf_instances/{{vnfInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolFunctionInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [vnfInstanceId](#API_GetSolFunctionInstance_RequestSyntax) **   <a name="TNB-GetSolFunctionInstance-request-uri-vnfInstanceId"></a>
ID of the network function.
Pattern: `fi-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolFunctionInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolFunctionInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "instantiatedVnfInfo": {
      "vnfcResourceInfo": [
         {
            "metadata": {
               "cluster": "string",
               "helmChart": "string",
               "nodeGroup": "string"
            }
         }
      ],
      "vnfState": "string"
   },
   "instantiationState": "string",
   "metadata": {
      "createdAt": "string",
      "lastModified": "string"
   },
   "nsInstanceId": "string",
   "tags": {
      "string" : "string"
   },
   "vnfdId": "string",
   "vnfdVersion": "string",
   "vnfPkgId": "string",
   "vnfProductName": "string",
   "vnfProvider": "string"
}
```

## Response Elements
<a name="API_GetSolFunctionInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-arn"></a>
Network function instance ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-instance/fi-[a-f0-9]{17})`

 ** [id](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-id"></a>
Network function instance ID.
Type: String
Pattern: `fi-[a-f0-9]{17}`

 ** [instantiatedVnfInfo](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-instantiatedVnfInfo"></a>
Information about the network function.
A network function instance is a function in a function package .
Type: [GetSolVnfInfo](API_GetSolVnfInfo.md) object

 ** [instantiationState](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-instantiationState"></a>
Network function instantiation state.
Type: String
Valid Values: `INSTANTIATED | NOT_INSTANTIATED`

 ** [metadata](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-metadata"></a>
The metadata of a network function instance.
A network function instance is a function in a function package .
Type: [GetSolFunctionInstanceMetadata](API_GetSolFunctionInstanceMetadata.md) object

 ** [nsInstanceId](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-nsInstanceId"></a>
Network instance ID.
Type: String
Pattern: `ni-[a-f0-9]{17}`

 ** [tags](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [vnfdId](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-vnfdId"></a>
Function package descriptor ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [vnfdVersion](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-vnfdVersion"></a>
Function package descriptor version.
Type: String

 ** [vnfPkgId](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-vnfPkgId"></a>
Function package ID.
Type: String
Pattern: `fp-[a-f0-9]{17}`

 ** [vnfProductName](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-vnfProductName"></a>
Network function product name.
Type: String

 ** [vnfProvider](#API_GetSolFunctionInstance_ResponseSyntax) **   <a name="TNB-GetSolFunctionInstance-response-vnfProvider"></a>
Network function provider.
Type: String

## Errors
<a name="API_GetSolFunctionInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_GetSolFunctionInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolFunctionInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolFunctionInstance)
