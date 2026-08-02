---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicyTags.html
---

# ListPolicyTags
<a name="API_ListPolicyTags"></a>

Lists the tags that are attached to the specified IAM customer managed policy. The returned list of tags is sorted by tag key. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_ListPolicyTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

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

 ** PolicyArn **
The ARN of the IAM customer managed policy whose tags you want to see.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_ListPolicyTags_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **Tags.member.N**
The list of tags that are currently attached to the IAM customer managed policy. Each tag consists of a key name and an associated value. If no tags are attached to the specified resource, the response contains an empty list.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_ListPolicyTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListPolicyTags_Examples"></a>

### Example
<a name="API_ListPolicyTags_Example_1"></a>

The following example is formatted with line breaks for legibility.

This example shows how to list the tags that are attached to an IAM customer managed policy whose ARN is `arn:aws:iam::123456789012:policy/UsersManageOwnCredentials`.

#### Sample Request
<a name="API_ListPolicyTags_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: https://iam.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.11.143 Python/3.6.1 Linux/3.2.45-0.6.wd.865.49.315.metal1.x86_64 botocore/1.7.1
X-Amz-Date: 20170929T182447Z
Authorization: <auth details>
Content-Length: 55
Content-Type: application/x-www-form-urlencoded

Action=ListPolicyTags&Version=2010-05-08&PolicyArn=arn:aws:iam::123456789012:policy/UsersManageOwnCredentials
```

#### Sample Response
<a name="API_ListPolicyTags_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE
Content-Type: text/xml
Content-Length: 484
Date: Fri, 29 Sep 2017 18:24:47 GMT

&ListPolicyTagsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  &ListPolicyTagsResult>
    &IsTruncated>false&/IsTruncated>
    &Tags>
      &member>
        &Key>Dept&/Key>
        &Value>12345&/Value>
      &/member>
      &member>
        &Key>Team&/Key>
        &Value>Accounting&/Value>
      &/member>
    &/Tags>
  &/ListPolicyTagsResult>
  &ResponseMetadata>
    &RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE&/RequestId>
  &/ResponseMetadata>
&/ListPolicyTagsResponse>
```

## See Also
<a name="API_ListPolicyTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListPolicyTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListPolicyTags)
