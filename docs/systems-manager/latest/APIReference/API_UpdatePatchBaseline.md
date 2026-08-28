---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdatePatchBaseline.html
---

# UpdatePatchBaseline
<a name="API_UpdatePatchBaseline"></a>

Modifies an existing patch baseline. Fields not specified in the request are left unchanged.

**Note**
For information about valid key-value pairs in `PatchFilters` for each supported operating system type, see [PatchFilter](API_PatchFilter.md).

## Request Syntax
<a name="API_UpdatePatchBaseline_RequestSyntax"></a>

```
{
   "ApprovalRules": {
      "PatchRules": [
         {
            "ApproveAfterDays": {{number}},
            "ApproveUntilDate": "{{string}}",
            "ComplianceLevel": "{{string}}",
            "EnableNonSecurity": {{boolean}},
            "PatchFilterGroup": {
               "PatchFilters": [
                  {
                     "Key": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               ]
            }
         }
      ]
   },
   "ApprovedPatches": [ "{{string}}" ],
   "ApprovedPatchesComplianceLevel": "{{string}}",
   "ApprovedPatchesEnableNonSecurity": {{boolean}},
   "AvailableSecurityUpdatesComplianceStatus": "{{string}}",
   "BaselineId": "{{string}}",
   "Description": "{{string}}",
   "GlobalFilters": {
      "PatchFilters": [
         {
            "Key": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "Name": "{{string}}",
   "RejectedPatches": [ "{{string}}" ],
   "RejectedPatchesAction": "{{string}}",
   "Replace": {{boolean}},
   "Sources": [
      {
         "Configuration": "{{string}}",
         "Name": "{{string}}",
         "Products": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_UpdatePatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApprovalRules](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-ApprovalRules"></a>
A set of rules used to include patches in the baseline.
Type: [PatchRuleGroup](API_PatchRuleGroup.md) object
Required: No

 ** [ApprovedPatches](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-ApprovedPatches"></a>
A list of explicitly approved patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [ApprovedPatchesComplianceLevel](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-ApprovedPatchesComplianceLevel"></a>
Assigns a new compliance severity level to an existing patch baseline.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** [ApprovedPatchesEnableNonSecurity](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-ApprovedPatchesEnableNonSecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean
Required: No

 ** [AvailableSecurityUpdatesComplianceStatus](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-AvailableSecurityUpdatesComplianceStatus"></a>
Indicates the status to be assigned to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.
Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.
Supported for Windows Server managed nodes only.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

 ** [BaselineId](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-BaselineId"></a>
The ID of the patch baseline to update.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`
Required: Yes

 ** [Description](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-Description"></a>
A description of the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [GlobalFilters](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-GlobalFilters"></a>
A set of global filters used to include patches in the baseline.
The `GlobalFilters` parameter can be configured only by using the AWS CLI or an AWS SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object
Required: No

 ** [Name](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-Name"></a>
The name of the patch baseline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [RejectedPatches](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-RejectedPatches"></a>
A list of explicitly rejected patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [RejectedPatchesAction](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-RejectedPatchesAction"></a>
The action for Patch Manager to take on patches included in the `RejectedPackages` list.
ALLOW\_AS\_DEPENDENCY
 **Linux and macOS**: A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as `INSTALLED_OTHER`. This is the default action if no option is specified.
 **Windows Server**: Windows Server doesn't support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as `INSTALLED_OTHER`. Any package not already installed on the node is skipped. This is the default action if no option is specified.
BLOCK
 **All OSs**: Packages in the rejected patches list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances.
State value assignment for patch compliance:
+ If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as `INSTALLED_REJECTED`.
+ If an update attempts to install a dependency package that is now rejected by the baseline, when previous versions of the package were not rejected, the package being updated is reported as `MISSING` for `SCAN` operations and as `FAILED` for `INSTALL` operations.
Type: String
Valid Values: `ALLOW_AS_DEPENDENCY | BLOCK`
Required: No

 ** [Replace](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-Replace"></a>
If True, then all fields that are required by the [CreatePatchBaseline](API_CreatePatchBaseline.md) operation are also required for this API request. Optional fields that aren't specified are set to null.
Type: Boolean
Required: No

 ** [Sources](#API_UpdatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-request-Sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
Type: Array of [PatchSource](API_PatchSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## Response Syntax
<a name="API_UpdatePatchBaseline_ResponseSyntax"></a>

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
<a name="API_UpdatePatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApprovalRules](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-ApprovalRules"></a>
A set of rules used to include patches in the baseline.
Type: [PatchRuleGroup](API_PatchRuleGroup.md) object

 ** [ApprovedPatches](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-ApprovedPatches"></a>
A list of explicitly approved patches for the baseline.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [ApprovedPatchesComplianceLevel](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-ApprovedPatchesComplianceLevel"></a>
The compliance severity level assigned to the patch baseline after the update completed.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`

 ** [ApprovedPatchesEnableNonSecurity](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-ApprovedPatchesEnableNonSecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean

 ** [AvailableSecurityUpdatesComplianceStatus](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-AvailableSecurityUpdatesComplianceStatus"></a>
Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the `CreatePatchBaseline` or `UpdatePatchBaseline` commands are run.
Applies to Windows Server managed nodes only.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`

 ** [BaselineId](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-BaselineId"></a>
The ID of the deleted patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

 ** [CreatedDate](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-CreatedDate"></a>
The date when the patch baseline was created.
Type: Timestamp

 ** [Description](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-Description"></a>
A description of the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [GlobalFilters](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-GlobalFilters"></a>
A set of global filters used to exclude patches from the baseline.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object

 ** [ModifiedDate](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-ModifiedDate"></a>
The date when the patch baseline was last modified.
Type: Timestamp

 ** [Name](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-Name"></a>
The name of the patch baseline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [OperatingSystem](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-OperatingSystem"></a>
The operating system rule used by the updated patch baseline.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`

 ** [RejectedPatches](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-RejectedPatches"></a>
A list of explicitly rejected patches for the baseline.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [RejectedPatchesAction](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-RejectedPatchesAction"></a>
The action specified to take on patches included in the `RejectedPatches` list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.
Type: String
Valid Values: `ALLOW_AS_DEPENDENCY | BLOCK`

 ** [Sources](#API_UpdatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-UpdatePatchBaseline-response-Sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
Type: Array of [PatchSource](API_PatchSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

## Errors
<a name="API_UpdatePatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_UpdatePatchBaseline_Examples"></a>

### Example
<a name="API_UpdatePatchBaseline_Example_1"></a>

This example illustrates one usage of UpdatePatchBaseline.

#### Sample Request
<a name="API_UpdatePatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
   Host: ssm.us-east-2.amazonaws.com
   Accept-Encoding: identity
   Content-Length: 306
   X-Amz-Target: AmazonSSM.UpdatePatchBaseline
   X-Amz-Date: 20240309T023346Z
   User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
   Content-Type: application/x-amz-json-1.1
   Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
   SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

  {
    "ApprovalRules": {
        "PatchRules": [
            {
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Values": [
                                "Critical",
                                "Important"
                            ],
                            "Key": "MSRC_SEVERITY"
                        },
                        {
                            "Values": [
                                "SecurityUpdates",
                                "Updates",
                                "UpdateRollups",
                                "CriticalUpdates"
                            ],
                            "Key": "CLASSIFICATION"
                        }
                    ]
                },
                "ApproveAfterDays": 3
            }
        ]
    },
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

#### Sample Response
<a name="API_UpdatePatchBaseline_Example_1_Response"></a>

```
{
    "ApprovalRules": {
        "PatchRules": [
            {
                "ApproveAfterDays": 3,
                "ComplianceLevel": "UNSPECIFIED",
                "EnableNonSecurity": false,
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Key": "MSRC_SEVERITY",
                            "Values": [
                                "Critical",
                                "Important"
                            ]
                        },
                        {
                            "Key": "CLASSIFICATION",
                            "Values": [
                                "SecurityUpdates",
                                "Updates",
                                "UpdateRollups",
                                "CriticalUpdates"
                            ]
                        }
                    ]
                }
            }
        ]
    },
    "ApprovedPatches": [],
    "ApprovedPatchesComplianceLevel": "UNSPECIFIED",
    "ApprovedPatchesEnableNonSecurity": false,
    "BaselineId": "pb-0c10e65780EXAMPLE",
    "Description": "Baseline containing all updates approved for production systems",
    "GlobalFilters": {
        "PatchFilters": []
    },
    "CreatedDate": 1520562237.968,
    "ModifiedDate": 1520562239.765,
    "Name": "my-Windows-Server-patch-baseline",
    "OperatingSystem": "WINDOWS",
    "RejectedPatches": [],
    "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY",
    "Sources": []
}
```

## See Also
<a name="API_UpdatePatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdatePatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdatePatchBaseline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
