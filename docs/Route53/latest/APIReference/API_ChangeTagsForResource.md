---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeTagsForResource.html
---

# ChangeTagsForResource
<a name="API_ChangeTagsForResource"></a>

Adds, edits, or deletes tags for a health check or a hosted zone.

For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*.

## Request Syntax
<a name="API_ChangeTagsForResource_RequestSyntax"></a>

```
POST /2013-04-01/tags/{{ResourceType}}/{{ResourceId}} HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeTagsForResourceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <AddTags>
      <Tag>
         <Key>{{string}}</Key>
         <Value>{{string}}</Value>
      </Tag>
   </AddTags>
   <RemoveTagKeys>
      <Key>{{string}}</Key>
   </RemoveTagKeys>
</ChangeTagsForResourceRequest>
```

## URI Request Parameters
<a name="API_ChangeTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceId](#API_ChangeTagsForResource_RequestSyntax) **   <a name="Route53-ChangeTagsForResource-request-uri-ResourceId"></a>
The ID of the resource for which you want to add, change, or delete tags.
Length Constraints: Maximum length of 64.
Required: Yes

 ** [ResourceType](#API_ChangeTagsForResource_RequestSyntax) **   <a name="Route53-ChangeTagsForResource-request-uri-ResourceType"></a>
The type of the resource.
+ The resource type for health checks is `healthcheck`.
+ The resource type for hosted zones is `hostedzone`.
Valid Values: `healthcheck | hostedzone`
Required: Yes

## Request Body
<a name="API_ChangeTagsForResource_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ChangeTagsForResourceRequest](#API_ChangeTagsForResource_RequestSyntax) **   <a name="Route53-ChangeTagsForResource-request-ChangeTagsForResourceRequest"></a>
Root level tag for the ChangeTagsForResourceRequest parameters.
Required: Yes

 ** [AddTags](#API_ChangeTagsForResource_RequestSyntax) **   <a name="Route53-ChangeTagsForResource-request-AddTags"></a>
A complex type that contains a list of the tags that you want to add to the specified health check or hosted zone and/or the tags that you want to edit `Value` for.
You can add a maximum of 10 tags to a health check or a hosted zone.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [RemoveTagKeys](#API_ChangeTagsForResource_RequestSyntax) **   <a name="Route53-ChangeTagsForResource-request-RemoveTagKeys"></a>
A complex type that contains a list of the tags that you want to delete from the specified health check or hosted zone. You can specify up to 10 keys.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 128.
Required: No

## Response Syntax
<a name="API_ChangeTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ChangeTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ChangeTagsForResource_Errors"></a>

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
<a name="API_ChangeTagsForResource_Examples"></a>

### Example Request
<a name="API_ChangeTagsForResource_Example_1"></a>

This example illustrates one usage of ChangeTagsForResource.

```
POST /2013-04-01/tags/healthcheck/abcdef11-2222-3333-4444-555555fedcba HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ChangeTagsForResourceRequest xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <RemoveTagKeys>
      <Key>Owner</Key>
   </RemoveTagKeys>
   <AddTags>
      <Tag>
         <Key>Cost Center</Key>
         <Value>80432</Value>
      </Tag>
   </AddTags>
</ChangeTagsForResourceRequest>
```

### Example Response
<a name="API_ChangeTagsForResource_Example_2"></a>

This example illustrates one usage of ChangeTagsForResource.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<ChangeTagsForResourceResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
</ChangeTagsForResourceResponse>
```

## See Also
<a name="API_ChangeTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/ChangeTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeTagsForResource)
