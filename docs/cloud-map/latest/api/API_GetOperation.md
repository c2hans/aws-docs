---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetOperation.html
---

# GetOperation
<a name="API_GetOperation"></a>

Gets information about any operation that returns an operation ID in the response, such as a `CreateHttpNamespace` request.

**Note**
To get a list of operations that match specified criteria, see [ListOperations](https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html).

## Request Syntax
<a name="API_GetOperation_RequestSyntax"></a>

```
{
   "OperationId": "{{string}}",
   "OwnerAccount": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOperation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OperationId](#API_GetOperation_RequestSyntax) **   <a name="cloudmap-GetOperation-request-OperationId"></a>
The ID of the operation that you want to get more information about.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [OwnerAccount](#API_GetOperation_RequestSyntax) **   <a name="cloudmap-GetOperation-request-OwnerAccount"></a>
The ID of the AWS account that owns the namespace associated with the operation, as specified in the namespace `ResourceOwner` field. For operations associated with namespaces that are shared with your account, you must specify an `OwnerAccount`.
Type: String
Length Constraints: Fixed length of 12.
Required: No

## Response Syntax
<a name="API_GetOperation_ResponseSyntax"></a>

```
{
   "Operation": {
      "CreateDate": number,
      "ErrorCode": "string",
      "ErrorMessage": "string",
      "Id": "string",
      "OwnerAccount": "string",
      "Status": "string",
      "Targets": {
         "string" : "string"
      },
      "Type": "string",
      "UpdateDate": number
   }
}
```

## Response Elements
<a name="API_GetOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Operation](#API_GetOperation_ResponseSyntax) **   <a name="cloudmap-GetOperation-response-Operation"></a>
A complex type that contains information about the operation.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_GetOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** OperationNotFound **
No operation exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetOperation_Examples"></a>

### GetOperation Example
<a name="API_GetOperation_Example_1"></a>

This example request retrieves information about the specified operation.

#### Sample Request
<a name="API_GetOperation_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211710Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetOperation
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "OperationId": "deleteelozuhfet5kzxoxg-a-response-example"
}
```

#### Sample Response
<a name="API_GetOperation_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Operation": {
        "CreateDate": "20181118T211707Z",
        "OwnerAccount": "123456789012"
        "Id": "deleteelozuhfet5kzxoxg-a-response-example",
        "Status": "SUCCESS",
        "Targets": {
            "NAMESPACE": "ns-e4anhexample0004"
        },
        "Type": "DELETE_NAMESPACE",
        "UpdateDate": "20181118T211708Z"
    }
}
```

### GetOperation Example using OwnerAccount
<a name="API_GetOperation_Example_2"></a>

This example request retrieves information about an operation associated with a shared namespace by specifying the OwnerAccount.

#### Sample Request
<a name="API_GetOperation_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211710Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetOperation
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "OperationId": "deleteelozuhfet5kzxoxg-a-response-example",
    "OwnerAccount": "123456789012"
}
```

#### Sample Response
<a name="API_GetOperation_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Operation": {
        "CreateDate": "20181118T211707Z",
        "OwnerAccount": "123456789012",
        "Id": "deleteelozuhfet5kzxoxg-a-response-example",
        "Status": "SUCCESS",
        "Targets": {
            "NAMESPACE": "ns-e4anhexample0004"
        },
        "Type": "DELETE_NAMESPACE",
        "UpdateDate": "20181118T211708Z"
    }
}
```

## See Also
<a name="API_GetOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
