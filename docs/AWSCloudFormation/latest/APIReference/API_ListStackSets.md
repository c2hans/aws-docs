---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSets.html
---

# ListStackSets
<a name="API_ListStackSets"></a>

Returns summary information about StackSets that are associated with the user.

**Note**
This API provides *strongly consistent* reads meaning it will always return the most up-to-date data.
+ [Self-managed permissions] If you set the `CallAs` parameter to `SELF` while signed in to your AWS account, `ListStackSets` returns all self-managed StackSets in your AWS account.
+ [Service-managed permissions] If you set the `CallAs` parameter to `SELF` while signed in to the organization's management account, `ListStackSets` returns all StackSets in the management account.
+ [Service-managed permissions] If you set the `CallAs` parameter to `DELEGATED_ADMIN` while signed in to your member account, `ListStackSets` returns all StackSets with service-managed permissions in the management account.

## Request Parameters
<a name="API_ListStackSets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CallAs **
[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.
By default, `SELF` is specified. Use `SELF` for StackSets with self-managed permissions.
+ If you are signed in to the management account, specify `SELF`.
+ If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `SELF | DELEGATED_ADMIN`
Required: No

 ** MaxResults **
The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a `NextToken` value that you can assign to the `NextToken` request parameter to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Status **
The status of the StackSets that you want to get summary information about.
Type: String
Valid Values: `ACTIVE | DELETED`
Required: No

## Response Elements
<a name="API_ListStackSets_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
If the request doesn't return all of the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call `ListStackInstances` again and assign that token to the request object's `NextToken` parameter. If the request returns all results, `NextToken` is set to `null`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 **Summaries.member.N**
A list of `StackSetSummary` structures that contain information about the user's StackSets.
Type: Array of [StackSetSummary](API_StackSetSummary.md) objects

## Errors
<a name="API_ListStackSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListStackSets_Examples"></a>

### ListStackSets
<a name="API_ListStackSets_Example_1"></a>

This example illustrates one usage of ListStackSets.

#### Sample Request
<a name="API_ListStackSets_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListStackSets
 &Status=ACTIVE
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListStackSets_Example_1_Response"></a>

```
<ListStackSetsResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <ListStackSetsResult>
    <Summaries>
      <member>
        <StackSetName>stack-set-example-one</StackSetName>
        <Description>Description of the StackSet</Description>
        <StackSetId>stack-set-example-one:c14cd6d1-cd17-40bd-82ed-ff97example</StackSetId>
        <Status>ACTIVE</Status>
      </member>
      <member>
        <StackSetName>stack-set-example-two</StackSetName>
        <StackSetId>stack-set-example-two:22f04391-472b-4e36-b11a-727example</StackSetId>
        <Status>ACTIVE</Status>
      </member>
    </Summaries>
  </ListStackSetsResult>
  <ResponseMetadata>
    <RequestId>35ec5187-794a-11e7-8c45-3f18example</RequestId>
  </ResponseMetadata>
</ListStackSetsResponse>
```

## See Also
<a name="API_ListStackSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListStackSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListStackSets)
