---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListOnPremisesInstances.html
---

# ListOnPremisesInstances
<a name="API_ListOnPremisesInstances"></a>

Gets a list of names for one or more on-premises instances.

Unless otherwise specified, both registered and deregistered on-premises instance names are listed. To list only registered or deregistered on-premises instance names, use the registration status parameter.

## Request Syntax
<a name="API_ListOnPremisesInstances_RequestSyntax"></a>

```
{
   "nextToken": "{{string}}",
   "registrationStatus": "{{string}}",
   "tagFilters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ListOnPremisesInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-ListOnPremisesInstances-request-nextToken"></a>
An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.
Type: String
Required: No

 ** [registrationStatus](#API_ListOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-ListOnPremisesInstances-request-registrationStatus"></a>
The registration status of the on-premises instances:
+  `Deregistered`: Include deregistered on-premises instances in the resulting list.
+  `Registered`: Include registered on-premises instances in the resulting list.
Type: String
Valid Values: `Registered | Deregistered`
Required: No

 ** [tagFilters](#API_ListOnPremisesInstances_RequestSyntax) **   <a name="CodeDeploy-ListOnPremisesInstances-request-tagFilters"></a>
The on-premises instance tags that are used to restrict the on-premises instance names returned.
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

## Response Syntax
<a name="API_ListOnPremisesInstances_ResponseSyntax"></a>

```
{
   "instanceNames": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListOnPremisesInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceNames](#API_ListOnPremisesInstances_ResponseSyntax) **   <a name="CodeDeploy-ListOnPremisesInstances-response-instanceNames"></a>
The list of matching on-premises instance names.
Type: Array of strings

 ** [nextToken](#API_ListOnPremisesInstances_ResponseSyntax) **   <a name="CodeDeploy-ListOnPremisesInstances-response-nextToken"></a>
If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list on-premises instances call to return the next set of on-premises instances in the list.
Type: String

## Errors
<a name="API_ListOnPremisesInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The next token was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidRegistrationStatusException **
The registration status was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTagFilterException **
The tag filter was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_ListOnPremisesInstances_Examples"></a>

### Example
<a name="API_ListOnPremisesInstances_Example_1"></a>

This example illustrates one usage of ListOnPremisesInstances.

#### Sample Request
<a name="API_ListOnPremisesInstances_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: CodeDeploy_20141006.ListOnPremisesInstances
X-Amz-Date: 20160707T022010Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListOnPremisesInstances_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: e69e5d14-88e3-11e5-bb59-fb8eade0dfc3
Content-Type: application/x-amz-json-1.1
Content-Length: 63

{
    "instanceNames": [
        "grp-a-inst-1",
        "grp-a-inst-2"
    ]
}
```

## See Also
<a name="API_ListOnPremisesInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/ListOnPremisesInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/ListOnPremisesInstances)
