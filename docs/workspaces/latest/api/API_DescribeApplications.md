---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeApplications.html
---

# DescribeApplications
<a name="API_DescribeApplications"></a>

Describes the specified applications by filtering based on their compute types, license availability, operating systems, and owners.

## Request Syntax
<a name="API_DescribeApplications_RequestSyntax"></a>

```
{
   "ApplicationIds": [ "{{string}}" ],
   "ComputeTypeNames": [ "{{string}}" ],
   "LicenseType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OperatingSystemNames": [ "{{string}}" ],
   "Owner": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplications_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationIds](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-ApplicationIds"></a>
The identifiers of one or more applications.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Pattern: `^wsa-[0-9a-z]{8,63}$`
Required: No

 ** [ComputeTypeNames](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-ComputeTypeNames"></a>
The compute types supported by the applications.
Type: Array of strings
Valid Values: `VALUE | STANDARD | PERFORMANCE | POWER | GRAPHICS | POWERPRO | GENERALPURPOSE_4XLARGE | GENERALPURPOSE_8XLARGE | GRAPHICSPRO | GRAPHICS_G4DN | GRAPHICSPRO_G4DN | GRAPHICS_G6_XLARGE | GRAPHICS_G6_2XLARGE | GRAPHICS_G6_4XLARGE | GRAPHICS_G6_8XLARGE | GRAPHICS_G6_16XLARGE | GRAPHICS_GR6_4XLARGE | GRAPHICS_GR6_8XLARGE | GRAPHICS_G6F_LARGE | GRAPHICS_G6F_XLARGE | GRAPHICS_G6F_2XLARGE | GRAPHICS_G6F_4XLARGE | GRAPHICS_GR6F_4XLARGE`
Required: No

 ** [LicenseType](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-LicenseType"></a>
The license availability for the applications.
Type: String
Valid Values: `LICENSED | UNLICENSED`
Required: No

 ** [MaxResults](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-MaxResults"></a>
The maximum number of applications to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [OperatingSystemNames](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-OperatingSystemNames"></a>
The operating systems supported by the applications.
Type: Array of strings
Valid Values: `AMAZON_LINUX_2 | UBUNTU_18_04 | UBUNTU_20_04 | UBUNTU_22_04 | UNKNOWN | WINDOWS_10 | WINDOWS_11 | WINDOWS_7 | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | RHEL_8 | ROCKY_8`
Required: No

 ** [Owner](#API_DescribeApplications_RequestSyntax) **   <a name="WorkSpaces-DescribeApplications-request-Owner"></a>
The owner of the applications.
Type: String
Pattern: `^\d{12}|AMAZON$`
Required: No

## Response Syntax
<a name="API_DescribeApplications_ResponseSyntax"></a>

```
{
   "Applications": [
      {
         "ApplicationId": "string",
         "Created": number,
         "Description": "string",
         "LicenseType": "string",
         "Name": "string",
         "Owner": "string",
         "State": "string",
         "SupportedComputeTypeNames": [ "string" ],
         "SupportedOperatingSystemNames": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Applications](#API_DescribeApplications_ResponseSyntax) **   <a name="WorkSpaces-DescribeApplications-response-Applications"></a>
List of information about the specified applications.
Type: Array of [WorkSpaceApplication](API_WorkSpaceApplication.md) objects

 ** [NextToken](#API_DescribeApplications_ResponseSyntax) **   <a name="WorkSpaces-DescribeApplications-response-NextToken"></a>
If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_DescribeApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user is not authorized to access a resource.
HTTP Status Code: 400

 ** InvalidParameterValuesException **
One or more parameter values are not valid.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** OperationNotSupportedException **
This operation is not supported.
 ** message **
The exception error message.
 ** reason **
The exception error reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** message **
The resource could not be found.
 ** ResourceId **
The ID of the resource that could not be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-2015-04-08/DescribeApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/DescribeApplications)
