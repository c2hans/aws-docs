---
source_url: https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes the specified tags from the Amazon Managed Blockchain resource.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide*, or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide*.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="ManagedBlockchain-UntagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn:.+:.+:.+:.+:.+`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="ManagedBlockchain-UntagResource-request-uri-TagKeys"></a>
The tag keys.
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidRequestException **
The action or operation requested is invalid. Verify that the action is typed correctly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A requested resource doesn't exist. It may have been deleted or referenced incorrectly.
 ** ResourceName **
A requested resource doesn't exist. It may have been deleted or referenced inaccurately.
HTTP Status Code: 404

 ** ResourceNotReadyException **
The requested resource exists but isn't in a status that can complete the operation.
HTTP Status Code: 409

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/managedblockchain-2018-09-24/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/managedblockchain-2018-09-24/UntagResource)
