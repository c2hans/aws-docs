---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIp.html
---

# GetDedicatedIp
<a name="API_GetDedicatedIp"></a>

Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.

## Request Syntax
<a name="API_GetDedicatedIp_RequestSyntax"></a>

```
GET /v1/email/dedicated-ips/{{IP}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDedicatedIp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IP](#API_GetDedicatedIp_RequestSyntax) **   <a name="pinpoint-GetDedicatedIp-request-uri-Ip"></a>
The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Pinpoint account.
Required: Yes

## Request Body
<a name="API_GetDedicatedIp_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDedicatedIp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DedicatedIp": {
      "Ip": "string",
      "PoolName": "string",
      "WarmupPercentage": number,
      "WarmupStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetDedicatedIp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DedicatedIp](#API_GetDedicatedIp_ResponseSyntax) **   <a name="pinpoint-GetDedicatedIp-response-DedicatedIp"></a>
An object that contains information about a dedicated IP address.
Type: [DedicatedIp](API_DedicatedIp.md) object

## Errors
<a name="API_GetDedicatedIp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_GetDedicatedIp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/GetDedicatedIp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/GetDedicatedIp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
