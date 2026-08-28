---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchGroupState.html
---

# DescribePatchGroupState
<a name="API_DescribePatchGroupState"></a>

Returns high-level aggregated patch compliance state information for a patch group.

## Request Syntax
<a name="API_DescribePatchGroupState_RequestSyntax"></a>

```
{
   "PatchGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePatchGroupState_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PatchGroup](#API_DescribePatchGroupState_RequestSyntax) **   <a name="systemsmanager-DescribePatchGroupState-request-PatchGroup"></a>
The name of the patch group whose patch snapshot should be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_DescribePatchGroupState_ResponseSyntax"></a>

```
{
   "Instances": number,
   "InstancesWithAvailableSecurityUpdates": number,
   "InstancesWithCriticalNonCompliantPatches": number,
   "InstancesWithFailedPatches": number,
   "InstancesWithInstalledOtherPatches": number,
   "InstancesWithInstalledPatches": number,
   "InstancesWithInstalledPendingRebootPatches": number,
   "InstancesWithInstalledRejectedPatches": number,
   "InstancesWithMissingPatches": number,
   "InstancesWithNotApplicablePatches": number,
   "InstancesWithOtherNonCompliantPatches": number,
   "InstancesWithSecurityNonCompliantPatches": number,
   "InstancesWithUnreportedNotApplicablePatches": number
}
```

## Response Elements
<a name="API_DescribePatchGroupState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-Instances"></a>
The number of managed nodes in the patch group.
Type: Integer

 ** [InstancesWithAvailableSecurityUpdates](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithAvailableSecurityUpdates"></a>
The number of managed nodes for which security-related patches are available but not approved because because they didn't meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.
Applies to Windows Server managed nodes only.
Type: Integer

 ** [InstancesWithCriticalNonCompliantPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithCriticalNonCompliantPatches"></a>
The number of managed nodes where patches that are specified as `Critical` for compliance reporting in the patch baseline aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer

 ** [InstancesWithFailedPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithFailedPatches"></a>
The number of managed nodes with patches from the patch baseline that failed to install.
Type: Integer

 ** [InstancesWithInstalledOtherPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithInstalledOtherPatches"></a>
The number of managed nodes with patches installed that aren't defined in the patch baseline.
Type: Integer

 ** [InstancesWithInstalledPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithInstalledPatches"></a>
The number of managed nodes with installed patches.
Type: Integer

 ** [InstancesWithInstalledPendingRebootPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithInstalledPendingRebootPatches"></a>
The number of managed nodes with patches installed by Patch Manager that haven't been rebooted after the patch installation. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer

 ** [InstancesWithInstalledRejectedPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithInstalledRejectedPatches"></a>
The number of managed nodes with patches installed that are specified in a `RejectedPatches` list. Patches with a status of `INSTALLED_REJECTED` were typically installed before they were added to a `RejectedPatches` list.
If `ALLOW_AS_DEPENDENCY` is the specified option for `RejectedPatchesAction`, the value of `InstancesWithInstalledRejectedPatches` will always be `0` (zero).
Type: Integer

 ** [InstancesWithMissingPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithMissingPatches"></a>
The number of managed nodes with missing patches from the patch baseline.
Type: Integer

 ** [InstancesWithNotApplicablePatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithNotApplicablePatches"></a>
The number of managed nodes with patches that aren't applicable.
Type: Integer

 ** [InstancesWithOtherNonCompliantPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithOtherNonCompliantPatches"></a>
The number of managed nodes with patches installed that are specified as other than `Critical` or `Security` but aren't compliant with the patch baseline. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer

 ** [InstancesWithSecurityNonCompliantPatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithSecurityNonCompliantPatches"></a>
The number of managed nodes where patches that are specified as `Security` in a patch advisory aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is `NON_COMPLIANT`.
Type: Integer

 ** [InstancesWithUnreportedNotApplicablePatches](#API_DescribePatchGroupState_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroupState-response-InstancesWithUnreportedNotApplicablePatches"></a>
The number of managed nodes with `NotApplicable` patches beyond the supported limit, which aren't reported by name to Inventory. Inventory is a tool in AWS Systems Manager.
Type: Integer

## Errors
<a name="API_DescribePatchGroupState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribePatchGroupState_Examples"></a>

### Example
<a name="API_DescribePatchGroupState_Example_1"></a>

This example illustrates one usage of DescribePatchGroupState.

#### Sample Request
<a name="API_DescribePatchGroupState_Example_1_Request"></a>

```
POST / HTTP/1.1
  Host: ssm.us-east-2.amazonaws.com
  Accept-Encoding: identity
  Content-Length: 33
  X-Amz-Target: AmazonSSM.DescribePatchGroupState
  X-Amz-Date: 20240308T205757Z
  User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
  Content-Type: application/x-amz-json-1.1
  Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

  {
    "PatchGroup": "mypatchgroup"
}
```

#### Sample Response
<a name="API_DescribePatchGroupState_Example_1_Response"></a>

```
{
    "Instances": 12,
    "InstancesWithCriticalNonCompliantPatches": 1,
    "InstancesWithFailedPatches": 2,
    "InstancesWithInstalledOtherPatches": 3,
    "InstancesWithInstalledPatches": 12,
    "InstancesWithInstalledPendingRebootPatches": 2,
    "InstancesWithInstalledRejectedPatches": 1,
    "InstancesWithMissingPatches": 3,
    "InstancesWithNotApplicablePatches": 0,
    "InstancesWithOtherNonCompliantPatches": 0,
    "InstancesWithSecurityNonCompliantPatches": 1,
    "InstancesWithUnreportedNotApplicablePatches": 0
}
```

## See Also
<a name="API_DescribePatchGroupState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribePatchGroupState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribePatchGroupState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
