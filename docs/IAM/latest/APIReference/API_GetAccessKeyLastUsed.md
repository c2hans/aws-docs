---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccessKeyLastUsed.html
---

# GetAccessKeyLastUsed
<a name="API_GetAccessKeyLastUsed"></a>

Retrieves information about when the specified access key was last used. The information includes the date and time of last use, along with the AWS service and Region that were specified in the last request made with that key.

## Request Parameters
<a name="API_GetAccessKeyLastUsed_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccessKeyId **
The identifier of an access key.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters that can consist of any upper or lowercased letter or digit.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

## Response Elements
<a name="API_GetAccessKeyLastUsed_ResponseElements"></a>

The following elements are returned by the service.

 ** AccessKeyLastUsed **
Contains information about the last time the access key was used.
Type: [AccessKeyLastUsed](API_AccessKeyLastUsed.md) object

 ** UserName **
The name of the IAM user that owns this access key.

Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`

## Errors
<a name="API_GetAccessKeyLastUsed_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetAccessKeyLastUsed_Examples"></a>

### Example
<a name="API_GetAccessKeyLastUsed_Example_1"></a>

This example illustrates one usage of GetAccessKeyLastUsed.

#### Sample Request
<a name="API_GetAccessKeyLastUsed_Example_1_Request"></a>

```
https://iam.amazonaws.com/
?Action=GetAccessKeyLastUsed
&AccessKeyId=AKIAIOSFODNN7EXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccessKeyLastUsed_Example_1_Response"></a>

```
<GetAccessKeyLastUsedResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetAccessKeyLastUsedResult>
    <AccessKeyLastUsed>
      <Region>us-west-2</Region>
      <LastUsedDate>2015-03-13T10:45:00Z</LastUsedDate>
      <ServiceName>s3</ServiceName>
    </AccessKeyLastUsed>
    <UserName>bob</UserName>
  </GetAccessKeyLastUsedResult>
  <ResponseMetadata>
    <RequestId>510a6abf-d022-11e4-abe8-9b0ebEXAMPLE</RequestId>
  </ResponseMetadata>
</GetAccessKeyLastUsedResponse>
```

## See Also
<a name="API_GetAccessKeyLastUsed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetAccessKeyLastUsed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetAccessKeyLastUsed)
