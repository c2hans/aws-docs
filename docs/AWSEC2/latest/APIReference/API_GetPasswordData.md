---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetPasswordData.html
---

# GetPasswordData
<a name="API_GetPasswordData"></a>

Retrieves the encrypted administrator password for a running Windows instance.

The Windows password is generated at boot by the `EC2Config` service or `EC2Launch` scripts (Windows Server 2016 and later). This usually only happens the first time an instance is launched. For more information, see [EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingConfig_WinAMI.html) and [EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch.html) in the *Amazon EC2 User Guide*.

For the `EC2Config` service, the password is not generated for rebundled AMIs unless `Ec2SetPassword` is enabled before bundling.

The password is encrypted using the key pair that you specified when you launched the instance. You must provide the corresponding key pair file.

When you launch an instance, password generation and encryption may take a few minutes. If you try to retrieve the password before it's available, the output returns an empty string. We recommend that you wait up to 15 minutes after launching an instance before trying to retrieve the generated password.

## Request Parameters
<a name="API_GetPasswordData_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the Windows instance.
Type: String
Required: Yes

## Response Elements
<a name="API_GetPasswordData_ResponseElements"></a>

The following elements are returned by the service.

 **instanceId**
The ID of the Windows instance.
Type: String

 **passwordData**
The password of the instance. Returns an empty string if the password is not available.
Type: String

 **requestId**
The ID of the request.
Type: String

 **timestamp**
The time the data was last updated.
Type: Timestamp

## Errors
<a name="API_GetPasswordData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetPasswordData_Examples"></a>

### Example
<a name="API_GetPasswordData_Example_1"></a>

This example returns the encrypted version of the administrator password for the specified instance.

#### Sample Request
<a name="API_GetPasswordData_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetPasswordData
&InstanceId=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetPasswordData_Example_1_Response"></a>

```
<GetPasswordDataResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <timestamp>2009-10-24 15:00:00</timestamp>
  <passwordData>TGludXggdmVyc2lvbiAyLjYuMTYteGVuVSAoYnVpbGRlckBwYXRjaGJhdC5hbWF6b25zYSkgKGdj</passwordData>
</GetPasswordDataResponse>
```

## See Also
<a name="API_GetPasswordData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetPasswordData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetPasswordData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
