---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_UntagResource.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# UntagResource
<a name="API_UntagResource"></a>

Removes metadata tags from a FinSpace resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="finspace-UntagResource-request-uri-resourceArn"></a>
A FinSpace resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN).
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:(environment|kxEnvironment)/[0-9A-Za-z_-]{1,128}(/(kxCluster|kxUser|kxVolume|kxScalingGroup)/[a-zA-Z0-9_-]{1,255}|/(kxDatabase/[a-zA-Z0-9_-]{1,255}(/kxDataview/[a-zA-Z0-9_-]{1,255})?))?$`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="finspace-UntagResource-request-uri-tagKeys"></a>
The tag keys (names) of one or more tags to be removed.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is invalid. Something is wrong with the input to the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/UntagResource)
