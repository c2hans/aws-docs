---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_ListDeviceResources.html
---

# ListDeviceResources
<a name="API_devicemanagement_ListDeviceResources"></a>

Returns a list of the AWS resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.

## Request Syntax
<a name="API_devicemanagement_ListDeviceResources_RequestSyntax"></a>

```
GET /managed-device/{{managedDeviceId}}/resources?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_devicemanagement_ListDeviceResources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [managedDeviceId](#API_devicemanagement_ListDeviceResources_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-request-uri-managedDeviceId"></a>
The ID of the managed device that you are listing the resources of.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [maxResults](#API_devicemanagement_ListDeviceResources_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-request-uri-maxResults"></a>
The maximum number of resources per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_devicemanagement_ListDeviceResources_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-request-uri-nextToken"></a>
A pagination token to continue to the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [type](#API_devicemanagement_ListDeviceResources_RequestSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-request-uri-type"></a>
A structure used to filter the results by type of resource.
Length Constraints: Minimum length of 1. Maximum length of 50.

## Request Body
<a name="API_devicemanagement_ListDeviceResources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_devicemanagement_ListDeviceResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resources": [
      {
         "arn": "string",
         "id": "string",
         "resourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_devicemanagement_ListDeviceResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_devicemanagement_ListDeviceResources_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-response-nextToken"></a>
A pagination token to continue to the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=]*`

 ** [resources](#API_devicemanagement_ListDeviceResources_ResponseSyntax) **   <a name="Snowball-devicemanagement_ListDeviceResources-response-resources"></a>
A structure defining the resource's type, Amazon Resource Name (ARN), and ID.
Type: Array of [ResourceSummary](API_devicemanagement_ResourceSummary.md) objects

## Errors
<a name="API_devicemanagement_ListDeviceResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_devicemanagement_ListDeviceResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snow-device-management-2021-08-04/ListDeviceResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/ListDeviceResources)
