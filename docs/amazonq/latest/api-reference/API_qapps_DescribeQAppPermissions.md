---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_DescribeQAppPermissions.html
---

# DescribeQAppPermissions
<a name="API_qapps_DescribeQAppPermissions"></a>

 Describes read permissions for a Amazon Q App in Amazon Q Business application environment instance.

## Request Syntax
<a name="API_qapps_DescribeQAppPermissions_RequestSyntax"></a>

```
GET /apps.describeQAppPermissions?appId={{appId}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_DescribeQAppPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_qapps_DescribeQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_DescribeQAppPermissions-request-uri-appId"></a>
The unique identifier of the Amazon Q App for which to retrieve permissions.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [instanceId](#API_qapps_DescribeQAppPermissions_RequestSyntax) **   <a name="qbusiness-qapps_DescribeQAppPermissions-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_DescribeQAppPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_DescribeQAppPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appId": "string",
   "permissions": [
      {
         "action": "string",
         "principal": {
            "email": "string",
            "userId": "string",
            "userType": "string"
         }
      }
   ],
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_qapps_DescribeQAppPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appId](#API_qapps_DescribeQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_DescribeQAppPermissions-response-appId"></a>
The unique identifier of the Amazon Q App for which permissions are returned.
Type: String

 ** [permissions](#API_qapps_DescribeQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_DescribeQAppPermissions-response-permissions"></a>
The list of permissions granted for the Amazon Q App.
Type: Array of [PermissionOutput](API_qapps_PermissionOutput.md) objects

 ** [resourceArn](#API_qapps_DescribeQAppPermissions_ResponseSyntax) **   <a name="qbusiness-qapps_DescribeQAppPermissions-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q App for which permissions are returned.
Type: String

## Errors
<a name="API_qapps_DescribeQAppPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

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
<a name="API_qapps_DescribeQAppPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/DescribeQAppPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/DescribeQAppPermissions)
