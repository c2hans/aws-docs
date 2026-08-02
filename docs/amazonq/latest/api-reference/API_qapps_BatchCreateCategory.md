---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategory.html
---

# BatchCreateCategory
<a name="API_qapps_BatchCreateCategory"></a>

Creates Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see [Custom labels for Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html).

## Request Syntax
<a name="API_qapps_BatchCreateCategory_RequestSyntax"></a>

```
POST /catalog.createCategories HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "categories": [
      {
         "color": "{{string}}",
         "id": "{{string}}",
         "title": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_qapps_BatchCreateCategory_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_BatchCreateCategory_RequestSyntax) **   <a name="qbusiness-qapps_BatchCreateCategory-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_BatchCreateCategory_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [categories](#API_qapps_BatchCreateCategory_RequestSyntax) **   <a name="qbusiness-qapps_BatchCreateCategory-request-categories"></a>
The list of category objects to be created
Type: Array of [BatchCreateCategoryInputCategory](API_qapps_BatchCreateCategoryInputCategory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_qapps_BatchCreateCategory_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_qapps_BatchCreateCategory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_qapps_BatchCreateCategory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** ConflictException **
The requested operation could not be completed due to a conflict with the current state of the resource.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_BatchCreateCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/BatchCreateCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/BatchCreateCategory)
