---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DeleteAlias.html
---

# DeleteAlias
<a name="API_DeleteAlias"></a>

Deletes the specified alias.

**Note**
Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the * AWS Key Management Service Developer Guide*.

Because an alias is not a property of a KMS key, you can delete and change the aliases of a KMS key without affecting the KMS key. Also, aliases do not appear in the response from the [DescribeKey](API_DescribeKey.md) operation. To get the aliases of all KMS keys, use the [ListAliases](API_ListAliases.md) operation.

Each KMS key can have multiple aliases. To change the alias of a KMS key, use [DeleteAlias](#API_DeleteAlias) to delete the current alias and [CreateAlias](API_CreateAlias.md) to create a new alias. To associate an existing alias with a different KMS key, call [UpdateAlias](API_UpdateAlias.md).

 **Cross-account use**: No. You cannot perform this operation on an alias in a different AWS account.

 **Required permissions**
+  [kms:DeleteAlias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) on the alias (IAM policy).
+  [kms:DeleteAlias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) on the KMS key (key policy).

For details, see [Controlling access to aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html#alias-access) in the * AWS Key Management Service Developer Guide*.

 **Related operations:**
+  [CreateAlias](API_CreateAlias.md)
+  [ListAliases](API_ListAliases.md)
+  [UpdateAlias](API_UpdateAlias.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DeleteAlias_RequestSyntax"></a>

```
{
   "AliasName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasName](#API_DeleteAlias_RequestSyntax) **   <a name="KMS-DeleteAlias-request-AliasName"></a>
The alias to be deleted. The alias name must begin with `alias/` followed by the alias name, such as `alias/ExampleAlias`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: Yes

## Response Elements
<a name="API_DeleteAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource is not valid for this request.
This exceptions means one of the following:
+ The key state of the KMS key is not compatible with the operation.

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_DeleteAlias_Examples"></a>

### Example Request
<a name="API_DeleteAlias_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 34
X-Amz-Target: TrentService.DeleteAlias
X-Amz-Date: 20161104T183415Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161104/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=a57d9c76f60733ea93fe92ac4fa90ca82058a72913e4b8e52c262ffc96704d53

{"AliasName": "alias/ExampleAlias"}
```

### Example Response
<a name="API_DeleteAlias_Example_2"></a>

This example illustrates one usage of DeleteAlias.

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 04 Nov 2016 18:34:15 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 4a2313ae-a2bd-11e6-aea3-9bf897a0ae69
```

## See Also
<a name="API_DeleteAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DeleteAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DeleteAlias)
