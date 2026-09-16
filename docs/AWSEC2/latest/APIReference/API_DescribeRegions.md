---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html
---

# DescribeRegions
<a name="API_DescribeRegions"></a>

Describes the Regions that are enabled for your account, or all Regions.

For a list of the Regions supported by Amazon EC2, see [Amazon EC2 service endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html).

For information about enabling and disabling Regions for your account, see [Specify which AWS Regions your account can use](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) in the * AWS Account Management Reference Guide*.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeRegions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllRegions**
Indicates whether to display all Regions, including Regions that are disabled for your account.
Type: Boolean
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `endpoint` - The endpoint of the Region (for example, `ec2.us-east-1.amazonaws.com`).
+  `opt-in-status` - The opt-in status of the Region (`opt-in-not-required` \| `opted-in` \| `not-opted-in`).
+  `region-name` - The name of the Region (for example, `us-east-1`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **RegionName.N**
The names of the Regions. You can specify any Regions, whether they are enabled and disabled for your account.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeRegions_ResponseElements"></a>

The following elements are returned by the service.

 **regionInfo**
Information about the Regions.
Type: Array of [Region](API_Region.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeRegions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeRegions_Examples"></a>

### Example 1
<a name="API_DescribeRegions_Example_1"></a>

This example displays information about all Regions enabled for your account.

#### Sample Request
<a name="API_DescribeRegions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeRegions
&AUTHPARAMS
```

### Example 2
<a name="API_DescribeRegions_Example_2"></a>

This example displays information about all Regions, even the Regions that are disabled for your account.

#### Sample Request
<a name="API_DescribeRegions_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeRegions
&AllRegions=true
&AUTHPARAMS
```

### Example 3
<a name="API_DescribeRegions_Example_3"></a>

This example displays information about the specified Regions only.

#### Sample Request
<a name="API_DescribeRegions_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeRegions
&RegionName.1=us-east-1
&RegionName.2=eu-west-1
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeRegions_Example_3_Response"></a>

```
<DescribeRegionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <regionInfo>
      <item>
         <regionName>us-east-1</regionName>
         <regionEndpoint>ec2.us-east-1.amazonaws.com</regionEndpoint>
         <optInStatus>opt-in-not-required</optInStatus>
         <geographySet>
            <item>
               <name>United States of America</name>
            </item>
         </geographySet>
      </item>
      <item>
         <regionName>eu-west-1</regionName>
         <regionEndpoint>ec2.eu-west-1.amazonaws.com</regionEndpoint>
         <optInStatus>opt-in-not-required</optInStatus>
         <geographySet>
            <item>
               <name>Ireland</name>
            </item>
         </geographySet>
      </item>
   </regionInfo>
</DescribeRegionsResponse>
```

## See Also
<a name="API_DescribeRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeRegions)
