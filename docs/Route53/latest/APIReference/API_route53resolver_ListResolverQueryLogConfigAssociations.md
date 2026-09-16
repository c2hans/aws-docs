---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html
---

# ListResolverQueryLogConfigAssociations
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations"></a>

Lists information about associations between Amazon VPCs and query logging configurations.

## Request Syntax
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-request-Filters"></a>
An optional specification to return a subset of query logging associations.
If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same values for `Filters`, if any, as in the previous request.
Type: Array of [Filter](API_route53resolver_Filter.md) objects
Required: No

 ** [MaxResults](#API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-request-MaxResults"></a>
The maximum number of query logging associations that you want to return in the response to a `ListResolverQueryLogConfigAssociations` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 query logging associations.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-request-NextToken"></a>
For the first `ListResolverQueryLogConfigAssociations` request, omit this value.
If there are more than `MaxResults` query logging associations that match the values that you specify for `Filters`, you can submit another `ListResolverQueryLogConfigAssociations` request to get the next group of associations. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

 ** [SortBy](#API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-request-SortBy"></a>
The element that you want Resolver to sort query logging associations by.
If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same value for `SortBy`, if any, as in the previous request.
Valid values include the following elements:
+  `CreationTime`: The ID of the query logging association.
+  `Error`: If the value of `Status` is `FAILED`, the value of `Error` indicates the cause:
  +  `DESTINATION_NOT_FOUND`: The specified destination (for example, an Amazon S3 bucket) was deleted.
  +  `ACCESS_DENIED`: Permissions don't allow sending logs to the destination.

  If `Status` is a value other than `FAILED`, `ERROR` is null.
+  `Id`: The ID of the query logging association
+  `ResolverQueryLogConfigId`: The ID of the query logging configuration
+  `ResourceId`: The ID of the VPC that is associated with the query logging configuration
+  `Status`: The current status of the configuration. Valid values include the following:
  +  `CREATING`: Resolver is creating an association between an Amazon VPC and a query logging configuration.
  +  `CREATED`: The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
  +  `DELETING`: Resolver is deleting this query logging association.
  +  `FAILED`: Resolver either couldn't create or couldn't delete the query logging association. Here are two common causes:
    + The specified destination (for example, an Amazon S3 bucket) was deleted.
    + Permissions don't allow sending logs to the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [SortOrder](#API_route53resolver_ListResolverQueryLogConfigAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-request-SortOrder"></a>
If you specified a value for `SortBy`, the order that you want query logging associations to be listed in, `ASCENDING` or `DESCENDING`.
If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same value for `SortOrder`, if any, as in the previous request.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResolverQueryLogConfigAssociations": [
      {
         "CreationTime": "string",
         "Error": "string",
         "ErrorMessage": "string",
         "Id": "string",
         "ResolverQueryLogConfigId": "string",
         "ResourceId": "string",
         "Status": "string"
      }
   ],
   "TotalCount": number,
   "TotalFilteredCount": number
}
```

## Response Elements
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-response-NextToken"></a>
If there are more than `MaxResults` query logging associations, you can submit another `ListResolverQueryLogConfigAssociations` request to get the next group of associations. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ResolverQueryLogConfigAssociations](#API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-response-ResolverQueryLogConfigAssociations"></a>
A list that contains one `ResolverQueryLogConfigAssociations` element for each query logging association that matches the values that you specified for `Filter`.
Type: Array of [ResolverQueryLogConfigAssociation](API_route53resolver_ResolverQueryLogConfigAssociation.md) objects

 ** [TotalCount](#API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-response-TotalCount"></a>
The total number of query logging associations that were created by the current account in the specified Region. This count can differ from the number of associations that are returned in a `ListResolverQueryLogConfigAssociations` response, depending on the values that you specify in the request.
Type: Integer

 ** [TotalFilteredCount](#API_route53resolver_ListResolverQueryLogConfigAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverQueryLogConfigAssociations-response-TotalFilteredCount"></a>
The total number of query logging associations that were created by the current account in the specified Region and that match the filters that were specified in the `ListResolverQueryLogConfigAssociations` request. For the total number of associations that were created by the current account in the specified Region, see `TotalCount`.
Type: Integer

## Errors
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_Examples"></a>

### ListResolverQueryLogConfigAssociations Example
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_Example_1"></a>

This example illustrates one usage of ListResolverQueryLogConfigAssociations.

#### Sample Request
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 283
X-Amz-Target: Route53Resolver.ListResolverQueryLogConfigAssociations
X-Amz-Date: 20200415T191344Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "Filters": [
        {
            "Name": "Status",
            "Values": "CREATED"
        }
    ],
    "MaxResults": 10,
    "SortBy": "DestinationArn",
    "SortOrder": "ASCENDING"
}
```

#### Sample Response
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:13:44 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 531
x-amzn-RequestId: 08afd081-9d67-4281-a277-b3880example
Connection: keep-alive

{
    "MaxResults": 10,
    "ResolverQueryLogConfigAssociations": [
        {
            "CreationTime": "2020-04-15T18:52:23.30Z",
            "Error": "",
            "ErrorMessage": "",
            "Id": "rqlca-ff85e1ffexample",
            "ResolverQueryLogConfigId": "rqlc-8ca61fe7cexample",
            "Resource": "vpc-03cf94c75cexample",
            "Status": "CREATED"
        }
    ],
    "TotalCount": 10,
    "TotalFilteredCount": 1
}
```

## See Also
<a name="API_route53resolver_ListResolverQueryLogConfigAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)
