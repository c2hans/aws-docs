---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchGroups.html
---

# DescribePatchGroups
<a name="API_DescribePatchGroups"></a>

Lists all patch groups that have been registered with patch baselines.

## Request Syntax
<a name="API_DescribePatchGroups_RequestSyntax"></a>

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
<a name="API_DescribePatchGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribePatchGroups_RequestSyntax) **   <a name="systemsmanager-DescribePatchGroups-request-Filters"></a>
Each element in the array is a structure containing a key-value pair.
Supported keys for `DescribePatchGroups` include the following:
+  ** `NAME_PREFIX` **

  Sample values: `AWS-` \| `My-`.
+  ** `OPERATING_SYSTEM` **

  Sample values: `AMAZON_LINUX` \| `SUSE` \| `WINDOWS`
Type: Array of [PatchOrchestratorFilter](API_PatchOrchestratorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribePatchGroups_RequestSyntax) **   <a name="systemsmanager-DescribePatchGroups-request-MaxResults"></a>
The maximum number of patch groups to return (per page).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribePatchGroups_RequestSyntax) **   <a name="systemsmanager-DescribePatchGroups-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribePatchGroups_ResponseSyntax"></a>

```
{
   "Mappings": [
      {
         "BaselineIdentity": {
            "BaselineDescription": "string",
            "BaselineId": "string",
            "BaselineName": "string",
            "DefaultBaseline": boolean,
            "OperatingSystem": "string"
         },
         "PatchGroup": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribePatchGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Mappings](#API_DescribePatchGroups_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroups-response-Mappings"></a>
Each entry in the array contains:
+  `PatchGroup`: string (between 1 and 256 characters. Regex: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$)`
+  `PatchBaselineIdentity`: A `PatchBaselineIdentity` element.
Type: Array of [PatchGroupPatchBaselineMapping](API_PatchGroupPatchBaselineMapping.md) objects

 ** [NextToken](#API_DescribePatchGroups_ResponseSyntax) **   <a name="systemsmanager-DescribePatchGroups-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribePatchGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribePatchGroups_Examples"></a>

### Example
<a name="API_DescribePatchGroups_Example_1"></a>

This example illustrates one usage of DescribePatchGroups.

#### Sample Request
<a name="API_DescribePatchGroups_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonSSM.DescribePatchGroups
X-Amz-Date: 20240308T211212Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{}
```

#### Sample Response
<a name="API_DescribePatchGroups_Example_1_Response"></a>

```
{
    "Mappings": [
        {
            "PatchGroup": "Database Servers",
            "BaselineIdentity": {
                "BaselineName": "Windows-Server-2012R2",
                "DefaultBaseline": false,
                "BaselineDescription": "Windows Server 2012 R2, Important and Critical security updates",
                "BaselineId": "pb-0c4e592064EXAMPLE",
                "OperatingSystem": "WINDOWS"
            }
        },
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineName": "Windows-Server-2012R2",
                "DefaultBaseline": false,
                "BaselineDescription": "Windows Server 2012 R2, Important and Critical security updates",
                "BaselineId": "pb-0c4e592064EXAMPLE",
                "OperatingSystem": "WINDOWS"
            }
        },
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineName": "Amazon-Linux-Production",
                "DefaultBaseline": false,
                "BaselineDescription": "Patch baseline used for production instances",
                "BaselineId": "pb-022cbaf99cEXAMPLE",
                "OperatingSystem": "AMAZON_LINUX"
            }
        },
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineName": "RHEL-ZeroDay-Critical",
                "DefaultBaseline": false,
                "BaselineId": "pb-0ea5bc85f4EXAMPLE",
                "OperatingSystem": "REDHAT_ENTERPRISE_LINUX"
            }
        },
        {
            "PatchGroup": "Production-Demo",
            "BaselineIdentity": {
                "BaselineName": "Only-Security-Patches",
                "DefaultBaseline": false,
                "BaselineDescription": "Security updates for all versions of Windows",
                "BaselineId": "pb-08521bdf9eEXAMPLE",
                "OperatingSystem": "WINDOWS"
            }
        }
    ]
}
```

## See Also
<a name="API_DescribePatchGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribePatchGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribePatchGroups)
