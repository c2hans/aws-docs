---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists tags for one health check or hosted zone.

For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /2013-04-01/tags/{{ResourceType}}/{{ResourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceId](#API_ListTagsForResource_RequestSyntax) **   <a name="Route53-ListTagsForResource-request-uri-ResourceId"></a>
The ID of the resource for which you want to retrieve tags.
Length Constraints: Maximum length of 64.
Required: Yes

 ** [ResourceType](#API_ListTagsForResource_RequestSyntax) **   <a name="Route53-ListTagsForResource-request-uri-ResourceType"></a>
The type of the resource.
+ The resource type for health checks is `healthcheck`.
+ The resource type for hosted zones is `hostedzone`.
Valid Values: `healthcheck | hostedzone`
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListTagsForResourceResponse>
   <ResourceTagSet>
      <ResourceId>string</ResourceId>
      <ResourceType>string</ResourceType>
      <Tags>
         <Tag>
            <Key>string</Key>
            <Value>string</Value>
         </Tag>
      </Tags>
   </ResourceTagSet>
</ListTagsForResourceResponse>
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListTagsForResourceResponse](#API_ListTagsForResource_ResponseSyntax) **   <a name="Route53-ListTagsForResource-response-ListTagsForResourceResponse"></a>
Root level tag for the ListTagsForResourceResponse parameters.
Required: Yes

 ** [ResourceTagSet](#API_ListTagsForResource_ResponseSyntax) **   <a name="Route53-ListTagsForResource-response-ResourceTagSet"></a>
A `ResourceTagSet` containing tags associated with the specified resource.
Type: [ResourceTagSet](API_ResourceTagSet.md) object

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchHealthCheck **
No health check exists with the specified ID.
 ** message **

HTTP Status Code: 404

 ** NoSuchHostedZone **
No hosted zone exists with the ID that you specified.
 ** message **

HTTP Status Code: 404

 ** PriorRequestNotComplete **
If Amazon Route 53 can't process a request before the next request arrives, it will reject subsequent requests for the same hosted zone and return an `HTTP 400 error` (`Bad request`). If Route 53 returns this error repeatedly for the same request, we recommend that you wait, in intervals of increasing duration, before you try the request again.
HTTP Status Code: 400

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 400

## Examples
<a name="API_ListTagsForResource_Examples"></a>

### Example Request
<a name="API_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

```
GET /2013-04-01/tags/healthcheck/abcdef11-2222-3333-4444-555555fedcba
```

### Example Response
<a name="API_ListTagsForResource_Example_2"></a>

This example illustrates one usage of ListTagsForResource.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ListTagsForResourceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <ResourceTagSet>
      <ResourceType>healthcheck</ResourceType>
      <ResourceId>abcdef11-2222-3333-4444-555555fedcba</ResourceId>
      <Tags>
         <Tag>
            <Key>Owner<Key>
            <Value>dbadmin<Value>
         </Tag>
         <Tag>
            <Key>Cost Center<Key>
            <Value>80432<Value>
         </Tag>
      </Tags>
   <ResourceTagSet>
</ListTagsForResourceResponse>
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ListTagsForResource)
