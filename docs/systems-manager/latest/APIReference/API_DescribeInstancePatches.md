---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatches.html
---

# DescribeInstancePatches
<a name="API_DescribeInstancePatches"></a>

Retrieves information about the patches on the specified managed node and their state relative to the patch baseline being used for the node.

## Request Syntax
<a name="API_DescribeInstancePatches_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstancePatches_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeInstancePatches_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatches-request-Filters"></a>
Each element in the array is a structure containing a key-value pair.
Supported keys for `DescribeInstancePatches`include the following:
+  ** `Classification` **

  Sample values: `Security` \| `SecurityUpdates`
+  ** `KBId` **

  Sample values: `KB4480056` \| `java-1.7.0-openjdk.x86_64`
+  ** `Severity` **

  Sample values: `Important` \| `Medium` \| `Low`
+  ** `State` **

  Sample values: `Installed` \| `InstalledOther` \| `InstalledPendingReboot`

  For lists of all `State` values, see [Patch compliance state values](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-states.html) in the * AWS Systems Manager User Guide*.
Type: Array of [PatchOrchestratorFilter](API_PatchOrchestratorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [InstanceId](#API_DescribeInstancePatches_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatches-request-InstanceId"></a>
The ID of the managed node whose patch state information should be retrieved.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [MaxResults](#API_DescribeInstancePatches_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatches-request-MaxResults"></a>
The maximum number of patches to return (per page).
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeInstancePatches_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatches-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInstancePatches_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Patches": [
      {
         "Classification": "string",
         "CVEIds": "string",
         "InstalledTime": number,
         "KBId": "string",
         "Severity": "string",
         "State": "string",
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeInstancePatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeInstancePatches_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatches-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Patches](#API_DescribeInstancePatches_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatches-response-Patches"></a>
Each entry in the array is a structure containing:
+ Title (string)
+ KBId (string)
+ Classification (string)
+ Severity (string)
+ State (string, such as "INSTALLED" or "FAILED")
+ InstalledTime (DateTime)
+ InstalledBy (string)
Type: Array of [PatchComplianceData](API_PatchComplianceData.md) objects

## Errors
<a name="API_DescribeInstancePatches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstancePatches_Examples"></a>

### Example
<a name="API_DescribeInstancePatches_Example_1"></a>

This example illustrates one usage of DescribeInstancePatches.

#### Sample Request
<a name="API_DescribeInstancePatches_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 37
X-Amz-Target: AmazonSSM.DescribeInstancePatches
X-Amz-Date: 20240308T205131Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "InstanceId": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeInstancePatches_Example_1_Response"></a>

```
{
    "Patches": [
        {
            "Title": "NetworkManager.x86_64:1:1.30.0-7.el8",
            "KBId": "NetworkManager.x86_64",
            "Classification": "Security",
            "Severity": "Moderate",
            "State": "Installed",
            "InstalledTime": "2024-05-19T10:03:07-07:00"
        },
        {
            "Title": "bash.x86_64:0:4.4.19-14.el8",
            "KBId": "bash.x86_64",
            "Classification": "Security",
            "Severity": "Low",
            "State": "Installed",
            "InstalledTime": "2024-05-19T10:03:25-07:00"
        },
        {
            "Title": "kernel-modules.x86_64:0:4.18.0-305.10.2.el8_4",
            "KBId": "kernel-modules.x86_64",
            "Classification": "Security",
            "Severity": "Important",
            "State": "Installed",
            "InstalledTime": "2024-08-04T10:45:42-07:00"
        }
        // There may be more content here
    ]
}
```

## See Also
<a name="API_DescribeInstancePatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstancePatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstancePatches)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
