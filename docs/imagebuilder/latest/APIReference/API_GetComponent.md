---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetComponent.html
---

# GetComponent
<a name="API_GetComponent"></a>

Retrieves a component object.

## Request Syntax
<a name="API_GetComponent_RequestSyntax"></a>

```
GET /GetComponent?componentBuildVersionArn={{componentBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetComponent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [componentBuildVersionArn](#API_GetComponent_RequestSyntax) **   <a name="imagebuilder-GetComponent-request-uri-componentBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the component that you want to get. Regex requires the suffix `/\d+$`.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

## Request Body
<a name="API_GetComponent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "component": {
      "arn": "string",
      "changeDescription": "string",
      "data": "string",
      "dateCreated": "string",
      "description": "string",
      "encrypted": boolean,
      "kmsKeyId": "string",
      "name": "string",
      "obfuscate": boolean,
      "owner": "string",
      "parameters": [
         {
            "defaultValue": [ "string" ],
            "description": "string",
            "name": "string",
            "type": "string"
         }
      ],
      "platform": "string",
      "productCodes": [
         {
            "productCodeId": "string",
            "productCodeType": "string"
         }
      ],
      "publisher": "string",
      "state": {
         "reason": "string",
         "status": "string"
      },
      "supportedOsVersions": [ "string" ],
      "tags": {
         "string" : "string"
      },
      "type": "string",
      "version": "string"
   },
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_GetComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [component](#API_GetComponent_ResponseSyntax) **   <a name="imagebuilder-GetComponent-response-component"></a>
The component object specified in the request.
Type: [Component](API_Component.md) object

 ** [latestVersionReferences](#API_GetComponent_ResponseSyntax) **   <a name="imagebuilder-GetComponent-response-latestVersionReferences"></a>
The resource ARNs with different wildcard variations of semantic versioning.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_GetComponent_ResponseSyntax) **   <a name="imagebuilder-GetComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_GetComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetComponent)
