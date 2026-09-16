---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutInventory.html
---

# PutInventory
<a name="API_PutInventory"></a>

Bulk update custom inventory items on one or more managed nodes. The request adds an inventory item, if it doesn't already exist, or updates an inventory item, if it does exist.

## Request Syntax
<a name="API_PutInventory_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "Items": [
      {
         "CaptureTime": "{{string}}",
         "Content": [
            {
               "{{string}}" : "{{string}}"
            }
         ],
         "ContentHash": "{{string}}",
         "Context": {
            "{{string}}" : "{{string}}"
         },
         "SchemaVersion": "{{string}}",
         "TypeName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutInventory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_PutInventory_RequestSyntax) **   <a name="systemsmanager-PutInventory-request-InstanceId"></a>
An managed node ID where you want to add or update inventory items.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [Items](#API_PutInventory_RequestSyntax) **   <a name="systemsmanager-PutInventory-request-Items"></a>
The inventory items that you want to add or update on managed nodes.
Type: Array of [InventoryItem](API_InventoryItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

## Response Syntax
<a name="API_PutInventory_ResponseSyntax"></a>

```
{
   "Message": "string"
}
```

## Response Elements
<a name="API_PutInventory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_PutInventory_ResponseSyntax) **   <a name="systemsmanager-PutInventory-response-Message"></a>
Information about the request.
Type: String

## Errors
<a name="API_PutInventory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CustomSchemaCountLimitExceededException **
You have exceeded the limit for custom schemas. Delete one or more custom schemas and try again.
HTTP Status Code: 400

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

 ** InvalidInventoryItemContextException **
You specified invalid keys or values in the `Context` attribute for `InventoryItem`. Verify the keys and values, and try again.
HTTP Status Code: 400

 ** InvalidItemContentException **
One or more content items isn't valid.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

 ** ItemContentMismatchException **
The inventory item has invalid content.
HTTP Status Code: 400

 ** ItemSizeLimitExceededException **
The inventory item size has exceeded the size limit.
HTTP Status Code: 400

 ** SubTypeCountLimitExceededException **
The sub-type count exceeded the limit for the inventory type.
HTTP Status Code: 400

 ** TotalSizeLimitExceededException **
The size of inventory data has exceeded the total size limit for the resource.
HTTP Status Code: 400

 ** UnsupportedInventoryItemContextException **
The `Context` attribute that you specified for the `InventoryItem` isn't allowed for this inventory type. You can only use the `Context` attribute with inventory types like `AWS:ComplianceItem`.
HTTP Status Code: 400

 ** UnsupportedInventorySchemaVersionException **
Inventory item type schema version has to match supported versions in the service. Check output of GetInventorySchema to see the available schema version for each type.
HTTP Status Code: 400

## Examples
<a name="API_PutInventory_Examples"></a>

### Example
<a name="API_PutInventory_Example_1"></a>

This example illustrates one usage of PutInventory.

#### Sample Request
<a name="API_PutInventory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.PutInventory
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240401T181858Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240401/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 180

{
    "InstanceId": "i-0cb99161f6EXAMPLE",
    "Items": [
        {
            "TypeName": "Custom:StageInfo",
            "SchemaVersion": "1.0",
            "CaptureTime": "2020-03-31T08:00:00Z",
            "Content": [
                {
                    "Stage": "PreProd"
                }
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_PutInventory_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_PutInventory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/PutInventory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/PutInventory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PutInventory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/PutInventory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PutInventory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/PutInventory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/PutInventory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/PutInventory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/PutInventory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PutInventory)
