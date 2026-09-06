---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudfront_example_cloudfront_GetCloudFrontOriginAccessIdentityConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetCloudFrontOriginAccessIdentityConfig` with a CLI
<a name="cloudfront_example_cloudfront_GetCloudFrontOriginAccessIdentityConfig_section"></a>

The following code examples show how to use `GetCloudFrontOriginAccessIdentityConfig`.

------
#### [ CLI ]

**AWS CLI**
**To get a CloudFront origin access identity configuration**
The following example gets metadata about the CloudFront origin access identity (OAI) with the ID `E74FTE3AEXAMPLE`, including its `ETag`. The OAI ID is returned in the output of the create-cloud-front-origin-access-identity and list-cloud-front-origin-access-identities commands.

```
aws cloudfront get-cloud-front-origin-access-identity-config --id {{E74FTE3AEXAMPLE}}
```
Output:

```
{
    "ETag": "E2QWRUHEXAMPLE",
    "CloudFrontOriginAccessIdentityConfig": {
        "CallerReference": "cli-example",
        "Comment": "Example OAI"
    }
}
```
+  For API details, see [GetCloudFrontOriginAccessIdentityConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

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

**Tools for PowerShell V5**
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
+  For API details, see [GetCloudFrontOriginAccessIdentityConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
