---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html
---

# ListPlatformApplications
<a name="API_ListPlatformApplications"></a>

Lists the platform application objects for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). The results for `ListPlatformApplications` are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call `ListPlatformApplications` using the NextToken string received from the previous call. When there are no more records to return, `NextToken` will be null. For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

This action is throttled at 15 transactions per second (TPS).

## Request Parameters
<a name="API_ListPlatformApplications_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
 `NextToken` string is used when calling `ListPlatformApplications` action to retrieve additional records that are available after the first page results.
Type: String
Required: No

## Response Elements
<a name="API_ListPlatformApplications_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
 `NextToken` string is returned when calling `ListPlatformApplications` action if additional records are available after the first page results.
Type: String

 **PlatformApplications.member.N**
Platform applications returned when calling `ListPlatformApplications` action.
Type: Array of [PlatformApplication](API_PlatformApplication.md) objects

## Errors
<a name="API_ListPlatformApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

## Examples
<a name="API_ListPlatformApplications_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListPlatformApplications_Example_1"></a>

This example illustrates one usage of ListPlatformApplications.

#### Sample Request
<a name="API_ListPlatformApplications_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=ListPlatformApplications
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListPlatformApplications_Example_1_Response"></a>

```
<ListPlatformApplicationsResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListPlatformApplicationsResult>
        <PlatformApplications>
            <member>
                <PlatformApplicationArn>arn:aws:sns:us-west-2:123456789012:app/APNS_SANDBOX/apnspushapp</PlatformApplicationArn>
                <Attributes>
                    <entry>
                        <key>AllowEndpointPolicies</key>
                        <value>false</value>
                    </entry>
                </Attributes>
            </member>
            <member>
                <PlatformApplicationArn>arn:aws:sns:us-west-2:123456789012:app/GCM/gcmpushapp</PlatformApplicationArn>
                <Attributes>
                    <entry>
                        <key>AllowEndpointPolicies</key>
                        <value>false</value>
                    </entry>
                </Attributes>
            </member>
        </PlatformApplications>
    </ListPlatformApplicationsResult>
    <ResponseMetadata>
        <RequestId>315a335e-85d8-52df-9349-791283cbb529</RequestId>
    </ResponseMetadata>
</ListPlatformApplicationsResponse>
```

## See Also
<a name="API_ListPlatformApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListPlatformApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListPlatformApplications)
