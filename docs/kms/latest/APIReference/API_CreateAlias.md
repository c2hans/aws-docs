---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateAlias.html
---

# CreateAlias
<a name="API_CreateAlias"></a>

Creates a friendly name for a KMS key.

**Note**
Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the * AWS Key Management Service Developer Guide*.

You can use an alias to identify a KMS key in the AWS KMS console, in the [DescribeKey](API_DescribeKey.md) operation and in [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations), such as [Encrypt](API_Encrypt.md) and [GenerateDataKey](API_GenerateDataKey.md). You can also change the KMS key that's associated with the alias ([UpdateAlias](API_UpdateAlias.md)) or delete the alias ([DeleteAlias](API_DeleteAlias.md)) at any time. These operations don't affect the underlying KMS key.

You can associate the alias with any customer managed key in the same AWS Region. Each alias is associated with only one KMS key at a time, but a KMS key can have multiple aliases. A valid KMS key is required. You can't create an alias without a KMS key.

The alias must be unique in the account and Region, but you can have aliases with the same name in different Regions. For detailed information about aliases, see [Aliases in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html) in the * AWS Key Management Service Developer Guide*.

This operation does not return a response. To get the alias that you created, use the [ListAliases](API_ListAliases.md) operation.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on an alias in a different AWS account.

 **Required permissions**
+  [kms:CreateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) on the alias (IAM policy).
+  [kms:CreateAlias](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) on the KMS key (key policy).

For details, see [Controlling access to aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-access.html) in the * AWS Key Management Service Developer Guide*.

 **Related operations:**
+  [DeleteAlias](API_DeleteAlias.md)
+  [ListAliases](API_ListAliases.md)
+  [UpdateAlias](API_UpdateAlias.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_CreateAlias_RequestSyntax"></a>

```
{
   "AliasName": "{{string}}",
   "TargetKeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAlias_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AliasName](#API_CreateAlias_RequestSyntax) **   <a name="KMS-CreateAlias-request-AliasName"></a>
Specifies the alias name. This value must begin with `alias/` followed by a name, such as `alias/ExampleAlias`.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
The `AliasName` value must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (\_), and dashes (-). The alias name cannot begin with `alias/aws/`. The `alias/aws/` prefix is reserved for [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^alias/[a-zA-Z0-9/_-]+$`
Required: Yes

 ** [TargetKeyId](#API_CreateAlias_RequestSyntax) **   <a name="KMS-CreateAlias-request-TargetKeyId"></a>
Associates the alias with the specified [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key). The KMS key must be in the same AWS Region.
A valid key ID is required. If you supply a null or empty string value, this operation returns an error.
For help finding the key ID and ARN, see [Find the key ID and key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html) in the * * AWS Key Management Service Developer Guide* *.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_CreateAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 400

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidAliasNameException **
The request was rejected because the specified alias name is not valid.
HTTP Status Code: 400

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

 ** LimitExceededException **
The request was rejected because a length constraint or quota was exceeded. For more information, see [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_CreateAlias_Examples"></a>

### Example Request
<a name="API_CreateAlias_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-west-2.amazonaws.com
Content-Length: 87
X-Amz-Target: TrentService.CreateAlias
X-Amz-Date: 20160517T204220Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20160517/us-west-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=ca7bcf1e8d5364dc3f0d881c05bdadf36f498c6c6a8b576a060142d9b2199123

{
  "TargetKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
  "AliasName": "alias/ExampleAlias"
}
```

### Example Response
<a name="API_CreateAlias_Example_2"></a>

This example illustrates one usage of CreateAlias.

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 17 May 2016 20:42:25 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: dcb07ca7-1c6f-11e6-8540-77c363708b91
```

## See Also
<a name="API_CreateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/CreateAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/CreateAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/CreateAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/CreateAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/CreateAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/CreateAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/CreateAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/CreateAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/CreateAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/CreateAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
