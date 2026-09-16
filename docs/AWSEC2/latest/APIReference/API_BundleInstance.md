---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleInstance.html
---

# BundleInstance
<a name="API_BundleInstance"></a>

Bundles an Amazon instance store-backed Windows instance.

During bundling, only the root device volume (C:\\) is bundled. Data on other instance store volumes is not preserved.

**Note**
BundleInstance is no longer supported. To create an AMI, use [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) instead. For more information about creating an Amazon EBS-backed AMI, see [ Create an Amazon EBS-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_BundleInstance_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance to bundle.
Default: None
Type: String
Required: Yes

 **Storage**
The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.
Type: [Storage](API_Storage.md) object
Required: Yes

## Response Elements
<a name="API_BundleInstance_ResponseElements"></a>

The following elements are returned by the service.

 **bundleInstanceTask**
Information about the bundle task.
Type: [BundleTask](API_BundleTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_BundleInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_BundleInstance_Examples"></a>

### Example
<a name="API_BundleInstance_Example_1"></a>

This example request bundles the specified instance.

Before you specify a value for your access key ID, review and follow the guidance in [Best Practices for AWS accounts](https://docs.aws.amazon.com/accounts/latest/reference/best-practices.html) in the * AWS Account Management Reference Guide*.

#### Sample Request
<a name="API_BundleInstance_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=BundleInstance
&InstanceId=i-1234567890abcdef0
&Storage.S3.AWSAccessKeyId='AKIAIOSFODNN7EXAMPLE'
&Storage.S3.Bucket=myawsbucket
&Storage.S3.Prefix=winami
&Storage.S3.UploadPolicy=eyJleHBpcmF0aW9uIjogIjIwMDgtMDgtMzBUMDg6NDk6MD
laIiwiY29uZGl0aW9ucyI6IFt7ImJ1Y2tldCI6ICJteS1idWNrZXQifSxbInN0YXJ0cy13aXRoIiwgI
iRrZXkiLCAibXktbmV3LWltYWdlIl0seyJhY2wiOiAiZWMyLWJ1bmRsZS1yZWFkIn1dfEXAMPLE
&Storage.S3.UploadPolicySignature=fh5tyyyQD8W4COEthj3nlGNEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_BundleInstance_Example_1_Response"></a>

```
<BundleInstanceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <bundleInstanceTask>
      <instanceId>i-1234567890abcdef0</instanceId>
      <bundleId>bun-c1a540a8</bundleId>
      <state>bundling</state>
      <startTime>2008-10-07T11:41:50.000Z</startTime>
      <updateTime>2008-10-07T11:51:50.000Z</updateTime>
      <progress>70%</progress>
      <storage>
        <S3>
          <bucket>myawsbucket</bucket>
          <prefix>winami</prefix>
        </S3>
      </storage>
  </bundleInstanceTask>
</BundleInstanceResponse>
```

## See Also
<a name="API_BundleInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/BundleInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BundleInstance)
