---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformBranches.html
---

# ListPlatformBranches
<a name="API_ListPlatformBranches"></a>

Lists the platform branches available for your account in an AWS Region. Provides summary information about each platform branch.

For definitions of platform branch and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html).

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_ListPlatformBranches_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.member.N**
Criteria for restricting the resulting list of platform branches. The filter is evaluated as a logical conjunction (AND) of the separate `SearchFilter` terms.
The following list shows valid attribute values for each of the `SearchFilter` terms. Most operators take a single value. The `in` and `not_in` operators can take multiple values.
+  `Attribute = BranchName`:
  +  `Operator`: `=` \| `!=` \| `begins_with` \| `ends_with` \| `contains` \| `in` \| `not_in`
+  `Attribute = LifecycleState`:
  +  `Operator`: `=` \| `!=` \| `in` \| `not_in`
  +  `Values`: `beta` \| `supported` \| `deprecated` \| `retired`
+  `Attribute = PlatformName`:
  +  `Operator`: `=` \| `!=` \| `begins_with` \| `ends_with` \| `contains` \| `in` \| `not_in`
+  `Attribute = TierType`:
  +  `Operator`: `=` \| `!=`
  +  `Values`: `WebServer/Standard` \| `Worker/SQS/HTTP`
Array size: limited to 10 `SearchFilter` objects.
Within each `SearchFilter` item, the `Values` array is limited to 10 items.
Type: Array of [SearchFilter](API_SearchFilter.md) objects
Required: No

 ** MaxRecords **
The maximum number of platform branch values returned in one call.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **
For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.
If no `NextToken` is specified, the first page is retrieved.
Type: String
Required: No

## Response Elements
<a name="API_ListPlatformBranches_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
In a paginated request, if this value isn't `null`, it's the token that you can pass in a subsequent request to get the next response page.
Type: String

 **PlatformBranchSummaryList.member.N**
Summary information about the platform branches.
Type: Array of [PlatformBranchSummary](API_PlatformBranchSummary.md) objects

## Errors
<a name="API_ListPlatformBranches_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListPlatformBranches_Examples"></a>

The following example requests the list of PHP platform branches that are in the Normal Maintenance state.

The request has some URL-encoded characters. `%3D` is the equals sign (`=`), and `%20` is the space character.

### Example
<a name="API_ListPlatformBranches_Example_1"></a>

This example illustrates one usage of ListPlatformBranches.

#### Sample Request
<a name="API_ListPlatformBranches_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?Filters.member.1.Attribute=PlatformName
&Filters.member.1.Operator=%3D
&Filters.member.1.Values.member.1=PHP
&Filters.member.1.Attribute=LifecycleState
&Filters.member.1.Operator=%3D
&Filters.member.1.Values.member.1=Supported
&Operation=ListPlatformBranches
&AuthParams
```

#### Sample Response
<a name="API_ListPlatformBranches_Example_1_Response"></a>

```
<ListPlatformBranches xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ListPlatformBranchesResult>
    <PlatformBranchSummaryList>
      <member>
        <BranchName>PHP 7.3</BranchName>
        <LifecycleState>Supported</BranchName>
        <PlatformName>PHP</BranchName>
      </member>
      <member>
        <BranchName>PHP 7.2</BranchName>
        <LifecycleState>Supported</BranchName>
        <PlatformName>PHP</BranchName>
      </member>
    </PlatformBranchSummaryList>
  </ListPlatformBranchesResult>
  <ResponseMetadata>
    <RequestId>7705f0bc-f28e-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</ListPlatformBranchesResponse>
```

## See Also
<a name="API_ListPlatformBranches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ListPlatformBranches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ListPlatformBranches)
