---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetInventory.html
---

# GetInventory
<a name="API_GetInventory"></a>

Query inventory information. This includes managed node status, such as `Stopped` or `Terminated`.

## Request Syntax
<a name="API_GetInventory_RequestSyntax"></a>

```
{
   "Aggregators": [
      {
         "Aggregators": [
            "InventoryAggregator"
         ],
         "Expression": "{{string}}",
         "Groups": [
            {
               "Filters": [
                  {
                     "Key": "{{string}}",
                     "Type": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               ],
               "Name": "{{string}}"
            }
         ]
      }
   ],
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResultAttributes": [
      {
         "TypeName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_GetInventory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aggregators](#API_GetInventory_RequestSyntax) **   <a name="systemsmanager-GetInventory-request-Aggregators"></a>
Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the `AWS:InstanceInformation.PlatformType` type, you can see a count of how many Windows and Linux managed nodes exist in your inventoried fleet.
Type: Array of [InventoryAggregator](API_InventoryAggregator.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [Filters](#API_GetInventory_RequestSyntax) **   <a name="systemsmanager-GetInventory-request-Filters"></a>
One or more filters. Use a filter to return a more specific list of results.
Type: Array of [InventoryFilter](API_InventoryFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_GetInventory_RequestSyntax) **   <a name="systemsmanager-GetInventory-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_GetInventory_RequestSyntax) **   <a name="systemsmanager-GetInventory-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [ResultAttributes](#API_GetInventory_RequestSyntax) **   <a name="systemsmanager-GetInventory-request-ResultAttributes"></a>
The list of inventory item types to return.
Type: Array of [ResultAttribute](API_ResultAttribute.md) objects
Array Members: Fixed number of 1 item.
Required: No

## Response Syntax
<a name="API_GetInventory_ResponseSyntax"></a>

```
{
   "Entities": [
      {
         "Data": {
            "string" : {
               "CaptureTime": "string",
               "Content": [
                  {
                     "string" : "string"
                  }
               ],
               "ContentHash": "string",
               "SchemaVersion": "string",
               "TypeName": "string"
            }
         },
         "Id": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetInventory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entities](#API_GetInventory_ResponseSyntax) **   <a name="systemsmanager-GetInventory-response-Entities"></a>
Collection of inventory entities such as a collection of managed node inventory.
Type: Array of [InventoryResultEntity](API_InventoryResultEntity.md) objects

 ** [NextToken](#API_GetInventory_ResponseSyntax) **   <a name="systemsmanager-GetInventory-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_GetInventory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAggregatorException **
The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.
HTTP Status Code: 400

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidInventoryGroupException **
The specified inventory group isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

 ** InvalidResultAttributeException **
The specified inventory item result attribute isn't valid.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_GetInventory_Examples"></a>

### Example
<a name="API_GetInventory_Example_1"></a>

This example illustrates one usage of GetInventory.

#### Sample Request
<a name="API_GetInventory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetInventory
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240330T145054Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240330/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_GetInventory_Example_1_Response"></a>

```
{
    "Entities": [
        {
            "Data": {
                "Id": "i-04bf6ad63bEXAMPLE",
                "AWS:InstanceInformation": {
                    "TypeName": "AWS:InstanceInformation",
                    "SchemaVersion": "1.0",
                    "CaptureTime": "2024-03-30T14:00:57Z",
                    "Content": [
                        {
                            "AgentType": "amazon-ssm-agent",
                            "AgentVersion": "2.3.930.0",
                            "ComputerName": "EC2AMAZ-EXAMPLE.WORKGROUP",
                            "InstanceId": "i-04bf6ad63bEXAMPLE",
                            "InstanceStatus": "Stopped",
                            "IpAddress": "172.16.0.4",
                            "PlatformName": "Microsoft Windows Server 2016 Datacenter",
                            "PlatformType": "Windows",
                            "PlatformVersion": "10.0.14393",
                            "ResourceType": "EC2Instance"
                        }
                    ]
                }
            }
        }
    ]
}
```

## See Also
<a name="API_GetInventory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetInventory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetInventory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetInventory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetInventory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetInventory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetInventory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetInventory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetInventory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetInventory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetInventory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
