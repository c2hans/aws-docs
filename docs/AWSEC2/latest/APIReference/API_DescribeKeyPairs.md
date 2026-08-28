---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeKeyPairs.html
---

# DescribeKeyPairs
<a name="API_DescribeKeyPairs"></a>

Describes the specified key pairs or all of your key pairs.

For more information about key pairs, see [Amazon EC2 key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeKeyPairs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `key-pair-id` - The ID of the key pair.
+  `fingerprint` - The fingerprint of the key pair.
+  `key-name` - The name of the key pair.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludePublicKey**
If `true`, the public key material is included in the response.
Default: `false`
Type: Boolean
Required: No

 **KeyName.N**
The key pair names.
Default: Describes all of your key pairs.
Type: Array of strings
Required: No

 **KeyPairId.N**
The IDs of the key pairs.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeKeyPairs_ResponseElements"></a>

The following elements are returned by the service.

 **keySet**
Information about the key pairs.
Type: Array of [KeyPairInfo](API_KeyPairInfo.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeKeyPairs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeKeyPairs_Examples"></a>

### Example
<a name="API_DescribeKeyPairs_Example_1"></a>

This example describes the key pair with name my-key-pair.

#### Sample Request
<a name="API_DescribeKeyPairs_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeKeyPairs
&KeyName.1=my-key-pair
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeKeyPairs_Example_1_Response"></a>

```
<DescribeKeyPairsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <keySet>
      <item>
         <keyName>my-key-pair</keyName>
         <keyFingerprint>1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f</keyFingerprint>
      </item>
   </keySet>
</DescribeKeyPairsResponse>
```

### Example
<a name="API_DescribeKeyPairs_Example_2"></a>

This example filters the response to include only key pairs whose names include the string `Dave`.

#### Sample Request
<a name="API_DescribeKeyPairs_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeKeyPairs
&Filter.1.Name=key-name
&Filter.1.Value.1=*Dave*
&AUTHPARAMS
```

## See Also
<a name="API_DescribeKeyPairs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeKeyPairs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeKeyPairs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
