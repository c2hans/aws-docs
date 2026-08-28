---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeImages.html
---

# DescribeImages
<a name="API_DescribeImages"></a>

Retrieves a list that describes one or more specified images, if the image names or image ARNs are provided. Otherwise, all images in the account are described.

## Request Syntax
<a name="API_DescribeImages_RequestSyntax"></a>

```
{
   "Arns": [ "{{string}}" ],
   "MaxResults": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImages_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arns](#API_DescribeImages_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImages-request-Arns"></a>
The ARNs of the public, private, and shared images to describe.
Type: Array of strings
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** [MaxResults](#API_DescribeImages_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImages-request-MaxResults"></a>
The maximum size of each page of results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [Names](#API_DescribeImages_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImages-request-Names"></a>
The names of the public or private images to describe.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** [NextToken](#API_DescribeImages_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImages-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [Type](#API_DescribeImages_RequestSyntax) **   <a name="WorkSpacesApplications-DescribeImages-request-Type"></a>
The type of image (public, private, or shared) to describe.
Type: String
Valid Values: `PUBLIC | PRIVATE | SHARED`
Required: No

## Response Syntax
<a name="API_DescribeImages_ResponseSyntax"></a>

```
{
   "Images": [
      {
         "Applications": [
            {
               "AppBlockArn": "string",
               "Arn": "string",
               "CreatedTime": number,
               "Description": "string",
               "DisplayName": "string",
               "Enabled": boolean,
               "IconS3Location": {
                  "S3Bucket": "string",
                  "S3Key": "string"
               },
               "IconURL": "string",
               "InstanceFamilies": [ "string" ],
               "LaunchParameters": "string",
               "LaunchPath": "string",
               "Metadata": {
                  "string" : "string"
               },
               "Name": "string",
               "Platforms": [ "string" ],
               "WorkingDirectory": "string"
            }
         ],
         "AppstreamAgentVersion": "string",
         "Arn": "string",
         "BaseImageArn": "string",
         "CreatedTime": number,
         "Description": "string",
         "DisplayName": "string",
         "DynamicAppProvidersEnabled": "string",
         "ImageBuilderName": "string",
         "ImageBuilderSupported": boolean,
         "ImageErrors": [
            {
               "ErrorCode": "string",
               "ErrorMessage": "string",
               "ErrorTimestamp": number
            }
         ],
         "ImagePermissions": {
            "allowFleet": boolean,
            "allowImageBuilder": boolean
         },
         "ImageSharedWithOthers": "string",
         "ImageType": "string",
         "LatestAppstreamAgentVersion": "string",
         "ManagedSoftwareIncluded": boolean,
         "Name": "string",
         "Platform": "string",
         "PublicBaseImageReleasedDate": number,
         "State": "string",
         "StateChangeReason": {
            "Code": "string",
            "Message": "string"
         },
         "SupportedInstanceFamilies": [ "string" ],
         "Visibility": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Images](#API_DescribeImages_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeImages-response-Images"></a>
Information about the images.
Type: Array of [Image](API_Image.md) objects

 ** [NextToken](#API_DescribeImages_ResponseSyntax) **   <a name="WorkSpacesApplications-DescribeImages-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DescribeImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DescribeImages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
