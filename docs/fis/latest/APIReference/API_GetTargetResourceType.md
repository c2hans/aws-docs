---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_GetTargetResourceType.html
---

# GetTargetResourceType
<a name="API_GetTargetResourceType"></a>

Gets information about the specified resource type.

## Request Syntax
<a name="API_GetTargetResourceType_RequestSyntax"></a>

```
GET /targetResourceTypes/{{resourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTargetResourceType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceType](#API_GetTargetResourceType_RequestSyntax) **   <a name="fis-GetTargetResourceType-request-uri-resourceType"></a>
The resource type.
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: Yes

## Request Body
<a name="API_GetTargetResourceType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTargetResourceType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "targetResourceType": {
      "description": "string",
      "parameters": {
         "string" : {
            "description": "string",
            "required": boolean
         }
      },
      "resourceType": "string"
   }
}
```

## Response Elements
<a name="API_GetTargetResourceType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [targetResourceType](#API_GetTargetResourceType_ResponseSyntax) **   <a name="fis-GetTargetResourceType-response-targetResourceType"></a>
Information about the resource type.
Type: [TargetResourceType](API_TargetResourceType.md) object

## Errors
<a name="API_GetTargetResourceType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ValidationException **
The specified input is not valid, or fails to satisfy the constraints for the request.
HTTP Status Code: 400

## See Also
<a name="API_GetTargetResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fis-2020-12-01/GetTargetResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/GetTargetResourceType)
