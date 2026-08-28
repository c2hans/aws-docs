---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html
---

# ListOriginationNumbers
<a name="API_ListOriginationNumbers"></a>

Lists the calling AWS account's dedicated origination numbers and their metadata. For more information about origination numbers, see [Origination numbers](https://docs.aws.amazon.com/sns/latest/dg/channels-sms-originating-identities-origination-numbers.html) in the *Amazon SNS Developer Guide*.

## Request Parameters
<a name="API_ListOriginationNumbers_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxResults **
The maximum number of origination numbers to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: No

 ** NextToken **
Token that the previous `ListOriginationNumbers` request returns.
Type: String
Required: No

## Response Elements
<a name="API_ListOriginationNumbers_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A `NextToken` string is returned when you call the `ListOriginationNumbers` operation if additional pages of records are available.
Type: String

 **PhoneNumbers.member.N**
A list of the calling account's verified and pending origination numbers.
Type: Array of [PhoneNumberInformation](API_PhoneNumberInformation.md) objects

## Errors
<a name="API_ListOriginationNumbers_Errors"></a>

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

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

 ** Validation **
Indicates that a parameter in the request is invalid.
HTTP Status Code: 400

## Examples
<a name="API_ListOriginationNumbers_Examples"></a>

### Example
<a name="API_ListOriginationNumbers_Example_1"></a>

This example illustrates one usage of ListOriginationNumbers.

#### Sample Request
<a name="API_ListOriginationNumbers_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=ListOriginationNumbers
&NextToken=AAMAATKBfxv6_MR2sl2KtICrU2ksVr9xAtdrIFgK60DYBC7S9uDbQFIkR6ZUugDSulzDRrnUbhQIlq3ZOg%3D%3D
&MaxResults=2
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListOriginationNumbers_Example_1_Response"></a>

```
<ListOriginationNumbersResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListOriginationNumbersResult>
        <NextToken>eyJBd3NBY2NvdW50SWQiOnsicyI6IjU3MjQ1OTY4NzAxNCJ9LCJEZXN0aW5hdGlvblBob25lTnVtYmVyIjp7InMiOiIrMTc3ODk4NjU0MjkifX0=</NextToken>
        <PhoneNumbers>
            <member>
                <CreatedAt>1611952514</CreatedAt>
                <Iso2CountryCode>US</Iso2CountryCode>
                <NumberCapabilities>
                    <member>SMS<member>
                </NumberCapabilities>
                <PhoneNumber>+12065550100</PhoneNumber>
                <RouteType>Transactional</RouteType>
                <Status>ACTIVE</Status>
            </member>
            <member>
                <CreatedAt>1611952589</CreatedAt>
                <Iso2CountryCode>CA</Iso2CountryCode>
                <NumberCapabilities>
                    <member>SMS</member>
                    <member>VOICE</member>
                </NumberCapabilities>
                <PhoneNumber>+12065550199</PhoneNumber>
                <RouteType>Promotional</RouteType>
                <Status>ACTIVE</Status>
            </member>
        </PhoneNumbers>
    </ListOriginationNumbersResult>
    <ResponseMetadata>
        <RequestId>a2430664-0bf0-559e-a20f-5f6bb47ae9b9</RequestId>
    </ResponseMetadata>
</ListOriginationNumbersResponse>
```

## See Also
<a name="API_ListOriginationNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListOriginationNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListOriginationNumbers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
