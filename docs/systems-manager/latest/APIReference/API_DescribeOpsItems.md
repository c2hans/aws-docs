---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeOpsItems.html
---

# DescribeOpsItems
<a name="API_DescribeOpsItems"></a>

Query a set of OpsItems. You must have permission in AWS Identity and Access Management (IAM) to query a list of OpsItems. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the * AWS Systems Manager User Guide*.

Operations engineers and IT professionals use AWS Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their AWS resources. For more information, see [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_DescribeOpsItems_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OpsItemFilters": [
      {
         "Key": "{{string}}",
         "Operator": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_DescribeOpsItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeOpsItems_RequestSyntax) **   <a name="systemsmanager-DescribeOpsItems-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeOpsItems_RequestSyntax) **   <a name="systemsmanager-DescribeOpsItems-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [OpsItemFilters](#API_DescribeOpsItems_RequestSyntax) **   <a name="systemsmanager-DescribeOpsItems-request-OpsItemFilters"></a>
One or more filters to limit the response.
+ Key: CreatedTime

  Operations: GreaterThan, LessThan
+ Key: LastModifiedBy

  Operations: Contains, Equals
+ Key: LastModifiedTime

  Operations: GreaterThan, LessThan
+ Key: Priority

  Operations: Equals
+ Key: Source

  Operations: Contains, Equals
+ Key: Status

  Operations: Equals
+ Key: Title\*

  Operations: Equals,Contains
+ Key: OperationalData\*\*

  Operations: Equals
+ Key: OperationalDataKey

  Operations: Equals
+ Key: OperationalDataValue

  Operations: Equals, Contains
+ Key: OpsItemId

  Operations: Equals
+ Key: ResourceId

  Operations: Contains
+ Key: AutomationId

  Operations: Equals
+ Key: AccountId

  Operations: Equals
\*The Equals operator for Title matches the first 100 characters. If you specify more than 100 characters, they system returns an error that the filter value exceeds the length limit.
\*\*If you filter the response by using the OperationalData operator, specify a key-value pair by using the following JSON format: {"key":"key\_name","value":"a\_value"}
Type: Array of [OpsItemFilter](API_OpsItemFilter.md) objects
Required: No

## Response Syntax
<a name="API_DescribeOpsItems_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OpsItemSummaries": [
      {
         "ActualEndTime": number,
         "ActualStartTime": number,
         "Category": "string",
         "CreatedBy": "string",
         "CreatedTime": number,
         "LastModifiedBy": "string",
         "LastModifiedTime": number,
         "OperationalData": {
            "string" : {
               "Type": "string",
               "Value": "string"
            }
         },
         "OpsItemId": "string",
         "OpsItemType": "string",
         "PlannedEndTime": number,
         "PlannedStartTime": number,
         "Priority": number,
         "Severity": "string",
         "Source": "string",
         "Status": "string",
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeOpsItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeOpsItems_ResponseSyntax) **   <a name="systemsmanager-DescribeOpsItems-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [OpsItemSummaries](#API_DescribeOpsItems_ResponseSyntax) **   <a name="systemsmanager-DescribeOpsItems-response-OpsItemSummaries"></a>
A list of OpsItems.
Type: Array of [OpsItemSummary](API_OpsItemSummary.md) objects

## Errors
<a name="API_DescribeOpsItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeOpsItems_Examples"></a>

### Example
<a name="API_DescribeOpsItems_Example_1"></a>

This example illustrates one usage of DescribeOpsItems.

#### Sample Request
<a name="API_DescribeOpsItems_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeOpsItems
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T163154Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 80

{
    "OpsItemFilters": [
        {
            "Key": "Status",
            "Values": [
                "Open"
            ],
            "Operator": "Equal"
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeOpsItems_Example_1_Response"></a>

```
{
    "OpsItemSummaries": [
        {
            "CreatedBy": "arn:aws:iam::111122223333:user/example",
            "CreatedTime": 1585757579.218,
            "LastModifiedBy": "arn:aws:iam::111122223333:user/example",
            "LastModifiedTime": 1585757579.218,
            "OpsItemId": "oi-1f050EXAMPLE",
            "Source": "SSM",
            "Status": "Open",
            "Title": "DocumentDeleted"
        },
        {
            "Category": "Availability",
            "CreatedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
            "CreatedTime": 1582701517.193,
            "LastModifiedBy": "arn:aws:sts::111122223333:assumed-role/OpsCenterRole/af3935bb93783f02aeea51784EXAMPLE",
            "LastModifiedTime": 1582701517.193,
            "OperationalData": {
                "/aws/dedup": {
                    "Type": "SearchableString",
                    "Value": "{\"dedupString\":\"SSMOpsItems-SSM-maintenance-window-execution-failed\"}"
                },
                "/aws/resources": {
                    "Type": "SearchableString",
                    "Value": "[{\"arn\":\"arn:aws:ssm:us-east-2:111122223333:maintenancewindow/mw-0e357ebdc6EXAMPLE\"}]"
                }
            },
            "OpsItemId": "oi-f99f2EXAMPLE",
            "Severity": "3",
            "Source": "SSM",
            "Status": "Open",
            "Title": "SSM Maintenance Window execution failed"
        }
    ]
}
```

## See Also
<a name="API_DescribeOpsItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeOpsItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeOpsItems)
