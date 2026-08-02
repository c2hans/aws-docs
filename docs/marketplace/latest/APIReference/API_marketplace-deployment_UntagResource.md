---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_UntagResource.html
---

# UntagResource
<a name="API_marketplace-deployment_UntagResource"></a>

Removes a tag or list of tags from a resource.

## Request Syntax
<a name="API_marketplace-deployment_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_marketplace-deployment_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_marketplace-deployment_UntagResource_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.
Required: Yes

 ** [tagKeys](#API_marketplace-deployment_UntagResource_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-deployment_UntagResource-request-uri-tagKeys"></a>
A list of key names of tags to be removed.
Required: Yes

## Request Body
<a name="API_marketplace-deployment_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_marketplace-deployment_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_marketplace-deployment_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_marketplace-deployment_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
 ** resourceId **
The unique identifier for the resource associated with the error.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal service exception.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests.
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
 ** fieldName **
The field name associated with the error.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-deployment_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-deployment-2023-01-25/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-deployment-2023-01-25/UntagResource)
