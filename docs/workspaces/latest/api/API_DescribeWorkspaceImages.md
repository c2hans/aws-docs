---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html
---

# DescribeWorkspaceImages
<a name="API_DescribeWorkspaceImages"></a>

Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described.

## Request Syntax
<a name="API_DescribeWorkspaceImages_RequestSyntax"></a>

```
{
   "ImageIds": [ "{{string}}" ],
   "ImageType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeWorkspaceImages_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ImageIds](#API_DescribeWorkspaceImages_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-request-ImageIds"></a>
The identifier of the image.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `wsi-[0-9a-z]{9,63}$`
Required: No

 ** [ImageType](#API_DescribeWorkspaceImages_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-request-ImageType"></a>
The type (owned or shared) of the image.
Type: String
Valid Values: `OWNED | SHARED`
Required: No

 ** [MaxResults](#API_DescribeWorkspaceImages_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-request-MaxResults"></a>
The maximum number of items to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeWorkspaceImages_RequestSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_DescribeWorkspaceImages_ResponseSyntax"></a>

```
{
   "Images": [
      {
         "Created": number,
         "Description": "string",
         "ErrorCode": "string",
         "ErrorDetails": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string"
            }
         ],
         "ErrorMessage": "string",
         "ImageId": "string",
         "Name": "string",
         "OperatingSystem": {
            "Type": "string"
         },
         "OwnerAccountId": "string",
         "RequiredTenancy": "string",
         "State": "string",
         "Updates": {
            "Description": "string",
            "UpdateAvailable": boolean
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeWorkspaceImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Images](#API_DescribeWorkspaceImages_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-response-Images"></a>
Information about the images.
Type: Array of [WorkspaceImage](API_WorkspaceImage.md) objects

 ** [NextToken](#API_DescribeWorkspaceImages_ResponseSyntax) **   <a name="WorkSpaces-DescribeWorkspaceImages-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeWorkspaceImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaceImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeWorkspaceImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeWorkspaceImages)
