---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListVirtualMFADevices.html
---

# ListVirtualMFADevices
<a name="API_ListVirtualMFADevices"></a>

Lists the virtual MFA devices defined in the AWS account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices. Assignment status can be `Assigned`, `Unassigned`, or `Any`.

**Note**
IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view tag information for a virtual MFA device, see [ListMFADeviceTags](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADeviceTags.html).

You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_ListVirtualMFADevices_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AssignmentStatus **
 The status (`Unassigned` or `Assigned`) of the devices to list. If you do not specify an `AssignmentStatus`, the operation defaults to `Any`, which lists both assigned and unassigned virtual MFA devices.,
Type: String
Valid Values: `Assigned | Unassigned | Any`
Required: No

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## Response Elements
<a name="API_ListVirtualMFADevices_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **VirtualMFADevices.member.N**
 The list of virtual MFA devices in the current account that match the `AssignmentStatus` value that was passed in the request.
Type: Array of [VirtualMFADevice](API_VirtualMFADevice.md) objects

## Errors
<a name="API_ListVirtualMFADevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListVirtualMFADevices_Examples"></a>

### Example
<a name="API_ListVirtualMFADevices_Example_1"></a>

This example illustrates one usage of ListVirtualMFADevices.

#### Sample Request
<a name="API_ListVirtualMFADevices_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListVirtualMFADevices
&AssignmentStatus=Any
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListVirtualMFADevices_Example_1_Response"></a>

```
<ListVirtualMFADevicesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListVirtualMFADevicesResult>
  <IsTruncated>false</IsTruncated>
  <VirtualMFADevices>
    <member>
      <EnableDate>20112-11-17T12:31:16Z</EnableDate>
      <SerialNumber>
      arn:aws:iam::123456789012:mfa/MyCustomUser
      </SerialNumber>
      <User>
        <Arn>arn:aws:iam::123456789012:user</MyCustomUser>
        <CreateDate>2012-10-13T22:00:36Z</CreateDate>
        <PasswordLastUsed>1540408180</PasswordLastUsed>
        <Path>/</Path>
        <UserId>AIDAEXAMPLE36EXAMPLEC</UserId>
        <UserName>MyCustomUser</UserName>
      </User>
    </member>
    <member>
      <EnableDate>2011-10-31T20:45:02Z</EnableDate>
      <SerialNumber>
      arn:aws:iam:::mfa/ExampleUser
      </SerialNumber>
      <User>
        <Arn>arn:aws:iam::111122223333:user/ExampleUser</Arn>
        <CreateDate>2011-07-01T17:23:07Z</CreateDate>
        <PasswordLastUsed>1380057478</PasswordLastUsed>
        <Path>/</Path>
        <UserId>AIDEXAMPLE4EXAMPLEXYZ</UserId>
        <UserName>ExampleUser</UserName>
      </User>
    </member>
  </VirtualMFADevices>
</ListVirtualMFADevicesResult>
<ResponseMetadata>
  <RequestId>b61ce1b1-0401-11e1-b2f8-2dEXAMPLEbfc</RequestId>
</ResponseMetadata>
</ListVirtualMFADevicesResponse>
```

## See Also
<a name="API_ListVirtualMFADevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListVirtualMFADevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListVirtualMFADevices)
