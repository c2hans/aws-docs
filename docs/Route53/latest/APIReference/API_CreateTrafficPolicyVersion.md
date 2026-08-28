---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicyVersion.html
---

# CreateTrafficPolicyVersion
<a name="API_CreateTrafficPolicyVersion"></a>

Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you'll need to start a new traffic policy.

## Request Syntax
<a name="API_CreateTrafficPolicyVersion_RequestSyntax"></a>

```
POST /2013-04-01/trafficpolicy/{{Id}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyVersionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Comment>{{string}}</Comment>
   <Document>{{string}}</Document>
</CreateTrafficPolicyVersionRequest>
```

## URI Request Parameters
<a name="API_CreateTrafficPolicyVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_CreateTrafficPolicyVersion_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-request-uri-Id"></a>
The ID of the traffic policy for which you want to create a new version.
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_CreateTrafficPolicyVersion_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateTrafficPolicyVersionRequest](#API_CreateTrafficPolicyVersion_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-request-CreateTrafficPolicyVersionRequest"></a>
Root level tag for the CreateTrafficPolicyVersionRequest parameters.
Required: Yes

 ** [Comment](#API_CreateTrafficPolicyVersion_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-request-Comment"></a>
The comment that you specified in the `CreateTrafficPolicyVersion` request, if any.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Document](#API_CreateTrafficPolicyVersion_RequestSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-request-Document"></a>
The definition of this version of the traffic policy, in JSON format. You specified the JSON in the `CreateTrafficPolicyVersion` request. For more information about the JSON format, see [CreateTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html).
Type: String
Length Constraints: Maximum length of 102400.
Required: Yes

## Response Syntax
<a name="API_CreateTrafficPolicyVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Location: {{Location}}
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyVersionResponse>
   <TrafficPolicy>
      <Comment>string</Comment>
      <Document>string</Document>
      <Id>string</Id>
      <Name>string</Name>
      <Type>string</Type>
      <Version>integer</Version>
   </TrafficPolicy>
</CreateTrafficPolicyVersionResponse>
```

## Response Elements
<a name="API_CreateTrafficPolicyVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The response returns the following HTTP headers.

 ** [Location](#API_CreateTrafficPolicyVersion_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-response-Location"></a>
A unique URL that represents a new traffic policy version.
Length Constraints: Maximum length of 1024.

The following data is returned in XML format by the service.

 ** [CreateTrafficPolicyVersionResponse](#API_CreateTrafficPolicyVersion_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-response-CreateTrafficPolicyVersionResponse"></a>
Root level tag for the CreateTrafficPolicyVersionResponse parameters.
Required: Yes

 ** [TrafficPolicy](#API_CreateTrafficPolicyVersion_ResponseSyntax) **   <a name="Route53-CreateTrafficPolicyVersion-response-TrafficPolicy"></a>
A complex type that contains settings for the new version of the traffic policy.
Type: [TrafficPolicy](API_TrafficPolicy.md) object

## Errors
<a name="API_CreateTrafficPolicyVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
Another user submitted a request to create, update, or delete the object at the same time that you did. Retry the request.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** InvalidTrafficPolicyDocument **
The format of the traffic policy document that you specified in the `Document` element is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchTrafficPolicy **
No traffic policy exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** TooManyTrafficPolicyVersionsForCurrentPolicy **
This traffic policy version can't be created because you've reached the limit of 1000 on the number of versions that you can create for the current traffic policy.
To create more traffic policy versions, you can use [GetTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html) to get the traffic policy document for a specified traffic policy version, and then use [CreateTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateTrafficPolicy.html) to create a new traffic policy using the traffic policy document.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateTrafficPolicyVersion_Examples"></a>

### Example Request
<a name="API_CreateTrafficPolicyVersion_Example_1"></a>

This example illustrates one usage of CreateTrafficPolicyVersion.

```
POST /2013-04-01/trafficpolicy/traffic policy ID HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyVersionRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Document>updated traffic policy definition in JSON format</Document>
   <Comment>Added us-east-2 region to traffic policy</Comment>
</CreateTrafficPolicyVersionRequest>
```

### Example Response
<a name="API_CreateTrafficPolicyVersion_Example_2"></a>

This example illustrates one usage of CreateTrafficPolicyVersion.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrafficPolicyVersionResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <TrafficPolicy>
      <Id>12345678-abcd-9876-fedc-1a2b3c4de5f6</Id>
      <Version>2</Version>
      <Name>MyTrafficPolicy</Name>
      <Type>A</Type>
      <Document>updated traffic policy definition in JSON format</Document>
      <Comment>Added us-east-2 region to traffic policy</Comment>
   </TrafficPolicy>
</CreateTrafficPolicyVersionResponse>
```

## See Also
<a name="API_CreateTrafficPolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/CreateTrafficPolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/CreateTrafficPolicyVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
