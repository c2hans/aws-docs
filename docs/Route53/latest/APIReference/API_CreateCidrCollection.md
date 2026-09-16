---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateCidrCollection.html
---

# CreateCidrCollection
<a name="API_CreateCidrCollection"></a>

Creates a CIDR collection in the current AWS account.

## Request Syntax
<a name="API_CreateCidrCollection_RequestSyntax"></a>

```
POST /2013-04-01/cidrcollection HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateCidrCollectionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <CallerReference>{{string}}</CallerReference>
   <Name>{{string}}</Name>
</CreateCidrCollectionRequest>
```

## URI Request Parameters
<a name="API_CreateCidrCollection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCidrCollection_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateCidrCollectionRequest](#API_CreateCidrCollection_RequestSyntax) **   <a name="Route53-CreateCidrCollection-request-CreateCidrCollectionRequest"></a>
Root level tag for the CreateCidrCollectionRequest parameters.
Required: Yes

 ** [CallerReference](#API_CreateCidrCollection_RequestSyntax) **   <a name="Route53-CreateCidrCollection-request-CallerReference"></a>
A client-specific token that allows requests to be securely retried so that the intended outcome will only occur once, retries receive a similar response, and there are no additional edge cases to handle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `\p{ASCII}+`
Required: Yes

 ** [Name](#API_CreateCidrCollection_RequestSyntax) **   <a name="Route53-CreateCidrCollection-request-Name"></a>
A unique identifier for the account that can be used to reference the collection from other API calls.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9A-Za-z_\-]+`
Required: Yes

## Response Syntax
<a name="API_CreateCidrCollection_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateCidrCollectionResponse>
   <Collection>
      <Arn>string</Arn>
      <Id>string</Id>
      <Name>string</Name>
      <Version>long</Version>
   </Collection>
</CreateCidrCollectionResponse>
```

## Response Elements
<a name="API_CreateCidrCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateCidrCollection_ResponseSyntax) **   <a name="Route53-CreateCidrCollection-response-Location"></a>
A unique URL that represents the location for the CIDR collection.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateCidrCollectionResponse](#API_CreateCidrCollection_ResponseSyntax) **   <a name="Route53-CreateCidrCollection-response-CreateCidrCollectionResponse"></a>
Root level tag for the CreateCidrCollectionResponse parameters.
Required: Yes

 ** [Collection](#API_CreateCidrCollection_ResponseSyntax) **   <a name="Route53-CreateCidrCollection-response-Collection"></a>
A complex type that contains information about the CIDR collection.
Type: [CidrCollection](API_CidrCollection.md) object

## Errors
<a name="API_CreateCidrCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CidrCollectionAlreadyExistsException **
A CIDR collection with this name and a different caller reference already exists in this account.
HTTP Status Code: 400

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** LimitsExceeded **
This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateCidrCollection_Examples"></a>

### Example request
<a name="API_CreateCidrCollection_Example_1"></a>

This example illustrates one usage of CreateCidrCollection.

```
POST /2013-04-01/cidrcollection
<?xml version="1.0" encoding="UTF-8"?>
<CreateCidrCollectionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Name>isp-city-cidrs</Name>
    <CallerReference>ref1</CallerReference>
</CreateCidrCollectionRequest>
```

### Example response
<a name="API_CreateCidrCollection_Example_2"></a>

This example illustrates one usage of CreateCidrCollection.

```
HTTP/1.1 201 Created
<?xml version="1.0"?>
<CreateCidrCollectionResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
 <Collection>
   <Arn>arn:aws:route53:::cidrcollection/c8c02a84-aaaa-bbbb-e0d2-d833a2f80106</Arn>
   <Id>c8c02a84-aaaa-bbbb-e0d2-d833a2f80106</Id>
   <Name>isp-city-cidrs</Name>
   <Version>1</Version>
  </Collection>
</CreateCidrCollectionResponse>
```

## See Also
<a name="API_CreateCidrCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateCidrCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateCidrCollection)
