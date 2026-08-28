---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_GetNamespace.html
---

# GetNamespace
<a name="API_GetNamespace"></a>

Gets information about a namespace.

## Request Syntax
<a name="API_GetNamespace_RequestSyntax"></a>

```
{
   "Id": "{{string}}"
}
```

## Request Parameters
<a name="API_GetNamespace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_GetNamespace_RequestSyntax) **   <a name="cloudmap-GetNamespace-request-Id"></a>
The ID or Amazon Resource Name (ARN) of the namespace that you want to get information about. For namespaces shared with your AWS account, specify the namespace ARN. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetNamespace_ResponseSyntax"></a>

```
{
   "Namespace": {
      "Arn": "string",
      "CreateDate": number,
      "CreatorRequestId": "string",
      "Description": "string",
      "Id": "string",
      "Name": "string",
      "Properties": {
         "DnsProperties": {
            "HostedZoneId": "string",
            "SOA": {
               "TTL": number
            }
         },
         "HttpProperties": {
            "HttpName": "string"
         }
      },
      "ResourceOwner": "string",
      "ServiceCount": number,
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_GetNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Namespace](#API_GetNamespace_ResponseSyntax) **   <a name="cloudmap-GetNamespace-response-Namespace"></a>
A complex type that contains information about the specified namespace.
Type: [Namespace](API_Namespace.md) object

## Errors
<a name="API_GetNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

 ** NamespaceNotFound **
No namespace exists with the specified ID.
HTTP Status Code: 400

## Examples
<a name="API_GetNamespace_Examples"></a>

### GetNamespace Example
<a name="API_GetNamespace_Example_1"></a>

This example request retrieves information about the specified namespace.

#### Sample Request
<a name="API_GetNamespace_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211711Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "ns-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetNamespace_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Namespace": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e1tpmexample0001",
        "CreateDate": "20181118T211712Z",
        "CreatorRequestId": "example-creator-request-id-0001",
        "Description": "Example.com AWS Cloud Map HTTP Namespace",
        "Id": "ns-e1tpmexample0001",
        "Name": "example-http.com",
        "Properties": {
            "DnsProperties": {},
            "HttpProperties": {
                "HttpName": "example-http.com"
            }
        },
        "Type": "HTTP",
        "ResourceOwner": "123456789012"
    }
}
```

### GetNamespace Example using ARN
<a name="API_GetNamespace_Example_2"></a>

This example request retrieves information about a shared namespace using its ARN. The namespace owner is account `123456789012` and the consumer is `111122223333`.

#### Sample Request
<a name="API_GetNamespace_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211711Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.GetNamespace
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Id": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004"
}
```

#### Sample Response
<a name="API_GetNamespace_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Namespace": {
        "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e1tpmexample0001",
        "CreateDate": "20181118T211712Z",
        "CreatorRequestId": "example-creator-request-id-0001",
        "Description": "Example.com AWS Cloud Map HTTP Namespace",
        "Id": "ns-e1tpmexample0001",
        "Name": "example-http.com",
        "Properties": {
            "DnsProperties": {},
            "HttpProperties": {
                "HttpName": "example-http.com"
            }
        },
        "Type": "HTTP",
        "ResourceOwner": "123456789012"
    }
}
```

## See Also
<a name="API_GetNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/GetNamespace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/GetNamespace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
