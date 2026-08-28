---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeCidrCollection.html
---

# ChangeCidrCollection
<a name="API_ChangeCidrCollection"></a>

Creates, changes, or deletes CIDR blocks within a collection. Contains authoritative IP information mapping blocks to one or multiple locations.

A change request can update multiple locations in a collection at a time, which is helpful if you want to move one or more CIDR blocks from one location to another in one transaction, without downtime.

 **Limits**

The max number of CIDR blocks included in the request is 1000. As a result, big updates require multiple API calls.

 ** PUT and DELETE\_IF\_EXISTS**

Use `ChangeCidrCollection` to perform the following actions:
+  `PUT`: Create a CIDR block within the specified collection.
+  ` DELETE_IF_EXISTS`: Delete an existing CIDR block from the collection.

## Request Syntax
<a name="API_ChangeCidrCollection_RequestSyntax"></a>

```
POST /2013-04-01/cidrcollection/{{CidrCollectionId}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeCidrCollectionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Changes>
      <CidrCollectionChange>
         <Action>{{string}}</Action>
         <CidrList>
            <Cidr>{{string}}</Cidr>
         </CidrList>
         <LocationName>{{string}}</LocationName>
      </CidrCollectionChange>
   </Changes>
   <CollectionVersion>{{long}}</CollectionVersion>
</ChangeCidrCollectionRequest>
```

## URI Request Parameters
<a name="API_ChangeCidrCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CidrCollectionId](#API_ChangeCidrCollection_RequestSyntax) **   <a name="Route53-ChangeCidrCollection-request-uri-Id"></a>
The UUID of the CIDR collection to update.
Pattern: `[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_ChangeCidrCollection_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ChangeCidrCollectionRequest](#API_ChangeCidrCollection_RequestSyntax) **   <a name="Route53-ChangeCidrCollection-request-ChangeCidrCollectionRequest"></a>
Root level tag for the ChangeCidrCollectionRequest parameters.
Required: Yes

 ** [Changes](#API_ChangeCidrCollection_RequestSyntax) **   <a name="Route53-ChangeCidrCollection-request-Changes"></a>
 Information about changes to a CIDR collection.
Type: Array of [CidrCollectionChange](API_CidrCollectionChange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: Yes

 ** [CollectionVersion](#API_ChangeCidrCollection_RequestSyntax) **   <a name="Route53-ChangeCidrCollection-request-CollectionVersion"></a>
A sequential counter that Amazon Route 53 sets to 1 when you create a collection and increments it by 1 each time you update the collection.
We recommend that you use `ListCidrCollection` to get the current value of `CollectionVersion` for the collection that you want to update, and then include that value with the change request. This prevents Route 53 from overwriting an intervening update:
+ If the value in the request matches the value of `CollectionVersion` in the collection, Route 53 updates the collection.
+ If the value of `CollectionVersion` in the collection is greater than the value in the request, the collection was changed after you got the version number. Route 53 does not update the collection, and it returns a `CidrCollectionVersionMismatch` error.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_ChangeCidrCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ChangeCidrCollectionResponse>
   <Id>string</Id>
</ChangeCidrCollectionResponse>
```

## Response Elements
<a name="API_ChangeCidrCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ChangeCidrCollectionResponse](#API_ChangeCidrCollection_ResponseSyntax) **   <a name="Route53-ChangeCidrCollection-response-ChangeCidrCollectionResponse"></a>
Root level tag for the ChangeCidrCollectionResponse parameters.
Required: Yes

 ** [Id](#API_ChangeCidrCollection_ResponseSyntax) **   <a name="Route53-ChangeCidrCollection-response-Id"></a>
The ID that is returned by `ChangeCidrCollection`. You can use it as input to `GetChange` to see if a CIDR collection change has propagated or not.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6500.

## Errors
<a name="API_ChangeCidrCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CidrBlockInUseException **
This CIDR block is already in use.
HTTP Status Code: 400

 ** CidrCollectionVersionMismatchException **
The CIDR collection version you provided, doesn't match the one in the `ListCidrCollections` operation.
HTTP Status Code: 409

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

 ** NoSuchCidrCollectionException **
The CIDR collection you specified, doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_ChangeCidrCollection_Examples"></a>

### Example request
<a name="API_ChangeCidrCollection_Example_1"></a>

This example illustrates one usage of ChangeCidrCollection.

```
POST /2013-04-01/cidrcollection/c8c02a84-aaaa-bbbb-e0d2-d833a2f80106
<?xml version="1.0" encoding="UTF-8"?>
<ChangeCidrCollectionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Changes>
     <CidrCollectionChange>
      <Action>PUT</Action>
       <CidrList>
        <Cidr>1.1.1.0/24</Cidr>
        <Cidr>1.1.2.0/24</Cidr>
       </CidrList>
       <LocationName>location-1</LocationName>
      </CidrCollectionChange>
      <CidrCollectionChange>
       <Action>DELETE_IF_EXISTS</Action>
        <CidrList>
         <Cidr>2.1.1.0/24</Cidr>
         <Cidr>2.1.2.0/24</Cidr>
        </CidrList>
      <LocationName>location-2</LocationName>
    </CidrCollectionChange>
   </Changes>
  <CollectionVersion>1</CollectionVersion>
</ChangeCidrCollectionRequest>
```

### Example response
<a name="API_ChangeCidrCollection_Example_2"></a>

This example illustrates one usage of ChangeCidrCollection.

```
HTTP/1.1 200
<?xml version="1.0"?>
<ChangeCidrCollectionResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Id>BAQICAHjlIdQ8CnglM29iyr9Fw_Dl6ubqnG8pAHlAe5xxLiDmTgGl7FQ54tpTXxv-GsVbPT2BAAAAwzCBwAYJKoZIhvcNAQcGoIGyMIGvAgEAMIGpBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDHQyia4ugqVBJFynEQIBEIB8yb9oghUN992DstGo6cAf4V6lFSwYeSk8z8lONyRuwbmhGMAXu7NHvn1cXLm18SlTBVvCS03PXUWhVPezQuzIZJMsP9ns1T_I1Eez5zBWMFJr8-4xIpgwRqtD_xhwU5DBL96BxmLCZWGM4iziVu0AZjyiUKONtKTE0GeIKg==</Id>
</ChangeCidrCollectionResponse>
```

## See Also
<a name="API_ChangeCidrCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ChangeCidrCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeCidrCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
