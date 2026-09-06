---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleTypes.html
---

# ListFirewallRuleTypes
<a name="API_route53resolver_ListFirewallRuleTypes"></a>

Retrieves the rule-type variants that can be used in the `FirewallRuleType` field of [CreateFirewallRule](API_route53resolver_CreateFirewallRule.md) and [UpdateFirewallRule](API_route53resolver_UpdateFirewallRule.md). Each returned [FirewallRuleTypeDefinition](API_route53resolver_FirewallRuleTypeDefinition.md) identifies one variant \+ value combination — for example, `FirewallAdvancedContentCategory` \+ `VIOLENCE_AND_HATE_SPEECH`, or `PartnerThreatProtection` \+ a partner-managed feed.

The supported `RuleType` filter values are `FirewallAdvancedContentCategory`, `FirewallAdvancedThreatCategory`, `DnsThreatProtection`, and `PartnerThreatProtection`. When a returned definition's variant requires an external subscription (currently only `PartnerThreatProtection`), the response also includes a [SubscriptionInfo](API_route53resolver_SubscriptionInfo.md) identifying the AWS Marketplace product that backs it; absence of `SubscriptionInfo` means the variant is fully managed by AWS and requires no separate subscription.

## Request Syntax
<a name="API_route53resolver_ListFirewallRuleTypes_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RuleType": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListFirewallRuleTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListFirewallRuleTypes_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleTypes-request-MaxResults"></a>
The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListFirewallRuleTypes_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleTypes-request-NextToken"></a>
For the first call to this list request, omit this value. When you request a list of objects, Resolver returns at most the number of objects specified in `MaxResults`. If more objects are available for retrieval, Resolver provides a `NextToken` value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.
Type: String
Required: No

 ** [RuleType](#API_route53resolver_ListFirewallRuleTypes_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleTypes-request-RuleType"></a>
An optional filter that restricts the response to a single [FirewallRuleType](API_route53resolver_FirewallRuleType.md) variant. Supported values: `FirewallAdvancedContentCategory`, `FirewallAdvancedThreatCategory`, `DnsThreatProtection`, and `PartnerThreatProtection`. If omitted, definitions across all variants are returned.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## Response Syntax
<a name="API_route53resolver_ListFirewallRuleTypes_ResponseSyntax"></a>

```
{
   "FirewallRuleTypes": [
      {
         "Description": "string",
         "DisplayName": "string",
         "RuleType": "string",
         "SubscriptionInfo": {
            "ProductId": "string",
            "VendorName": "string"
         },
         "Value": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_route53resolver_ListFirewallRuleTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRuleTypes](#API_route53resolver_ListFirewallRuleTypes_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleTypes-response-FirewallRuleTypes"></a>
A list of the available rule type definitions.
Type: Array of [FirewallRuleTypeDefinition](API_route53resolver_FirewallRuleTypeDefinition.md) objects

 ** [NextToken](#API_route53resolver_ListFirewallRuleTypes_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleTypes-response-NextToken"></a>
If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.
Type: String

## Errors
<a name="API_route53resolver_ListFirewallRuleTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_ListFirewallRuleTypes_Examples"></a>

### ListFirewallRuleTypes Example
<a name="API_route53resolver_ListFirewallRuleTypes_Example_1"></a>

This example illustrates one usage of ListFirewallRuleTypes.

#### Sample Request
<a name="API_route53resolver_ListFirewallRuleTypes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 22
X-Amz-Target: Route53Resolver.ListFirewallRuleTypes
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "MaxResults": 10
}
```

#### Sample Response
<a name="API_route53resolver_ListFirewallRuleTypes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:04 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 450
x-amzn-RequestId: 7e5d4f6a-8b9c-0d1e-2f3a-4b5c6example
Connection: keep-alive

{
    "FirewallRuleTypes": [
        {
            "RuleType": "FirewallAdvancedContentCategory",
            "Value": "VIOLENCE_AND_HATE_SPEECH",
            "DisplayName": "Violence and Hate Speech",
            "Description": "Content category: Violence and Hate Speech"
        },
        {
            "RuleType": "FirewallAdvancedThreatCategory",
            "Value": "PHISHING",
            "DisplayName": "Phishing",
            "Description": "Advanced threat category: Phishing"
        }
    ]
}
```

### ListFirewallRuleTypes Example - filter by PartnerThreatProtection
<a name="API_route53resolver_ListFirewallRuleTypes_Example_2"></a>

This example illustrates one usage of ListFirewallRuleTypes.

#### Sample Request
<a name="API_route53resolver_ListFirewallRuleTypes_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 64
X-Amz-Target: Route53Resolver.ListFirewallRuleTypes
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "RuleType": "PartnerThreatProtection",
    "MaxResults": 10
}
```

#### Sample Response
<a name="API_route53resolver_ListFirewallRuleTypes_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:06 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 612
x-amzn-RequestId: 3d4e5f6a-7b8c-9d0e-1f2a-3b4c5example
Connection: keep-alive

{
    "FirewallRuleTypes": [
        {
            "RuleType": "PartnerThreatProtection",
            "Value": "PANW_MALWARE_DOMAINS",
            "DisplayName": "Palo Alto Networks - Malware Domains",
            "Description": "Partner-managed advanced threat protection delivered by Palo Alto Networks.",
            "SubscriptionInfo": {
                "VendorName": "Palo Alto Networks",
                "ProductId": "prod-aaaaaaaaaaaaa"
            }
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListFirewallRuleTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListFirewallRuleTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListFirewallRuleTypes)
