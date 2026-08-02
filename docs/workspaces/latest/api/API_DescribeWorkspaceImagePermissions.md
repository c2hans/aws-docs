---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html
---

# DescribeWorkspaceImagePermissions
<a name="API_DescribeWorkspaceImagePermissions"></a>

Describes the permissions that the owner of an image has granted to other AWS accounts for an image.

## Request Syntax
<a name="API_DescribeWorkspaceImagePermissions_RequestSyntax"></a>

```
{
   "ImageId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspaceImagePermissions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ImageId](#API_DescribeWorkspaceImagePermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-request-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: Yes

 ** [MaxResults](#API_DescribeWorkspaceImagePermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeWorkspaceImagePermissions_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeWorkspaceImagePermissions_ResponseSyntax"></a>

```
{
   "ImageId": "string",
   "ImagePermissions": [
      {
         "SharedAccountId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeWorkspaceImagePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageId](#API_DescribeWorkspaceImagePermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-response-ImageId"></a>
The identifier of the image.
Type: String
Pattern: `wsi-[0-9a-z]{9,63}$`

 ** [ImagePermissions](#API_DescribeWorkspaceImagePermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-response-ImagePermissions"></a>
The identifiers of the AWS accounts that the image has been shared with.
Type: Array of [ImagePermission](API_ImagePermission.md) objects

 ** [NextToken](#API_DescribeWorkspaceImagePermissions_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImagePermissions-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeWorkspaceImagePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaceImagePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceImagePermissions)
