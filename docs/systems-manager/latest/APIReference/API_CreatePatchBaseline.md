---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html
---

# CreatePatchBaseline
<a name="API_CreatePatchBaseline"></a>

Creates a patch baseline.

**Note**
For information about valid key-value pairs in `PatchFilters` for each supported operating system type, see [PatchFilter](API_PatchFilter.md).

## Request Syntax
<a name="API_CreatePatchBaseline_RequestSyntax"></a>

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
   "ClientToken": "{{string}}",
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
   "OperatingSystem": "{{string}}",
   "RejectedPatches": [ "{{string}}" ],
   "RejectedPatchesAction": "{{string}}",
   "Sources": [
      {
         "Configuration": "{{string}}",
         "Name": "{{string}}",
         "Products": [ "{{string}}" ]
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePatchBaseline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApprovalRules](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-ApprovalRules"></a>
A set of rules used to include patches in the baseline.
Type: [PatchRuleGroup](API_PatchRuleGroup.md) object
Required: No

 ** [ApprovedPatches](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-ApprovedPatches"></a>
A list of explicitly approved patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [ApprovedPatchesComplianceLevel](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-ApprovedPatchesComplianceLevel"></a>
Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is `UNSPECIFIED`.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** [ApprovedPatchesEnableNonSecurity](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-ApprovedPatchesEnableNonSecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
Type: Boolean
Required: No

 ** [AvailableSecurityUpdatesComplianceStatus](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-AvailableSecurityUpdatesComplianceStatus"></a>
Indicates the status you want to assign to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.
Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.
Supported for Windows Server managed nodes only.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

 ** [ClientToken](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Description](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-Description"></a>
A description of the patch baseline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [GlobalFilters](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-GlobalFilters"></a>
A set of global filters used to include patches in the baseline.
The `GlobalFilters` parameter can be configured only by using the AWS CLI or an AWS SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.
Type: [PatchFilterGroup](API_PatchFilterGroup.md) object
Required: No

 ** [Name](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-Name"></a>
The name of the patch baseline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [OperatingSystem](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-OperatingSystem"></a>
Defines the operating system the patch baseline applies to. The default value is `WINDOWS`.
Type: String
Valid Values: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX | AMAZON_LINUX_2023`
Required: No

 ** [RejectedPatches](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-RejectedPatches"></a>
A list of explicitly rejected patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [RejectedPatchesAction](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-RejectedPatchesAction"></a>
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

 ** [Sources](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-Sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
Type: Array of [PatchSource](API_PatchSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [Tags](#API_CreatePatchBaseline_RequestSyntax) **   <a name="systemsmanager-CreatePatchBaseline-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to. In this case, you could specify the following key-value pairs:
+  `Key=PatchSeverity,Value=Critical`
+  `Key=OS,Value=Windows`
To add tags to an existing patch baseline, use the [AddTagsToResource](API_AddTagsToResource.md) operation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_CreatePatchBaseline_ResponseSyntax"></a>

```
{
   "BaselineId": "string"
}
```

## Response Elements
<a name="API_CreatePatchBaseline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineId](#API_CreatePatchBaseline_ResponseSyntax) **   <a name="systemsmanager-CreatePatchBaseline-response-BaselineId"></a>
The ID of the created patch baseline.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-:/]{20,128}$`

## Errors
<a name="API_CreatePatchBaseline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatch **
Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceLimitExceededException **
Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.
For information about resource quotas in Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_CreatePatchBaseline_Examples"></a>

### Example
<a name="API_CreatePatchBaseline_Example_1"></a>

This example illustrates one usage of CreatePatchBaseline.

#### Sample Request
<a name="API_CreatePatchBaseline_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 461
X-Amz-Target: AmazonSSM.CreatePatchBaseline
X-Amz-Date: 20240309T022356Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Description": "Baseline containing all updates approved for production systems",
    "ApprovalRules": {
        "PatchRules": [
            {
                "PatchFilterGroup": {
                    "PatchFilters": [
                        {
                            "Values": [
                                "Critical",
                                "Important",
                                "Moderate"
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
                "ApproveAfterDays": 7,
                "ApproveUntilDate": "",
                "EnableNonSecurity": true,
                "ComplianceLevel": "MEDIUM"
            }
        ]
    },
    "Name": "my-Windows-Server-patch-baseline",
    "OperatingSystem": "WINDOWS",
    "ClientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_CreatePatchBaseline_Example_1_Response"></a>

```
{
    "BaselineId": "pb-0c10e65780EXAMPLE"
}
```

## See Also
<a name="API_CreatePatchBaseline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreatePatchBaseline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreatePatchBaseline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
