---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHealthCheckCount.html
---

# GetHealthCheckCount
<a name="API_GetHealthCheckCount"></a>

Retrieves the number of health checks that are associated with the current AWS account.

## Request Syntax
<a name="API_GetHealthCheckCount_RequestSyntax"></a>

```
GET /2013-04-01/healthcheckcount HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHealthCheckCount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetHealthCheckCount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHealthCheckCount_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckCountResponse>
   <HealthCheckCount>long</HealthCheckCount>
</GetHealthCheckCountResponse>
```

## Response Elements
<a name="API_GetHealthCheckCount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetHealthCheckCountResponse](#API_GetHealthCheckCount_ResponseSyntax) **   <a name="Route53-GetHealthCheckCount-response-GetHealthCheckCountResponse"></a>
Root level tag for the GetHealthCheckCountResponse parameters.
Required: Yes

 ** [HealthCheckCount](#API_GetHealthCheckCount_ResponseSyntax) **   <a name="Route53-GetHealthCheckCount-response-HealthCheckCount"></a>
The number of health checks associated with the current AWS account.
Type: Long

## Errors
<a name="API_GetHealthCheckCount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetHealthCheckCount_Examples"></a>

### Example Request
<a name="API_GetHealthCheckCount_Example_1"></a>

This example illustrates one usage of GetHealthCheckCount.

```
GET /2013-04-01/healthcheckcount
```

### Example Response
<a name="API_GetHealthCheckCount_Example_2"></a>

This example illustrates one usage of GetHealthCheckCount.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<GetHealthCheckCountResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <HealthCheckCount>42</HealthCheckCount>
</GetHealthCheckCountResponse>
```

## See Also
<a name="API_GetHealthCheckCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/GetHealthCheckCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/GetHealthCheckCount)
