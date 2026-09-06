---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_BatchDisassociateResource.html
---

# BatchDisassociateResource
<a name="API_BatchDisassociateResource"></a>

Disassociates resources from a Firewall Manager resource set.

## Request Syntax
<a name="API_BatchDisassociateResource_RequestSyntax"></a>

```
{
   "Items": [ "{{string}}" ],
   "ResourceSetIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchDisassociateResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Items](#API_BatchDisassociateResource_RequestSyntax) **   <a name="fms-BatchDisassociateResource-request-Items"></a>
The uniform resource identifiers (URI) of resources that should be disassociated from the resource set. The URIs must be Amazon Resource Names (ARNs).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** [ResourceSetIdentifier](#API_BatchDisassociateResource_RequestSyntax) **   <a name="fms-BatchDisassociateResource-request-ResourceSetIdentifier"></a>
A unique identifier for the resource set, used in a request to refer to the resource set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_BatchDisassociateResource_ResponseSyntax"></a>

```
{
   "FailedItems": [
      {
         "Reason": "string",
         "URI": "string"
      }
   ],
   "ResourceSetIdentifier": "string"
}
```

## Response Elements
<a name="API_BatchDisassociateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FailedItems](#API_BatchDisassociateResource_ResponseSyntax) **   <a name="fms-BatchDisassociateResource-response-FailedItems"></a>
The resources that failed to disassociate from the resource set.
Type: Array of [FailedItem](API_FailedItem.md) objects

 ** [ResourceSetIdentifier](#API_BatchDisassociateResource_ResponseSyntax) **   <a name="fms-BatchDisassociateResource-response-ResourceSetIdentifier"></a>
A unique identifier for the resource set, used in a request to refer to the resource set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_BatchDisassociateResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_BatchDisassociateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/BatchDisassociateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/BatchDisassociateResource)
