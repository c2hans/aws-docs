---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteInventory.html
---

# DeleteInventory
<a name="API_DeleteInventory"></a>

Delete a custom inventory type or the data associated with a custom Inventory type. Deleting a custom inventory type is also referred to as deleting a custom inventory schema.

## Request Syntax
<a name="API_DeleteInventory_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DryRun": {{boolean}},
   "SchemaDeleteOption": "{{string}}",
   "TypeName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteInventory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_DeleteInventory_RequestSyntax) **   <a name="systemsmanager-DeleteInventory-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [DryRun](#API_DeleteInventory_RequestSyntax) **   <a name="systemsmanager-DeleteInventory-request-DryRun"></a>
Use this option to view a summary of the deletion request without deleting any data or the data type. This option is useful when you only want to understand what will be deleted. Once you validate that the data to be deleted is what you intend to delete, you can run the same command without specifying the `DryRun` option.
Type: Boolean
Required: No

 ** [SchemaDeleteOption](#API_DeleteInventory_RequestSyntax) **   <a name="systemsmanager-DeleteInventory-request-SchemaDeleteOption"></a>
Use the `SchemaDeleteOption` to delete a custom inventory type (schema). If you don't choose this option, the system only deletes existing inventory data associated with the custom inventory type. Choose one of the following options:
DisableSchema: If you choose this option, the system ignores all inventory data for the specified version, and any earlier versions. To enable this schema again, you must call the `PutInventory` operation for a version greater than the disabled version.
DeleteSchema: This option deletes the specified custom type from the Inventory service. You can recreate the schema later, if you want.
Type: String
Valid Values: `DisableSchema | DeleteSchema`
Required: No

 ** [TypeName](#API_DeleteInventory_RequestSyntax) **   <a name="systemsmanager-DeleteInventory-request-TypeName"></a>
The name of the custom inventory type for which you want to delete either all previously collected data or the inventory type itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

## Response Syntax
<a name="API_DeleteInventory_ResponseSyntax"></a>

```
{
   "DeletionId": "string",
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
   "TypeName": "string"
}
```

## Response Elements
<a name="API_DeleteInventory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionId](#API_DeleteInventory_ResponseSyntax) **   <a name="systemsmanager-DeleteInventory-response-DeletionId"></a>
Every `DeleteInventory` operation is assigned a unique ID. This option returns a unique ID. You can use this ID to query the status of a delete operation. This option is useful for ensuring that a delete operation has completed before you begin other operations.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [DeletionSummary](#API_DeleteInventory_ResponseSyntax) **   <a name="systemsmanager-DeleteInventory-response-DeletionSummary"></a>
A summary of the delete operation. For more information about this summary, see [Deleting custom inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom.html#delete-custom-inventory-summary) in the * AWS Systems Manager User Guide*.
Type: [InventoryDeletionSummary](API_InventoryDeletionSummary.md) object

 ** [TypeName](#API_DeleteInventory_ResponseSyntax) **   <a name="systemsmanager-DeleteInventory-response-TypeName"></a>
The name of the inventory data type specified in the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`

## Errors
<a name="API_DeleteInventory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDeleteInventoryParametersException **
One or more of the parameters specified for the delete operation isn't valid. Verify all parameters and try again.
HTTP Status Code: 400

 ** InvalidInventoryRequestException **
The request isn't valid.
HTTP Status Code: 400

 ** InvalidOptionException **
The delete inventory option specified isn't valid. Verify the option and try again.
HTTP Status Code: 400

 ** InvalidTypeNameException **
The parameter type name isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DeleteInventory_Examples"></a>

### Example
<a name="API_DeleteInventory_Example_1"></a>

This example illustrates one usage of DeleteInventory.

#### Sample Request
<a name="API_DeleteInventory_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-west-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteInventory
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.25 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/ssm.delete-inventory
X-Amz-Date: 20240809T230226Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240809/us-west-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature39c3b3042cd2aEXAMPLE
Content-Length: 124

{
  "TypeName": "Custom:RackInfo",
  "SchemaDeleteOption": "DeleteSchema",
  "ClientToken": "a7d4972c-ab3e-4b9a-b5c0-d5aExample"
}
```

#### Sample Response
<a name="API_DeleteInventory_Example_1_Response"></a>

```
{
  "DeletionId": "5bc2ba3b-ee6a-40fa-8d09-5e5Example",
  "DeletionSummary": {
    "RemainingCount": 1,
    "SummaryItems": [
      {
        "Count": 1,
        "RemainingCount": 1,
        "Version": "1.0"
      }
    ],
    "TotalCount": 1
  },
  "TypeName": "Custom:RackInfo"
}
```

## See Also
<a name="API_DeleteInventory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteInventory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteInventory)
