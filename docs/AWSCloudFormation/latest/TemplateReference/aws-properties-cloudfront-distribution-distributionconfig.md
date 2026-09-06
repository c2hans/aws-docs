---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-distributionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution DistributionConfig
<a name="aws-properties-cloudfront-distribution-distributionconfig"></a>

A distribution configuration.

## Syntax
<a name="aws-properties-cloudfront-distribution-distributionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-distributionconfig-syntax.json"></a>

```
{
  "[Aliases](#cfn-cloudfront-distribution-distributionconfig-aliases)" : {{[ String, ... ]}},
  "[AnycastIpListId](#cfn-cloudfront-distribution-distributionconfig-anycastiplistid)" : {{String}},
  "[CacheBehaviors](#cfn-cloudfront-distribution-distributionconfig-cachebehaviors)" : {{[ CacheBehavior, ... ]}},
  "[CacheTagConfig](#cfn-cloudfront-distribution-distributionconfig-cachetagconfig)" : {{CacheTagConfig}},
  "[CNAMEs](#cfn-cloudfront-distribution-distributionconfig-cnames)" : {{[ String, ... ]}},
  "[Comment](#cfn-cloudfront-distribution-distributionconfig-comment)" : {{String}},
  "[ConnectionFunctionAssociation](#cfn-cloudfront-distribution-distributionconfig-connectionfunctionassociation)" : {{ConnectionFunctionAssociation}},
  "[ConnectionMode](#cfn-cloudfront-distribution-distributionconfig-connectionmode)" : {{String}},
  "[ContinuousDeploymentPolicyId](#cfn-cloudfront-distribution-distributionconfig-continuousdeploymentpolicyid)" : {{String}},
  "[CustomErrorResponses](#cfn-cloudfront-distribution-distributionconfig-customerrorresponses)" : {{[ CustomErrorResponse, ... ]}},
  "[CustomOrigin](#cfn-cloudfront-distribution-distributionconfig-customorigin)" : {{LegacyCustomOrigin}},
  "[DefaultCacheBehavior](#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior)" : {{DefaultCacheBehavior}},
  "[DefaultRootObject](#cfn-cloudfront-distribution-distributionconfig-defaultrootobject)" : {{String}},
  "[Enabled](#cfn-cloudfront-distribution-distributionconfig-enabled)" : {{Boolean}},
  "[HttpVersion](#cfn-cloudfront-distribution-distributionconfig-httpversion)" : {{String}},
  "[IPV6Enabled](#cfn-cloudfront-distribution-distributionconfig-ipv6enabled)" : {{Boolean}},
  "[Logging](#cfn-cloudfront-distribution-distributionconfig-logging)" : {{Logging}},
  "[OriginGroups](#cfn-cloudfront-distribution-distributionconfig-origingroups)" : {{OriginGroups}},
  "[Origins](#cfn-cloudfront-distribution-distributionconfig-origins)" : {{[ Origin, ... ]}},
  "[PriceClass](#cfn-cloudfront-distribution-distributionconfig-priceclass)" : {{String}},
  "[Restrictions](#cfn-cloudfront-distribution-distributionconfig-restrictions)" : {{Restrictions}},
  "[S3Origin](#cfn-cloudfront-distribution-distributionconfig-s3origin)" : {{LegacyS3Origin}},
  "[Staging](#cfn-cloudfront-distribution-distributionconfig-staging)" : {{Boolean}},
  "[TenantConfig](#cfn-cloudfront-distribution-distributionconfig-tenantconfig)" : {{TenantConfig}},
  "[ViewerCertificate](#cfn-cloudfront-distribution-distributionconfig-viewercertificate)" : {{ViewerCertificate}},
  "[ViewerMtlsConfig](#cfn-cloudfront-distribution-distributionconfig-viewermtlsconfig)" : {{ViewerMtlsConfig}},
  "[WebACLId](#cfn-cloudfront-distribution-distributionconfig-webaclid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-distributionconfig-syntax.yaml"></a>

```
  [Aliases](#cfn-cloudfront-distribution-distributionconfig-aliases): {{
    - String}}
  [AnycastIpListId](#cfn-cloudfront-distribution-distributionconfig-anycastiplistid): {{String}}
  [CacheBehaviors](#cfn-cloudfront-distribution-distributionconfig-cachebehaviors): {{
    - CacheBehavior}}
  [CacheTagConfig](#cfn-cloudfront-distribution-distributionconfig-cachetagconfig): {{
    CacheTagConfig}}
  [CNAMEs](#cfn-cloudfront-distribution-distributionconfig-cnames): {{
    - String}}
  [Comment](#cfn-cloudfront-distribution-distributionconfig-comment): {{String}}
  [ConnectionFunctionAssociation](#cfn-cloudfront-distribution-distributionconfig-connectionfunctionassociation): {{
    ConnectionFunctionAssociation}}
  [ConnectionMode](#cfn-cloudfront-distribution-distributionconfig-connectionmode): {{String}}
  [ContinuousDeploymentPolicyId](#cfn-cloudfront-distribution-distributionconfig-continuousdeploymentpolicyid): {{String}}
  [CustomErrorResponses](#cfn-cloudfront-distribution-distributionconfig-customerrorresponses): {{
    - CustomErrorResponse}}
  [CustomOrigin](#cfn-cloudfront-distribution-distributionconfig-customorigin): {{
    LegacyCustomOrigin}}
  [DefaultCacheBehavior](#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior): {{
    DefaultCacheBehavior}}
  [DefaultRootObject](#cfn-cloudfront-distribution-distributionconfig-defaultrootobject): {{String}}
  [Enabled](#cfn-cloudfront-distribution-distributionconfig-enabled): {{Boolean}}
  [HttpVersion](#cfn-cloudfront-distribution-distributionconfig-httpversion): {{String}}
  [IPV6Enabled](#cfn-cloudfront-distribution-distributionconfig-ipv6enabled): {{Boolean}}
  [Logging](#cfn-cloudfront-distribution-distributionconfig-logging): {{
    Logging}}
  [OriginGroups](#cfn-cloudfront-distribution-distributionconfig-origingroups): {{
    OriginGroups}}
  [Origins](#cfn-cloudfront-distribution-distributionconfig-origins): {{
    - Origin}}
  [PriceClass](#cfn-cloudfront-distribution-distributionconfig-priceclass): {{String}}
  [Restrictions](#cfn-cloudfront-distribution-distributionconfig-restrictions): {{
    Restrictions}}
  [S3Origin](#cfn-cloudfront-distribution-distributionconfig-s3origin): {{
    LegacyS3Origin}}
  [Staging](#cfn-cloudfront-distribution-distributionconfig-staging): {{Boolean}}
  [TenantConfig](#cfn-cloudfront-distribution-distributionconfig-tenantconfig): {{
    TenantConfig}}
  [ViewerCertificate](#cfn-cloudfront-distribution-distributionconfig-viewercertificate): {{
    ViewerCertificate}}
  [ViewerMtlsConfig](#cfn-cloudfront-distribution-distributionconfig-viewermtlsconfig): {{
    ViewerMtlsConfig}}
  [WebACLId](#cfn-cloudfront-distribution-distributionconfig-webaclid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-distributionconfig-properties"></a>

`Aliases`  <a name="cfn-cloudfront-distribution-distributionconfig-aliases"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AnycastIpListId`  <a name="cfn-cloudfront-distribution-distributionconfig-anycastiplistid"></a>
To use this field for a multi-tenant distribution, use a connection group instead. For more information, see [ConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html).
ID of the Anycast static IP list that is associated with the distribution.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheBehaviors`  <a name="cfn-cloudfront-distribution-distributionconfig-cachebehaviors"></a>
A complex type that contains zero or more `CacheBehavior` elements.
*Required*: No
*Type*: Array of [CacheBehavior](aws-properties-cloudfront-distribution-cachebehavior.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheTagConfig`  <a name="cfn-cloudfront-distribution-distributionconfig-cachetagconfig"></a>
Configuration for cache tag extraction from origin responses. When specified, CloudFront reads the header named in `HeaderName` from origin responses and stores the comma-separated values as cache tags on the object.
Distributions without `CacheTagConfig` do not extract tags. When `CacheTagConfig` is removed from a distribution via `UpdateDistribution`, CloudFront stops extracting tags from origin responses.
Changing the `HeaderName` on an existing distribution does not retroactively affect previously cached objects. Tag-based invalidations will not apply to objects already cached using a previous header. To ensure tag invalidations function after updating the header name, use path-based invalidations to recache all objects that use cache tags.
*Required*: No
*Type*: [CacheTagConfig](aws-properties-cloudfront-distribution-cachetagconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CNAMEs`  <a name="cfn-cloudfront-distribution-distributionconfig-cnames"></a>
An alias for the CloudFront distribution's domain name.
This property is legacy. We recommend that you use [Aliases](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases) instead.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Comment`  <a name="cfn-cloudfront-distribution-distributionconfig-comment"></a>
A comment to describe the distribution. The comment cannot be longer than 128 characters.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionFunctionAssociation`  <a name="cfn-cloudfront-distribution-distributionconfig-connectionfunctionassociation"></a>
The distribution's connection function association.
*Required*: No
*Type*: [ConnectionFunctionAssociation](aws-properties-cloudfront-distribution-connectionfunctionassociation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionMode`  <a name="cfn-cloudfront-distribution-distributionconfig-connectionmode"></a>
This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).
*Required*: No
*Type*: String
*Allowed values*: `direct | tenant-only`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContinuousDeploymentPolicyId`  <a name="cfn-cloudfront-distribution-distributionconfig-continuousdeploymentpolicyid"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
The identifier of a continuous deployment policy. For more information, see `CreateContinuousDeploymentPolicy`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomErrorResponses`  <a name="cfn-cloudfront-distribution-distributionconfig-customerrorresponses"></a>
A complex type that controls the following:
+ Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
+ How long CloudFront caches HTTP status codes in the 4xx and 5xx range.
For more information about custom error pages, see [Customizing Error Responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: Array of [CustomErrorResponse](aws-properties-cloudfront-distribution-customerrorresponse.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomOrigin`  <a name="cfn-cloudfront-distribution-distributionconfig-customorigin"></a>
The user-defined HTTP server that serves as the origin for content that CloudFront distributes.
This property is legacy. We recommend that you use [Origin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html) instead.
*Required*: No
*Type*: [LegacyCustomOrigin](aws-properties-cloudfront-distribution-legacycustomorigin.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultCacheBehavior`  <a name="cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior"></a>
A complex type that describes the default cache behavior if you don't specify a `CacheBehavior` element or if files don't match any of the values of `PathPattern` in `CacheBehavior` elements. You must create exactly one default cache behavior.
*Required*: Yes
*Type*: [DefaultCacheBehavior](aws-properties-cloudfront-distribution-defaultcachebehavior.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultRootObject`  <a name="cfn-cloudfront-distribution-distributionconfig-defaultrootobject"></a>
When a viewer requests the root URL for your distribution, the default root object is the object that you want CloudFront to request from your origin. For example, if your root URL is `https://www.example.com`, you can specify CloudFront to return the `index.html` file as the default root object. You can specify a default root object so that viewers see a specific file or object, instead of another object in your distribution (for example, `https://www.example.com/product-description.html`). A default root object avoids exposing the contents of your distribution.
You can specify the object name or a path to the object name (for example, `index.html` or `exampleFolderName/index.html`). Your string can't begin with a forward slash (`/`). Only specify the object name or the path to the object.
If you don't want to specify a default root object when you create a distribution, include an empty `DefaultRootObject` element.
To delete the default root object from an existing distribution, update the distribution configuration and include an empty `DefaultRootObject` element.
To replace the default root object, update the distribution configuration and specify the new object.
For more information about the default root object, see [Specify a default root object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-cloudfront-distribution-distributionconfig-enabled"></a>
From this field, you can enable or disable the selected distribution.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpVersion`  <a name="cfn-cloudfront-distribution-distributionconfig-httpversion"></a>
(Optional) Specify the HTTP version(s) that you want viewers to use to communicate with CloudFront. The default value for new distributions is `http1.1`.
For viewers and CloudFront to use HTTP/2, viewers must support TLSv1.2 or later, and must support Server Name Indication (SNI).
For viewers and CloudFront to use HTTP/3, viewers must support TLSv1.3 and Server Name Indication (SNI). CloudFront supports HTTP/3 connection migration to allow the viewer to switch networks without losing connection. For more information about connection migration, see [Connection Migration](https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration) at RFC 9000. For more information about supported TLSv1.3 ciphers, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).
*Required*: No
*Type*: String
*Allowed values*: `http1.1 | http2 | http3 | http2and3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IPV6Enabled`  <a name="cfn-cloudfront-distribution-distributionconfig-ipv6enabled"></a>
To use this field for a multi-tenant distribution, use a connection group instead. For more information, see [ConnectionGroup](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html).
If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify `true`. If you specify `false`, CloudFront responds to IPv6 DNS requests with the DNS response code `NOERROR` and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.
In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the `IpAddress` parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see [Creating a Signed URL Using a Custom Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html) in the *Amazon CloudFront Developer Guide*.
If you're using an Amazon Route 53 AWS Integration alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:
+ You enable IPv6 for the distribution
+ You're using alternate domain names in the URLs for your objects
For more information, see [Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html) in the *Amazon Route 53 AWS Integration Developer Guide*.
If you created a CNAME resource record set, either with Amazon Route 53 AWS Integration or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-cloudfront-distribution-distributionconfig-logging"></a>
A complex type that controls whether access logs are written for the distribution.
For more information about logging, see [Access Logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide*.
*Required*: No
*Type*: [Logging](aws-properties-cloudfront-distribution-logging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OriginGroups`  <a name="cfn-cloudfront-distribution-distributionconfig-origingroups"></a>
A complex type that contains information about origin groups for this distribution.
Specify a value for either the `Origins` or `OriginGroups` property.
*Required*: Conditional
*Type*: [OriginGroups](aws-properties-cloudfront-distribution-origingroups.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Origins`  <a name="cfn-cloudfront-distribution-distributionconfig-origins"></a>
A complex type that contains information about origins for this distribution.
Specify a value for either the `Origins` or `OriginGroups` property.
*Required*: Conditional
*Type*: Array of [Origin](aws-properties-cloudfront-distribution-origin.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PriceClass`  <a name="cfn-cloudfront-distribution-distributionconfig-priceclass"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify `PriceClass_All`, CloudFront responds to requests for your objects from all CloudFront edge locations.
If you specify a price class other than `PriceClass_All`, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.
For more information about price classes, see [Choosing the Price Class for a CloudFront Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html) in the *Amazon CloudFront Developer Guide*. For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see [Amazon CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/).
*Required*: No
*Type*: String
*Allowed values*: `PriceClass_100 | PriceClass_200 | PriceClass_All | None`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Restrictions`  <a name="cfn-cloudfront-distribution-distributionconfig-restrictions"></a>
A complex type that identifies ways in which you want to restrict distribution of your content.
*Required*: No
*Type*: [Restrictions](aws-properties-cloudfront-distribution-restrictions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Origin`  <a name="cfn-cloudfront-distribution-distributionconfig-s3origin"></a>
The origin as an Amazon S3 bucket.
This property is legacy. We recommend that you use [Origin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html) instead.
*Required*: No
*Type*: [LegacyS3Origin](aws-properties-cloudfront-distribution-legacys3origin.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Staging`  <a name="cfn-cloudfront-distribution-distributionconfig-staging"></a>
This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A Boolean that indicates whether this is a staging distribution. When this value is `true`, this is a staging distribution. When this value is `false`, this is not a staging distribution.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TenantConfig`  <a name="cfn-cloudfront-distribution-distributionconfig-tenantconfig"></a>
This field only supports multi-tenant distributions. You can't specify this field for standard distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.
A distribution tenant configuration.
*Required*: No
*Type*: [TenantConfig](aws-properties-cloudfront-distribution-tenantconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewerCertificate`  <a name="cfn-cloudfront-distribution-distributionconfig-viewercertificate"></a>
A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.
*Required*: No
*Type*: [ViewerCertificate](aws-properties-cloudfront-distribution-viewercertificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViewerMtlsConfig`  <a name="cfn-cloudfront-distribution-distributionconfig-viewermtlsconfig"></a>
The distribution's viewer mTLS configuration.
*Required*: No
*Type*: [ViewerMtlsConfig](aws-properties-cloudfront-distribution-viewermtlsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebACLId`  <a name="cfn-cloudfront-distribution-distributionconfig-webaclid"></a>
Multi-tenant distributions only support AWS WAF V2 web ACLs.
A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of AWS WAF, use the ACL ARN, for example `arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. To specify a web ACL created using AWS WAF Classic, use the ACL ID, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-distributionconfig--seealso"></a>
+ [DistributionConfig](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionConfig.html) in the *Amazon CloudFront API Reference*
