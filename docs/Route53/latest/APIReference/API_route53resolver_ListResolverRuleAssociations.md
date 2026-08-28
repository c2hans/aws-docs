---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html
---

# ListResolverRuleAssociations
<a name="API_route53resolver_ListResolverRuleAssociations"></a>

Lists the associations that were created between Resolver rules and VPCs using the current AWS account.

## Request Syntax
<a name="API_route53resolver_ListResolverRuleAssociations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListResolverRuleAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_route53resolver_ListResolverRuleAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-request-Filters"></a>
An optional specification to return a subset of Resolver rules, such as Resolver rules that are associated with the same VPC ID.
If you submit a second or subsequent `ListResolverRuleAssociations` request and specify the `NextToken` parameter, you must use the same values for `Filters`, if any, as in the previous request.
Type: Array of [Filter](API_route53resolver_Filter.md) objects
Required: No

 ** [MaxResults](#API_route53resolver_ListResolverRuleAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-request-MaxResults"></a>
The maximum number of rule associations that you want to return in the response to a `ListResolverRuleAssociations` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 rule associations.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverRuleAssociations_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-request-NextToken"></a>
For the first `ListResolverRuleAssociation` request, omit this value.
If you have more than `MaxResults` rule associations, you can submit another `ListResolverRuleAssociation` request to get the next group of rule associations. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverRuleAssociations_ResponseSyntax"></a>

```
{
   "MaxResults": number,
   "NextToken": "string",
   "ResolverRuleAssociations": [
      {
         "Id": "string",
         "Name": "string",
         "ResolverRuleId": "string",
         "Status": "string",
         "StatusMessage": "string",
         "VPCId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListResolverRuleAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaxResults](#API_route53resolver_ListResolverRuleAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-response-MaxResults"></a>
The value that you specified for `MaxResults` in the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53resolver_ListResolverRuleAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-response-NextToken"></a>
If more than `MaxResults` rule associations match the specified criteria, you can submit another `ListResolverRuleAssociation` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ResolverRuleAssociations](#API_route53resolver_ListResolverRuleAssociations_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRuleAssociations-response-ResolverRuleAssociations"></a>
The associations that were created between Resolver rules and VPCs using the current AWS account, and that match the specified filters, if any.
Type: Array of [ResolverRuleAssociation](API_route53resolver_ResolverRuleAssociation.md) objects

## Errors
<a name="API_route53resolver_ListResolverRuleAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The value that you specified for `NextToken` in a `List` request isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_ListResolverRuleAssociations_Examples"></a>

### ListResolverRuleAssociations Example
<a name="API_route53resolver_ListResolverRuleAssociations_Example_1"></a>

This example illustrates one usage of ListResolverRuleAssociations.

#### Sample Request
<a name="API_route53resolver_ListResolverRuleAssociations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: Route53Resolver.ListResolverRuleAssociations
X-Amz-Date: 20181101T193011Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{}
```

#### Sample Response
<a name="API_route53resolver_ListResolverRuleAssociations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:30:11 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 277
x-amzn-RequestId: 5ad8f14f-64c0-4cb0-a4f9-e5c48example
Connection: keep-alive

{
    "MaxResults": 30,
    "ResolverRuleAssociations": [
        {
            "Id": "rslvr-rrassoc-97242eaf88example",
            "Name":"forward example.com for gamma VPC",
            "ResolverRuleId": "rslvr-rr-5328a0899aexample",
            "Status": "COMPLETE",
            "StatusMessage": "[Trace id: 1-5bdb53db-75f3852c8384ad30fexample] Creating the association.",
            "VPCId": "vpc-03cf94c75eexample"
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListResolverRuleAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverRuleAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverRuleAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
