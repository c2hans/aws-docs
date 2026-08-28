---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListComplianceItems.html
---

# ListComplianceItems
<a name="API_ListComplianceItems"></a>

For a specified resource ID, this API operation returns a list of compliance statuses for different resource types. Currently, you can only specify one resource ID per call. List results depend on the criteria specified in the filter.

## Request Syntax
<a name="API_ListComplianceItems_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceIds": [ "{{string}}" ],
   "ResourceTypes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListComplianceItems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListComplianceItems_RequestSyntax) **   <a name="systemsmanager-ListComplianceItems-request-Filters"></a>
One or more compliance filters. Use a filter to return a more specific list of results.
Type: Array of [ComplianceStringFilter](API_ComplianceStringFilter.md) objects
Required: No

 ** [MaxResults](#API_ListComplianceItems_RequestSyntax) **   <a name="systemsmanager-ListComplianceItems-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListComplianceItems_RequestSyntax) **   <a name="systemsmanager-ListComplianceItems-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [ResourceIds](#API_ListComplianceItems_RequestSyntax) **   <a name="systemsmanager-ListComplianceItems-request-ResourceIds"></a>
The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [ResourceTypes](#API_ListComplianceItems_RequestSyntax) **   <a name="systemsmanager-ListComplianceItems-request-ResourceTypes"></a>
The type of resource from which to get compliance information. Currently, the only supported resource type is `ManagedInstance`.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## Response Syntax
<a name="API_ListComplianceItems_ResponseSyntax"></a>

```
{
   "ComplianceItems": [
      {
         "ComplianceType": "string",
         "Details": {
            "string" : "string"
         },
         "ExecutionSummary": {
            "ExecutionId": "string",
            "ExecutionTime": number,
            "ExecutionType": "string"
         },
         "Id": "string",
         "ResourceId": "string",
         "ResourceType": "string",
         "Severity": "string",
         "Status": "string",
         "Title": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListComplianceItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComplianceItems](#API_ListComplianceItems_ResponseSyntax) **   <a name="systemsmanager-ListComplianceItems-response-ComplianceItems"></a>
A list of compliance information for the specified resource ID.
Type: Array of [ComplianceItem](API_ComplianceItem.md) objects

 ** [NextToken](#API_ListComplianceItems_ResponseSyntax) **   <a name="systemsmanager-ListComplianceItems-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

## Errors
<a name="API_ListComplianceItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidResourceId **
The resource ID isn't valid. Verify that you entered the correct ID and try again.
HTTP Status Code: 400

 ** InvalidResourceType **
The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.
HTTP Status Code: 400

## Examples
<a name="API_ListComplianceItems_Examples"></a>

### Example
<a name="API_ListComplianceItems_Example_1"></a>

This example illustrates one usage of ListComplianceItems.

#### Sample Request
<a name="API_ListComplianceItems_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListComplianceItems
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T173645Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 40

{
    "ResourceIds": [
        "i-0cb99161f6EXAMPLE"
    ]
}
```

#### Sample Response
<a name="API_ListComplianceItems_Example_1_Response"></a>

```
{
    "ComplianceItems": [
        {
            "ComplianceType": "Association",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-0cb99161f6EXAMPLE",
            "Id": "bdf308d4-b431-440d-a2ee-dcca7EXAMPLE",
            "Title": "",
            "Status": "COMPLIANT",
            "Severity": "UNSPECIFIED",
            "ExecutionSummary": {
                "ExecutionTime": 1585761335
            },
            "Details": {
                "DocumentName": "AWS-GatherSoftwareInventory",
                "DocumentVersion": "1"
            }
        },
        {
            "ComplianceType": "Association",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-0cb99161f6EXAMPLE",
            "Id": "fa94c678-85c6-4d40-926b-7c791EXAMPLE",
            "Title": "",
            "Status": "COMPLIANT",
            "Severity": "HIGH",
            "ExecutionSummary": {
                "ExecutionTime": 1585761335
            },
            "Details": {
                "DocumentName": "AWS-UpdateSSMAgent",
                "DocumentVersion": "1"
            }
        }
    ]
}
```

## See Also
<a name="API_ListComplianceItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListComplianceItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListComplianceItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
