---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchBaselines.html
---

# DescribePatchBaselines
<a name="API_DescribePatchBaselines"></a>

Lists the patch baselines in your AWS account.

## Request Syntax
<a name="API_DescribePatchBaselines_RequestSyntax"></a>

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
<a name="API_DescribePatchBaselines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribePatchBaselines_RequestSyntax) **   <a name="systemsmanager-DescribePatchBaselines-request-Filters"></a>
Each element in the array is a structure containing a key-value pair.
Supported keys for `DescribePatchBaselines` include the following:
+  ** `NAME_PREFIX` **

  Sample values: `AWS-` \| `My-`
+  ** `OWNER` **

  Sample values: `AWS` \| `Self`
+  ** `OPERATING_SYSTEM` **

  Sample values: `AMAZON_LINUX` \| `SUSE` \| `WINDOWS`
Type: Array of [PatchOrchestratorFilter](API_PatchOrchestratorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribePatchBaselines_RequestSyntax) **   <a name="systemsmanager-DescribePatchBaselines-request-MaxResults"></a>
The maximum number of patch baselines to return (per page).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribePatchBaselines_RequestSyntax) **   <a name="systemsmanager-DescribePatchBaselines-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribePatchBaselines_ResponseSyntax"></a>

```
{
   "BaselineIdentities": [
      {
         "BaselineDescription": "string",
         "BaselineId": "string",
         "BaselineName": "string",
         "DefaultBaseline": boolean,
         "OperatingSystem": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribePatchBaselines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaselineIdentities](#API_DescribePatchBaselines_ResponseSyntax) **   <a name="systemsmanager-DescribePatchBaselines-response-BaselineIdentities"></a>
An array of `PatchBaselineIdentity` elements.
Type: Array of [PatchBaselineIdentity](API_PatchBaselineIdentity.md) objects

 ** [NextToken](#API_DescribePatchBaselines_ResponseSyntax) **   <a name="systemsmanager-DescribePatchBaselines-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribePatchBaselines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribePatchBaselines_Examples"></a>

### Example
<a name="API_DescribePatchBaselines_Example_1"></a>

This example illustrates one usage of DescribePatchBaselines.

#### Sample Request
<a name="API_DescribePatchBaselines_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonSSM.DescribePatchBaselines
X-Amz-Date: 20240309T024139Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240309/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{}
```

#### Sample Response
<a name="API_DescribePatchBaselines_Example_1_Response"></a>

```
{
    "BaselineIdentities": [
        {
            "BaselineDescription": "Default Patch Baseline for Suse Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-07d8884178EXAMPLE",
            "BaselineName": "AWS-SuseDefaultPatchBaseline",
            "DefaultBaseline": true,
            "OperatingSystem": "SUSE"
        },
        {
            "BaselineDescription": "Default Patch Baseline Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-09ca3fb51fEXAMPLE",
            "BaselineName": "AWS-DefaultPatchBaseline",
            "DefaultBaseline": true,
            "OperatingSystem": "WINDOWS"
        },
        {
            "BaselineDescription": "Default Patch Baseline for Amazon Linux Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-0c10e65780EXAMPLE",
            "BaselineName": "AWS-AmazonLinuxDefaultPatchBaseline",
            "DefaultBaseline": true,
            "OperatingSystem": "AMAZON_LINUX"
        },
        {
            "BaselineDescription": "Default Patch Baseline for Ubuntu Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-0c7e89f711EXAMPLE",
            "BaselineName": "AWS-UbuntuDefaultPatchBaseline",
            "DefaultBaseline": true,
            "OperatingSystem": "UBUNTU"
        },
        {
            "BaselineDescription": "Default Patch Baseline for Redhat Enterprise Linux Provided by AWS.",
            "BaselineId": "arn:aws:ssm:us-east-2:111122223333:patchbaseline/pb-0cbb3a633dEXAMPLE",
            "BaselineName": "AWS-RedHatDefaultPatchBaseline",
            "DefaultBaseline": true,
            "OperatingSystem": "REDHAT_ENTERPRISE_LINUX"
        }
        // There may be more content here
    ]
}
```

## See Also
<a name="API_DescribePatchBaselines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribePatchBaselines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribePatchBaselines)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
