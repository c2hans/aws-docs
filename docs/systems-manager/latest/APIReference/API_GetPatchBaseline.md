---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetPatchBaseline.html
---

# GetPatchBaseline
<a name="API_GetPatchBaseline"></a>

Retrieves information about a patch baseline.

## Request Syntax
<a name="API_GetPatchBaseline_RequestSyntax"></a>

```
{
   "BaselineId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineId](#API_GetPatchBaseline_RequestSyntax) **   <a name="systemsmanager-GetPatchBaseline-request-BaselineId"></a>
The ID of the patch baseline to retrieve.
To retrieve information about an AWS managed patch baseline, specify the full Amazon Resource Name (ARN) of the baseline. For example, for the baseline `AWS-AmazonLinuxDefaultPatchBaseline`, specify `arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0e392de35e7c563b7` instead of `pb-0e392de35e7c563b7`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

## Response Syntax
<a name="API_GetPatchBaseline_ResponseSyntax"></a>

```
{
   "ApprovalRules": {
      "PatchRules": [
         {
            "ApproveAfterDays": number,
            "ApproveUntilDate": "string",
            "ComplianceLevel": "string",
            "EnableNonSecurity": boolean,
            "PatchFilterGroup": {
               "PatchFilters": [
                  {
                     "Key": "string",
                     "Values": [ "string" ]
                  }
               ]
            }
         }
      ]
   },
   "ApprovedPatches": [ "string" ],
   "ApprovedPatchesComplianceLevel": "string",
   "ApprovedPatchesEnableNonSecurity": boolean,
   "AvailableSecurityUpdatesComplianceStatus": "string",
   "BaselineId": "string",
   "CreatedDate": number,
   "Description": "string",
   "GlobalFilters": {
      "PatchFilters": [
         {
            "Key": "string",
            "Values": [ "string" ]
         }
      ]
   },
   "ModifiedDate": number,
   "Name": "string",
   "OperatingSystem": "string",
   "PatchGroups": [ "string" ],
   "RejectedPatches": [ "string" ],
   "RejectedPatchesAction": "string",
   "Sources": [
      {
         "Configuration": "string",
         "Name": "string",
         "Products": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_GetPatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApprovalRules](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-ApprovalRules"></a>
A set of rules used to include patches in the baseline.
Type: [PatchRuleGroup](API_PatchRuleGroup.md) object

 ** [ApprovedPatches](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-ApprovedPatches"></a>
A list of explicitly approved patches for the baseline.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [ApprovedPatchesComplianceLevel](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-ApprovedPatchesComplianceLevel"></a>
Returns the specified compliance severity level for approved patches in the patch baseline.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`

 ** [ApprovedPatchesEnableNonSecurity](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-ApprovedPatchesEnableNonSecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean

 ** [AvailableSecurityUpdatesComplianceStatus](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-AvailableSecurityUpdatesComplianceStatus"></a>
Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the `CreatePatchBaseline` or `UpdatePatchBaseline` commands are run.
Applies to Windows Server managed nodes only.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`

 ** [BaselineId](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-BaselineId"></a>
The ID of the retrieved patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

 ** [CreatedDate](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-CreatedDate"></a>
The date the patch baseline was created.
Type: Timestamp

 ** [Description](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-Description"></a>
A description of the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [GlobalFilters](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-GlobalFilters"></a>
A set of global filters used to exclude patches from the baseline.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object

 ** [ModifiedDate](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-ModifiedDate"></a>
The date the patch baseline was last modified.
Type: Timestamp

 ** [Name](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-Name"></a>
The name of the patch baseline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [OperatingSystem](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-OperatingSystem"></a>
Returns the operating system specified for the patch baseline.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`

 ** [PatchGroups](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-PatchGroups"></a>
Patch groups included in the patch baseline.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [RejectedPatches](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-RejectedPatches"></a>
A list of explicitly rejected patches for the baseline.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [RejectedPatchesAction](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-RejectedPatchesAction"></a>
The action specified to take on patches included in the `RejectedPatches` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.
Type: String
Valid Values: `ALLOW_AS_DEPENDENCY | BLOCK`

 ** [Sources](#API_GetPatchBaseline_ResponseSyntax) **   <a name="systemsmanager-GetPatchBaseline-response-Sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
Type: Array of [PatchSource](API_PatchSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_GetPatchBaseline_Errors"></a>

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

## Examples
<a name="API_GetPatchBaseline_Examples"></a>

### Example
<a name="API_GetPatchBaseline_Example_1"></a>

This example illustrates one usage of GetPatchBaseline.

#### Sample Request
<a name="API_GetPatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 38
X-Amz-Target: AmazonSSM.GetPatchBaseline
X-Amz-Date: 20240309T020232Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_GetPatchBaseline_Example_1_Response"></a>

```
{
    "ApprovalRules": {
        "PatchRules": [
            {
                "ApproveAfterDays": 1,
                "ComplianceLevel": "UNSPECIFIED",
                "EnableNonSecurity": false,
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Key": "PRODUCT",
                            "Values": [
                                "WindowsServer2012R2"
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
                                "Important",
                                "Critical",
                                "Moderate"
                            ]
                        }
                    ]
                }
            }
        ]
    },
    "ApprovedPatches": [],
    "ApprovedPatchesComplianceLevel": "HIGH",
    "ApprovedPatchesEnableNonSecurity": false,
    "BaselineId": "pb-0c10e65780EXAMPLE",
    "Description": "My Moderate, Important, and Critical security updates for Windows Server 2012 R2",
    "GlobalFilters": {
        "PatchFilters": []
    },
    "CreatedDate": 1520561435.87,
    "ModifiedDate": 1520561435.869,
    "Name": "my-Windows-Server-2012R2",
    "OperatingSystem": "WINDOWS",
    "PatchGroups": [
        "mypatchgroup"
    ],
    "RejectedPatches": [
        "KB3452678"
    ],
    "RejecteddPatchesAction": "ALLOW_AS_DEPENDENCY",
    "Sources": []
}
```

## See Also
<a name="API_GetPatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetPatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetPatchBaseline)
