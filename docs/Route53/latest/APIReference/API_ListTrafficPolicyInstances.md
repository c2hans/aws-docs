---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicyInstances.html
---

# ListTrafficPolicyInstances
<a name="API_ListTrafficPolicyInstances"></a>

Gets information about the traffic policy instances that you created by using the current AWS account.

**Note**
After you submit an `UpdateTrafficPolicyInstance` request, there's a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the `State` response element.

Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the `MaxItems` parameter to list them in groups of up to 100.

## Request Syntax
<a name="API_ListTrafficPolicyInstances_RequestSyntax"></a>

```
GET /2013-04-01/trafficpolicyinstances?hostedzoneid={{HostedZoneIdMarker}}&maxitems={{MaxItems}}&trafficpolicyinstancename={{TrafficPolicyInstanceNameMarker}}&trafficpolicyinstancetype={{TrafficPolicyInstanceTypeMarker}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrafficPolicyInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [hostedzoneid](#API_ListTrafficPolicyInstances_RequestSyntax) **   <a name="Route53-ListTrafficPolicyInstances-request-uri-HostedZoneIdMarker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more traffic policy instances. To get more traffic policy instances, submit another `ListTrafficPolicyInstances` request. For the value of `HostedZoneId`, specify the value of `HostedZoneIdMarker` from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.
If the value of `IsTruncated` in the previous response was `false`, there are no more traffic policy instances to get.
Length Constraints: Maximum length of 32.

 ** [maxitems](#API_ListTrafficPolicyInstances_RequestSyntax) **   <a name="Route53-ListTrafficPolicyInstances-request-uri-MaxItems"></a>
The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a `ListTrafficPolicyInstances` request. If you have more than `MaxItems` traffic policy instances, the value of the `IsTruncated` element in the response is `true`, and the values of `HostedZoneIdMarker`, `TrafficPolicyInstanceNameMarker`, and `TrafficPolicyInstanceTypeMarker` represent the first traffic policy instance in the next group of `MaxItems` traffic policy instances.

 ** [trafficpolicyinstancename](#API_ListTrafficPolicyInstances_RequestSyntax) **   <a name="Route53-ListTrafficPolicyInstances-request-uri-TrafficPolicyInstanceNameMarker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more traffic policy instances. To get more traffic policy instances, submit another `ListTrafficPolicyInstances` request. For the value of `trafficpolicyinstancename`, specify the value of `TrafficPolicyInstanceNameMarker` from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.
If the value of `IsTruncated` in the previous response was `false`, there are no more traffic policy instances to get.
Length Constraints: Maximum length of 1024.

 ** [trafficpolicyinstancetype](#API_ListTrafficPolicyInstances_RequestSyntax) **   <a name="Route53-ListTrafficPolicyInstances-request-uri-TrafficPolicyInstanceTypeMarker"></a>
If the value of `IsTruncated` in the previous response was `true`, you have more traffic policy instances. To get more traffic policy instances, submit another `ListTrafficPolicyInstances` request. For the value of `trafficpolicyinstancetype`, specify the value of `TrafficPolicyInstanceTypeMarker` from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.
If the value of `IsTruncated` in the previous response was `false`, there are no more traffic policy instances to get.
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

## Request Body
<a name="API_ListTrafficPolicyInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrafficPolicyInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPolicyInstancesResponse>
   <HostedZoneIdMarker>string</HostedZoneIdMarker>
   <IsTruncated>boolean</IsTruncated>
   <MaxItems>string</MaxItems>
   <TrafficPolicyInstanceNameMarker>string</TrafficPolicyInstanceNameMarker>
   <TrafficPolicyInstances>
      <TrafficPolicyInstance>
         <HostedZoneId>string</HostedZoneId>
         <Id>string</Id>
         <Message>string</Message>
         <Name>string</Name>
         <State>string</State>
         <TrafficPolicyId>string</TrafficPolicyId>
         <TrafficPolicyType>string</TrafficPolicyType>
         <TrafficPolicyVersion>integer</TrafficPolicyVersion>
         <TTL>long</TTL>
      </TrafficPolicyInstance>
   </TrafficPolicyInstances>
   <TrafficPolicyInstanceTypeMarker>string</TrafficPolicyInstanceTypeMarker>
</ListTrafficPolicyInstancesResponse>
```

