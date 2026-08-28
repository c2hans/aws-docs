---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceAssociationsStatus.html
---

# DescribeInstanceAssociationsStatus
<a name="API_DescribeInstanceAssociationsStatus"></a>

The status of the associations for the managed nodes.

## Request Syntax
<a name="API_DescribeInstanceAssociationsStatus_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstanceAssociationsStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_DescribeInstanceAssociationsStatus_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceAssociationsStatus-request-InstanceId"></a>
The managed node IDs for which you want association status information.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [MaxResults](#API_DescribeInstanceAssociationsStatus_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceAssociationsStatus-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeInstanceAssociationsStatus_RequestSyntax) **   <a name="systemsmanager-DescribeInstanceAssociationsStatus-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInstanceAssociationsStatus_ResponseSyntax"></a>

```
{
   "InstanceAssociationStatusInfos": [
      {
         "AssociationId": "string",
         "AssociationName": "string",
         "AssociationVersion": "string",
         "DetailedStatus": "string",
         "DocumentVersion": "string",
         "ErrorCode": "string",
         "ExecutionDate": number,
         "ExecutionSummary": "string",
         "InstanceId": "string",
         "Name": "string",
         "OutputUrl": {
            "S3OutputUrl": {
               "OutputUrl": "string"
            }
         },
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInstanceAssociationsStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceAssociationStatusInfos](#API_DescribeInstanceAssociationsStatus_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceAssociationsStatus-response-InstanceAssociationStatusInfos"></a>
Status information about the association.
Type: Array of [InstanceAssociationStatusInfo](API_InstanceAssociationStatusInfo.md) objects

 ** [NextToken](#API_DescribeInstanceAssociationsStatus_ResponseSyntax) **   <a name="systemsmanager-DescribeInstanceAssociationsStatus-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeInstanceAssociationsStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

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
<a name="API_DescribeInstanceAssociationsStatus_Examples"></a>

### Example
<a name="API_DescribeInstanceAssociationsStatus_Example_1"></a>

This example illustrates one usage of DescribeInstanceAssociationsStatus.

#### Sample Request
<a name="API_DescribeInstanceAssociationsStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeInstanceAssociationsStatus
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T185152Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 37

{
    "InstanceId": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeInstanceAssociationsStatus_Example_1_Response"></a>

```
{
    "InstanceAssociationStatusInfos": [
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "DetailedStatus": "Success",
            "DocumentVersion": "1",
            "ExecutionDate": 1581948052.198,
            "InstanceId": "i-02573cafcfEXAMPLE",
            "Name": "AWS-UpdateSSMAgent",
            "Status": "Success"
        }
    ]
}
```

## See Also
<a name="API_DescribeInstanceAssociationsStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstanceAssociationsStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstanceAssociationsStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
