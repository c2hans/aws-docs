---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeEffectivePatchesForPatchBaseline.html
---

# DescribeEffectivePatchesForPatchBaseline
<a name="API_DescribeEffectivePatchesForPatchBaseline"></a>

Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Applies to patch baselines for Windows only.

## Request Syntax
<a name="API_DescribeEffectivePatchesForPatchBaseline_RequestSyntax"></a>

```
{
   "BaselineId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEffectivePatchesForPatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineId](#API_DescribeEffectivePatchesForPatchBaseline_RequestSyntax) **   <a name="systemsmanager-DescribeEffectivePatchesForPatchBaseline-request-BaselineId"></a>
The ID of the patch baseline to retrieve the effective patches for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

 ** [MaxResults](#API_DescribeEffectivePatchesForPatchBaseline_RequestSyntax) **   <a name="systemsmanager-DescribeEffectivePatchesForPatchBaseline-request-MaxResults"></a>
The maximum number of patches to return (per page).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeEffectivePatchesForPatchBaseline_RequestSyntax) **   <a name="systemsmanager-DescribeEffectivePatchesForPatchBaseline-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeEffectivePatchesForPatchBaseline_ResponseSyntax"></a>

```
{
   "EffectivePatches": [
      {
         "Patch": {
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
         },
         "PatchStatus": {
            "ApprovalDate": number,
            "ComplianceLevel": "string",
            "DeploymentStatus": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEffectivePatchesForPatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EffectivePatches](#API_DescribeEffectivePatchesForPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-DescribeEffectivePatchesForPatchBaseline-response-EffectivePatches"></a>
An array of patches and patch status.
Type: Array of [EffectivePatch](API_EffectivePatch.md) objects

 ** [NextToken](#API_DescribeEffectivePatchesForPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-DescribeEffectivePatchesForPatchBaseline-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeEffectivePatchesForPatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

 ** UnsupportedOperatingSystem **
The operating systems you specified isn't supported, or the operation isn't supported for the operating system.
HTTP Status Code: 400

## Examples
<a name="API_DescribeEffectivePatchesForPatchBaseline_Examples"></a>

### Example
<a name="API_DescribeEffectivePatchesForPatchBaseline_Example_1"></a>

This example illustrates one usage of DescribeEffectivePatchesForPatchBaseline.

#### Sample Request
<a name="API_DescribeEffectivePatchesForPatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 38
X-Amz-Target: AmazonSSM.DescribeEffectivePatchesForPatchBaseline
X-Amz-Date: 20240309T061447Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeEffectivePatchesForPatchBaseline_Example_1_Response"></a>

```
{
    "EffectivePatches": [
        {
            "Patch": {
                "Classification": "SecurityUpdates",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/2032276",
                "Description": "A security issue has been identified that could allow an
                unauthenticated remote attacker to compromise your system and gain control
                over it. You can help protect your system by installing this update from
                Microsoft. After you install this update, you may have to restart your system.",
                "Id": "8692029b-a3a2-4a87-a73b-8ea881b4b4d6",
                "KbNumber": "KB2032276",
                "Language": "All",
                "MsrcNumber": "MS10-043",
                "MsrcSeverity": "Important",
                "Product": "WindowsServer2008R2",
                "ProductFamily": "Windows",
                "ReleaseDate": 1279040400,
                "Title": "Security Update for Windows Server 2008 R2 x64 Edition (KB2032276)",
                "Vendor": "Microsoft"
            },
            "PatchStatus": {
                "ApprovalDate": 1279299600,
                "ComplianceLevel": "UNSPECIFIED",
                "DeploymentStatus": "APPROVED"
            }
        },
        {
            "Patch": {
                "Classification": "SecurityUpdates",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/2124261",
                "Description": "A security issue has been identified that could allow an
                unauthenticated remote attacker to compromise your system and gain control
                over it. You can help protect your system by installing this update from
                Microsoft. After you install this update, you may have to restart your system.",
                "Id": "12ef1bed-0dd2-4633-b3ac-60888aa8ba33",
                "KbNumber": "KB2124261",
                "Language": "All",
                "MsrcNumber": "MS10-065",
                "MsrcSeverity": "Important",
                "Product": "Windows7",
                "ProductFamily": "Windows",
                "ReleaseDate": 1284483600,
                "Title": "Security Update for Windows 7 (KB2124261)",
                "Vendor": "Microsoft"
            },
            "PatchStatus": {
                "ApprovalDate": 1284742800,
                "ComplianceLevel": "UNSPECIFIED",
                "DeploymentStatus": "APPROVED"
            }
        },
        {
            "Patch": {
                "Classification": "SecurityUpdates",
                "ContentUrl": "https://support.microsoft.com/en-us/kb/2124261",
                "Description": "A security issue has been identified that could allow an
                unauthenticated remote attacker to compromise your system and gain control
                over it. You can help protect your system by installing this update from
                Microsoft. After you install this update, you may have to restart your system.",
                "Id": "1b571637-30ed-48d6-b2f3-24d374fdebb8",
                "KbNumber": "KB2124261",
                "Language": "All",
                "MsrcNumber": "MS10-065",
                "MsrcSeverity": "Important",
                "Product": "WindowsServer2008R2",
                "ProductFamily": "Windows",
                "ReleaseDate": 1284483600,
                "Title": "Security Update for Windows Server 2008 R2 x64 Edition (KB2124261)",
                "Vendor": "Microsoft"
            },
            "PatchStatus": {
                "ApprovalDate": 1284742800,
                "ComplianceLevel": "UNSPECIFIED",
                "DeploymentStatus": "APPROVED"
            }
        }
        // There may be more content here
    ]
}
```

## See Also
<a name="API_DescribeEffectivePatchesForPatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeEffectivePatchesForPatchBaseline)
