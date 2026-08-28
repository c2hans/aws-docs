---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyVersions.html
---

# ListTrafficPolicyVersions
<a name="API_ListTrafficPolicyVersions"></a>

Gets information about all of the versions for a specified traffic policy.

Traffic policy versions are listed in numerical order by `VersionNumber`.

## Request Syntax
<a name="API_ListTrafficPolicyVersions_RequestSyntax"></a>

```
GET /2013-04-01/trafficpolicies/{{Id}}/versions?maxitems={{MaxItems}}&trafficpolicyversion={{TrafficPolicyVersionMarker}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrafficPolicyVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_ListTrafficPolicyVersions_RequestSyntax) **   <a name="Route53-ListTrafficPolicyVersions-request-uri-Id"></a>
Specify the value of `Id` of the traffic policy for which you want to list all versions.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [maxitems](#API_ListTrafficPolicyVersions_RequestSyntax) **   <a name="Route53-ListTrafficPolicyVersions-request-uri-MaxItems"></a>
The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than `MaxItems` versions, the value of `IsTruncated` in the response is `true`, and the value of the `TrafficPolicyVersionMarker` element is the ID of the first version that Route 53 will return if you submit another request.

 ** [trafficpolicyversion](#API_ListTrafficPolicyVersions_RequestSyntax) **   <a name="Route53-ListTrafficPolicyVersions-request-uri-TrafficPolicyVersionMarker"></a>
For your first request to `ListTrafficPolicyVersions`, don't include the `TrafficPolicyVersionMarker` parameter.
If you have more traffic policy versions than the value of `MaxItems`, `ListTrafficPolicyVersions` returns only the first group of `MaxItems` versions. To get more traffic policy versions, submit another `ListTrafficPolicyVersions` request. For the value of `TrafficPolicyVersionMarker`, specify the value of `TrafficPolicyVersionMarker` in the previous response.
Length Constraints: Maximum length of 4.

## Request Body
<a name="API_ListTrafficPolicyVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrafficPolicyVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPolicyVersionsResponse>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <TrafficPolicies>
      <TrafficPolicy>
         <Comment>string</Comment>
         <Document>string</Document>
         <Id>string</Id>
         <Name>string</Name>
         <Type>string</Type>
         <Version>integer</Version>
      </TrafficPolicy>
   </TrafficPolicies>
   <TrafficPolicyVersionMarker>string</TrafficPolicyVersionMarker>
</ListTrafficPolicyVersionsResponse>
```

## Response Elements
<a name="API_ListTrafficPolicyVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListTrafficPolicyVersionsResponse](#API_ListTrafficPolicyVersions_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyVersions-response-ListTrafficPolicyVersionsResponse"></a>
Root level tag for the ListTrafficPolicyVersionsResponse parameters.
Required: Yes

 ** [IsTruncated](#API_ListTrafficPolicyVersions_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyVersions-response-IsTruncated"></a>
A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another `ListTrafficPolicyVersions` request and specifying the value of `NextMarker` in the `marker` parameter.
Type: Boolean

 ** [MaxItems](#API_ListTrafficPolicyVersions_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyVersions-response-MaxItems"></a>
The value that you specified for the `maxitems` parameter in the `ListTrafficPolicyVersions` request that produced the current response.
Type: String

 ** [TrafficPolicies](#API_ListTrafficPolicyVersions_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyVersions-response-TrafficPolicies"></a>
A list that contains one `TrafficPolicy` element for each traffic policy version that is associated with the specified traffic policy.
Type: Array of [TrafficPolicy](API_TrafficPolicy.md) objects

 ** [TrafficPolicyVersionMarker](#API_ListTrafficPolicyVersions_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyVersions-response-TrafficPolicyVersionMarker"></a>
If `IsTruncated` is `true`, the value of `TrafficPolicyVersionMarker` identifies the first traffic policy that Amazon Route 53 will return if you submit another request. Call `ListTrafficPolicyVersions` again and specify the value of `TrafficPolicyVersionMarker` in the `TrafficPolicyVersionMarker` request parameter.
This element is present only if `IsTruncated` is `true`.
Type: String
Length Constraints: Maximum length of 4.

## Errors
<a name="API_ListTrafficPolicyVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_ListTrafficPolicyVersions_Examples"></a>

### Example Request
<a name="API_ListTrafficPolicyVersions_Example_1"></a>

This example illustrates one usage of ListTrafficPolicyVersions.

```
GET /2013-04-01/trafficpolicy/12345678-abcd-9876-fedc-1a2b3c4de5f6/versions?maxitems=1
```

### Example Response
<a name="API_ListTrafficPolicyVersions_Example_2"></a>

This example illustrates one usage of ListTrafficPolicyVersions.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPolicyVersionsResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicies>
      <TrafficPolicy>
         <Id>12345678-abcd-9876-fedc-1a2b3c4de5f6</Id>
         <VersionNumber>77</VersionNumber>
         <Name>MyTrafficPolicy</Name>
         <Type>A</Type>
         <Document>JSON-formatted definition of this traffic policy</Definition>
         <Comment>First traffic policy</Comment>
      </TrafficPolicy>
   </TrafficPolicies>
   <IsTrucated>true</IsTruncated>
   <TrafficPolicyVersionMarker>12345678-abcd-9876-fedc-1a2b3c4de5f7</TrafficPolicyVersionMarker>
   <MaxItems>1</MaxItems>
</ListTrafficPolicyVersionsResponse>
```

## See Also
<a name="API_ListTrafficPolicyVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListTrafficPolicyVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListTrafficPolicyVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
