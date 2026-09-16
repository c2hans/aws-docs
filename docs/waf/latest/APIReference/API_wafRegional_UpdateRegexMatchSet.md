---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_UpdateRegexMatchSet.html
---

# UpdateRegexMatchSet
<a name="API_wafRegional_UpdateRegexMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md) objects (filters) in a [RegexMatchSet](API_wafRegional_RegexMatchSet.md). For each `RegexMatchSetUpdate` object, you specify the following values:
+ Whether to insert or delete the object from the array. If you want to change a `RegexMatchSetUpdate` object, you delete the existing object and add a new one.
+ The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.
+ The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see [RegexPatternSet](API_wafRegional_RegexPatternSet.md).
+ Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

 For example, you can create a `RegexPatternSet` that matches any requests with `User-Agent` headers that contain the string `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

To create and configure a `RegexMatchSet`, perform the following steps:

1. Create a `RegexMatchSet.` For more information, see [CreateRegexMatchSet](API_wafRegional_CreateRegexMatchSet.md).

1. Use [GetChangeToken](API_wafRegional_GetChangeToken.md) to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexMatchSet` request.

1. Submit an `UpdateRegexMatchSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI path) and the identifier of the `RegexPatternSet` that contain the regular expression patterns you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_wafRegional_UpdateRegexMatchSet_RequestSyntax"></a>

```
{
   "ChangeToken": "{{string}}",
   "RegexMatchSetId": "{{string}}",
   "Updates": [
      {
         "Action": "{{string}}",
         "RegexMatchTuple": {
            "FieldToMatch": {
               "Data": "{{string}}",
               "Type": "{{string}}"
            },
            "RegexPatternSetId": "{{string}}",
            "TextTransformation": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_wafRegional_UpdateRegexMatchSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeToken](#API_wafRegional_UpdateRegexMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_UpdateRegexMatchSet-request-ChangeToken"></a>
The value returned by the most recent call to [GetChangeToken](API_wafRegional_GetChangeToken.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [RegexMatchSetId](#API_wafRegional_UpdateRegexMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_UpdateRegexMatchSet-request-RegexMatchSetId"></a>
The `RegexMatchSetId` of the [RegexMatchSet](API_wafRegional_RegexMatchSet.md) that you want to update. `RegexMatchSetId` is returned by [CreateRegexMatchSet](API_wafRegional_CreateRegexMatchSet.md) and by [ListRegexMatchSets](API_wafRegional_ListRegexMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** [Updates](#API_wafRegional_UpdateRegexMatchSet_RequestSyntax) **   <a name="WAF-wafRegional_UpdateRegexMatchSet-request-Updates"></a>
An array of `RegexMatchSetUpdate` objects that you want to insert into or delete from a [RegexMatchSet](API_wafRegional_RegexMatchSet.md). For more information, see [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md).
Type: Array of [RegexMatchSetUpdate](API_wafRegional_RegexMatchSetUpdate.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_wafRegional_UpdateRegexMatchSet_ResponseSyntax"></a>

```
{
   "ChangeToken": "string"
}
```

## Response Elements
<a name="API_wafRegional_UpdateRegexMatchSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeToken](#API_wafRegional_UpdateRegexMatchSet_ResponseSyntax) **   <a name="WAF-wafRegional_UpdateRegexMatchSet-response-ChangeToken"></a>
The `ChangeToken` that you used to submit the `UpdateRegexMatchSet` request. You can also use this value to query the status of the request. For more information, see [GetChangeTokenStatus](API_wafRegional_GetChangeTokenStatus.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`

## Errors
<a name="API_wafRegional_UpdateRegexMatchSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFDisallowedNameException **
The name specified is invalid.
HTTP Status Code: 400

 ** WAFInternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 500

 ** WAFInvalidAccountException **
The operation failed because you tried to create, update, or delete an object by using an invalid account identifier.
HTTP Status Code: 400

 ** WAFInvalidOperationException **
The operation failed because there was nothing to do. For example:
+ You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the specified `WebACL`.
+ You tried to remove an IP address from an `IPSet`, but the IP address isn't in the specified `IPSet`.
+ You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the `ByteMatchTuple` isn't in the specified `WebACL`.
+ You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the specified `WebACL`.
+ You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple` already exists in the specified `WebACL`.
HTTP Status Code: 400

 ** WAFLimitsExceededException **
The operation exceeds a resource limit, for example, the maximum number of `WebACL` objects that you can create for an AWS account. For more information, see [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** WAFNonexistentContainerException **
The operation failed because you tried to add an object to or delete an object from another object that doesn't exist. For example:
+ You tried to add a `Rule` to or delete a `Rule` from a `WebACL` that doesn't exist.
+ You tried to add a `ByteMatchSet` to or delete a `ByteMatchSet` from a `Rule` that doesn't exist.
+ You tried to add an IP address to or delete an IP address from an `IPSet` that doesn't exist.
+ You tried to add a `ByteMatchTuple` to or delete a `ByteMatchTuple` from a `ByteMatchSet` that doesn't exist.
HTTP Status Code: 400

 ** WAFNonexistentItemException **
The operation failed because the referenced object doesn't exist.
HTTP Status Code: 400

 ** WAFStaleDataException **
The operation failed because you tried to create, update, or delete an object by using a change token that has already been used.
HTTP Status Code: 400

## See Also
<a name="API_wafRegional_UpdateRegexMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/UpdateRegexMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/UpdateRegexMatchSet)
