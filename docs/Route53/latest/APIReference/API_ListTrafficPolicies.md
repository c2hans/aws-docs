---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html
---

# ListTrafficPolicies
<a name="API_ListTrafficPolicies"></a>

Gets information about the latest version for every traffic policy that is associated with the current AWS account. Policies are listed in the order that they were created in.

For information about how of deleting a traffic policy affects the response from `ListTrafficPolicies`, see [DeleteTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html).

## Request Syntax
<a name="API_ListTrafficPolicies_RequestSyntax"></a>

```
GET /2013-04-01/trafficpolicies?maxitems={{MaxItems}}&trafficpolicyid={{TrafficPolicyIdMarker}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrafficPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxitems](#API_ListTrafficPolicies_RequestSyntax) **   <a name="Route53-ListTrafficPolicies-request-uri-MaxItems"></a>
(Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than `MaxItems` traffic policies, the value of `IsTruncated` in the response is `true`, and the value of `TrafficPolicyIdMarker` is the ID of the first traffic policy that Route 53 will return if you submit another request.

 ** [trafficpolicyid](#API_ListTrafficPolicies_RequestSyntax) **   <a name="Route53-ListTrafficPolicies-request-uri-TrafficPolicyIdMarker"></a>
(Conditional) For your first request to `ListTrafficPolicies`, don't include the `TrafficPolicyIdMarker` parameter.
If you have more traffic policies than the value of `MaxItems`, `ListTrafficPolicies` returns only the first `MaxItems` traffic policies. To get the next group of policies, submit another request to `ListTrafficPolicies`. For the value of `TrafficPolicyIdMarker`, specify the value of `TrafficPolicyIdMarker` that was returned in the previous response.
Length Constraints: Minimum length of 1. Maximum length of 36.

## Request Body
<a name="API_ListTrafficPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrafficPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPoliciesResponse>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <TrafficPolicyIdMarker>string</TrafficPolicyIdMarker>
   <TrafficPolicySummaries>
      <TrafficPolicySummary>
         <Id>string</Id>
         <LatestVersion>integer</LatestVersion>
         <Name>string</Name>
         <TrafficPolicyCount>integer</TrafficPolicyCount>
         <Type>string</Type>
      </TrafficPolicySummary>
   </TrafficPolicySummaries>
</ListTrafficPoliciesResponse>
```

## Response Elements
<a name="API_ListTrafficPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListTrafficPoliciesResponse](#API_ListTrafficPolicies_ResponseSyntax) **   <a name="Route53-ListTrafficPolicies-response-ListTrafficPoliciesResponse"></a>
Root level tag for the ListTrafficPoliciesResponse parameters.
Required: Yes

 ** [IsTruncated](#API_ListTrafficPolicies_ResponseSyntax) **   <a name="Route53-ListTrafficPolicies-response-IsTruncated"></a>
A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another `ListTrafficPolicies` request and specifying the value of `TrafficPolicyIdMarker` in the `TrafficPolicyIdMarker` request parameter.
Type: Boolean

 ** [MaxItems](#API_ListTrafficPolicies_ResponseSyntax) **   <a name="Route53-ListTrafficPolicies-response-MaxItems"></a>
The value that you specified for the `MaxItems` parameter in the `ListTrafficPolicies` request that produced the current response.
Type: String

 ** [TrafficPolicyIdMarker](#API_ListTrafficPolicies_ResponseSyntax) **   <a name="Route53-ListTrafficPolicies-response-TrafficPolicyIdMarker"></a>
If the value of `IsTruncated` is `true`, `TrafficPolicyIdMarker` is the ID of the first traffic policy in the next group of `MaxItems` traffic policies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.

 ** [TrafficPolicySummaries](#API_ListTrafficPolicies_ResponseSyntax) **   <a name="Route53-ListTrafficPolicies-response-TrafficPolicySummaries"></a>
A list that contains one `TrafficPolicySummary` element for each traffic policy that was created by the current AWS account.
Type: Array of [TrafficPolicySummary](API_TrafficPolicySummary.md) objects

## Errors
<a name="API_ListTrafficPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ListTrafficPolicies_Examples"></a>

### Example Request
<a name="API_ListTrafficPolicies_Example_1"></a>

This example illustrates one usage of ListTrafficPolicies.

```
GET /2013-04-01/trafficpolicies?maxitems=1
```

### Example Response
<a name="API_ListTrafficPolicies_Example_2"></a>

This example illustrates one usage of ListTrafficPolicies.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPoliciesResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicySummaries>
      <TrafficPolicySummary>
         <Id>12345678-abcd-9876-fedc-1a2b3c4de5f6</Id>
         <Name>MyTrafficPolicy</Name>
         <Type>A</Type>
         <LatestVersion>77</LatestVersion>
         <TrafficPolicyCount>44</TrafficPolicyCount>
      </TrafficPolicySummary>
   </TrafficPolicySummaries>
   <IsTrucated>true</IsTruncated>
   <TrafficPolicyIdMarker>12345678-abcd-9876-fedc-1a2b3c4de5f7</TrafficPolicyIdMarker>
   <MaxItems>1</MaxItems>
</ListTrafficPoliciesResponse>
```

## See Also
<a name="API_ListTrafficPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListTrafficPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListTrafficPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
