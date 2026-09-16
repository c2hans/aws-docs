---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeprecateThingType.html
---

# DeprecateThingType
<a name="API_DeprecateThingType"></a>

Deprecates a thing type. You can not associate new things with deprecated thing type.

Requires permission to access the [DeprecateThingType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeprecateThingType_RequestSyntax"></a>

```
POST /thing-types/{{thingTypeName}}/deprecate HTTP/1.1
Content-type: application/json

{
   "undoDeprecate": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DeprecateThingType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingTypeName](#API_DeprecateThingType_RequestSyntax) **   <a name="iot-DeprecateThingType-request-uri-thingTypeName"></a>
The name of the thing type to deprecate.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DeprecateThingType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [undoDeprecate](#API_DeprecateThingType_RequestSyntax) **   <a name="iot-DeprecateThingType-request-undoDeprecate"></a>
Whether to undeprecate a deprecated thing type. If **true**, the thing type will not be deprecated anymore and you can associate it with things.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DeprecateThingType_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeprecateThingType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeprecateThingType_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DeprecateThingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeprecateThingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeprecateThingType)
