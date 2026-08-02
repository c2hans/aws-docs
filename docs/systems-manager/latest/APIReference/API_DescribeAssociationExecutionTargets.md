---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutionTargets.html
---

# DescribeAssociationExecutionTargets
<a name="API_DescribeAssociationExecutionTargets"></a>

Views information about a specific execution of a specific association.

## Request Syntax
<a name="API_DescribeAssociationExecutionTargets_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "ExecutionId": "{{string}}",
   "Filters": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAssociationExecutionTargets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DescribeAssociationExecutionTargets_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-request-AssociationId"></a>
The association ID that includes the execution for which you want to view details.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [ExecutionId](#API_DescribeAssociationExecutionTargets_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-request-ExecutionId"></a>
The execution ID for which you want to view details.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [Filters](#API_DescribeAssociationExecutionTargets_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-request-Filters"></a>
Filters for the request. You can specify the following filters and values.
Status (EQUAL)
ResourceId (EQUAL)
ResourceType (EQUAL)
Type: Array of [AssociationExecutionTargetsFilter](API_AssociationExecutionTargetsFilter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [MaxResults](#API_DescribeAssociationExecutionTargets_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeAssociationExecutionTargets_RequestSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAssociationExecutionTargets_ResponseSyntax"></a>

```
{
   "AssociationExecutionTargets": [
      {
         "AssociationId": "string",
         "AssociationVersion": "string",
         "DetailedStatus": "string",
         "ExecutionId": "string",
         "LastExecutionDate": number,
         "OutputSource": {
            "OutputSourceId": "string",
            "OutputSourceType": "string"
         },
         "ResourceId": "string",
         "ResourceType": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAssociationExecutionTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationExecutionTargets](#API_DescribeAssociationExecutionTargets_ResponseSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-response-AssociationExecutionTargets"></a>
Information about the execution.
Type: Array of [AssociationExecutionTarget](API_AssociationExecutionTarget.md) objects

 ** [NextToken](#API_DescribeAssociationExecutionTargets_ResponseSyntax) **   <a name="systemsmanager-DescribeAssociationExecutionTargets-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeAssociationExecutionTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** AssociationExecutionDoesNotExist **
The specified execution ID doesn't exist. Verify the ID number and try again.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAssociationExecutionTargets_Examples"></a>

### Example
<a name="API_DescribeAssociationExecutionTargets_Example_1"></a>

This example illustrates one usage of DescribeAssociationExecutionTargets.

#### Sample Request
<a name="API_DescribeAssociationExecutionTargets_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeAssociationExecutionTargets
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T165104Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 112

{
    "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
    "ExecutionId": "d6d51ef5-4eca-48ef-9d7d-bd6ceEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeAssociationExecutionTargets_Example_1_Response"></a>

```
{
    "AssociationExecutionTargets": [
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "DetailedStatus": "Success",
            "ExecutionId": "d6d51ef5-4eca-48ef-9d7d-bd6ceEXAMPLE",
            "LastExecutionDate": 1582037438.692,
            "OutputSource": {
                "OutputSourceId": "1cdbb1e6-2e69-40b1-ac1d-121dcEXAMPLE",
                "OutputSourceType": "RunCommand"
            },
            "ResourceId": "i-02573cafcfEXAMPLE",
            "ResourceType": "ManagedInstance",
            "Status": "Success"
        },
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "DetailedStatus": "Success",
            "ExecutionId": "d6d51ef5-4eca-48ef-9d7d-bd6ceEXAMPLE",
            "LastExecutionDate": 1581948052.198,
            "OutputSource": {
                "OutputSourceId": "b170ae99-4959-479b-ab4d-f6ae0EXAMPLE",
                "OutputSourceType": "RunCommand"
            },
            "ResourceId": "i-0471e04240EXAMPLE",
            "ResourceType": "ManagedInstance",
            "Status": "Success"
        },
        {
            "AssociationId": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "AssociationVersion": "1",
            "DetailedStatus": "Success",
            "ExecutionId": "d6d51ef5-4eca-48ef-9d7d-bd6ceEXAMPLE",
            "LastExecutionDate": 1561053316.711,
            "OutputSource": {
                "OutputSourceId": "89cd739c-d1a5-4dc9-af4f-8b624EXAMPLE",
                "OutputSourceType": "RunCommand"
            },
            "ResourceId": "i-07782c72faEXAMPLE",
            "ResourceType": "ManagedInstance",
            "Status": "Success"
        }
    ]
}
```

## See Also
<a name="API_DescribeAssociationExecutionTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAssociationExecutionTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAssociationExecutionTargets)
