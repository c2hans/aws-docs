---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateResourceRecordSetProtections.html
---

# CreateResourceRecordSetProtections
<a name="API_CreateResourceRecordSetProtections"></a>

Creates one or more resource record set protections in a hosted zone. A protection applies to every resource record set in the hosted zone that has the specified name and type. While a protection exists, Route 53 rejects any `ChangeResourceRecordSets` request that creates, updates, or deletes a resource record set with that name and type, and returns an `InvalidChangeBatch` error. To change a protected resource record set, first delete its protection by using `DeleteResourceRecordSetProtections`.

You can create a protection for a name and type that doesn't have a resource record set yet. In that case, Route 53 also rejects requests to create that resource record set.

You can't delete a hosted zone that has protections. To delete the hosted zone, first delete all of its protections by using `DeleteResourceRecordSetProtections`.

The request is atomic. Route 53 either creates all of the protections in the request or none of them. If one or more entries fail, the response is an error that lists the failing entries and the reason that each one failed. Route 53 checks for invalid entries before it checks for existing protections, so if any entry is invalid, the error lists only the invalid entries.

The error that Route 53 returns depends on the failures:
+ If every entry already has a protection, Route 53 returns a `ProtectionAlreadyExists` error.
+ For any other combination of failures, Route 53 returns an `InvalidResourceRecordSetProtectionBatch` error.

You can specify up to 100 protections in one request. The number of protections that you can have in a hosted zone is limited by a quota. If the request would exceed that quota, Route 53 returns a `LimitsExceeded` error.

## Request Syntax
<a name="API_CreateResourceRecordSetProtections_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/rrsetprotection HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateResourceRecordSetProtectionsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Protections>
      <ResourceRecordSetProtectionConfig>
         <Comment>{{string}}</Comment>
         <RecordName>{{string}}</RecordName>
         <RecordType>{{string}}</RecordType>
      </ResourceRecordSetProtectionConfig>
   </Protections>
</CreateResourceRecordSetProtectionsRequest>
```

## URI Request Parameters
<a name="API_CreateResourceRecordSetProtections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_CreateResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-CreateResourceRecordSetProtections-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the resource record sets that you want to protect.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_CreateResourceRecordSetProtections_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateResourceRecordSetProtectionsRequest](#API_CreateResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-CreateResourceRecordSetProtections-request-CreateResourceRecordSetProtectionsRequest"></a>
Root level tag for the CreateResourceRecordSetProtectionsRequest parameters.
Required: Yes

 ** [Protections](#API_CreateResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-CreateResourceRecordSetProtections-request-Protections"></a>
The protections to create. Each entry specifies a resource record set name and type, and an optional comment. The list must contain at least one entry and can contain up to 100 entries. Each name and type can appear only once in the list.
Type: Array of [ResourceRecordSetProtectionConfig](API_ResourceRecordSetProtectionConfig.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreateResourceRecordSetProtections_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateResourceRecordSetProtections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateResourceRecordSetProtections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceRecordSetProtectionBatch **
One or more entries in the request couldn't be processed, so Route 53 didn't create or delete any of the protections in the request. The `Errors` element lists the failing entries and the reason that each one failed.
 ** Errors **
The entries that failed, with the reason that each one failed.
 ** Message **
A message that explains why Route 53 couldn't process the `CreateResourceRecordSetProtections` or `DeleteResourceRecordSetProtections` request.
HTTP Status Code: 400

 ** LimitsExceeded **
This operation can't be completed because the current account has reached the limit on the resource you are trying to create. To request a higher limit, [create a case](http://aws.amazon.com/route53-request) with the AWS Support Center.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

 ** ProtectionAlreadyExists **
A protection already exists for every name and type in the request, so Route 53 didn't create any protections. The `Errors` element lists each entry.
 ** Errors **
The entries that already have a protection.
 ** Message **
A message that explains that a protection already exists for every name and type in the `CreateResourceRecordSetProtections` request.
HTTP Status Code: 409

## See Also
<a name="API_CreateResourceRecordSetProtections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateResourceRecordSetProtections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateResourceRecordSetProtections)
