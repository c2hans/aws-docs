---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteApplicationStatusCheck.html
---

# DeleteApplicationStatusCheck
<a name="API_DeleteApplicationStatusCheck"></a>

Deletes an application status check. The following rules apply:
+ Deleting a check automatically removes all of its associations.
+ Use `DescribeApplicationStatusChecks` to view existing checks before deleting.

## Request Parameters
<a name="API_DeleteApplicationStatusCheck_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ApplicationStatusCheckId**
The ID of the application status check to delete.
Type: String
Required: Yes

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteApplicationStatusCheck_ResponseElements"></a>

The following elements are returned by the service.

 **applicationStatusCheck**
Information about the deleted application status check.
Type: [ApplicationStatusCheckResponseObject](API_ApplicationStatusCheckResponseObject.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteApplicationStatusCheck_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteApplicationStatusCheck_Examples"></a>

### To delete an application status check
<a name="API_DeleteApplicationStatusCheck_Example_1"></a>

This example deletes the specified application status check.

#### Sample Request
<a name="API_DeleteApplicationStatusCheck_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteApplicationStatusCheck
&ApplicationStatusCheckId=asc-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteApplicationStatusCheck_Example_1_Response"></a>

```
<DeleteApplicationStatusCheckResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <applicationStatusCheck>
        <applicationStatusCheckId>asc-0123456789abcdef0</applicationStatusCheckId>
    </applicationStatusCheck>
</DeleteApplicationStatusCheckResult>
```

## See Also
<a name="API_DeleteApplicationStatusCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteApplicationStatusCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteApplicationStatusCheck)
