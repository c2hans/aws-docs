---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutions.html
---

# DescribeAssociationExecutions
<a name="API_DescribeAssociationExecutions"></a>

Views all executions for a specific association ID.

## Request Syntax
<a name="API_DescribeAssociationExecutions_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAssociationExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DescribeAssociationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-request-AssociationId"></a>
The association ID for which you want to view execution history details.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [Filters](#API_DescribeAssociationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-request-Filters"></a>
Filters for the request. You can specify the following filters and values.
ExecutionId (EQUAL)
Status (EQUAL)
CreatedTime (EQUAL, GREATER\_THAN, LESS\_THAN)
Type: Array of [AssociationExecutionFilter](API_AssociationExecutionFilter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [MaxResults](#API_DescribeAssociationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeAssociationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAssociationExecutions_ResponseSyntax"></a>

```
{
   "AssociationExecutions": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "AssociationId": "string",
         "AssociationVersion": "string",
         "CreatedTime": number,
         "DetailedStatus": "string",
         "ExecutionId": "string",
         "LastExecutionDate": number,
         "ResourceCountByStatus": "string",
         "Status": "string",
         "TriggeredAlarms": [
            {
               "Name": "string",
               "State": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAssociationExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationExecutions](#API_DescribeAssociationExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-response-AssociationExecutions"></a>
A list of the executions for the specified association ID.
Type: Array of [AssociationExecution](API_AssociationExecution.md) objects

 ** [NextToken](#API_DescribeAssociationExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAssociationExecutions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeAssociationExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAssociationExecutions_Examples"></a>

### Example
<a name="API_DescribeAssociationExecutions_Example_1"></a>

This example illustrates one usage of DescribeAssociationExecutions.

#### Sample Request
<a name="API_DescribeAssociationExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeAssociationExecutions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T154610Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 57

{
    "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeAssociationExecutions_Example_1_Response"></a>

```
{
    "AssociationExecutions": [
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "CreatedTime": 1561053271.718,
            "DetailedStatus": "Success",
            "ExecutionId": "d6d51ef5-4eca-48ef-9d7d-bd6ceEXAMPLE",
            "ResourceCountByStatus": "{Success=3}",
            "Status": "Success"
        }
    ]
}
```

## See Also
<a name="API_DescribeAssociationExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAssociationExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAssociationExecutions)
