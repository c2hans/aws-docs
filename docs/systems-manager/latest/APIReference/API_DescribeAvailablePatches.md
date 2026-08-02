---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAvailablePatches.html
---

# DescribeAvailablePatches
<a name="API_DescribeAvailablePatches"></a>

Lists all patches eligible to be included in a patch baseline.

**Note**
Currently, `DescribeAvailablePatches` supports only the Amazon Linux 1, Amazon Linux 2, and Windows Server operating systems.

## Request Syntax
<a name="API_DescribeAvailablePatches_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAvailablePatches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeAvailablePatches_RequestSyntax) **   <a name="systemsmanager-DescribeAvailablePatches-request-Filters"></a>
Each element in the array is a structure containing a key-value pair.
 **Windows Server**
Supported keys for Windows Server managed node patches include the following:
+  ** `PATCH_SET` **

  Sample values: `OS` \| `APPLICATION`
+  ** `PRODUCT` **

  Sample values: `WindowsServer2012` \| `Office 2010` \| `MicrosoftDefenderAntivirus`
+  ** `PRODUCT_FAMILY` **

  Sample values: `Windows` \| `Office`
+  ** `MSRC_SEVERITY` **

  Sample values: `ServicePacks` \| `Important` \| `Moderate`
+  ** `CLASSIFICATION` **

  Sample values: `ServicePacks` \| `SecurityUpdates` \| `DefinitionUpdates`
+  ** `PATCH_ID` **

  Sample values: `KB123456` \| `KB4516046`
 **Linux**
When specifying filters for Linux patches, you must specify a key-pair for `PRODUCT`. For example, using the AWS Command Line Interface (AWS CLI), the following command fails:
 `aws ssm describe-available-patches --filters Key=CVE_ID,Values=CVE-2018-3615`
However, the following command succeeds:
 `aws ssm describe-available-patches --filters Key=PRODUCT,Values=AmazonLinux2018.03 Key=CVE_ID,Values=CVE-2018-3615`
Supported keys for Linux managed node patches include the following:
+  ** `PRODUCT` **

  Sample values: `AmazonLinux2018.03` \| `AmazonLinux2.0`
+  ** `NAME` **

  Sample values: `kernel-headers` \| `samba-python` \| `php`
+  ** `SEVERITY` **

  Sample values: `Critical` \| `Important` \| `Medium` \| `Low`
+  ** `EPOCH` **

  Sample values: `0` \| `1`
+  ** `VERSION` **

  Sample values: `78.6.1` \| `4.10.16`
+  ** `RELEASE` **

  Sample values: `9.56.amzn1` \| `1.amzn2`
+  ** `ARCH` **

  Sample values: `i686` \| `x86_64`
+  ** `REPOSITORY` **

  Sample values: `Core` \| `Updates`
+  ** `ADVISORY_ID` **

  Sample values: `ALAS-2018-1058` \| `ALAS2-2021-1594`
+  ** `CVE_ID` **

  Sample values: `CVE-2018-3615` \| `CVE-2020-1472`
+  ** `BUGZILLA_ID` **

  Sample values: `1463241`
