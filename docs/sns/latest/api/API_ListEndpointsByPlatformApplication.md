---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html
---

# ListEndpointsByPlatformApplication
<a name="API_ListEndpointsByPlatformApplication"></a>

Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM (Firebase Cloud Messaging) and APNS. The results for `ListEndpointsByPlatformApplication` are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call `ListEndpointsByPlatformApplication` again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html).

This action is throttled at 30 transactions per second (TPS).

## Request Parameters
<a name="API_ListEndpointsByPlatformApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
 `NextToken` string is used when calling `ListEndpointsByPlatformApplication` action to retrieve additional records that are available after the first page results.
Type: String
Required: No

 ** PlatformApplicationArn **
 `PlatformApplicationArn` for `ListEndpointsByPlatformApplicationInput` action.
Type: String
Required: Yes

## Response Elements
<a name="API_ListEndpointsByPlatformApplication_ResponseElements"></a>

The following elements are returned by the service.

 **Endpoints.member.N**
Endpoints returned for `ListEndpointsByPlatformApplication` action.
Type: Array of [Endpoint](API_Endpoint.md) objects

 ** NextToken **
 `NextToken` string is returned when calling `ListEndpointsByPlatformApplication` action if additional records are available after the first page results.
Type: String

## Errors
<a name="API_ListEndpointsByPlatformApplication_Errors"></a>

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

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_ListEndpointsByPlatformApplication_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListEndpointsByPlatformApplication_Example_1"></a>

This example illustrates one usage of ListEndpointsByPlatformApplication.

#### Sample Request
<a name="API_ListEndpointsByPlatformApplication_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=ListEndpointsByPlatformApplication
&PlatformApplicationArn=arn%3Aaws%3Asns%3Aus-west-2%3A123456789012%3Aapp%2FGCM%2Fgcmpushapp
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListEndpointsByPlatformApplication_Example_1_Response"></a>

```
<ListEndpointsByPlatformApplicationResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListEndpointsByPlatformApplicationResult>
        <Endpoints>
            <member>
                <EndpointArn>arn:aws:sns:us-west-2:123456789012:endpoint/GCM/gcmpushapp/5e3e9847-3183-3f18-a7e8-671c3a57d4b3</EndpointArn>
                <Attributes>
                    <entry>
                        <key>Enabled</key>
                        <value>true</value>
                    </entry>
                    <entry>
                        <key>CustomUserData</key>
                        <value>UserId=27576823</value>
                    </entry>
                    <entry>
                        <key>Token</key>
                        <value>APA91bGi7fFachkC1xjlqT66VYEucGHochmf1VQAr9k...jsM0PKPxKhddCzx6paEsyay9Zn3D4wNUJb8m6HZrBEXAMPLE</value>
                    </entry>
                </Attributes>
            </member>
        </Endpoints>
    </ListEndpointsByPlatformApplicationResult>
    <ResponseMetadata>
        <RequestId>9a48768c-dac8-5a60-aec0-3cc27ea08d96</RequestId>
    </ResponseMetadata>
</ListEndpointsByPlatformApplicationResponse>
```

## See Also
<a name="API_ListEndpointsByPlatformApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListEndpointsByPlatformApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListEndpointsByPlatformApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
