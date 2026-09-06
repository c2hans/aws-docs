---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_4_cloudfront_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudFront examples using Tools for PowerShell V4
<a name="powershell_4_cloudfront_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with CloudFront.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CFCloudFrontOriginAccessIdentity`
<a name="cloudfront_GetCloudFrontOriginAccessIdentity_powershell_4_topic"></a>

The following code example shows how to use `Get-CFCloudFrontOriginAccessIdentity`.

**Tools for PowerShell V4**
**Example 1: This example returns a specific Amazon CloudFront origin access identity, specified by the -Id parameter. Although the -Id parameter is not required, if you do not specify it, no results are returned.**

```
Get-CFCloudFrontOriginAccessIdentity -Id E3XXXXXXXXXXRT
```
**Output:**

```
      CloudFrontOriginAccessIdentityConfig    Id                                      S3CanonicalUserId
      ------------------------------------    --                                      -----------------
      Amazon.CloudFront.Model.CloudFrontOr... E3XXXXXXXXXXRT                          4b6e...
```
+  For API details, see [GetCloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFCloudFrontOriginAccessIdentityConfig`
<a name="cloudfront_GetCloudFrontOriginAccessIdentityConfig_powershell_4_topic"></a>

The following code example shows how to use `Get-CFCloudFrontOriginAccessIdentityConfig`.

**Tools for PowerShell V4**
**Example 1: This example returns configuration information about a single Amazon CloudFront origin access identity, specified by the -Id parameter. Errors occur if no -Id parameter is specified..**

```
Get-CFCloudFrontOriginAccessIdentityConfig -Id E3XXXXXXXXXXRT
```
**Output:**

```
      CallerReference                                             Comment
      ---------------                                             -------
      mycallerreference: 2/1/2011 1:16:32 PM                      Caller reference: 2/1/2011 1:16:32 PM
```
+  For API details, see [GetCloudFrontOriginAccessIdentityConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFCloudFrontOriginAccessIdentityList`
<a name="cloudfront_ListCloudFrontOriginAccessIdentities_powershell_4_topic"></a>

The following code example shows how to use `Get-CFCloudFrontOriginAccessIdentityList`.

**Tools for PowerShell V4**
**Example 1: This example returns a list of Amazon CloudFront origin access identities. Because the -MaxItem parameter specifies a value of 2, the results include two identities.**

```
Get-CFCloudFrontOriginAccessIdentityList -MaxItem 2
```
**Output:**

```
IsTruncated : True
Items       : {E326XXXXXXXXXT, E1YWXXXXXXX9B}
Marker      :
MaxItems    : 2
NextMarker  : E1YXXXXXXXXX9B
Quantity    : 2
```
+  For API details, see [ListCloudFrontOriginAccessIdentities](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFDistribution`
<a name="cloudfront_GetDistribution_powershell_4_topic"></a>

The following code example shows how to use `Get-CFDistribution`.

**Tools for PowerShell V4**
**Example 1: Retrieves the information for a specific distribution.**

```
Get-CFDistribution -Id EXAMPLE0000ID
```
+  For API details, see [GetDistribution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFDistributionConfig`
<a name="cloudfront_GetDistributionConfig_powershell_4_topic"></a>

The following code example shows how to use `Get-CFDistributionConfig`.

**Tools for PowerShell V4**
**Example 1: Retrieves the configuration for a specific distribution.**

```
Get-CFDistributionConfig -Id EXAMPLE0000ID
```
+  For API details, see [GetDistributionConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-CFDistributionList`
<a name="cloudfront_ListDistributions_powershell_4_topic"></a>

The following code example shows how to use `Get-CFDistributionList`.

**Tools for PowerShell V4**
**Example 1: Returns distributions.**

```
Get-CFDistributionList
```
+  For API details, see [ListDistributions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CFDistribution`
<a name="cloudfront_CreateDistribution_powershell_4_topic"></a>

The following code example shows how to use `New-CFDistribution`.

**Tools for PowerShell V4**
**Example 1: Creates a basic CloudFront distribution, configured with logging and caching.**

```
$origin = New-Object Amazon.CloudFront.Model.Origin
$origin.DomainName = "amzn-s3-demo-bucket.s3.amazonaws.com"
$origin.Id = "UniqueOrigin1"
$origin.S3OriginConfig = New-Object Amazon.CloudFront.Model.S3OriginConfig
$origin.S3OriginConfig.OriginAccessIdentity = ""
New-CFDistribution `
      -DistributionConfig_Enabled $true `
      -DistributionConfig_Comment "Test distribution" `
      -Origins_Item $origin `
      -Origins_Quantity 1 `
      -Logging_Enabled $true `
      -Logging_IncludeCookie $true `
      -Logging_Bucket amzn-s3-demo-logging-bucket.s3.amazonaws.com `
      -Logging_Prefix "help/" `
      -DistributionConfig_CallerReference Client1 `
      -DistributionConfig_DefaultRootObject index.html `
      -DefaultCacheBehavior_TargetOriginId $origin.Id `
      -ForwardedValues_QueryString $true `
      -Cookies_Forward all `
      -WhitelistedNames_Quantity 0 `
      -TrustedSigners_Enabled $false `
      -TrustedSigners_Quantity 0 `
      -DefaultCacheBehavior_ViewerProtocolPolicy allow-all `
      -DefaultCacheBehavior_MinTTL 1000 `
      -DistributionConfig_PriceClass "PriceClass_All" `
      -CacheBehaviors_Quantity 0 `
      -Aliases_Quantity 0
```
+  For API details, see [CreateDistribution](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CFInvalidation`
<a name="cloudfront_CreateInvalidation_powershell_4_topic"></a>

The following code example shows how to use `New-CFInvalidation`.

**Tools for PowerShell V4**
**Example 1: This example creates a new invalidation on a distribution with an ID of EXAMPLENSTXAXE. The CallerReference is a unique ID chosen by the user; in this case, a time stamp representing May 15, 2019 at 9:00 a.m. is used. The $Paths variable stores three paths to image and media files that the user does not want as part of the distribution's cache. The -Paths\_Quantity parameter value is the total number of paths specified in the -Paths\_Item parameter.**

```
$Paths = "/images/*.gif", "/images/image1.jpg", "/videos/*.mp4"
New-CFInvalidation -DistributionId "EXAMPLENSTXAXE" -InvalidationBatch_CallerReference 20190515090000 -Paths_Item $Paths -Paths_Quantity 3
```
**Output:**

```
Invalidation                         Location
------------                         --------
Amazon.CloudFront.Model.Invalidation https://cloudfront.amazonaws.com/2018-11-05/distribution/EXAMPLENSTXAXE/invalidation/EXAMPLE8NOK9H
```
+  For API details, see [CreateInvalidation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CFSignedCookie`
<a name="cloudfront_New-CFSignedCookie_powershell_4_topic"></a>

The following code example shows how to use `New-CFSignedCookie`.

**Tools for PowerShell V4**
**Example 1: Creates a signed cookie to the specified resource using a canned policy. The cookie will be valid for one year.**

```
$params = @{
	"ResourceUri"="http://xyz.cloudfront.net/image1.jpeg"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=(Get-Date).AddYears(1)
}
New-CFSignedCookie @params
```
**Output:**

```
Expires
-------
[CloudFront-Expires, 1472227284]
```
**Example 2: Creates a signed cookie to the specified resources using a custom policy. The cookie will be valid in 24 hours and will expire one week afterward.**

```
$start = (Get-Date).AddHours(24)
$params = @{
	"ResourceUri"="http://xyz.cloudfront.net/content/*.jpeg"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=$start.AddDays(7)
    "ActiveFrom"=$start
}

New-CFSignedCookie @params
```
**Output:**

```
Policy
------
[CloudFront-Policy, eyJTd...wIjo...
```
**Example 3: Creates a signed cookie to the specified resources using a custom policy. The cookie will be valid in 24 hours and will expire one week afterward. Access to the resources is restricted to the specified ip range.**

```
$start = (Get-Date).AddHours(24)
$params = @{
	"ResourceUri"="http://xyz.cloudfront.net/content/*.jpeg"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=$start.AddDays(7)
    "ActiveFrom"=$start
	"IpRange"="192.0.2.0/24"
}

New-CFSignedCookie @params
```
**Output:**

```
Policy                                                                                                                                         ------                                                                                                                                         [CloudFront-Policy, eyJTd...wIjo...
```
+  For API details, see [New-CFSignedCookie](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-CFSignedUrl`
<a name="cloudfront_New-CFSignedUrl_powershell_4_topic"></a>

The following code example shows how to use `New-CFSignedUrl`.

**Tools for PowerShell V4**
**Example 1: Creates a signed url to the specified resource using a canned policy. The url will be valid for one hour. A System.Uri object containing the signed url is emitted to the pipeline.**

```
$params = @{
	"ResourceUri"="https://cdn.example.com/index.html"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=(Get-Date).AddHours(1)
}
New-CFSignedUrl @params
```
**Example 2: Creates a signed url to the specified resource using a custom policy. The url will be valid starting in 24 hours and will expire one week later.**

```
$start = (Get-Date).AddHours(24)
$params = @{
	"ResourceUri"="https://cdn.example.com/index.html"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=(Get-Date).AddDays(7)
    "ActiveFrom"=$start
}
New-CFSignedUrl @params
```
**Example 3: Creates a signed url to the specified resource using a custom policy. The url will be valid starting in 24 hours and will expire one week later. Access to the resource is restricted to the specified ip range.**

```
$start = (Get-Date).AddHours(24)
$params = @{
	"ResourceUri"="https://cdn.example.com/index.html"
	"KeyPairId"="AKIAIOSFODNN7EXAMPLE"
	"PrivateKeyFile"="C:\pk-AKIAIOSFODNN7EXAMPLE.pem"
	"ExpiresOn"=(Get-Date).AddDays(7)
    "ActiveFrom"=$start
    "IpRange"="192.0.2.0/24"
}
New-CFSignedUrl @params
```
+  For API details, see [New-CFSignedUrl](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.
