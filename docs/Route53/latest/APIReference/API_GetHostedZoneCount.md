---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZoneCount.html
---

# GetHostedZoneCount
<a name="API_GetHostedZoneCount"></a>

Retrieves the number of hosted zones that are associated with the current AWS account.

## Request Syntax
<a name="API_GetHostedZoneCount_RequestSyntax"></a>

```
GET /2013-04-01/hostedzonecount HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHostedZoneCount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetHostedZoneCount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHostedZoneCount_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneCountResponse>
   <HostedZoneCount>long</HostedZoneCount>
</GetHostedZoneCountResponse>
```

## Response Elements
<a name="API_GetHostedZoneCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHostedZoneCountResponse](#API_GetHostedZoneCount_ResponseSyntax) **   <a name="Route53-GetHostedZoneCount-response-GetHostedZoneCountResponse"></a>
Root level tag for the GetHostedZoneCountResponse parameters.
Required: Yes

 ** [HostedZoneCount](#API_GetHostedZoneCount_ResponseSyntax) **   <a name="Route53-GetHostedZoneCount-response-HostedZoneCount"></a>
The total number of public and private hosted zones that are associated with the current AWS account.
Type: Long

## Errors
<a name="API_GetHostedZoneCount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_GetHostedZoneCount_Examples"></a>

### Example Request
<a name="API_GetHostedZoneCount_Example_1"></a>

This example illustrates one usage of GetHostedZoneCount.

```
GET /2013-04-01/hostedzonecount
```

### Example Response
<a name="API_GetHostedZoneCount_Example_2"></a>

This example illustrates one usage of GetHostedZoneCount.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHostedZoneCountResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HostedZoneCount>42</HostedZoneCount>
</GetHostedZoneCountResponse>
```

## See Also
<a name="API_GetHostedZoneCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHostedZoneCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHostedZoneCount)