Type: Array of [PatchOrchestratorFilter](API_PatchOrchestratorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeAvailablePatches_RequestSyntax) **   <a name="systemsmanager-DescribeAvailablePatches-request-MaxResults"></a>
The maximum number of patches to return (per page).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeAvailablePatches_RequestSyntax) **   <a name="systemsmanager-DescribeAvailablePatches-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAvailablePatches_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Patches": [
      {
         "AdvisoryIds": [ "string" ],
         "Arch": "string",
         "BugzillaIds": [ "string" ],
         "Classification": "string",
         "ContentUrl": "string",
         "CVEIds": [ "string" ],
         "Description": "string",
         "Epoch": number,
         "Id": "string",
         "KbNumber": "string",
         "Language": "string",
         "MsrcNumber": "string",
         "MsrcSeverity": "string",
         "Name": "string",
         "Product": "string",
         "ProductFamily": "string",
         "Release": "string",
         "ReleaseDate": number,
         "Repository": "string",
         "Severity": "string",
         "Title": "string",
         "Vendor": "string",
         "Version": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAvailablePatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeAvailablePatches_ResponseSyntax) **   <a name="systemsmanager-DescribeAvailablePatches-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Patches](#API_DescribeAvailablePatches_ResponseSyntax) **   <a name="systemsmanager-DescribeAvailablePatches-response-Patches"></a>
An array of patches. Each entry in the array is a patch structure.
Type: Array of [Patch](API_Patch.md) objects

## Errors
<a name="API_DescribeAvailablePatches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeAvailablePatches_Examples"></a>

### Example
<a name="API_DescribeAvailablePatches_Example_1"></a>

This example illustrates one usage of DescribeAvailablePatches.

#### Sample Request
<a name="API_DescribeAvailablePatches_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 17
X-Amz-Target: AmazonSSM.DescribeAvailablePatches
X-Amz-Date: 20240308T193543Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Filters": [
        {
            "Key": "PRODUCT",
            "Values": [
                "WindowsServer2016"
            ]
        },
        {
            "Key": "CLASSIFICATION",
            "Values": [
                "SecurityUpdates"
            ]
        },
        {
            "Key": "MSRC_SEVERITY",
            "Values": [
                "Critical"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeAvailablePatches_Example_1_Response"></a>

```
{
    "Patches": [
        {
            "Classification": "SecurityUpdates",
            "ContentUrl": "https://support.microsoft.com/en-us/kb/4074588",
            "Description": "A security issue has been identified in a Microsoft software
            product that could affect your system. You can help protect your system by
            installing this update from Microsoft. For a complete listing of the issues
            that are included in this update, see the associated Microsoft Knowledge Base
            article. After you install this update, you may have to restart your system.",
            "Id": "11adea10-0701-430e-954f-9471595ae246",
            "KbNumber": "KB4074588",
            "Language": "All",
            "MsrcNumber": "",
            "MsrcSeverity": "Critical",
            "Product": "WindowsServer2016",
            "ProductFamily": "Windows",
            "ReleaseDate": 1518548400,
            "Title": "2018-02 Cumulative Update for Windows Server 2016 (1709) for x64-based
            Systems (KB4074588)",
            "Vendor": "Microsoft"
        },
        {
            "Classification": "SecurityUpdates",
            "ContentUrl": "https://support.microsoft.com/en-us/kb/4074590",
            "Description": "A security issue has been identified in a Microsoft software
            product that could affect your system. You can help protect your system by
            installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.",
            "Id": "f5f58231-ac5d-4640-ab1b-9dc8d857c265",
            "KbNumber": "KB4074590",
            "Language": "All",
            "MsrcNumber": "",
            "MsrcSeverity": "Critical",
            "Product": "WindowsServer2016",
            "ProductFamily": "Windows",
            "ReleaseDate": 1518544805,
            "Title": "2018-02 Cumulative Update for Windows Server 2016 for x64-based
            Systems (KB4074590)",
            "Vendor": "Microsoft"
        },
        {
            "Classification": "SecurityUpdates",
            "ContentUrl": "https://support.microsoft.com/en-us/kb/4074595",
            "Description": "A security issue has been identified in a Microsoft software
            product that could affect your system. You can help protect your system by
            installing this update from Microsoft. For a complete listing of the issues
            that are included in this update, see the associated Microsoft Knowledge Base
            article. After you install this update, you may have to restart your system.",
            "Id": "754b5889-2e01-40cc-8833-edf86b35541f",
            "KbNumber": "KB4074595",
            "Language": "All",
            "MsrcNumber": "",
            "MsrcSeverity": "Critical",
            "Product": "WindowsServer2016",
            "ProductFamily": "Windows",
            "ReleaseDate": 1517965209,
            "Title": "2018-02 Security Update for Adobe Flash Player for Windows Server 2016
            for x64-based Systems (KB4074595)",
            "Vendor": "Microsoft"
        }
    ]
}
```

## See Also
<a name="API_DescribeAvailablePatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAvailablePatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAvailablePatches)
