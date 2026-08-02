---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListNodes.html
---

# ListNodes
<a name="API_ListNodes"></a>

Takes in filters and returns a list of managed nodes matching the filter criteria.

## Request Syntax
<a name="API_ListNodes_RequestSyntax"></a>

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
   "SyncName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNodes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListNodes_RequestSyntax) **   <a name="systemsmanager-ListNodes-request-Filters"></a>
One or more filters. Use a filter to return a more specific list of managed nodes.
Type: Array of [NodeFilter](API_NodeFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_ListNodes_RequestSyntax) **   <a name="systemsmanager-ListNodes-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListNodes_RequestSyntax) **   <a name="systemsmanager-ListNodes-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [SyncName](#API_ListNodes_RequestSyntax) **   <a name="systemsmanager-ListNodes-request-SyncName"></a>
The name of the AWS managed resource data sync to retrieve information about.
For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is `AWS-QuickSetup-ManagedNode`.
For single account/single-Region configurations, the parameter is not required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_ListNodes_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Nodes": [
      {
         "CaptureTime": number,
         "Id": "string",
         "NodeType": { ... },
         "Owner": {
            "AccountId": "string",
            "OrganizationalUnitId": "string",
            "OrganizationalUnitPath": "string"
         },
         "Region": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNodes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNodes_ResponseSyntax) **   <a name="systemsmanager-ListNodes-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Nodes](#API_ListNodes_ResponseSyntax) **   <a name="systemsmanager-ListNodes-response-Nodes"></a>
A list of managed nodes that match the specified filter criteria.
Type: Array of [Node](API_Node.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListNodes_Errors"></a>

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

 ** ResourceDataSyncNotFoundException **
The specified sync name wasn't found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
This operation is not supported for the current account. You must first enable the Systems Manager integrated experience in your account.
HTTP Status Code: 400

## Examples
<a name="API_ListNodes_Examples"></a>

### Example
<a name="API_ListNodes_Example_1"></a>

This example illustrates one usage of ListNodes.

#### Sample Request
<a name="API_ListNodes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListNodes
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20241119/25T150301Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 97

{
  "SyncName": "AWS-QuickSetup-ManagedNode",
  "Filters": [
    {
      "Key": "Region",
      "Values": [
        "us-east-2"
      ],
      "Type": "Equal"
    }
  ],
  "MaxResults": 1
}
```

#### Sample Response
<a name="API_ListNodes_Example_1_Response"></a>

```
{
  "NextToken": "A9lT8CAxj9aDFRi+MNA---truncated---oFq08IEXAMPLE",
  "Nodes": [
    {
      "CaptureTime": 2024-11-19T22:01:18,
      "Id": "i-0471e04240EXAMPLE",
      "NodeType": {
        "Instance": {
          "AgentType": "amazon-ssm-agent",
          "AgentVersion": "3.3.859.0",
          "ComputerName": "ip-192.0.2.0.ec2.internal",
          "InstanceStatus": "Active",
          "IpAddress": "192.0.2.0",
          "ManagedStatus": "Managed",
          "PlatformName": "Amazon Linux",
          "PlatformType": "Linux",
          "PlatformVersion": "2023",
          "ResourceType": "EC2Instance"
        }
      },
      "Owner": {
        "AccountId": "444455556666",
        "OrganizationalUnitId": "ou-b8dn-sEXAMPLE",
        "OrganizationalUnitPath": "r-b8dn/ou-b8dn-sEXAMPLE"
      },
      "Region": "us-east-2"
    }
  ]
}
```

## See Also
<a name="API_ListNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListNodes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListNodes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListNodes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListNodes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListNodes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListNodes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListNodes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListNodes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListNodes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListNodes)
