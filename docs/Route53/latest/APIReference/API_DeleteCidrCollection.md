---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteCidrCollection.html
---

# DeleteCidrCollection
<a name="API_DeleteCidrCollection"></a>

Deletes a CIDR collection in the current AWS account. The collection must be empty before it can be deleted.

## Request Syntax
<a name="API_DeleteCidrCollection_RequestSyntax"></a>

```
DELETE /2013-04-01/cidrcollection/{{CidrCollectionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCidrCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CidrCollectionId](#API_DeleteCidrCollection_RequestSyntax) **   <a name="Route53-DeleteCidrCollection-request-uri-Id"></a>
The UUID of the collection to delete.
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_DeleteCidrCollection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCidrCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCidrCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCidrCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CidrCollectionInUseException **
This CIDR collection is in use, and isn't empty.
HTTP Status Code: 400

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchCidrCollectionException **
The CIDR collection you specified, doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_DeleteCidrCollection_Examples"></a>

### Example request
<a name="API_DeleteCidrCollection_Example_1"></a>

This example illustrates one usage of DeleteCidrCollection.

```
DELETE /2013-04-01/cidrcollection/c8c02a84-aaaa-bbbb-e0d2-d833a2f80106
```

### Example response
<a name="API_DeleteCidrCollection_Example_2"></a>

This example illustrates one usage of DeleteCidrCollection.

```
HTTP/1.1 200 OK
<?xml version="1.0"?>
<DeleteCidrCollectionResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/"/>
```

## See Also
<a name="API_DeleteCidrCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteCidrCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteCidrCollection)
