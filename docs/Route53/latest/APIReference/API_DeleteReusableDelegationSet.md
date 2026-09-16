---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteReusableDelegationSet.html
---

# DeleteReusableDelegationSet
<a name="API_DeleteReusableDelegationSet"></a>

Deletes a reusable delegation set.

**Important**
You can delete a reusable delegation set only if it isn't associated with any hosted zones.

To verify that the reusable delegation set is not associated with any hosted zones, submit a [GetReusableDelegationSet](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html) request and specify the ID of the reusable delegation set that you want to delete.

## Request Syntax
<a name="API_DeleteReusableDelegationSet_RequestSyntax"></a>

```
DELETE /2013-04-01/delegationset/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteReusableDelegationSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteReusableDelegationSet_RequestSyntax) **   <a name="Route53-DeleteReusableDelegationSet-request-uri-Id"></a>
The ID of the reusable delegation set that you want to delete.
Length Constraints: Maximum length of 32.
Required: Yes

## Request Body
<a name="API_DeleteReusableDelegationSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteReusableDelegationSet_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteReusableDelegationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteReusableDelegationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DelegationSetInUse **
The specified delegation contains associated hosted zones which must be deleted before the reusable delegation set can be deleted.
 ** message **

HTTP Status Code: 400

 ** DelegationSetNotReusable **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

 ** InvalidInput **
The input is not valid.
 ** message **

HTTP Status Code: 400

 ** NoSuchDelegationSet **
A reusable delegation set with the specified ID does not exist.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteReusableDelegationSet_Examples"></a>

### Example Request
<a name="API_DeleteReusableDelegationSet_Example_1"></a>

This example illustrates one usage of DeleteReusableDelegationSet.

```
DELETE /2013-04-01/delegationset/N1PA6795SAMPLE
```

### Example Response
<a name="API_DeleteReusableDelegationSet_Example_2"></a>

This example illustrates one usage of DeleteReusableDelegationSet.

```
HTTP/1.1 200 OK
<?xml version="1.0" encoding="UTF-8"?>
<DeleteReusableDelegationSetResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/"/>
```

## See Also
<a name="API_DeleteReusableDelegationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53-2013-04-01/DeleteReusableDelegationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/DeleteReusableDelegationSet)
