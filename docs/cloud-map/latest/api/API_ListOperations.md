---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ListOperations.html
---

# ListOperations
<a name="API_ListOperations"></a>

Lists operations that match the criteria that you specify.

## Request Syntax
<a name="API_ListOperations_RequestSyntax"></a>

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
<a name="API_ListOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListOperations_RequestSyntax) **   <a name="cloudmap-ListOperations-request-Filters"></a>
A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.
If you specify more than one filter, an operation must match all filters to be returned by `ListOperations`.
Type: Array of [OperationFilter](API_OperationFilter.md) objects
Required: No

 ** [MaxResults](#API_ListOperations_RequestSyntax) **   <a name="cloudmap-ListOperations-request-MaxResults"></a>
The maximum number of items that you want AWS Cloud Map to return in the response to a `ListOperations` request. If you don't specify a value for `MaxResults`, AWS Cloud Map returns up to 100 operations.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListOperations_RequestSyntax) **   <a name="cloudmap-ListOperations-request-NextToken"></a>
For the first `ListOperations` request, omit this value.
If the response contains `NextToken`, submit another `ListOperations` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` operations and then filters them based on the specified criteria. It's possible that no operations in the first `MaxResults` operations matched the specified criteria but that subsequent groups of `MaxResults` operations do contain operations that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## Response Syntax
<a name="API_ListOperations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Operations": [
      {
         "Id": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOperations_ResponseSyntax) **   <a name="cloudmap-ListOperations-response-NextToken"></a>
If the response contains `NextToken`, submit another `ListOperations` request to get the next group of results. Specify the value of `NextToken` from the previous response in the next request.
 AWS Cloud Map gets `MaxResults` operations and then filters them based on the specified criteria. It's possible that no operations in the first `MaxResults` operations matched the specified criteria but that subsequent groups of `MaxResults` operations do contain operations that match the criteria.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Operations](#API_ListOperations_ResponseSyntax) **   <a name="cloudmap-ListOperations-response-Operations"></a>
Summary information about the operations that match the specified criteria.
Type: Array of [OperationSummary](API_OperationSummary.md) objects

## Errors
<a name="API_ListOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
One or more specified values aren't valid. For example, a required value might be missing, a numeric value might be outside the allowed range, or a string value might exceed length constraints.
HTTP Status Code: 400

## Examples
<a name="API_ListOperations_Examples"></a>

### ListOperations Example
<a name="API_ListOperations_Example_1"></a>

This example request lists operations that have a status of `PENDING` or `SUCCESS`.

#### Sample Request
<a name="API_ListOperations_Example_1_Request"></a>

```
POST / HTTP/1.1
host:servicediscovery.us-west-2.amazonaws.com
x-amz-date:20181118T211813Z
authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20181118/us-west-2/servicediscovery/aws4_request,
               SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
               Signature=[calculated-signature]
x-amz-target:Route53AutoNaming_v20170314.ListOperations
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]

{
    "Filters": [
        {
            "Name": "STATUS",
            "Condition": "IN",
            "Values": [
                "PENDING",
                "SUCCESS"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListOperations_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length: [number of characters in the JSON string]
Content-Type: application/x-amz-json-1.1

{
    "Operations": [
        {
            "Id": "76yy8ovhpdz0plmjzbsnqgnrqvpv2qdt-kexample",
            "Status": "SUCCESS"
        },
        {
            "Id": "prysnyzpji3u2ciy45nke83x2zanl7yk-dexample",
            "Status": "SUCCESS"
        },
        {
            "Id": "ko4ekftir7kzlbechsh7xvcdgcpk66gh-7example",
            "Status": "PENDING"
        }
    ]
}
```

## See Also
<a name="API_ListOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicediscovery-2017-03-14/ListOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ListOperations)
