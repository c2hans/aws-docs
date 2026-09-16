---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneComment.html
---

# UpdateHostedZoneComment
<a name="API_UpdateHostedZoneComment"></a>

Updates the comment for a specified hosted zone.

## Request Syntax
<a name="API_UpdateHostedZoneComment_RequestSyntax"></a>

```
POST /2013-04-01/hostedzone/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneCommentRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>{{string}}</Comment>
</UpdateHostedZoneCommentRequest>
```

## URI Request Parameters
<a name="API_UpdateHostedZoneComment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateHostedZoneComment_RequestSyntax) **   <a name="Route53-UpdateHostedZoneComment-request-uri-Id"></a>
The ID for the hosted zone that you want to update the comment for.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_UpdateHostedZoneComment_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateHostedZoneCommentRequest](#API_UpdateHostedZoneComment_RequestSyntax) **   <a name="Route53-UpdateHostedZoneComment-request-UpdateHostedZoneCommentRequest"></a>
Root level tag for the UpdateHostedZoneCommentRequest parameters.
Required: Yes

 ** [Comment](#API_UpdateHostedZoneComment_RequestSyntax) **   <a name="Route53-UpdateHostedZoneComment-request-Comment"></a>
The new comment for the hosted zone. If you don't specify a value for `Comment`, Amazon Route 53 deletes the existing value of the `Comment` element, if any.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateHostedZoneComment_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneCommentResponse>
   <HostedZone>
      <CallerReference>string</CallerReference>
      <Config>
         <Comment>string</Comment>
         <PrivateZone>boolean</PrivateZone>
      </Config>
      <Features>
         <AcceleratedRecoveryStatus>string</AcceleratedRecoveryStatus>
         <FailureReasons>
            <AcceleratedRecovery>string</AcceleratedRecovery>
         </FailureReasons>
      </Features>
      <Id>string</Id>
      <LinkedService>
         <Description>string</Description>
         <ServicePrincipal>string</ServicePrincipal>
      </LinkedService>
      <Name>string</Name>
      <ResourceRecordSetCount>long</ResourceRecordSetCount>
   </HostedZone>
</UpdateHostedZoneCommentResponse>
```

## Response Elements
<a name="API_UpdateHostedZoneComment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateHostedZoneCommentResponse](#API_UpdateHostedZoneComment_ResponseSyntax) **   <a name="Route53-UpdateHostedZoneComment-response-UpdateHostedZoneCommentResponse"></a>
Root level tag for the UpdateHostedZoneCommentResponse parameters.
Required: Yes

 ** [HostedZone](#API_UpdateHostedZoneComment_ResponseSyntax) **   <a name="Route53-UpdateHostedZoneComment-response-HostedZone"></a>
A complex type that contains the response to the `UpdateHostedZoneComment` request.
Type: [HostedZone](API_HostedZone.md) object

## Errors
<a name="API_UpdateHostedZoneComment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

## Examples
<a name="API_UpdateHostedZoneComment_Examples"></a>

### Example Request
<a name="API_UpdateHostedZoneComment_Example_1"></a>

This example illustrates one usage of UpdateHostedZoneComment.

```
POST /2013-04-01/hostedzone/hosted zone ID HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneCommentRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>for internal testing</Comment>
</UpdateHostedZoneCommentRequest>
```

### Example Response
<a name="API_UpdateHostedZoneComment_Example_2"></a>

This example illustrates one usage of UpdateHostedZoneComment.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<UpdateHostedZoneCommentResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZone>
      <Id>/hostedzone/Z1D633PJN98FT9</Id>
      <Name>example.com</Name>
      <CallerReference>2014-10-15T01:36:41.958Z</CallerReference>
      <Config>
         <Comment>for internal testing</Comment>
         <PrivateZone>false</PrivateZone>
      </Config>
      <ResourceRecordSetCount>42</ResourceRecordSetCount>
   </HostedZone>
</UpdateHostedZoneCommentResponse>
```

## See Also
<a name="API_UpdateHostedZoneComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/UpdateHostedZoneComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/UpdateHostedZoneComment)
