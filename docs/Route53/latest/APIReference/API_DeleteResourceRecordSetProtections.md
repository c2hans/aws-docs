---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteResourceRecordSetProtections.html
---

# DeleteResourceRecordSetProtections
<a name="API_DeleteResourceRecordSetProtections"></a>

Deletes one or more resource record set protections from a hosted zone. After a protection is deleted, you can change the resource record sets that have that name and type by using `ChangeResourceRecordSets`.

The request is atomic. Route 53 either deletes all of the protections in the request or none of them. If one or more entries fail, for example because no protection exists for the specified name and type, Route 53 returns an `InvalidResourceRecordSetProtectionBatch` error that lists the failing entries and the reason that each one failed.

You can specify up to 100 protections in one request.

## Request Syntax
<a name="API_DeleteResourceRecordSetProtections_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}}/rrsetprotection/delete HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DeleteResourceRecordSetProtectionsRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Protections>
      <ResourceRecordSetProtectionKey>
         <RecordName>{{string}}</RecordName>
         <RecordType>{{string}}</RecordType>
      </ResourceRecordSetProtectionKey>
   </Protections>
</DeleteResourceRecordSetProtectionsRequest>
```

## URI Request Parameters
<a name="API_DeleteResourceRecordSetProtections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-DeleteResourceRecordSetProtections-request-uri-HostedZoneId"></a>
The ID of the hosted zone that contains the protections that you want to delete.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_DeleteResourceRecordSetProtections_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DeleteResourceRecordSetProtectionsRequest](#API_DeleteResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-DeleteResourceRecordSetProtections-request-DeleteResourceRecordSetProtectionsRequest"></a>
Root level tag for the DeleteResourceRecordSetProtectionsRequest parameters.
Required: Yes

 ** [Protections](#API_DeleteResourceRecordSetProtections_RequestSyntax) **   <a name="Route53-DeleteResourceRecordSetProtections-request-Protections"></a>
The name and type of each protection to delete. The list must contain at least one entry and can contain up to 100 entries. Each name and type can appear only once in the list.
Type: Array of [ResourceRecordSetProtectionKey](API_ResourceRecordSetProtectionKey.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_DeleteResourceRecordSetProtections_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteResourceRecordSetProtections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourceRecordSetProtections_Errors"></a>

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

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourceRecordSetProtections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteResourceRecordSetProtections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteResourceRecordSetProtections)
