---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

Lists summary information for all the services that are associated with one or more namespaces.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

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
<a name="API_ListServices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListServices_RequestSyntax) **   <a name="cloudmap-ListServices-request-Filters"></a>
A complex type that contains specifications for the namespaces that you want to list services for.
If you specify more than one filter, an operation must match all filters to be returned by `ListServices`.
Type: Array of [ServiceFilter](API_ServiceFilter.md) objects
Required: No

 ** [MaxResults](#API_ListServices_RequestSyntax) **   <a name="cloudmap-ListServices-request-MaxResults"></a>
The maximum number of services that you want AWS Cloud Map to return in the response to a `ListServices` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 services.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListServices_RequestSyntax) **   <a name="cloudmap-ListServices-request-NextToken"></a>
For the first `ListServices` request, omit this value.
If the response contains `NextToken`, submit another `ListServices` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` services and then filters them based on the specified criteria. It's possible that no services in the first `MaxResults` services matched the specified criteria but that subsequent groups of `MaxResults` services do contain services that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Services": [
      {
         "Arn": "string",
         "CreateDate": number,
         "CreatedByAccount": "string",
         "Description": "string",
         "DnsConfig": {
            "DnsRecords": [
               {
                  "TTL": number,
                  "Type": "string"
               }
            ],
            "NamespaceId": "string",
            "RoutingPolicy": "string"
         },
         "HealthCheckConfig": {
            "FailureThreshold": number,
            "ResourcePath": "string",
            "Type": "string"
         },
         "HealthCheckCustomConfig": {
            "FailureThreshold": number
         },
         "Id": "string",
         "InstanceCount": number,
         "Name": "string",
         "ResourceOwner": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServices_ResponseSyntax) **   <a name="cloudmap-ListServices-response-NextToken"></a>
If the response contains `NextToken`, submit another `ListServices` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` services and then filters them based on the specified criteria. It's possible that no services in the first `MaxResults` services matched the specified criteria but that subsequent groups of `MaxResults` services do contain services that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Services](#API_ListServices_ResponseSyntax) **   <a name="cloudmap-ListServices-response-Services"></a>
An array that contains one `ServiceSummary` object for each service that matches the specified filter criteria.
Type: Array of [ServiceSummary](API_ServiceSummary.md) objects

## Errors
<a name="API_ListServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

## Examples
<a name="API_ListServices_Examples"></a>

### ListServices Example
<a name="API_ListServices_Example_1"></a>

This example request retrieves information about services that are associated with the specified namespace.

#### Sample Request
<a name="API_ListServices_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211713Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListServices
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Filters": [
        {
            "Name": "NAMESPACE_ID",
            "Condition": "EQ",
            "Values": [
                "ns-e3r0sexample0003"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListServices_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Services": [
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-e4anhexample0004",
            "CreateDate": "20181118T211707Z",
            "Description": "Example.com AWS Cloud Map HTTP Service",
            "HealthCheckConfig": {
                "FailureThreshold": 1,
                "ResourcePath": "/",
                "Type": "HTTPS"
            },
            "Id": "srv-e4anhexample0004",
            "Name": "example-http-service",
            "ResourceOwner": "123456789012",
            "CreatedByAccount": "123456789012"
        }
    ]
}
```

### ListServices Example using RESOURCE\_OWNER filter
<a name="API_ListServices_Example_2"></a>

This example request retrieves information about services created by `123456789012` in a namespace shared by another account `111122223333`.

#### Sample Request
<a name="API_ListServices_Example_2_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211713Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListServices
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
<a name="API_ListServices_Example_2_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Services": [
        {
            "Arn": "arn:aws:servicediscovery:us-west-2:111122223333:service/srv-e4anhexample0004",
            "CreateDate": "20181118T211707Z",
            "Description": "Service in shared namespace",
            "HealthCheckConfig": {
                "FailureThreshold": 1,
                "ResourcePath": "/",
                "Type": "HTTPS"
            },
            "Id": "srv-e4anhexample0004",
            "Name": "shared-service",
            "CreatedByAccount":"123456789012",
            "ResourceOwner": "111122223333"
        }
    ]
}
```

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ListServices)
