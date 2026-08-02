---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPermissions.html
---

# ListPermissions
<a name="API_ListPermissions"></a>

Retrieves a list of available AWS RAM permissions that you can use for the supported resource types.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_ListPermissions_RequestSyntax"></a>

```
POST /listpermissions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "permissionType": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPermissions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPermissions_RequestSyntax) **   <a name="ram-ListPermissions-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListPermissions_RequestSyntax) **   <a name="ram-ListPermissions-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [permissionType](#API_ListPermissions_RequestSyntax) **   <a name="ram-ListPermissions-request-permissionType"></a>
Specifies that you want to list only permissions of this type:
+  `AWS` – returns only AWS managed permissions.
+  `LOCAL` – returns only customer managed permissions
+  `ALL` – returns both AWS managed permissions and customer managed permissions.
If you don't specify this parameter, the default is `All`.
Type: String
Valid Values: `ALL | AWS_MANAGED | CUSTOMER_MANAGED`
Required: No

 ** [resourceType](#API_ListPermissions_RequestSyntax) **   <a name="ram-ListPermissions-request-resourceType"></a>
Specifies that you want to list only those permissions that apply to the specified resource type. This parameter is not case sensitive.
For example, to list only permissions that apply to Amazon EC2 subnets, specify `ec2:subnet`. You can use the [ListResourceTypes](API_ListResourceTypes.md) operation to get the specific string required.
Type: String
Required: No

## Response Syntax
<a name="API_ListPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "permissions": [
      {
         "arn": "string",
         "creationTime": number,
         "defaultVersion": boolean,
         "featureSet": "string",
         "isResourceTypeDefault": boolean,
         "lastUpdatedTime": number,
         "name": "string",
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
   ]
}
```

## Response Elements
<a name="API_ListPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPermissions_ResponseSyntax) **   <a name="ram-ListPermissions-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [permissions](#API_ListPermissions_ResponseSyntax) **   <a name="ram-ListPermissions-response-permissions"></a>
An array of objects with information about the permissions.
Type: Array of [ResourceSharePermissionSummary](API_ResourceSharePermissionSummary.md) objects

## Errors
<a name="API_ListPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
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

## See Also
<a name="API_ListPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListPermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListPermissions)
