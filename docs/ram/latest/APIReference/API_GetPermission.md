---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_GetPermission.html
---

# GetPermission
<a name="API_GetPermission"></a>

Retrieves the contents of a managed permission in JSON format.

## Request Syntax
<a name="API_GetPermission_RequestSyntax"></a>

```
POST /getpermission HTTP/1.1
Content-type: application/json

{
   "permissionArn": "{{string}}",
   "permissionVersion": {{number}}
}
```

## URI Request Parameters
<a name="API_GetPermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [permissionArn](#API_GetPermission_RequestSyntax) **   <a name="ram-GetPermission-request-permissionArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the permission whose contents you want to retrieve. To find the ARN for a permission, use either the [ListPermissions](API_ListPermissions.md) operation or go to the [Permissions library](https://console.aws.amazon.com/ram/home#Permissions:) page in the AWS RAM console and then choose the name of the permission. The ARN is displayed on the detail page.
Type: String
Required: Yes

 ** [permissionVersion](#API_GetPermission_RequestSyntax) **   <a name="ram-GetPermission-request-permissionVersion"></a>
Specifies the version number of the AWS RAM permission to retrieve. If you don't specify this parameter, the operation retrieves the default version.
To see the list of available versions, use [ListPermissionVersions](API_ListPermissionVersions.md).
Type: Integer
Required: No

## Response Syntax
<a name="API_GetPermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "permission": {
      "arn": "string",
      "creationTime": number,
      "defaultVersion": boolean,
      "featureSet": "string",
      "isResourceTypeDefault": boolean,
      "lastUpdatedTime": number,
      "name": "string",
      "permission": "string",
      "permissionType": "string",
      "resourceType": "string",
      "status": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "version": "string"
   }
}
```

## Response Elements
<a name="API_GetPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [permission](#API_GetPermission_ResponseSyntax) **   <a name="ram-GetPermission-response-permission"></a>
An object with details about the permission.
Type: [ResourceSharePermissionDetail](API_ResourceSharePermissionDetail.md) object

## Errors
<a name="API_GetPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_GetPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/GetPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/GetPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/GetPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/GetPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/GetPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/GetPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/GetPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/GetPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/GetPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/GetPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
