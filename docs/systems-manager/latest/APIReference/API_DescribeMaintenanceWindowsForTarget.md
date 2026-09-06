---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowsForTarget.html
---

# DescribeMaintenanceWindowsForTarget
<a name="API_DescribeMaintenanceWindowsForTarget"></a>

Retrieves information about the maintenance window targets or tasks that a managed node is associated with.

## Request Syntax
<a name="API_DescribeMaintenanceWindowsForTarget_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceType": "{{string}}",
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowsForTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeMaintenanceWindowsForTarget_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowsForTarget_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [ResourceType](#API_DescribeMaintenanceWindowsForTarget_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-request-ResourceType"></a>
The type of resource you want to retrieve information about. For example, `INSTANCE`.
Type: String
Valid Values: `INSTANCE | RESOURCE_GROUP`
Required: Yes

 ** [Targets](#API_DescribeMaintenanceWindowsForTarget_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-request-Targets"></a>
The managed node ID or key-value pair to retrieve information about.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowsForTarget_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WindowIdentities": [
      {
         "Name": "string",
         "WindowId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowsForTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowsForTarget_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-response-NextToken"></a>
The token for the next set of items to return. (You use this token in the next call.)
Type: String

 ** [WindowIdentities](#API_DescribeMaintenanceWindowsForTarget_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowsForTarget-response-WindowIdentities"></a>
Information about the maintenance window targets and tasks a managed node is associated with.
Type: Array of [MaintenanceWindowIdentityForTarget](API_MaintenanceWindowIdentityForTarget.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowsForTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowsForTarget_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowsForTarget_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowsForTarget.

#### Sample Request
<a name="API_DescribeMaintenanceWindowsForTarget_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowsForTarget
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T003520Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 100

{
    "Targets": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-07782c72faEXAMPLE"
            ]
        }
    ],
    "ResourceType": "INSTANCE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowsForTarget_Example_1_Response"></a>

```
{
    "WindowIdentities": [
        {
            "Name": "MyFirstMaintenanceWindow",
            "WindowId": "mw-0c50858d01EXAMPLE"
        },
        {
            "Name": "MySecondMaintenanceWindow",
            "WindowId": "mw-05aaf9f490EXAMPLE"
        },
        {
            "Name": "MyThirdMaintenanceWindow",
            "WindowId": "mw-0ecb1226ddEXAMPLE"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowsForTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowsForTarget)
