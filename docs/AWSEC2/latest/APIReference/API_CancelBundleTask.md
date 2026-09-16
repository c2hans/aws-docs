---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelBundleTask.html
---

# CancelBundleTask
<a name="API_CancelBundleTask"></a>

Cancels a bundling operation for an instance store-backed Windows instance.

**Note**
CancelBundleTask is no longer supported because [BundleInstance](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BundleInstance.html), the operation it cancels, is no longer supported.

## Request Parameters
<a name="API_CancelBundleTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **BundleId**
The ID of the bundle task.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_CancelBundleTask_ResponseElements"></a>

The following elements are returned by the service.

 **bundleInstanceTask**
Information about the bundle task.
Type: [BundleTask](API_BundleTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CancelBundleTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CancelBundleTask_Examples"></a>

### Example
<a name="API_CancelBundleTask_Example_1"></a>

This example request cancels the specified bundle task.

#### Sample Request
<a name="API_CancelBundleTask_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CancelBundleTask
&BundleId=bun-cla322b9
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelBundleTask_Example_1_Response"></a>

```
<CancelBundleTaskResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <bundleInstanceTask>
      <instanceId>i-1234567890abcdef0</instanceId>
      <bundleId>bun-cla322b9</bundleId>
      <state>canceling</state>
      <startTime>2008-10-07T11:41:50.000Z</startTime>
      <updateTime>2008-10-07T11:51:50.000Z</updateTime>
      <progress>20%</progress>
      <storage>
        <S3>
          <bucket>myawsbucket</bucket>
          <prefix>my-new-image</prefix>
        </S3>
      </storage>
  </bundleInstanceTask>
</CancelBundleTaskResponse>
```

## See Also
<a name="API_CancelBundleTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelBundleTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelBundleTask)
