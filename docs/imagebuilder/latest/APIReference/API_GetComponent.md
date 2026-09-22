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
The Amazon Resource Name (ARN) of the component that you want to get. You can specify a build version ARN, or a component version ARN. The version can use the `x` wildcard in trailing positions, for example `1.0.x` or `1.x.x`. Version ARNs resolve to the latest available matching component build version.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
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
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_GetComponent_ResponseSyntax) **   <a name="imagebuilder-GetComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetComponent_Examples"></a>

### Get the details of a component build version
<a name="API_GetComponent_Example_1"></a>

The following example retrieves a component build version. The data field in the response contains the YAML document that defines the component.

#### Sample Request
<a name="API_GetComponent_Example_1_Request"></a>

```
GET /GetComponent?componentBuildVersionArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Acomponent%2Fmy-example-component%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_GetComponent_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "f5401098-035f-4be2-9eee-784c388ed04b",
    "component": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1",
        "name": "my-example-component",
        "version": "1.0.0",
        "description": "Installs the latest version of my application",
        "changeDescription": "Initial version",
        "type": "BUILD",
        "platform": "Linux",
        "state": {
            "status": "ACTIVE"
        },
        "owner": "111122223333",
        "data": "name: InstallMyApp\ndescription: Installs my application\nschemaVersion: 1.0\nphases:\n  - name: build\n    steps:\n      - name: InstallApp\n        action: ExecuteBash\n        inputs:\n          commands:\n            - sudo yum -y install my-app\n",
        "encrypted": true,
        "dateCreated": "2026-09-09T18:31:30.404Z",
        "tags": {}
    },
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0"
    }
}
```

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
