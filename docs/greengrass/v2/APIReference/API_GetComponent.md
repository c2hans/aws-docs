---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html
---

# GetComponent
<a name="API_GetComponent"></a>

Gets the recipe for a version of a component.

## Request Syntax
<a name="API_GetComponent_RequestSyntax"></a>

```
GET /greengrass/v2/components/{{arn}}?recipeOutputFormat={{recipeOutputFormat}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetComponent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetComponent_RequestSyntax) **   <a name="greengrassv2-GetComponent-request-uri-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+:versions:[^:]+`
Required: Yes

 ** [recipeOutputFormat](#API_GetComponent_RequestSyntax) **   <a name="greengrassv2-GetComponent-request-uri-recipeOutputFormat"></a>
The format of the recipe.
Valid Values: `JSON | YAML`

## Request Body
<a name="API_GetComponent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recipe": blob,
   "recipeOutputFormat": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recipe](#API_GetComponent_ResponseSyntax) **   <a name="greengrassv2-GetComponent-response-recipe"></a>
The recipe of the component version.
Type: Base64-encoded binary data object

 ** [recipeOutputFormat](#API_GetComponent_ResponseSyntax) **   <a name="greengrassv2-GetComponent-response-recipeOutputFormat"></a>
The format of the recipe.
Type: String
Valid Values: `JSON | YAML`

 ** [tags](#API_GetComponent_ResponseSyntax) **   <a name="greengrassv2-GetComponent-response-tags"></a>
A list of key-value pairs that contain metadata for the resource. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html) in the * AWS IoT Greengrass V2 Developer Guide*.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action.
HTTP Status Code: 403

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource can't be found.
 ** resourceId **
The ID of the resource that isn't found.
 ** resourceType **
The type of the resource that isn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a request rate quota. For example, you might have exceeded the amount of times that you can retrieve device or deployment status per second.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/GetComponent)
