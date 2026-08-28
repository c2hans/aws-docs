---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInventoryDeletions.html
---

# DescribeInventoryDeletions
<a name="API_DescribeInventoryDeletions"></a>

Describes a specific delete inventory operation.

## Request Syntax
<a name="API_DescribeInventoryDeletions_RequestSyntax"></a>

```
{
   "DeletionId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInventoryDeletions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeletionId](#API_DescribeInventoryDeletions_RequestSyntax) **   <a name="systemsmanager-DescribeInventoryDeletions-request-DeletionId"></a>
Specify the delete inventory ID for which you want information. This ID was returned by the `DeleteInventory` operation.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [MaxResults](#API_DescribeInventoryDeletions_RequestSyntax) **   <a name="systemsmanager-DescribeInventoryDeletions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeInventoryDeletions_RequestSyntax) **   <a name="systemsmanager-DescribeInventoryDeletions-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInventoryDeletions_ResponseSyntax"></a>

```
{
   "InventoryDeletions": [
      {
         "DeletionId": "string",
         "DeletionStartTime": number,
         "DeletionSummary": {
            "RemainingCount": number,
            "SummaryItems": [
               {
                  "Count": number,
                  "RemainingCount": number,
                  "Version": "string"
               }
            ],
            "TotalCount": number
         },
         "LastStatus": "string",
         "LastStatusMessage": "string",
         "LastStatusUpdateTime": number,
         "TypeName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInventoryDeletions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InventoryDeletions](#API_DescribeInventoryDeletions_ResponseSyntax) **   <a name="systemsmanager-DescribeInventoryDeletions-response-InventoryDeletions"></a>
A list of status items for deleted inventory.
Type: Array of [InventoryDeletionStatusItem](API_InventoryDeletionStatusItem.md) objects

 ** [NextToken](#API_DescribeInventoryDeletions_ResponseSyntax) **   <a name="systemsmanager-DescribeInventoryDeletions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_DescribeInventoryDeletions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDeletionIdException **
The ID specified for the delete operation doesn't exist or isn't valid. Verify the ID and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInventoryDeletions_Examples"></a>

### Example
<a name="API_DescribeInventoryDeletions_Example_1"></a>

This example illustrates one usage of DescribeInventoryDeletions.

#### Sample Request
<a name="API_DescribeInventoryDeletions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeInventoryDeletions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.25 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/ssm.describe-inventory-deletions
X-Amz-Date: 20240810T211220Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240810/us-west-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2

{}
```

#### Sample Response
<a name="API_DescribeInventoryDeletions_Example_1_Response"></a>

```
{
  "InventoryDeletions": [
    {
      "DeletionId": "5bc2ba3b-ee6a-40fa-8d09-5eExample",
      "DeletionStartTime": 1628550146,
      "DeletionSummary": {
        "RemainingCount": 0,
        "SummaryItems": [
          {
            "Count": 1,
            "RemainingCount": 0,
            "Version": "1.0"
          }
        ],
        "TotalCount": 1
      },
      "LastStatus": "Complete",
      "LastStatusMessage": "Deletion is successful",
      "LastStatusUpdateTime": 1628550238,
      "TypeName": "Custom:RackInfo"
    }
  ]
}
```

## See Also
<a name="API_DescribeInventoryDeletions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInventoryDeletions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInventoryDeletions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
