---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html
---

# GetChange
<a name="API_GetChange"></a>

Returns the current status of a change batch request. The status is one of the following values:
+  `PENDING` indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers managing the hosted zone. This is the initial status of all change batch requests.
+  `INSYNC` indicates that the changes have propagated to all Route 53 DNS servers managing the hosted zone.

## Request Syntax
<a name="API_GetChange_RequestSyntax"></a>

```
GET /2013-04-01/change/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChange_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetChange_RequestSyntax) **   <a name="Route53-GetChange-request-uri-Id"></a>
The ID of the change batch request. The value that you specify here is the value that `ChangeResourceRecordSets` returned in the `Id` element when you submitted the request.
Length Constraints: Minimum length of 1. Maximum length of 6500.
Required: Yes

## Request Body
<a name="API_GetChange_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChange_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetChangeResponse>
   <ChangeInfo>
      <Comment>string</Comment>
      <Id>string</Id>
      <Status>string</Status>
      <SubmittedAt>timestamp</SubmittedAt>
   </ChangeInfo>
</GetChangeResponse>
```

## Response Elements
<a name="API_GetChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetChangeResponse](#API_GetChange_ResponseSyntax) **   <a name="Route53-GetChange-response-GetChangeResponse"></a>
Root level tag for the GetChangeResponse parameters.
Required: Yes

 ** [ChangeInfo](#API_GetChange_ResponseSyntax) **   <a name="Route53-GetChange-response-ChangeInfo"></a>
A complex type that contains information about the specified change batch.
Type: [ChangeInfo](API_ChangeInfo.md) object

## Errors
<a name="API_GetChange_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchChange **
A change with the specified change ID does not exist.
HTTP Status Code: 404

## Examples
<a name="API_GetChange_Examples"></a>

### Example Request
<a name="API_GetChange_Example_1"></a>

This example illustrates one usage of GetChange.

```
GET /2013-04-01/change/C2682N5HXP0BZ4
```

### Example Response
<a name="API_GetChange_Example_2"></a>

This example illustrates one usage of GetChange.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetChangeResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ChangeInfo>
      <Id>C2682N5HXP0BZ4</Id>
      <Status>INSYNC</Status>
      <SubmittedAt>2017-03-10T01:36:41.958Z</SubmittedAt>
   </ChangeInfo>
</GetChangeResponse>
```

## See Also
<a name="API_GetChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetChange)
