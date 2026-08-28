---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFpgaImageAttribute.html
---

# DescribeFpgaImageAttribute
<a name="API_DescribeFpgaImageAttribute"></a>

Describes the specified attribute of the specified Amazon FPGA Image (AFI).

## Request Parameters
<a name="API_DescribeFpgaImageAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The AFI attribute.
Type: String
Valid Values: `description | name | loadPermission | productCodes`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FpgaImageId**
The ID of the AFI.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeFpgaImageAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **fpgaImageAttribute**
Information about the attribute.
Type: [FpgaImageAttribute](API_FpgaImageAttribute.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeFpgaImageAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeFpgaImageAttribute_Examples"></a>

### Example
<a name="API_DescribeFpgaImageAttribute_Example_1"></a>

This example describes the load permissions for the specified AFI.

#### Sample Request
<a name="API_DescribeFpgaImageAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeFpgaImageAttribute
&FpgaImageId=afi-0d123e21abcc85abc
&Attribute=loadPermission
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeFpgaImageAttribute_Example_1_Response"></a>

```
<DescribeFpgaImageAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>19106033-3723-481e-8cc4-aedexample</requestId>
    <fpgaImageAttribute>
        <fpgaImageId>afi-0d123e21abcc85abc</fpgaImageId>
        <loadPermissions>
            <item>
                <userId>123456789012</userId>
            </item>
        </loadPermissions>
    </fpgaImageAttribute>
</DescribeFpgaImageAttributeResponse>
```

## See Also
<a name="API_DescribeFpgaImageAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeFpgaImageAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeFpgaImageAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
