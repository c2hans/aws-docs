---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetServiceAttributes.html
---

# GetServiceAttributes
<a name="API_GetServiceAttributes"></a>

Returns the attributes associated with a specified service.

## Request Syntax
<a name="API_GetServiceAttributes_RequestSyntax"></a>

```
{
   "ServiceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetServiceAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ServiceId](#API_GetServiceAttributes_RequestSyntax) **   <a name="cloudmap-GetServiceAttributes-request-ServiceId"></a>
The ID or Amazon Resource Name (ARN) of the service that you want to get attributes for. For services created in a namespace shared with your AWS account, specify the service ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetServiceAttributes_ResponseSyntax"></a>

```
{
   "ServiceAttributes": {
      "Attributes": {
         "string" : "string"
      },
      "ResourceOwner": "string",
      "ServiceArn": "string"
   }
}
```

## Response Elements
<a name="API_GetServiceAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceAttributes](#API_GetServiceAttributes_ResponseSyntax) **   <a name="cloudmap-GetServiceAttributes-response-ServiceAttributes"></a>
A complex type that contains the service ARN and a list of attribute key-value pairs associated with the service.
Type: [ServiceAttributes](API_ServiceAttributes.md) object

## Errors
<a name="API_GetServiceAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** ServiceNotFound **
No service exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetServiceAttributes_Examples"></a>

### GetServiceAttributes Example for service with an attribute
<a name="API_GetServiceAttributes_Example_1"></a>

The following API request retrieves attributes for the service `srv-e4anhexample0004`. The service has the attribute `Port` with the value `80`.

#### Sample Request
<a name="API_GetServiceAttributes_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetServiceAttributes_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "ServiceAttributes": {
        "ServiceArn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
        "Attributes": {
            "Port": "80"
        },
        "ResourceOwner": "123456789012"
    }
}
```

### GetServiceAttributes Example for service without attributes
<a name="API_GetServiceAttributes_Example_2"></a>

The following API request demonstrates the response returned when a service does not have any attributes associated with it.

#### Sample Request
<a name="API_GetServiceAttributes_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "srv-e4anhexample0005"
}
```

#### Sample Response
<a name="API_GetServiceAttributes_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "ServiceAttributes": {
        "ServiceArn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0005",
        "Attributes": {},
        "ResourceOwner": "123456789012"
    }
}
```

### GetServiceAttributes Example using service ARN
<a name="API_GetServiceAttributes_Example_3"></a>

The following API request retrieves attributes for a service in a shared namespace using its ARN.

#### Sample Request
<a name="API_GetServiceAttributes_Example_3_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20241223T173136Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetServiceAttributes
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "ServiceId": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetServiceAttributes_Example_3_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1
{
    "ServiceAttributes": {
        "ServiceArn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
        "Attributes": {
            "Port": "80"
        },
        "ResourceOwner": "123456789012"

    }
}
```

## See Also
<a name="API_GetServiceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetServiceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetServiceAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
