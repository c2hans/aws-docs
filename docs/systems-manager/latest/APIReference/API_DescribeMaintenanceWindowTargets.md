---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowTargets.html
---

# DescribeMaintenanceWindowTargets
<a name="API_DescribeMaintenanceWindowTargets"></a>

Lists the targets registered with the maintenance window.

## Request Syntax
<a name="API_DescribeMaintenanceWindowTargets_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowTargets_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-request-Filters"></a>
Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are `Type`, `WindowTargetId`, and `OwnerInformation`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowTargets_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowTargets_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [WindowId](#API_DescribeMaintenanceWindowTargets_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-request-WindowId"></a>
The ID of the maintenance window whose targets should be retrieved.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowTargets_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Targets": [
      {
         "Description": "string",
         "Name": "string",
         "OwnerInformation": "string",
         "ResourceType": "string",
         "Targets": [
            {
               "Key": "string",
               "Values": [ "string" ]
            }
         ],
         "WindowId": "string",
         "WindowTargetId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowTargets_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Targets](#API_DescribeMaintenanceWindowTargets_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTargets-response-Targets"></a>
Information about the targets in the maintenance window.
Type: Array of [MaintenanceWindowTarget](API_MaintenanceWindowTarget.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowTargets_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowTargets_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowTargets.

#### Sample Request
<a name="API_DescribeMaintenanceWindowTargets_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowTargets
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T003928Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 36

{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowTargets_Example_1_Response"></a>

```
{
    "Targets": [
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "Name": "MyTargets",
            "WindowTargetId": "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE",
            "ResourceType": "INSTANCE",
            "Targets": [
                {
                    "Key": "InstanceIds",
                    "Values": [
                        "i-02573cafcfEXAMPLE",
                        "i-0471e04240EXAMPLE"
                    ]
                }
            ]
        },
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "WindowTargetId": "7f4813bb-df25-4e59-b34f-c9e83EXAMPLE",
            "ResourceType": "INSTANCE",
            "Targets": [
                {
                    "Key": "InstanceIds",
                    "Values": [
                        "i-07782c72faEXAMPLE"
                    ]
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
