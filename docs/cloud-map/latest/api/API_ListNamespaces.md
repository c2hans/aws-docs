---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ListNamespaces.html
---

# ListNamespaces
<a name="API_ListNamespaces"></a>

Lists summary information about the namespaces that were created by the current AWS account and shared with the current AWS account.

## Request Syntax
<a name="API_ListNamespaces_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Condition": "{{string}}",
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNamespaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListNamespaces_RequestSyntax) **   <a name="cloudmap-ListNamespaces-request-Filters"></a>
A complex type that contains specifications for the namespaces that you want to list.
If you specify more than one filter, a namespace must match all filters to be returned by `ListNamespaces`.
Type: Array of [NamespaceFilter](API_NamespaceFilter.md) objects
Required: No

 ** [MaxResults](#API_ListNamespaces_RequestSyntax) **   <a name="cloudmap-ListNamespaces-request-MaxResults"></a>
The maximum number of namespaces that you want AWS Cloud Map to return in the response to a `ListNamespaces` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 namespaces.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListNamespaces_RequestSyntax) **   <a name="cloudmap-ListNamespaces-request-NextToken"></a>
For the first `ListNamespaces` request, omit this value.
If the response contains `NextToken`, submit another `ListNamespaces` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first `MaxResults` namespaces matched the specified criteria but that subsequent groups of `MaxResults` namespaces do contain namespaces that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListNamespaces_ResponseSyntax"></a>

```
{
   "Namespaces": [
      {
         "Arn": "string",
         "CreateDate": number,
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListNamespaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Namespaces](#API_ListNamespaces_ResponseSyntax) **   <a name="cloudmap-ListNamespaces-response-Namespaces"></a>
An array that contains one `NamespaceSummary` object for each namespace that matches the specified filter criteria.
Type: Array of [NamespaceSummary](API_NamespaceSummary.md) objects

 ** [NextToken](#API_ListNamespaces_ResponseSyntax) **   <a name="cloudmap-ListNamespaces-response-NextToken"></a>
If the response contains `NextToken`, submit another `ListNamespaces` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first `MaxResults` namespaces matched the specified criteria but that subsequent groups of `MaxResults` namespaces do contain namespaces that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_ListNamespaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

## Examples
<a name="API_ListNamespaces_Examples"></a>

### ListNamespaces Example
<a name="API_ListNamespaces_Example_1"></a>

This example request lists the namespaces created by and shared with the current AWS account `123456789012` in the current AWS region. `example-http.com` is a shared namespace.

#### Sample Request
<a name="API_ListNamespaces_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211712Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListNamespaces
content-type:application/x-amz-json-1.1
content-length:2

{}
```

#### Sample Response
<a name="API_ListNamespaces_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Namespaces": [
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e1tpmexample0001",
            "CreateDate": "20181118T211701Z",
            "Description": "Example.com AWS Cloud Map Public DNS Namespace",
            "Id": "ns-e1tpmexample0001",
            "Name": "example-public-dns.com",
            "Properties": {
                "DnsProperties": {
                    "HostedZoneId": "TH3TGRTT0TR20S"
                },
                "HttpProperties": {
                    "HttpName": "example-public-dns.com"
                }
            },
            "Type": "DNS_PUBLIC"
            "ResourceOwner": "123456789012"
        },
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e2a0cexample0002",
            "CreateDate": "20181118T211702Z",
            "Description": "Example.com AWS Cloud Map Private DNS Namespace",
            "Id": "ns-e2a0cexample0002",
            "Name": "example-private-dns.com",
            "Properties": {
                "DnsProperties": {
                    "HostedZoneId": "T1U1TGSSKSSHD"
                },
                "HttpProperties": {
                    "HttpName": "example-private-dns.com"
                }
            },
            "Type": "DNS_PRIVATE",
            "ResourceOwner": "123456789012"
        },
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:111122223333;:namespace/ns-e3r0sexample0003",
            "CreateDate": "20181118T211703Z",
            "Description": "Example.com AWS Cloud Map HTTP Namespace",
            "Id": "ns-e3r0sexample0003",
            "Name": "example-http.com",
            "Properties": {
                "DnsProperties": {},
                "HttpProperties": {
                    "HttpName": "example-http.com"
                }
            },
            "Type": "HTTP",
            "ResourceOwner": "111122223333"
        }
    ]
}
```

### ListNamespaces Example using RESOURCE\_OWNER filter
<a name="API_ListNamespaces_Example_2"></a>

This example request retrieves information about services associated with a namespace shared by another account `111122223333` that account `123456789012` has access to.

#### Sample Request
<a name="API_ListNamespaces_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211712Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListNamespaces
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Filters": [
        {
            "Name": "RESOURCE_OWNER",
            "Condition": "EQ",
            "Values": [
                "OTHER_ACCOUNTS"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListNamespaces_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Namespaces": [
         {
            "Arn": "arn:aws:servicediscovery:us-west-2:111122223333;:namespace/ns-e3r0sexample0003",
            "CreateDate": "20181118T211703Z",
            "Description": "Example.com AWS Cloud Map HTTP Namespace",
            "Id": "ns-e3r0sexample0003",
            "Name": "example-http.com",
            "Properties": {
                "DnsProperties": {},
                "HttpProperties": {
                    "HttpName": "example-http.com"
                }
            },
            "Type": "HTTP",
            "ResourceOwner": "111122223333"
        }
    ]
}
```

## See Also
<a name="API_ListNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/ListNamespaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ListNamespaces)
