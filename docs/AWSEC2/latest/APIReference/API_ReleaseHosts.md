---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseHosts.html
---

# ReleaseHosts
<a name="API_ReleaseHosts"></a>

When you no longer want to use an On-Demand Dedicated Host it can be released. On-Demand billing is stopped and the host goes into `released` state. The host ID of Dedicated Hosts that have been released can no longer be specified in another request, for example, to modify the host. You must stop or terminate all instances on a host before it can be released.

When Dedicated Hosts are released, it may take some time for them to stop counting toward your limit and you may receive capacity errors when trying to allocate new Dedicated Hosts. Wait a few minutes and then try again.

Released hosts still appear in a [DescribeHosts](API_DescribeHosts.md) response.

## Request Parameters
<a name="API_ReleaseHosts_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **HostId.N**
The IDs of the Dedicated Hosts to release.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_ReleaseHosts_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successful**
The IDs of the Dedicated Hosts that were successfully released.
Type: Array of strings

 **unsuccessful**
The IDs of the Dedicated Hosts that could not be released, including an error message.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_ReleaseHosts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReleaseHosts_Examples"></a>

### Example
<a name="API_ReleaseHosts_Example_1"></a>

This releases a Dedicated Host successfully.

#### Sample Request
<a name="API_ReleaseHosts_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReleaseHosts
&HostId=h-00548908djdsgfs
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReleaseHosts_Example_1_Response"></a>

```
<ReleaseHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <unsuccessful/>
    <successful>
        <item>h-00548908djdsgfs</item>
    </successful>
</ReleaseHostsResponse>
```

### Example
<a name="API_ReleaseHosts_Example_2"></a>

This request is unsuccessful.

#### Sample Request
<a name="API_ReleaseHosts_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReleaseHosts
&HostId=h-00548908djdsgfs
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReleaseHosts_Example_2_Response"></a>

```
<ReleaseHostsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <unsuccessful>
        <item>
       <error>
            <message>Dedicated host 'h-00548908djdsgfs' cannot be released as it is occupied</message>
            <code>Client.InvalidHost.Occupied</code<
       </error>
       <resourceId>h-00548908djdsgfs</resourceId>
        </item>
    </unsuccessful>
    <successful/>
</ReleaseHostsResponse>
```

## See Also
<a name="API_ReleaseHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReleaseHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReleaseHosts)
