---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImagePermissions.html
---

# DescribeImagePermissions
<a name="API_DescribeImagePermissions"></a>

Retrieves a list that describes the permissions for shared AWS account IDs on a private image that you own.

## Request Syntax
<a name="API_DescribeImagePermissions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}",
   "SharedAwsAccountIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeImagePermissions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 500.
Required: No

 ** [Name](#API_DescribeImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-request-Name"></a>
The name of the private image for which to describe permissions. The image must be one that you own.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [NextToken](#API_DescribeImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [SharedAwsAccountIds](#API_DescribeImagePermissions_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-request-SharedAwsAccountIds"></a>
The 12-digit identifier of one or more AWS accounts with which the image is shared.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Pattern: `^\d+$`
Required: No

## Response Syntax
<a name="API_DescribeImagePermissions_ResponseSyntax"></a>

```
{
   "Name": "string",
   "NextToken": "string",
   "SharedImagePermissionsList": [
      {
         "imagePermissions": {
            "allowFleet": boolean,
            "allowImageBuilder": boolean
         },
         "sharedAccountId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeImagePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_DescribeImagePermissions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-response-Name"></a>
The name of the private image.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`

 ** [NextToken](#API_DescribeImagePermissions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

 ** [SharedImagePermissionsList](#API_DescribeImagePermissions_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeImagePermissions-response-SharedImagePermissionsList"></a>
The permissions for a private image that you own.
Type: Array of [SharedImagePermissions](API_SharedImagePermissions.md) objects

## Errors
<a name="API_DescribeImagePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImagePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeImagePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeImagePermissions)
