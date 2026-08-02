---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetOperation.html
---

# GetOperation
<a name="API_GetOperation"></a>

Gets the details of an operation by specifying the operation ID.

## Request Syntax
<a name="API_GetOperation_RequestSyntax"></a>

```
POST /get-operation HTTP/1.1
Content-type: application/json

{
   "OperationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetOperation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetOperation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OperationId](#API_GetOperation_RequestSyntax) **   <a name="ssmsap-GetOperation-request-OperationId"></a>
The ID of the operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: Yes

## Response Syntax
<a name="API_GetOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Operation": {
      "EndTime": number,
      "Id": "string",
      "LastUpdatedTime": number,
      "Properties": {
         "string" : "string"
      },
      "ResourceArn": "string",
      "ResourceId": "string",
      "ResourceType": "string",
      "StartTime": number,
      "Status": "string",
      "StatusMessage": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_GetOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Operation](#API_GetOperation_ResponseSyntax) **   <a name="ssmsap-GetOperation-response-Operation"></a>
Returns the details of an operation.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_GetOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetOperation)