## Response Elements
<a name="API_ListTrafficPolicyInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListTrafficPolicyInstancesResponse](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-ListTrafficPolicyInstancesResponse"></a>
Root level tag for the ListTrafficPolicyInstancesResponse parameters.
Required: Yes

 ** [HostedZoneIdMarker](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-HostedZoneIdMarker"></a>
If `IsTruncated` is `true`, `HostedZoneIdMarker` is the ID of the hosted zone of the first traffic policy instance that Route 53 will return if you submit another `ListTrafficPolicyInstances` request.
Type: String
Length Constraints: Maximum length of 32.

 ** [IsTruncated](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-IsTruncated"></a>
A flag that indicates whether there are more traffic policy instances to be listed. If the response was truncated, you can get more traffic policy instances by calling `ListTrafficPolicyInstances` again and specifying the values of the `HostedZoneIdMarker`, `TrafficPolicyInstanceNameMarker`, and `TrafficPolicyInstanceTypeMarker` in the corresponding request parameters.
Type: Boolean

 ** [MaxItems](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-MaxItems"></a>
The value that you specified for the `MaxItems` parameter in the call to `ListTrafficPolicyInstances` that produced the current response.
Type: String

 ** [TrafficPolicyInstanceNameMarker](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-TrafficPolicyInstanceNameMarker"></a>
If `IsTruncated` is `true`, `TrafficPolicyInstanceNameMarker` is the name of the first traffic policy instance that Route 53 will return if you submit another `ListTrafficPolicyInstances` request.
Type: String
Length Constraints: Maximum length of 1024.

 ** [TrafficPolicyInstances](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-TrafficPolicyInstances"></a>
A list that contains one `TrafficPolicyInstance` element for each traffic policy instance that matches the elements in the request.
Type: Array of [TrafficPolicyInstance](API_TrafficPolicyInstance.md) objects

 ** [TrafficPolicyInstanceTypeMarker](#API_ListTrafficPolicyInstances_ResponseSyntax) **   <a name="Route53-ListTrafficPolicyInstances-response-TrafficPolicyInstanceTypeMarker"></a>
If `IsTruncated` is `true`, `TrafficPolicyInstanceTypeMarker` is the DNS type of the resource record sets that are associated with the first traffic policy instance that Amazon Route 53 will return if you submit another `ListTrafficPolicyInstances` request.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`

## Errors
<a name="API_ListTrafficPolicyInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicyInstance **
No traffic policy instance exists with the specified ID.
 ** message **

HTTP Status Code: 404

## Examples
<a name="API_ListTrafficPolicyInstances_Examples"></a>

### Example Request
<a name="API_ListTrafficPolicyInstances_Example_1"></a>

The following example shows a request after the first request. (For the first request, you'd specify only the maxitems parameter.)

```
GET /2013-04-01/trafficpolicyinstances?hostedzoneid=Z1D633PJN98FT9
   &trafficpolicyinstancename=www.example.com
   &trafficpolicyinstancetype=A
   &maxitems=1
```

### Example Response
<a name="API_ListTrafficPolicyInstances_Example_2"></a>

This example illustrates one usage of ListTrafficPolicyInstances.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListTrafficPolicyInstancesResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicyInstances>
      <TrafficPolicyInstance>
         <Id>12131415-abac-5432-caba-6f5e4d3c2b1a</Id>
         <HostedZoneId>Z1D633PJN98FT9</HostedZoneId>
         <Name>www.example.com</Name>
         <TTL>300</TTL>
         <State>Applied</State>
         <Message/>
         <TrafficPolicyId>12345678-abcd-9876-fedc-1a2b3c4de5f6</TrafficPolicyId>
         <TrafficPolicyVersion>7</TrafficPolicyVersion>
         <TrafficPolicyType>A</TrafficPolicyType>
      </TrafficPolicyInstance>
   </TrafficPolicyInstances>
   <HostedZoneIdMarker>Z217DLHR85079R</HostedZoneIdMarker>
   <TrafficPolicyInstanceNameMarker>www.example.net</TrafficPolicyInstanceNameMarker>
   <TrafficPolicyInstanceTypeMarker>A</TrafficPolicyInstanceTypeMarker>
   <IsTruncated>true</IsTruncated>
   <MaxItems>1</MaxItems>
</ListTrafficPolicyInstancesResponse>
```

## See Also
<a name="API_ListTrafficPolicyInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListTrafficPolicyInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListTrafficPolicyInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
